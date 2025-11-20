# NeuroBrainSeg Troubleshooting Guide

## Problem 1: Module Recognized but No Interface Appears

**Symptom:** Module appears in the list but clicking it shows a blank screen.

**Causes:**
1. UI file not loading properly
2. Missing Qt widgets imports
3. Layout not being added to main widget

**Solutions:**

### Solution A: Check the Error Log
1. Open View → Error Log in 3D Slicer
2. Look for Python errors
3. Common errors:
   - `FileNotFoundError: UI/NeuroBrainSeg.ui`
   - `ImportError: cannot import name 'QComboBox'`
   - `AttributeError: 'NoneType' object has no attribute 'layout'`

### Solution B: Use the Fixed Python File
The module now has a fallback mechanism:
- If UI file fails to load → creates UI programmatically
- This should work even without the .ui file

Replace your NeuroBrainSeg.py with the FIXED version:
```
NeuroBrainSeg-FIXED.py → rename to → NeuroBrainSeg.py
```

### Solution C: Verify Directory Structure
Ensure your directory looks like this:
```
SlicerNeuroBrainSeg/
├── NeuroBrainSeg/
│   ├── __init__.py                 (MUST exist!)
│   ├── NeuroBrainSeg.py            (the FIXED version)
│   ├── CMakeLists.txt
│   ├── Resources/
│   │   ├── Icons/
│   │   │   └── NeuroBrainSeg.png
│   │   └── UI/
│   │       └── NeuroBrainSeg.ui    (optional - falls back if missing)
│   └── Testing/
│       ├── CMakeLists.txt
│       └── Python/
│           └── test_NeuroBrainSeg.py
```

---

## Problem 2: Module Crashes When Clicked

**Symptom:** Error message or Slicer crashes when opening the module.

**Solutions:**

### Check for Python import errors
```python
# In Slicer Python console, test each import:
import slicer
import vtk
from slicer.ScriptedLoadableModule import *
```

If any of these fail, install missing packages.

### Test module loading
```python
# In Slicer Python console:
import sys
sys.path.append('/path/to/SlicerNeuroBrainSeg/NeuroBrainSeg')

try:
    import NeuroBrainSeg
    print("Module loaded successfully!")
except Exception as e:
    print(f"Error loading module: {e}")
    import traceback
    traceback.print_exc()
```

---

## Problem 3: "No Module Named" Errors

**Symptom:** 
```
ModuleNotFoundError: No module named 'slicer'
ImportError: cannot import name 'qt'
```

**Cause:** Running Python code outside of 3D Slicer context.

**Solution:** Always use Slicer's Python interpreter:
```bash
# Windows
"C:\Program Files\Slicer 5.X\bin\PythonSlicer.exe" script.py

# macOS
"/Applications/Slicer.app/Contents/bin/PythonSlicer" script.py

# Linux
/path/to/Slicer-build/bin/PythonSlicer script.py
```

---

## Problem 4: UI Widgets Not Responding

**Symptom:** Buttons don't work when clicked, no feedback.

**Solutions:**

### Check connections
```python
# In Slicer Python console after loading module:
widget = slicer.modules.neurobrainseg.widgetRepresentation()
print(f"Apply button: {widget.applyButton}")
print(f"Export button: {widget.exportButton}")
```

### Verify signal connections
```python
# Test if buttons are properly connected:
# Click button and check Python console for error messages
```

---

## Problem 5: Module Not Appearing in List

**Symptom:** Module doesn't show in Modules menu.

**Solutions:**

### A. Verify path is added correctly
1. Edit → Application Settings → Modules
2. Check "Additional module paths" contains the correct path
3. Should point to: `.../SlicerNeuroBrainSeg/NeuroBrainSeg`
4. NOT to the whole extension folder

### B. Restart Slicer completely
```bash
# Close and reopen Slicer completely
# Don't just reload - do a full restart
```

### C. Check CMakeLists.txt
Ensure the root CMakeLists.txt is present and correct:
```cmake
cmake_minimum_required(VERSION 3.16)
project(SlicerNeuroBrainSeg)

find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

add_subdirectory(NeuroBrainSeg)

include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})
```

---

## Problem 6: Segmentation Button Does Nothing

**Symptom:** Click "Apply Segmentation" but nothing happens.

**Solutions:**

### Check Python console for errors
View → Python Interactor and watch for error messages.

### Common causes:
1. No input volume selected
2. No output segmentation selected
3. Deep learning model not installed

### Debug in Python console:
```python
# Get the module widget
widget = slicer.modules.neurobrainseg.widgetRepresentation()

# Check selections
print(f"Input: {widget.inputVolumeSelector.currentNode()}")
print(f"Output: {widget.outputSegmentationSelector.currentNode()}")

# Try segmentation manually
logic = NeuroBrainSegLogic()
inputVol = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
outputSeg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")

try:
    logic.process(inputVol, outputSeg, "SynthSeg (Robust, All Contrasts)")
    print("Segmentation completed!")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
```

---

## Problem 7: Export Button Not Working

**Symptom:** Click "Export to STL" but no files are created.

**Solutions:**

### Verify segmentation exists
```python
widget = slicer.modules.neurobrainseg.widgetRepresentation()
seg = widget.outputSegmentationSelector.currentNode()
print(f"Segmentation: {seg}")
print(f"Number of segments: {seg.GetSegmentation().GetNumberOfSegments()}")
```

### Check export directory permissions
```python
import os
exportDir = "/path/to/export"
print(f"Directory exists: {os.path.exists(exportDir)}")
print(f"Is writable: {os.access(exportDir, os.W_OK)}")
```

### Manual export test:
```python
seg = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
logic = NeuroBrainSegLogic()
logic.exportToSTL(seg, "/tmp/export", "STL (Individual Files)", 0.5)
```

---

## Complete Reinstallation Steps

If all else fails, perform a clean reinstall:

### Step 1: Clean Slicer configuration
```bash
# Find Slicer settings folder:
# Windows: C:\Users\YourUsername\AppData\Roaming\NA-MIC\Slicer.ini
# macOS: ~/.config/NA-MIC/Slicer.ini
# Linux: ~/.config/NA-MIC/Slicer.ini

# Delete all Slicer configuration to reset
```

### Step 2: Remove old extension
```bash
# Delete the entire SlicerNeuroBrainSeg folder
rm -rf /path/to/SlicerNeuroBrainSeg
```

### Step 3: Fresh installation
```bash
# Clone fresh from GitHub
git clone https://github.com/YourUsername/SlicerNeuroBrainSeg.git

# Restart Slicer completely
```

### Step 4: Add module correctly
1. Open 3D Slicer
2. Edit → Application Settings → Modules
3. Click "+" to add new path
4. Select: `.../SlicerNeuroBrainSeg/NeuroBrainSeg`
5. Click OK
6. Restart Slicer

---

## Getting Help

If problems persist:

### 1. Check the Error Log
View → Error Log - copy all messages

### 2. Check Slicer Console
View → Python Interactor - look for exceptions

### 3. Post to 3D Slicer Discourse
https://discourse.slicer.org/
- Include: Slicer version, OS, Error log, Python console output

### 4. Check GitHub Issues
https://github.com/YourUsername/SlicerNeuroBrainSeg/issues
- Search for similar issues
- Create new issue with details

---

## Quick Checklist

- [ ] Directory structure is correct
- [ ] __init__.py exists in NeuroBrainSeg folder
- [ ] NeuroBrainSeg.py is the FIXED version
- [ ] CMakeLists.txt is present in root folder
- [ ] Module path added correctly in Settings
- [ ] Slicer fully restarted (not just reloaded)
- [ ] No errors in Error Log or Python console
- [ ] Input volume selected
- [ ] Output segmentation created
- [ ] Clicked "Apply Segmentation" button

---

## File Sizes (for verification)

- NeuroBrainSeg.py (FIXED): ~25 KB
- requirements.txt: ~0.5 KB
- __init__.py: ~0.2 KB
- CMakeLists.txt (root): ~1.5 KB
- CMakeLists.txt (module): ~0.8 KB

---

**Version:** 1.0
**Last Updated:** November 17, 2025

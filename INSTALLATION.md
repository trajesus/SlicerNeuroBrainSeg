# Installation Instructions

## System Requirements

- 3D Slicer 5.2 or newer
- Python 3.6+
- 8 GB RAM minimum (16 GB recommended for optimal performance)

## Installation Steps

### Step 1: Prepare Files

1. Download all files from this package
2. Organize them according to this structure:

```
SlicerNeuroBrainSeg/
├── CMakeLists.txt (rename ROOT-CMakeLists.txt)
├── README.md (rename ROOT-README.md)
├── LICENSE (rename ROOT-LICENSE.txt)
├── requirements.txt (rename ROOT-requirements.txt)
├── .gitignore (rename ROOT-.gitignore)
│
└── NeuroBrainSeg/
    ├── __init__.py (rename NeuroBrainSeg-__init__.py)
    ├── NeuroBrainSeg.py
    ├── CMakeLists.txt (rename MODULE-CMakeLists.txt)
    ├── Resources/
    │   └── Icons/
    │       └── NeuroBrainSeg.png (optional - add your own 128x128 PNG)
    └── Testing/
        ├── CMakeLists.txt (rename TESTING-CMakeLists.txt)
        └── Python/
            └── test_NeuroBrainSeg.py
```

### Step 2: Add to 3D Slicer

1. Open 3D Slicer
2. Go to: **Edit** → **Application Settings**
3. Click on **"Modules"** in the left panel
4. In **"Additional module paths"** section, click the **"+"** button
5. Navigate to and select: `SlicerNeuroBrainSeg/NeuroBrainSeg` folder
6. Click **OK**

### Step 3: Restart 3D Slicer

1. **Close 3D Slicer completely** (don't just minimize)
2. Wait 5 seconds
3. **Reopen 3D Slicer**

### Step 4: Verify Installation

1. Go to: **Modules** → **Segmentation** → **Neuro Brain Segmentation**
2. The module should appear with a complete interface showing:
   - Input Volume selector
   - Model Type combo box
   - Output Segmentation selector
   - Show 3D checkbox
   - Export format options
   - Smoothing slider
   - Apply Segmentation button
   - Export to STL button

## Testing the Installation

1. Load sample data: **Modules** → **Sample Data** → **MRHead**
2. In NeuroBrainSeg module, select the loaded MRHead as input volume
3. Click "Apply Segmentation"
4. Wait for processing to complete
5. You should see colored brain structures in the 3D view
6. Click "Export to STL" and select a folder to save the STL files

## Troubleshooting

### Module doesn't appear in list
- Check that path is set to: `.../SlicerNeuroBrainSeg/NeuroBrainSeg` (NOT the root folder)
- Make sure you completely closed and reopened Slicer
- Check Application Settings again to verify path is saved

### Interface appears blank
- Check View → Error Log for Python errors
- Verify that `__init__.py` exists in NeuroBrainSeg folder
- Try View → Python Interactor and run: `from NeuroBrainSeg import NeuroBrainSeg`

### Buttons don't work
- Make sure you've selected an input volume
- Create a new output segmentation node if needed
- Check Error Log for exceptions

## Getting Help

- See TROUBLESHOOTING.md for detailed solutions
- Check 3D Slicer Documentation: https://slicer.readthedocs.io/
- 3D Slicer Community: https://discourse.slicer.org/

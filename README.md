# SlicerNeuroBrainSeg

**Deep Learning-Based Brain Structure Segmentation for 3D Slicer**

This extension provides automatic segmentation of brain structures using state-of-the-art deep learning models, with easy export functionality for 3D printing.

## Features

- **Automatic Brain Segmentation**: Segment all brain structures with a single click
- **Multiple Deep Learning Models**:
  - **SynthSeg**: Robust, contrast-agnostic segmentation (T1, T2, FLAIR, CT)
  - **FastSurfer**: Fast T1-weighted MRI segmentation (95 structures in <1 minute)
  - **TotalSegmentator**: Full-body CT segmentation (117 anatomical structures)
- **Easy STL Export**: Export segmented structures for 3D printing
- **Multiple Export Formats**: Individual STL, merged STL, OBJ with colors
- **Interactive 3D Visualization**: Immediate 3D rendering of segmentation results
- **Customizable Smoothing**: Adjustable smoothing factor for cleaner 3D prints

## Installation

### Prerequisites

- 3D Slicer 5.2 or newer
- Python 3.6+
- 8 GB RAM (16 GB recommended)

### Install from Source

1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/SlicerNeuroBrainSeg.git
   ```

2. Open 3D Slicer

3. Go to Edit → Application Settings → Modules

4. Add path to: `SlicerNeuroBrainSeg/NeuroBrainSeg`

5. Restart 3D Slicer

## Usage

1. Load your brain MRI (DICOM, NIFTI, etc.)
2. Open NeuroBrainSeg module (Modules → Segmentation → Neuro Brain Segmentation)
3. Select input volume and output segmentation
4. Choose deep learning model
5. Click "Apply Segmentation"
6. Explore results in 3D view
7. Export to STL for 3D printing

## Supported Models

### SynthSeg
- Robust, contrast-agnostic segmentation
- Works with T1, T2, FLAIR, CT
- 95+ brain structures
- Processing time: 1-2 min (CPU), ~30 sec (GPU)

### FastSurfer
- Fast T1-weighted MRI segmentation
- 95 anatomical structures
- Processing time: <1 min (GPU)
- Requires GPU for optimal performance

### TotalSegmentator
- Full-body CT segmentation
- 117 anatomical structures
- Processing time: 1-2 min (GPU), 40-50 min (CPU)
- Comprehensive anatomical coverage

## License

BSD-3-Clause License - See LICENSE file for details

## Acknowledgements

- SynthSeg development team
- FastSurfer development team
- TotalSegmentator development team
- 3D Slicer community

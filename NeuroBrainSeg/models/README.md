# Models folder

Put here the AI models used for segmentation, for example:

- SynthSeg: models/synthseg/...
- FastSurfer: models/fastsurfer/...
- TotalSegmentator: models/totalsegmentator/...

The Slicer module will only *detect* available models by checking if the
respective subfolder exists. The actual inference pipeline must be implemented
in the logic methods:
- _runSynthSegModel()
- _runFastSurferModel()
- _runTotalSegmentatorModel()

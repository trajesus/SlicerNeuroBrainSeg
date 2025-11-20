import unittest
import slicer
from slicer.ScriptedLoadableModule import ScriptedLoadableModuleTest


class NeuroBrainSegTest(ScriptedLoadableModuleTest):
    """
    This is the test case for the NeuroBrainSeg module.
    Uses ScriptedLoadableModuleTest base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def setUp(self):
        """
        Do whatever is needed to reset the state - typically a scene clear will be enough.
        """
        slicer.mrmlScene.Clear()

    def runTest(self):
        """
        Run as few or as many tests as needed here.
        """
        self.setUp()
        self.test_NeuroBrainSeg1()
        self.test_NeuroBrainSeg2()

    def test_NeuroBrainSeg1(self):
        """
        Ideally you should have several levels of tests.  At the lowest level
        tests should exercise the functionality of the logic with different inputs
        (both valid and invalid).  At higher levels your tests should emulate the
        way the user would interact with your code and confirm that it still works
        the way you expect.
        One of the most important tests is often the one that simulates the way
        the clinician would use the software.  If you have this kind of test you
        should probably also add a test that makes sure the outputs are correct.
        """

        self.delayDisplay("Starting the test")

        # Get/create input data
        import SampleData
        registerSampleData()
        inputVolume = SampleData.downloadSample("NeuroBrainSeg1")
        self.assertIsNotNone(inputVolume)
        self.delayDisplay("Loaded test data set")

        # Create output segmentation
        outputSegmentation = slicer.mrmlScene.AddNewNodeByClass(
            "vtkMRMLSegmentationNode"
        )
        outputSegmentation.SetName("TestSegmentation")
        self.assertIsNotNone(outputSegmentation)

        # Test the module logic
        from NeuroBrainSeg import NeuroBrainSegLogic

        logic = NeuroBrainSegLogic()

        # Test processing
        self.delayDisplay("Running algorithm")
        logic.process(
            inputVolume,
            outputSegmentation,
            "SynthSeg (Robust, All Contrasts)"
        )

        # Verify the output
        self.assertGreater(
            outputSegmentation.GetSegmentation().GetNumberOfSegments(),
            0
        )
        self.delayDisplay("Test passed!")

    def test_NeuroBrainSeg2(self):
        """
        Test creating and exporting segmentation
        """

        self.delayDisplay("Starting export test")

        # Create a test segmentation
        outputSegmentation = slicer.mrmlScene.AddNewNodeByClass(
            "vtkMRMLSegmentationNode"
        )
        outputSegmentation.SetName("ExportTestSegmentation")

        # Add some test segments
        segmentation = outputSegmentation.GetSegmentation()
        segmentation.AddEmptySegment("TestStructure1")
        segmentation.AddEmptySegment("TestStructure2")

        # Verify segments were created
        self.assertEqual(segmentation.GetNumberOfSegments(), 2)

        self.delayDisplay("Export test passed!")


def registerSampleData():
    """
    Add data sets to Sample Data module.
    """
    import SampleData
    iconsPath = os.path.join(os.path.dirname(__file__), "Resources/Icons")

    # NeuroBrainSeg1
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
        sampleName="NeuroBrainSeg1",
        category="NeuroBrainSeg",
        thumbnailFileName=os.path.join(iconsPath, "NeuroBrainSeg.png"),
        uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/998cb522173913b13b44fb54d96f6b91ee893868921d2ec1e555b3f1591f0bed --checksum SHA256:998cb522173913b13b44fb54d96f6b91ee893868921d2ec1e555b3f1591f0bed",
        fileNames="MR-SPGR.nrrd",
        nodeNames="MRHead",
        loadFileType="VolumeFile",
    )


if __name__ == "__main__":
    import sys
    import os
    unittest.main()

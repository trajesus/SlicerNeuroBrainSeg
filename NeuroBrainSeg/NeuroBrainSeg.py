"""
NeuroBrainSeg - ULTRA-MINIMAL WORKING VERSION
Garantido funcionar com botões visíveis
"""

import logging
import os
import vtk
import slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin

logger = logging.getLogger(__name__)


class NeuroBrainSeg(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Neuro Brain Segmentation"
        self.parent.categories = ["Segmentation"]


class NeuroBrainSegWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
    def __init__(self, parent=None):
        ScriptedLoadableModuleWidget.__init__(self, parent)
        VTKObservationMixin.__init__(self)
        
        # Initialize everything
        self.applyButton = None
        self.exportButton = None
        self.progressLabel = None
        self.logic = NeuroBrainSegLogic()

    def setup(self):
        ScriptedLoadableModuleWidget.setup(self)
        
        # Direct imports
        from qt import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget
        
        # Main layout
        mainWidget = QWidget()
        mainLayout = QVBoxLayout(mainWidget)
        
        # Title
        titleLabel = QLabel("Neuro Brain Segmentation")
        mainLayout.addWidget(titleLabel)
        
        # Progress
        self.progressLabel = QLabel("Status: Ready")
        mainLayout.addWidget(self.progressLabel)
        
        # Apply button
        self.applyButton = QPushButton("Apply Segmentation")
        self.applyButton.setMinimumHeight(40)
        mainLayout.addWidget(self.applyButton)
        
        # Export button  
        self.exportButton = QPushButton("Export to STL")
        self.exportButton.setMinimumHeight(40)
        mainLayout.addWidget(self.exportButton)
        
        # Stretch
        mainLayout.addStretch()
        
        # Add to widget
        self.layout.addWidget(mainWidget)
        
        # Connections
        self.applyButton.connect("clicked(bool)", self.onApply)
        self.exportButton.connect("clicked(bool)", self.onExport)
        
        logger.info("Setup complete")

    def onApply(self):
        try:
            self.progressLabel.setText("Processing...")
            slicer.util.infoDisplay("Apply clicked - Working!")
            self.progressLabel.setText("Done!")
        except Exception as e:
            logger.error(str(e))
            slicer.util.errorDisplay(str(e))

    def onExport(self):
        try:
            self.progressLabel.setText("Exporting...")
            slicer.util.infoDisplay("Export clicked - Working!")
            self.progressLabel.setText("Ready")
        except Exception as e:
            logger.error(str(e))
            slicer.util.errorDisplay(str(e))


class NeuroBrainSegLogic(ScriptedLoadableModuleLogic):
    def __init__(self):
        ScriptedLoadableModuleLogic.__init__(self)


class NeuroBrainSegTest(ScriptedLoadableModuleTest):
    def runTest(self):
        self.delayDisplay("Test")

cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(SlicerNeuroBrainSeg)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/trajesus/SlicerNeuroBrainSeg")
set(EXTENSION_CATEGORY "Segmentation")
set(EXTENSION_CONTRIBUTORS "Tiago Jesus (University of Minho)")
set(EXTENSION_DESCRIPTION "Deep learning-based automatic brain structure segmentation with easy STL export for 3D printing. Integrates state-of-the-art models for robust segmentation of all brain structures.")
set(EXTENSION_ICONURL "https://raw.githubusercontent.com/trajesus/SlicerNeuroBrainSeg/main/NeuroBrainSeg/Resources/Icons/NeuroBrainSeg.png")

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(NeuroBrainSeg)

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})

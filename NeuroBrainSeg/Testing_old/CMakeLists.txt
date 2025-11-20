set(MODULE_TEST_PYTHON_SCRIPTS
  test_NeuroBrainSeg.py
)

foreach(script_name ${MODULE_TEST_PYTHON_SCRIPTS})
  slicer_add_python_unittest(
    SCRIPT ${script_name}
    SLICER_ARGS --disable-cli-modules --disable-scripted-loadable-modules
  )
endforeach()

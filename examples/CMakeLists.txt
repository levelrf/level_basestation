include(GrPython)

GR_PYTHON_INSTALL(
    PROGRAMS
	test_rx.py
    DESTINATION ${GR_PKG_LVL_EXAMPLES_DIR}
    COMPONENT "level_examples"
)
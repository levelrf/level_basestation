include(GrPython)

GR_PYTHON_INSTALL(
    PROGRAMS
	test_rx.py
    DESTINATION ${GR_PKG_LEVEL_EXAMPLES_DIR}
    COMPONENT "level_examples"
)
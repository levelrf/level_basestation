include(GrPython)

GR_PYTHON_INSTALL(
    PROGRAMS
    fsk_demod_dev.py
	test_rx.py
    DESTINATION ${GR_PKG_LEVEL_EXAMPLES_DIR}
    COMPONENT "level_examples"
)
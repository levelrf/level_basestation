include(GrPython)

GR_PYTHON_INSTALL(
    FILES
    __init__.py
    fsk.py
    msk.py
    pubsub.py
    fft_window.py
    zmq_fft_sink.py
    cc1k_level_pkt.py
    DESTINATION ${GR_PYTHON_DIR}/gnuradio/level
    COMPONENT "level_python"
)
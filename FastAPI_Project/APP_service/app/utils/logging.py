"""
File contains global logger across all the modules:
1.Trace: The Trace level designates finer-grained informational events than the Debug.
2.Debug: The Debug level designates fine-grained informational events that are most useful
to debug an application.
3.Info: The Info level designates informational messages that highlight the progress
of the application at coarse-grained level.
4.Warn: The Warn level designates potentially harmful situations.
5.Error: The Error level designates error events that might still allow the application
to continue running.
6.Fatal: The Fatal level designates very severe error events that will presumably lead the
application to abort.
7.All: The All has the lowest possible rank and is intended to turn on all logging.
8.OFF: The Off has the highest possible rank and is intended to turn off logging.
"""
import logging


def setup_logger_singleton():
    """
    Function responsible for initializing logger instance to be used throughout application.
    :return:
    """
    logger = logging.getLogger(name="App-Service")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(filename)-20s:%(funcName)-21s:%(lineno)-5s]'
                                  '[%(levelname)s] >> %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)

import logging

# A logger object named after module:
# https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial
logger = logging.getLogger(__name__)


LOG_DEV_LEVEL_NUM = 15
logging.addLevelName(LOG_DEV_LEVEL_NUM, "DEV")
def log_dev(self, message, *args, **kwargs):
    """Create a custom log level between INFO and DEBUG named DEV."""
    if self.isEnabledFor(LOG_DEV_LEVEL_NUM):
        # Yes, logger takes its '*args' as 'args'.
        self._log(LOG_DEV_LEVEL_NUM, message, args, **kwargs) 
logging.Logger.dev = log_dev


def init_logger_basic(log_level: int) -> None:
    """Instantiate a basic logger object to be used across modules.

    Parameters
    ----------
    log_level
        The level of logging to be recorded. Can be defined either as the
        integer level or the logging.<LEVEL> values in line with the
        definitions of the logging module 
        (see - https://docs.python.org/3/library/logging.html#levels)
    
    Returns
    -------
    None
        The logger created by this function is available in any other modules
        by using `logger = logging,getLogger(__name__)` at the global scope
        level in a module (i.e. below imports, not in a function).
    """
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s %(levelname)s %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

import logging

# logger object named after module: https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial
logger = logging.getLogger(__name__)


def hello_world():
    """Logging at the info level."""
    logger.info('hello world 👋')


def hello_heaven():
    """Logging at the dev level."""
    logger.dev('hello heaven - here is some more info 😇')


def hello_behind_the_curtain():
    """Logging at the debug level."""
    logger.debug("""
    hello behind the curtain 
    here is a big dump of debug things 
    🛠 ⚙️ 🪛 🪚 🗜 ⛏ 🪓 🧰 🔩 ✏️ 🔧 🔨
    """)


def hello_hell():
    """Logging and raising an exception."""
    msg = 'HELLO HELL 👹'
    logger.exception(msg=msg)
    raise Exception(msg)

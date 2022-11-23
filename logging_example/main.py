import logging

from utils import log_setup
from utils import talk

logger = logging.getLogger(__name__)


def run():
    """Run the demo."""
    talk.hello_world()

    talk.hello_heaven()

    talk.hello_behind_the_curtain()

    talk.hello_hell()


if __name__ == '__main__':

    log_setup.init_logger_basic(
        log_level=logging.DEBUG  # Level 10 and up.
        # log_level=15  # DEV level and up.
        # log_level=logging.INFO  # Level 20 and up.
        # log_level=logging.ERROR  # Level 40 and up.
    )

    run()

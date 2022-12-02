import sys

from loguru import logger

from rating_bot.bot import TwitchBot
from rating_bot.config import settings

logger.add(
    sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>"
)
logger.add("debug.log", rotation="500 MB", compression="zip", enqueue=True)


def main() -> None:
    bot = TwitchBot(
        token=settings.BOT_TOKEN,
        channel=settings.CHANNEL,
        test_channel=settings.TEST_CHANNEL,
    )
    bot.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        logger.exception(exc)

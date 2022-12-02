import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    BOT_TOKEN: str

    CHANNEL: str
    TEST_CHANNEL: str


load_dotenv()


settings = Settings(
    BOT_TOKEN=os.getenv("TOKEN", ""),
    CHANNEL=os.getenv("CHANNEL", ""),
    TEST_CHANNEL=os.getenv("TEST_CHANNEL", ""),
)

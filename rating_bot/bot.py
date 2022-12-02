from typing import TYPE_CHECKING, Any

from loguru import logger
from twitchio.ext.commands import Bot, Context, command

from rating_bot.messages import (
    get_rating_result_msg,
    get_start_rating_msg,
    get_test_msg,
)
from rating_bot.services import get_rating_result
from rating_bot.states import State

if TYPE_CHECKING:
    from twitchio import Message


class TwitchBot(Bot):
    BASE_COMMAND_PRIFIX = "!"

    def __init__(
        self,
        *args: Any,
        token: str,
        channel: str,
        test_channel: str,
        case_insensitive: bool = True,
        **kwargs: Any,
    ) -> None:
        kwargs.setdefault("prefix", self.BASE_COMMAND_PRIFIX)
        initial_channels = kwargs.get("initial_channels", [])
        initial_channels.append(channel)
        super().__init__(
            *args,
            token=token,
            initial_channels=initial_channels,
            case_insensitive=case_insensitive,
            **kwargs,
        )

        self._channel = channel
        self._test_channel = test_channel

        self._rating = {}
        self._state = State.WAITING

    async def event_ready(self) -> None:
        logger.info(f"Logged in as | {self.nick}")

    async def event_message(self, message: "Message") -> None:
        """Receives all chat messages"""

        if message.echo:
            # Messages with echo set to True are messages sent by the bot...
            # For now we just want to ignore them...
            return

        if self._state == State.RATING:
            try:
                evaluation = int(message.content)  # type: ignore[misc]
                self._rating[message.author.name] = evaluation
            except (TypeError, ValueError):
                pass

        await self.handle_commands(message)

    # WARNING: logger should be after @command
    @command(name="startrating")
    @logger.catch
    async def start_rating(self, ctx: Context) -> None:
        if ctx.author.name == self._channel:
            self._rating = {}
            self._state = State.RATING
            await ctx.send(get_start_rating_msg())
        elif ctx.author.name == self._test_channel:
            await ctx.send(get_test_msg())

    # WARNING: logger should be after @command
    @command(name="endrating")
    @logger.catch
    async def end_rating(self, ctx: Context) -> None:
        if ctx.author.name != self._channel or self._state != State.RATING:
            return

        rating_result = get_rating_result(self._rating)
        result_message = get_rating_result_msg(rating_result)

        self._rating = {}
        self._state = State.WAITING
        await ctx.send(result_message)
        logger.info(result_message)

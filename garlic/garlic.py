from typing import Callable

from garlic import EventHandler, EventDispatcher, BaseEvent
from garlic.protocol import Protocol
from garlic.types import DecoratedCallable


class Garlic:
    def __init__(
            self,
            protocol: str = Protocol.MEMORY,
            channel_path: str = None,
            channel_delimiter: str = ".",
            event_handler: EventHandler = None,
            event_dispatcher: EventDispatcher = None
            ) -> None:
        self._protocol = protocol
        self._channel_path = channel_path
        self._channel_delimiter = channel_delimiter
        self._event_handler = event_handler
        self._event_dispatcher = event_dispatcher
        self._bootstrap()

    def subscribe(self) -> Callable[[DecoratedCallable], DecoratedCallable]:
        def decorator(func: DecoratedCallable) -> DecoratedCallable:
            self._event_handler.subscribe(
                subscriber=func,
            )
            return func

        return decorator

    def publish(self, event: BaseEvent):
        self._event_dispatcher(event=event)

    def _bootstrap(self):
        self._event_handler = self._event_handler or EventHandler()
        self._event_dispatcher = self._event_dispatcher or EventDispatcher(event_handler=self._event_handler)


from typing import Callable

from garlic import BaseEvent, EventBus
from garlic.types import DecoratedCallable


class Garlic:
    def __init__(
        self,
        channel_path: str = None,
        channel_delimiter: str = ".",
        event_bus: EventBus = None,
    ) -> None:
        self._channel_path = channel_path
        self._channel_delimiter = channel_delimiter
        self._event_bus = event_bus
        self._bootstrap()

    def subscribe(self) -> Callable[[DecoratedCallable], DecoratedCallable]:
        def decorator(func: DecoratedCallable) -> DecoratedCallable:
            self._event_bus.subscribe(
                subscriber=func,
            )
            return func

        return decorator

    def emit(self, event: BaseEvent):
        self._event_bus(event=event)

    def _bootstrap(self):
        self._event_bus = self._event_bus or EventBus()

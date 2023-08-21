from typing import Callable, Optional

from garlic import BaseEvent, EventBus
from garlic.types import DecoratedCallable


class Garlic:
    def __init__(
        self,
        channel_path: Optional[str] = None,
        channel_delimiter: str = ".",
        event_bus: Optional[EventBus] = None,
    ) -> None:
        self._channel_path = channel_path
        self._channel_delimiter = channel_delimiter
        self._event_bus = event_bus or EventBus(
            channel_path=self._channel_path, channel_delimiter=self._channel_delimiter
        )

    def subscribe(self) -> Callable[[DecoratedCallable], DecoratedCallable]:
        def decorator(func: DecoratedCallable) -> DecoratedCallable:
            self._event_bus.subscribe(
                subscriber=func,
            )
            return func

        return decorator

    def emit(self, event: BaseEvent) -> None:
        self._event_bus(event=event)

    def __call__(self, event: BaseEvent) -> None:
        self.emit(event=event)

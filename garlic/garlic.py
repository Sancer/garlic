from typing import Callable

from garlic import EventHandler, EventDispatcher
from garlic.types import DecoratedCallable


class Garlic:
    def __init__(self, config):
        self.config = config

        self._event_handler = EventHandler()
        self._event_dispatcher = EventDispatcher(event_handler=self._event_handler)

    def subscribe(self, event_class) -> Callable[[DecoratedCallable], DecoratedCallable]:
        def decorator(func: DecoratedCallable) -> DecoratedCallable:
            self._event_handler.subscribe(
                event_class=event_class,
                subscriber=func,
            )
            return func

        return decorator

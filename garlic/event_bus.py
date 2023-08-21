from typing import Any, Callable, Optional

from .base_event import BaseEvent
from .protocol import Protocol
from .utils import get_typed_signature


class EventNotProvidedError(Exception):
    message = "Subscriber should have an event parameter"


class EventBus:
    protocol: Protocol = Protocol.MEMORY

    def __init__(
        self,
        channel_path: Optional[str] = None,
        channel_delimiter: Optional[str] = None,
    ) -> None:
        self._channel_path = channel_path
        self._channel_delimiter = channel_delimiter
        self._subscriptions: dict[str, list[Callable[..., Any]]] = {}

    def subscribe(self, subscriber: Callable[..., Any]) -> None:
        event_name = self._get_subscriber_event_name(subscriber)
        channel_name = self.get_channel_name(event_name=event_name)

        if channel_name not in self._subscriptions:
            self._subscriptions[channel_name] = []

        self._subscriptions[channel_name].append(subscriber)

    def send(self, event: BaseEvent) -> None:
        channel_name = self.get_channel_name(event_name=event.__class__.__name__)

        if channel_name in self._subscriptions:
            for subscriber in self._subscriptions[channel_name]:
                subscriber(event)

    def __call__(self, event: BaseEvent) -> None:
        self.send(event)

    def _get_subscriber_event_name(self, subscriber: Callable[..., Any]) -> str:
        signature = get_typed_signature(subscriber)
        signature_params = signature.parameters

        if "event" not in signature_params:
            raise EventNotProvidedError()

        event_class = signature_params["event"].annotation
        return f"{event_class.__name__}"

    def get_channel_name(self, event_name: str) -> str:
        channel_name = f"{self._channel_path}{self._channel_delimiter}{event_name}"
        return channel_name

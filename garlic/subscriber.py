from uuid import UUID

from garlic import BaseEvent


class Subscriber:
    _consumed_events: dict[UUID, BaseEvent]

    def __init__(self) -> None:
        self._consumed_events = {}

    def __call__(self, event: BaseEvent) -> None:
        self._check_duplicated_event(event)
        self._consumed_events[event.id] = event

    def _check_duplicated_event(self, event: BaseEvent) -> None:
        if event.id in self._consumed_events:
            raise ValueError(f"Event {event.id} already consumed")

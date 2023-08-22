import logging

from garlic import BaseEvent, Garlic

logger = logging.getLogger(__name__)

bus = Garlic()


class CustomerRegisteredEvent(BaseEvent):
    name: str


@bus.subscribe()
def send_email(event: CustomerRegisteredEvent):
    logger.info(f"Sending email to {event.name}")


@bus.subscribe()
def subscribe_to_newsletter(event: CustomerRegisteredEvent):
    logger.info(f"Subscribing {event.name} to newsletter")


if __name__ == "__main__":
    bus()

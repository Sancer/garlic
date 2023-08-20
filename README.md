# 🧄 Garlic

Craft powerful **Event-Driven Architectures (EDA)** in Python, effortlessly. With Garlic, respond to app events, like user actions, in a snap.

## Why Garlic?

**Simple, Yet Robust**: Drawing inspiration from tools like Celery and FastAPI, Garlic brings a fresh approach to EDA, making it approachable without sacrificing power.

- 🚀 **EDA Simplified**: Want actions like email notifications or newsletter sign-ups after a user registers? Garlic streamlines these event-driven responses.
- 📦 **FastAPI Inspired**: Just as FastAPI made web APIs intuitive, Garlic aims to demystify EDA.
- 🔍 **Beyond Regular Tasks**: While Celery is a go-to for background tasks, Garlic emphasizes responding to events.
- 📝 **Typed and Transparent**: Using Python typings, understand and control the data in your events.
- 🔌 **Flexible & Extendable**: Adapt and grow Garlic according to your needs.

## Coming Soon

📖 **Visual Event Flows**: We're building tools to visually map out your event-driven pathways, similar to how web routes are displayed in some platforms.

## Get Started
1. **Install**: 
```bash
pip install garlic
```
2. **Dive In**: FastAPI integration example

* Create a file `main.py` with:

```python
from fastapi import FastAPI
from garlic import Garlic, BaseEvent

bus = Garlic()

api = FastApi()


class CustomerRegisteredEvent(BaseEvent):
    name: str


@bus.subscribe()
def send_email(event: CustomerRegisteredEvent):
    pass


@bus.subscribe()
def subscribe_to_newsletter(event: CustomerRegisteredEvent):
    pass


@api.route('customer/register/')
def register_user(user: dict):
    # .... business logics  ....
    bus.emit(CustomerRegisteredEvent(
        name=user['name']
    ))
    # ... http response ...
```

* Run the app with `uvicorn main:api --reload`
* Send a POST request to `http://localhost:8000/customer/register/` with a JSON body like `{"name": "Uriel Reina"}`
* Check the terminal to see the event being published and handled by the subscribers


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

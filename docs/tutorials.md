# Tutorials

## Get Started
### Install Garlic
```bash
pip install garlic fastapi uvicorn
```

### Create a FastAPI app with Garlic

```python
# main.py
from fastapi import FastAPI
from garlic import Garlic, BaseEvent

bus = Garlic()

api = FastAPI()


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

### Run the code
```bash
uvicorn main:api --reload
```

### Test it out
* Send a POST request to `http://localhost:8000/customer/register/` with a JSON body like `{"name": "Uriel Reina"}`
* Check the terminal to see the event being published and handled by the subscribers
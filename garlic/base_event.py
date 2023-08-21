from datetime import datetime
from typing import Any, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class BaseEvent(BaseModel):
    id: UUID = uuid4()
    created_at: datetime = datetime.now()
    version: str = "1"
    payload: Optional[dict[Any, Any]] = None

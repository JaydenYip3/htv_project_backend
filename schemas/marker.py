from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel

class Marker(BaseModel):
    position: Any  # Can be list of floats or any JSON-serializable data
    description: str
    title: str
    category: str
    status: str = "Pending"  # Default value
    address_id: Optional[int] = None  # Optional foreign key to address


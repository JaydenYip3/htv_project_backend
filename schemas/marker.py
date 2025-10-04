from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel
from schemas.address import AddressCreate
from db.enums import MarkerCategory, MarkerUrgency, MarkerStatus

class Marker(BaseModel):
    position: Any  # Can be list of floats or any JSON-serializable data
    description: str
    title: str
    urgency: MarkerUrgency = MarkerUrgency.LOW  # Use enum with default
    category: MarkerCategory = MarkerCategory.OTHER  # Use enum with default
    status: MarkerStatus = MarkerStatus.PENDING  # Default value
    address_id: Optional[int] = None  # Optional foreign key to address
    address: Optional[AddressCreate] = None  # Nested address object
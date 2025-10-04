from datetime import datetime
from pydantic import BaseModel

class Marker(BaseModel):
    position: list[float]
    animal: str
    status: str


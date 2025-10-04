from pydantic import BaseModel

class Marker(BaseModel):
    position: list[float]
    animal: str
    timestamp: str
    status: str


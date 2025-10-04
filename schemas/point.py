from pydantic import BaseModel

class Point(BaseModel):
    point_x: int
    point_y: int
    animal: str
    timestamp: str


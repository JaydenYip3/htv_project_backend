from datetime import datetime
from typing import List, Any
from sqlmodel import Field, SQLModel, Column
from sqlalchemy import JSON

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Marker(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    position: Any = Field(sa_column=Column(JSON))
    animal: str
    timestamp: str
    status: str = Field(default="dead")
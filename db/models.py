from datetime import datetime
from typing import List, Any, Optional
from sqlmodel import Field, SQLModel, Column, Relationship
from sqlalchemy import JSON, ForeignKey

class Address(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    street: str
    city: str
    state: str
    postal_code: str
    country: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    # Back reference to markers
    markers: List["Marker"] = Relationship(back_populates="address")

class Item(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Marker(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    position: Any = Field(sa_column=Column(JSON))
    description: str
    title: str
    category: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="dead")
    
    # Foreign key to Address
    address_id: Optional[int] = Field(default=None, foreign_key="address.id")
    # Relationship to Address
    address: Optional[Address] = Relationship(back_populates="markers")
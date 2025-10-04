from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.db import get_session
from db.models import Item
from schemas.item import ItemCreate

router = APIRouter()


    

@router.post("/generate")
def generate_item(item_data: ItemCreate, session: Session = Depends(get_session)):
    """Generate/create a new item"""
    new_item = Item(name=item_data.name)
    session.add(new_item)
    session.commit()
    session.refresh(new_item)
    return {"message": f"Item '{item_data.name}' created successfully", "item": new_item}

@router.get("/items")
def get_items(session: Session = Depends(get_session)):
    """Get all items"""
    items = session.query(Item).all()
    return {"items": items}
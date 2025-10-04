from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.db import get_session
from db.models import Marker
from schemas.marker import Marker as MarkerSchema

router = APIRouter()

@router.get("/marker")
def get_markers(session: Session = Depends(get_session)):
    markers = session.query(Marker).all()
    return {"markers": markers}

@router.get("/marker/{marker_id}")
def get_marker(marker_id: int, session: Session = Depends(get_session)):
    marker = session.get(Marker, marker_id)
    if not marker:
        return {"message": f"Marker {marker_id} not found"}
    return {"marker": marker}

@router.post("/marker")
def create_marker(marker: MarkerSchema, session: Session = Depends(get_session)):
    new_marker = Marker(**marker.dict())
    session.add(new_marker)
    session.commit()
    session.refresh(new_marker)
    return {"message": f"Marker created successfully", "marker": new_marker}

@router.put("/marker/{marker_id}")
def update_marker(marker_id: int, marker: MarkerSchema, session: Session = Depends(get_session)):
    existing_marker = session.get(Marker, marker_id)
    if not existing_marker:
        return {"message": f"Marker {marker_id} not found"}
    for key, value in marker.dict().items():
        setattr(existing_marker, key, value)
    session.add(existing_marker)
    session.commit()
    return {"message": f"Marker {marker_id} updated"}
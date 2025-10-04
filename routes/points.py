from fastapi import APIRouter
import schemas.point as point_schema

router = APIRouter()

@router.get("/points")
def get_points():
    return {"message": "This is the points endpoint"}

@router.post("/points/{point_id}")
def create_point(point_id: int):
    return {"message": f"Point {point_id} created"}

@router.put("/points")
def update_point(point: point_schema.Point):
    return {"message": f"Point at ({point.point_x}, {point.point_y}) updated"}
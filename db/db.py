from typing import Generator
from sqlmodel import Session, SQLModel, create_engine
from db.models import Marker, Item

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db() -> None:
    SQLModel.metadata.create_all(engine)
    
    # Create initial data if tables are empty
    with Session(engine) as session:
        # Check if markers already exist
        existing_markers = session.query(Marker).first()
        if not existing_markers:
            # Create sample markers
            sample_markers = [
                Marker(
                    position=[43.78472822909501, -79.1861080766575], # UTSC coordiantes
                    animal="cat",
                    status="alive"
                ),
                Marker(
                    position=[40.7128, -74.0060],  # NYC coordinates
                    animal="dog",
                    status="dead"
                ),
                Marker(
                    position=[51.5074, -0.1278],   # London coordinates
                    animal="bird",
                    status="alive"
                )
            ]
            
            for marker in sample_markers:
                session.add(marker)
            
            session.commit()
            print("Database initialized with sample marker data")

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
from typing import Generator
from sqlmodel import Session, SQLModel, create_engine, select
from db.models import Marker
from db.fixture import sample_markers
DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db() -> None:
    SQLModel.metadata.create_all(engine)
    
    # Create initial data if tables are empty
    with Session(engine) as session:
        # Check if markers already exist
        existing_markers = session.exec(select(Marker)).first()
        if not existing_markers:
            # Create sample markers with correct schema
            for marker in sample_markers:
                session.add(marker)
            
            session.commit()
            print("Database initialized with sample marker data")

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
from typing import Generator
from sqlmodel import Session, SQLModel, create_engine
from db.models import Marker, Address

DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db() -> None:
    SQLModel.metadata.create_all(engine)
    
    # Create initial data if tables are empty
    with Session(engine) as session:
        # Check if markers already exist
        existing_markers = session.query(Marker).first()
        if not existing_markers:
            # Create sample markers with correct schema
            sample_markers = [
                Marker(
                    position=[43.78472822909501, -79.1861080766575],  # UTSC coordinates
                    description="A stray cat spotted near the campus",
                    title="Stray Cat Sighting",
                    category="Animal",
                    urgency="Low",
                    address=Address(
                        street="123 Campus Rd",
                        city="Toronto",
                        state="ON",
                        postal_code="M1C 1A4",
                        country="Canada"
                    )
                ),
                Marker(
                    position=[40.7128, -74.0060],  # NYC coordinates
                    description="Lost dog reported in the area",
                    title="Lost Dog",
                    category="Animal",
                    urgency="Low",
                    address=Address(
                        street="456 Dog St",
                        city="New York",
                        state="NY",
                        postal_code="10001",
                        country="USA"
                    )
 
                ),
                Marker(
                    position=[51.5074, -0.1278],   # London coordinates
                    description="Bird rescue needed",
                    title="Injured Bird",
                    category="Wildlife",
                    urgency="Low",
                    address=Address(
                        street="789 Bird Ln",
                        city="London",
                        state="N/A",
                        postal_code="SW1A 1AA",
                        country="UK"
                    )
                )
            ]
            
            for marker in sample_markers:
                session.add(marker)
            
            session.commit()
            print("Database initialized with sample marker data")

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
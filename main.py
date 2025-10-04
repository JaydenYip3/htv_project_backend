from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import points
from routes import items
from db.db import init_db

app = FastAPI(title="HTV Project API")

# Initialize database
init_db()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(points.router)
app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Welcome to HTV Project API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

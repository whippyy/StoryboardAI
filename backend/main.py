from fastapi import FastAPI
from routes import router
from database import engine
from models import Base

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "AI storyboard backend is running"}

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(router)
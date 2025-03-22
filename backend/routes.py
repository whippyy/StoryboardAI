from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Storyboard
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()

class StoryboardCreate(BaseModel):
    title: str 
    description: str

class StoryboardResponse(StoryboardCreate):
    id: int

# Create a storyboard
@router.post("/storyboards", response_model = StoryboardResponse)
def create_storyboard(storyboard: StoryboardCreate, db: Session = Depends(get_db)):
    new_storyboard = Storyboard(title = storyboard.title, description = storyboard.description)
    db.add(new_storyboard)
    db.commit()
    db.refresh(new_storyboard)
    return new_storyboard

# Get all storyboard
router.get("/storyboards", response_model=List[StoryboardResponse])
def get_storyboards(db: Session = Depends(get_db)):
    return db.query(Storyboard).all()

# Get single storyboard by ID
@router.get("/storyboards/{id}", response_model=StoryboardResponse)
def get_storyboard(id: int, db: Session = Depends(get_db)):
    storyboard = db.query(Storyboard).filter(Storyboard.id == id).first()
    if not storyboard:
        raise HTTPException(status_code=404, detail="Storyboard not found")
    return storyboard

# Delete a storyboard
@router.delete("/storyboards/{id}")
def delete_storyboard(id: int, db: Session = Depends(get_db)):
    storyboard = db.query(Storyboard).filter(Storyboard.id == id).first()
    if not storyboard:
        raise HTTPException(status_code=404, detail="Storyboard not found")
    db.delete(storyboard)
    db.commit()
    return {"message": "Storyboard deleted"}

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection URL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/storyboard_db")

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Ensure the connection works
try:
    with engine.connect() as conn:
        print("✅ Connected to the database!")
except Exception as e:
    print("❌ Database connection failed:", e)

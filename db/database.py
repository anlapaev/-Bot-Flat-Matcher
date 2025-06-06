import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def init_db():
    # Import models so that they are registered with the metadata
    from . import models  # noqa: F401
    models.Base.metadata.create_all(bind=engine)


from __future__ import annotations

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base_class import Base

load_dotenv()


engine = create_engine(os.getenv('DATABASE_URL'))
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

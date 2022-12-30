from __future__ import annotations

import logging
import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.base_class import Base
from app.models.country import Country
from app.models.enumerator import Enumerator
from app.models.fuel import FuelType
from app.models.photos import Photos
from app.models.project import Project
from app.models.project_data import ProjectData
from app.models.project_photos import ProjectPhotos
from app.models.region import Region
from app.models.surveyor import Surveyor
from app.models.village import Village
from app.models.district import District
from app.models.sector import Sector
from app.models.cell import Cell


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


load_dotenv()
try:
    engine = create_engine(os.getenv('DATABASE_URL'))
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    session = Session()
    logger.info('DB_OPERATIONS: Database created and tables initialized')
except Exception as e:
    logger.error('DB_OPERATIONS: Error: Database Initialization failed see error --> ', e)


def get_db() -> Generator:
    db = session
    try:
        yield db
    finally:
        db.close()


def init_db():
    # Drop all tables
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    logger.info('DB_OPERATIONS: Database created and tables initialized')

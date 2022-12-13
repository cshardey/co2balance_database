from __future__ import annotations

from datetime import datetime
from typing import List

import uvicorn
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.api_service import repository
from app.db.session import engine
from app.db.session import get_db
from app.db.session import session
from app.schema import base as base_schemas
from app.schema import project_data as project_data_schema

app = FastAPI(title='API Service for CO2balance',
              description='API access to project data', version='1.0.0')


@app.exception_handler(Exception)
def validation_exception_handler(request: Request, exc: Exception):
    base_error_message = f'Failed to execute request: {request.url.path} due to {exc}'
    return JSONResponse(
        status_code=400,
        content=jsonable_encoder({'detail': base_error_message}),
    )


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/project_data/{project_name}', response_model=List[project_data_schema.ProjectDataResponses])
def read_project_data(project_name: str, start_date: datetime, end_date: datetime, company_name: str, db: Session = Depends(get_db)):
    project_data = repository.ProjectDataRepository(db).get_by_date_range(
        start_date=start_date, end_date=end_date, project_name=project_name, comapny_name=company_name)
    if project_data is None:
        raise HTTPException(status_code=404, detail='Project data not found')
    return project_data


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)

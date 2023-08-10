# Fastapi
from fastapi import FastAPI, Depends
# DB
from db import models
from db.database import engine

from typing import Optional
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette import status
#  Routers
from routes import all

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(all.router)

@app.get('/')
async def root():
    return {"data": "start"}
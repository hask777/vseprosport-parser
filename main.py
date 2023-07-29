from fastapi import FastAPI, Depends
from db import models
from db.database import engine
from typing import Optional
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
from starlette import status

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
async def root():
    return {"data": "start"}
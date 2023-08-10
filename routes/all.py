from fastapi import APIRouter, Depends, Request
# DB
from db.models import Prediction
from db.database import engine, SessionLocal
from sqlalchemy.orm import Session
from routes.utils import get_db
# Date
from datetime import date


router = APIRouter(
    prefix='/all',
    tags=['all'],
    responses={404: {"description": "Not found"}}
)


# router all
@router.get('')
async def get_all(request: Request, db: Session = Depends(get_db)):
    today = str(date.today())

    predictions = db.query(Prediction).filter(Prediction.matchdate == '10.08.2023').all()

    # for pr in predictions:
    #     if f'победа' in pr.prediction2 and 'форой' not in pr.prediction2:
    #         print(pr.prediction2)

    for pr in predictions:
        if f'форой' in pr.prediction2 or 'фору' in pr.prediction2 or 'фора' in pr.prediction2:
            print(pr.prediction2)
    
    return predictions



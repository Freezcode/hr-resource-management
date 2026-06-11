from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.survey import SurveyResponse
from app.schemas import SurveyCreate, SurveyOut
from app.security import get_current_user


router = APIRouter(prefix="/surveys", tags=["surveys"])


@router.get("", response_model=list[SurveyOut])
def list_surveys(db: Session = Depends(get_db), _=Depends(get_current_user)):
    return db.query(SurveyResponse).all()


@router.post("", response_model=SurveyOut)
def create_survey(payload: SurveyCreate, db: Session = Depends(get_db), _=Depends(get_current_user)):
    survey = SurveyResponse(**payload.model_dump())
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey

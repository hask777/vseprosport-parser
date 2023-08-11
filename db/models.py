from sqlalchemy import Boolean, String, Integer, Column, ForeignKey, JSON, DateTime, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped
from db.database import Base
from typing import Dict
import datetime

class Prediction(Base):
    __tablename__ = 'predictions'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    country = Column(String)
    league = Column(String)
    matchtime = Column(String)
    matchdate = Column(String)
    home_team_link = Column(String)
    away_team_link = Column(String)
    home_team_img = Column(String)
    away_team_img = Column(String)
    home_team_name_en = Column(String)
    away_team_name_en = Column(String)
    home_team_name = Column(String)
    away_team_name = Column(String)
    author = Column(String)
    home_team_anons = Column(String)
    away_team_anons = Column(String)
    predictions = Column(JSON)
   
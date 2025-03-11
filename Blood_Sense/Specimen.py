"""
Datbase model for BloodSpecimen

"""
import datetime

from extensions.sql_alchemy import db
from sqlalchemy.sql import func
from dataclasses import dataclass
from sqlalchemy_serializer import SerializerMixin

@dataclass
class Specimen(db.Model,SerializerMixin):

  id:int = db.Column(db.Integer, primary_key=True, autoincrement=True) # unique id
  WBCSI:float = db.Column(db.Float, nullable=True) # white blood cell count
  LYPCT:float = db.Column(db.Float, nullable=True) # lymphocyte count
  MOPCT:float = db.Column(db.Float, nullable=True) # monocyte percent
  NEPCT:float = db.Column(db.Float, nullable=True) # segmented neutrophils percent
  EOPCT:float = db.Column(db.Float, nullable=True) # eiosinophils percent
  BAPCT:float = db.Column(db.Float, nullable=True) # basophils percenr
  LYMNO:float = db.Column(db.Float, nullable=True) # lymphocyte number
  MONO:float = db.Column(db.Float, nullable=True) # monocyte number
  NENO:float = db.Column(db.Float, nullable=True) # segmented neutrophils number
  EONO:float = db.Column(db.Float, nullable=True) # eosinophils number
  BANO:float = db.Column(db.Float, nullable=True) # basophils number
  RBCSI:float = db.Column(db.Float, nullable=True) # red blood cell count
  HGB:float = db.Column(db.Float, nullable=True) # hemoglobin
  HCT:float = db.Column(db.Float, nullable=True) # hematocrit
  PLTSI:float = db.Column(db.Float, nullable=True) # platlet count
  MCV: float = db.Column(db.Float, nullable=True) # Mean Corposcular Volume
  MCH: float = db.Column(db.Float, nullable=True) # Mean Corposcular Volume
  collected_at:datetime.datetime = db.Column(db.DateTime, nullable=True, default=func.now())
  created_at:datetime.datetime = db.Column(db.DateTime, nullable=True, default=func.now())
  deleted_at:datetime.datetime = db.Column(db.DateTime, nullable=True)
  def __repr__(self):
    return f'<Specimen {self.id}>'
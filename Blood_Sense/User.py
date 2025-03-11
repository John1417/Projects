import datetime

from extensions.sql_alchemy import db
from dataclasses import dataclass
from sqlalchemy_serializer import SerializerMixin


@dataclass
class User(db.Model):


    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    gender: str = db.Column(db.String(120), unique=False, nullable=False)
    bloodGroup: str = db.Column(db.String(5), unique=False, nullable=False)
    donatedOn: datetime.datetime = db.Column(db.DateTime(), unique=False, nullable=False)

    specimen_id: int = db.Column(db.Integer, db.ForeignKey('specimen.id'),nullable=False)
    specimen = db.Relationship('Specimen',backref="User",uselist=False)


    def __repr__(self):
        return '<User %r>' % self.username
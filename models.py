from sqlalchemy import Column, String, Date
from datetime import date
from app import db


class GeneralData(db.Model):

    __tablename__ = 'general_data'

    id = db.Column(db.Integer, primary_key=True)
    specialization = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    profile = Column(String)

    @classmethod
    def age(cls, date_of_birth):
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return age


class Skills(db.Model):

    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True)
    skill = Column(String(50))


class Qualities(db.Model):

    __tablename__ = 'qualities'

    id = db.Column(db.Integer, primary_key=True)
    qualities = Column(String(50))


class Contacts(db.Model):

    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(String(20))
    contact_value = db.Column(String(255))


class Languages(db.Model):

    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True)
    languages = Column(String(20))


class Experience(db.Model):

    __tablename__ = 'experience'

    id = db.Column(db.Integer, primary_key=True)
    company_name = Column(String, nullable=True)
    position = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    description = Column(String, nullable=True)

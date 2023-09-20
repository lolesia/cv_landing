from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *


menu = ['PROFILE', 'SKILLS', 'WORK EXPERIENCE', 'PERSONAL QUALITIES', 'LANGUAGE', 'CONTACTS']


@app.route("/")
def wtf():
    contacts = Contacts.query.all()
    skills = Skills.query.all()
    general_data = GeneralData.query.all()
    qualities = Qualities.query.all()
    experience = Experience.query.all()

    return render_template('wtf.html', contacts=contacts, skills=skills, general_data=general_data, qualities=qualities,
                           menu=menu, experience=experience,  title="ALESSA SHEVCHENKO | JUNIOR PYTHON DEVELOPER")


if __name__ == "__main__":
    app.run(debug=True)
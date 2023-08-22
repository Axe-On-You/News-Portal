from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

from . import models, views  # noqa

db.create_all()
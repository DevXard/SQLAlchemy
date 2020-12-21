from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


#MODELS

class Pet(db.Model):
    __tablename__ = 'pets'

    
    id = db.Column(db.Integer,
                    primery_key=True,
                    autoincrement=True)

    name = db.Column(db.String(50),
                    nullable=False,
                    unique=True)

    speacies = db.Column(db.String(30), nullable=True)

    hunger = db.Column(db.Integer, nullable=False, default=20)
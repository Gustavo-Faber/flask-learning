from application import db
from datetime import datetime

class Contatos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    shipping_date = db.Column(db.DateTime, default = datetime.utcnow())
    name = db.Column(db.String, nullable = True)
    email = db.Column(db.String, nullable = True)
    subject = db.Column(db.String, nullable = True)
    message = db.Column(db.String, nullable = True)

from climb import db
from datetime import datetime

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    sector = db.Column(db.String(50))
    location = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Record('{self.name}', '{self.grade}', '{self.sector}', '{self.location}')"
  
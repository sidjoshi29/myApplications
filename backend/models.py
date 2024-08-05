from app import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    notes = db.Column(db.Text, nullable=True)

    def to_json(self):      
        return {
            "id": self.id,
            "status": self.status,
            "role":self.role,
            "company": self.company,
            "notes": self.notes,
        }
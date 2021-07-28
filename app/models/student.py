from app import db


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    emailid = db.Column(db.String(200))
    courses= db.relationship('Courses', cascade="all,delete", backref='student')

    def __repr__(self):
        return f"Student('id:{self.id}','name:{self.name}','emailid:{self.emailid}')"

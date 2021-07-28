from app import db


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100))
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))

    def __repr__(self):
        return f"Course('id:{self.id}','course:{self.course}','student_id:{self.student_id}')"
db.create_all()
db.session.commit()
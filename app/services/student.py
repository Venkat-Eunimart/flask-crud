from flask import jsonify, request
from app import db,app
from app.models.student import Student
from app.schemas.students import students
from flask_json_schema import JsonSchema
schema = JsonSchema(app)
from app.util.errorhandler import handle_error
class Student_services:
    @staticmethod
    @handle_error
    def get_student():
        id = request.args.get('id')
        if id:
            students = Student.query.filter_by(id=id).first()
            return jsonify(Students=repr(students))

    @staticmethod
    @schema.validate(students)
    @handle_error
    def add_student():
        data = request.get_json()
        id = data["id"]
        name = data["name"]
        emailid = data["emailid"]
        if id and name and emailid:
            student = Student(id=id, name=name, emailid=emailid)
            db.session.add(student)
            db.session.commit()
            return "Inserted Successfully"

    @staticmethod
    @schema.validate(students)
    @handle_error
    def update_student():
        data=request.get_json()
        id=data['id']
        name = data["name"]
        emailid = data["emailid"]
        students = Student.query.filter_by(id=id).first()
        if id and name and emailid:
            students.id=id
            students.name=name
            students.emailid=emailid
            db.session.commit()
            return "Successfully updated"





    @staticmethod
    @handle_error
    def delete_student():
        data = request.get_json()
        id = data["id"]
        student = Student.query.filter_by(id=id).first()
        db.session.delete(student)
        db.session.commit()
        return "succesfully_deleted"

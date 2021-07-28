from flask import jsonify, request,Response
from app import db,app
from app.models.course import Courses
from app.schemas.course import courses
from flask_json_schema import JsonSchema
schema = JsonSchema(app)
from app.util.errorhandler import handle_error

class Course_services:
    @staticmethod
    @schema.validate(courses)
    @handle_error
    def add_course():
        data = request.get_json()
        id=data["id"]
        course = data["course"]
        sid = data["student_id"]
        if course and sid:
            course = Courses(id=id,course=course, student_id=sid)
            db.session.add(course)
            db.session.commit()
            return jsonify("Inserted Successfully")

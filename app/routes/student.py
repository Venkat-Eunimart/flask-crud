from app import app
from app.services.student import Student_services


app.add_url_rule(
    "/student", view_func=Student_services.get_student, methods=["GET"])

app.add_url_rule(
    "/addstudent", view_func=Student_services.add_student, methods=["POST"])

app.add_url_rule(
    "/updatestudent", view_func=Student_services.update_student, methods=["PUT"])

app.add_url_rule(
    "/dstudent", view_func=Student_services.delete_student, methods=["DELETE"]
)

from app import app
from app.services.course import Course_services



app.add_url_rule(
    "/addcourse", view_func=Course_services.add_course, methods=["POST"])

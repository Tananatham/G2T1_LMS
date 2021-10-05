from flask import Flask, request, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Class Class
class Class(db.Model):
    __tablename__ = 'class'

    class_id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50), nullable=False)
    start_time = db.Column(db.String(50), nullable=False)
    end_time = db.Column(db.String(50), nullable=False)
    class_size = db.Column(db.Integer, nullable=False)
    current_class_size = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.Integer, nullable=False)
    duration_of_class = db.Column(db.Integer, nullable=False)

    def __init__(self, class_id, lesson_id, course_name, start_date, end_date, start_time, end_time, class_size, current_class_size, employee_id, duration_of_class):
        self.class_id = class_id
        self.lesson_id = lesson_id
        self.course_name = course_name
        self.start_date = start_date
        self.end_date = end_date
        self.start_time = start_time
        self.end_time = end_time
        self.class_size = class_size
        self.current_class_size = current_class_size
        self.employee_id = employee_id
        self.duration_of_class = duration_of_class

    def json(self):
        return {"class_id": self.class_id, "lesson_id": self.lesson_id, "course_name": self.course_name, "start_date": self.start_date, "end_date": self.end_date, "start_time": self.start_time, "end_time": self.end_time, "class_size": self.class_size, "current_class_size": self.current_class_size, "employee_id": self.employee_id, "duration_of_class": self.duration_of_class}

# Get All Classes
@app.route("/class")
def get_all():
    classlist = Class.query.all()
    if len(classlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [classes.json() for classes in classlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

class Course(db.Model):
    __tablename__ = 'course'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(50), nullable=False)
    total_no_of_class = db.Column(db.Integer, nullable=False)
    total_no_of_lesson = db.Column(db.Integer, nullable=False)
    class_id = db.Column(db.Integer, nullable=False)
    course_description = db.Column(db.String(50), nullable=False)
    course_prerequisite = db.Column(db.String(50), nullable=False)
    coursem_id = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.String(50), nullable=False)
    end_time = db.Column(db.String(50), nullable=False)
    datetime_uploaded = db.Column(db.String(50), nullable=False)

    def __init__(self, course_id, course_name, total_no_of_class, total_no_of_lesson, class_id, course_description, course_prerequisite, coursem_id, employee_id, start_time, end_time, datetime_uploaded):
        self.course_id = course_id
        self.course_name = course_name
        self.total_no_of_class = total_no_of_class
        self.total_no_of_lesson = total_no_of_lesson
        self.class_id = class_id
        self.course_description = course_description
        self.course_prerequisite = course_prerequisite
        self.coursem_id = coursem_id
        self.employee_id = employee_id
        self.start_time = start_time
        self.end_time = end_time
        self.datetime_uploaded = datetime_uploaded

    def json(self):
        return {"course_id": self.course_id, "course_name": self.course_name, "total_no_of_class": self.total_no_of_class, "total_no_of_lesson": self.total_no_of_lesson, "class_id": self.class_id, "course_description": self.course_description, "coursem_id": self.coursem_id, "employee_id": self.employee_id, "start_time":self.start_time, "end_time":self.end_time, "datetime_uploaded":self.datetime_uploaded}

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

# Lesson Class

class Lesson(db.Model):
    __tablename__ = 'lesson'

    lesson_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, nullable=False)
    quiz_id = db.Column(db.Integer, nullable=False)
    coursem_id = db.Column(db.Integer, nullable=False)
    lesson_descriptions = db.Column(db.String(50), nullable=False)

    def __init__(self, lesson_id, class_id, course_id, quiz_id, coursem_id, lesson_descriptions):
        self.lesson_id = lesson_id
        self.class_id = class_id
        self.course_id = course_id
        self.quiz_id = quiz_id
        self.coursem_id = coursem_id
        self.lesson_descriptions = lesson_descriptions

    def json(self):
        return {"lesson_id": self.lesson_id, "class_id": self.class_id, "course_id": self.course_id, "quiz_id": self.quiz_id, "coursem_id": self.coursem_id, "section_description": self.section_description}


@app.route("/course")
def get_all():
    courselist = Course.query.all()
    if len(courselist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [course.json() for course in courselist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no courses."
        }
    ), 404

#  Get details of one course in JSON form
@app.route("/course/<string:course_id>")
def find_by_id(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        return jsonify(
            {
                "code": 200,
                "data": course.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    ), 404

#  POST Insert a new course
@app.route("/course", methods=['POST'])
def create():

    data = request.get_json()
    course = Course(None, **data)

    try:
        db.session.add(course)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred creating the course."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": course.json()
        }
    ), 201

#Update a course
@app.route("/course/<string:course_id>", methods=['PUT'])
def update(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    print(course)
    if course:
        data = request.get_json()
        if data['course_name']:
            course.course_name = data['course_name']
        if data['total_no_of_class']:
            course.total_no_of_class = data['total_no_of_class']
        if data['total_no_of_lesson']:
            course.total_no_of_lesson = data['total_no_of_lesson']
        if data['class_id']:
            course.class_id = data['class_id']
        if data['course_description']:
            course.course_description = data['course_description']
        if data['course_prerequisite']:
            course.course_prerequisite = data['course_prerequisite']
        if data['coursem_id']:
            course.coursem_id = data['coursem_id']
        if data['employee_id']:
            course.employee_id = data['employee_id']
        if data['start_time']:
            course.start_time = data['start_time']
        if data['end_time']:
            course.end_time = data['end_time']
        if data['datetime_uploaded']:
            course.datetime_uploaded = data['datetime_uploaded']

        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": course.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "course_id": course_id
            },
            "message": "Course is not found."
        }
    ), 404


@app.route("/course/<string:course_id>", methods=['DELETE'])
def delete(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        db.session.delete(course)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course_id": course_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "course_id": course_id
            },
            "message": "Course not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6900, debug=True)

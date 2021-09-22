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

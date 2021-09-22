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
    total_no_of_sections = db.Column(db.Integer, nullable=False)
    section_id = db.Column(db.Integer, nullable=False)
    course_description = db.Column(db.String(50), nullable=False)
    coursem_id = db.Column(db.Integer, nullable=False)
    trainer_id = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.String(50), nullable=False)
    end_time = db.Column(db.String(50), nullable=False)
    datetime_uploaded = db.Column(db.String(50), nullable=False)

    def __init__(self, course_id, course_name, total_no_of_sections, section_id, course_description, coursem_id, trainer_id, start_time, end_time, datetime_uploaded):
        self.course_id = course_id
        self.course_name = course_name
        self.total_no_of_sections = total_no_of_sections
        self.section_id = section_id
        self.course_description = course_description
        self.coursem_id = coursem_id
        self.trainer_id = trainer_id
        self.start_time = start_time
        self.end_time = end_time
        self.datetime_uploaded = datetime_uploaded

    def json(self):
        return {"course_id": self.course_id, "course_name": self.course_name, "total_no_of_sections": self.total_no_of_sections, "section_id": self.section_id, "course_description": self.course_description, "coursem_id": self.coursem_id, "trainer_id": self.trainer_id, "start_time":self.start_time, "end_time":self.end_time, "datetime_uploaded":self.datetime_uploaded}


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
        if data['total_no_of_sections']:
            course.total_no_of_sections = data['total_no_of_sections']
        if data['section_id']:
            course.section_id = data['section_id']
        if data['course_description']:
            course.course_description = data['course_description']
        if data['coursem_id']:
            course.coursem_id = data['coursem_id']
        if data['trainer_id']:
            course.trainer_id = data['trainer_id']
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

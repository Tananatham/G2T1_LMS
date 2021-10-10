import os
from flask import Flask, request, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost:3306/lms_course"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Lessons
class Lesson(db.Model):
    __tablename__ = 'lesson'

    lesson_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, nullable=True)
    course_id = db.Column(db.Integer, nullable=True)
    quiz_id = db.Column(db.Integer, nullable=True)
    coursem_id = db.Column(db.Integer, nullable=True)
    lesson_descriptions = db.Column(db.String(50), nullable=False)
    lesson_name = db.Column(db.String(50), nullable=False)
    quiz_type = db.Column(db.String(50), nullable=False)
    lesson_material = db.Column(db.String(200), nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, lesson_id, class_id, course_id, quiz_id, coursem_id, lesson_descriptions,lesson_name,quiz_type,lesson_material,created_on):
        self.lesson_id = lesson_id
        self.class_id = class_id
        self.course_id = course_id
        self.quiz_id = quiz_id
        self.coursem_id = coursem_id
        self.lesson_descriptions = lesson_descriptions
        self.lesson_name = lesson_name
        self.quiz_type = quiz_type
        self.lesson_material = lesson_material
        self.created_on = created_on

    def json(self):
        return {"lesson_id": self.lesson_id, "class_id": self.class_id, "course_id": self.course_id, "quiz_id": self.quiz_id, "coursem_id": self.coursem_id, "lesson_descriptions": self.lesson_descriptions, "lesson_name": self.lesson_name, "quiz_type": self.quiz_type, "lesson_material": self.lesson_material, "created_on": self.created_on}

# Get All Classes
@app.route("/lesson")
def get_all():
    lessonlist = Lesson.query.all()
    if len(lessonlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lessons": [lessons.json() for lessons in lessonlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no lesson."
        }
    ), 404

@app.route("/lesson/<int:lesson_id>")
def find_by_lessonid(lesson_id):
    lesson = Lesson.query.filter_by(lesson_id=lesson_id).first()
    if lesson:
        return jsonify(
            {
                "code": 200,
                "data": lesson.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Lesson not found."
        }
    ), 404

@app.route("/lessonclass/<int:class_id>")
def find_by_class_id(class_id):
    lesson = Lesson.query.filter_by(class_id=class_id).first()
    if lesson:
        return jsonify(
            {
                "code": 200,
                "data": lesson.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Lesson not found."
        }
    ), 404


@app.route("/lessons", methods=['POST'])
def create_lesson():

    data = request.get_json()
    print(data)
    lesson = Lesson(data)

    try:
        db.session.add(lesson)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred creating the book."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": lesson.json()
        }
    ), 201


#Update a lesson
@app.route("/lesson/<int:lesson_id>", methods=['PUT'])
def update(lesson_id):
    lesson = Lesson.query.filter_by(lesson_id=lesson_id).first()
    if lesson:
        data = request.get_json()
        if data['lesson_name']:
            lesson.lesson_name = data['lesson_name']
        if data['lesson_descriptions']:
            lesson.lesson_descriptions = data['lesson_descriptions']
        if data['quiz_type']:
            lesson.quiz_type = data['quiz_type']
        if data['lesson_material']:
            lesson.lesson_material = data['lesson_material'] 
        
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": lesson.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "lesson_id": lesson_id
            },
            "message": "Lesson is not found."
        }
    ), 404

#Delete a lesson 
@app.route("/lesson/<int:lesson_id>", methods=['DELETE'])
def delete(lesson_id):
    lesson = Lesson.query.filter_by(lesson_id=lesson_id).first()
    if lesson:
        db.session.delete(lesson)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lesson_id": lesson_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "lesson_id": lesson_id
            },
            "message": "Lesson not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    

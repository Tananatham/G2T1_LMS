from flask import Flask, request, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Lessons
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
        return {"lesson_id": self.lesson_id, "class_id": self.class_id, "course_id": self.course_id, "quiz_id": self.quiz_id, "coursem_id": self.coursem_id, "lesson_descriptions": self.lesson_descriptions}

# Get All lessons
@app.route("/lesson")
def get_all_lessons():
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

#  Get details of one lesson in JSON form
@app.route("/lesson/<string:lesson_id>")
def find_by_lessonid2(lesson_id):
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

#  POST > Insert a new lesson
@app.route("/lesson", methods=['POST'])
def create_lesson():

    data = request.get_json()
    lesson = Lesson(None, **data)

    try:
        db.session.add(lesson)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred creating the lesson."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": lesson.json()
        }
    ), 201

# Update a lesson
@app.route("/lesson/<string:lesson_id>", methods=['PUT'])
def update_lesson(lesson_id):
    lesson = Lesson.query.filter_by(lesson_id=lesson_id).first()
    print(lesson)
    if lesson:
        data = request.get_json()
        if data['lesson_id']:
            lesson.lesson_id = data['lesson_id']
        if data['class_id']:
            lesson.class_id = data['class_id']
        if data['course_id']:
            lesson.course_id = data['course_id']
        if data['quiz_id']:
            lesson.quiz_id = data['quiz_id']
        if data['coursem_id']:
            lesson.coursem_id = data['coursem_id']
        if data['lesson_descriptions']:
            lesson.lesson_descriptions = data['lesson_descriptions']
        
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

# Delete a lesson
@app.route("/lesson/<string:lesson_id>", methods=['DELETE'])
def delete_lesson(lesson_id):
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

    

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

    

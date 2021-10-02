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

#Create Quiz
class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(50), nullable=False)
    quiz_type = db.Column(db.String(10), nullable=False)
    quizq_id = db.Column(db.Integer, nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.lesson_id'), nullable=False)
    quiz_descriptions = db.Column(db.String(50), nullable=False)
    datetime_created = db.Column(db.DateTime, nullable=False)
    passing_score = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
    quiz_details = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
   
    def __init__(self, quiz_id, quiz_name, quiz_type, quizq_id, lesson_id, quiz_descriptions, datetime_created, passing_score, start_time, end_time, quiz_details, correct_answer):
        self.quiz_id = quiz_id
        self.quiz_name = quiz_name
        self.quiz_type = quiz_type
        self.quizq_id = quizq_id
        self.lesson_id =  lesson_id
        self.quiz_descriptions = quiz_descriptions
        self.datetime_created = datetime_created
        self.passing_score = passing_score
        self.start_time = start_time
        self.end_time = end_time
        self.quiz_details = quiz_details
        self.correct_answer = correct_answer

    def json(self):
        return {"quiz_id": self.quiz_id, "quiz_name": self.quiz_name, "quizq_id": self.quizq_id, "lesson_id": self.lesson_id, "quiz_descriptions": self.quiz_descriptions, "datetime_created": self.datetime_created, "passing_score": self.passing_score, "start_time":self.start_time, "end_time":self.end_time, "quiz_details":self.quiz_details, "correct_answer":self.correct_answer}

# Class QuizQuestions
# class Quizq(db.Model):
#     __tablename__ = 'quizq'
#     quizq_id = db.Column(db.Integer, primary_key=True)
#     quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.quiz_id'), nullable=False)
#     quiz_name = db.Column(db.String(10), nullable=False)
#     lesson_id = db.Column(db.Integer, nullable=False)
#     quiz_details = db.Column(db.String(100), nullable=False)
#     correct_answer = db.Column(db.String(100), nullable=False)
   
#     def __init__(self, quizq_id, quiz_id, quiz_name, lesson_id, quiz_details, correct_answer):
#         self.quizq_id = quizq_id
#         self.quiz_id = quiz_id
#         self.quiz_name = quiz_name
#         self.lesson_id =  lesson_id
#         self.quiz_details = quiz_details
#         self.correct_answer = correct_answer

#     def json(self):
#         return {"quizq_id": self.quizq_id,"quiz_id": self.quiz_id, "quiz_name": self.quiz_name, "lesson_id": self.lesson_id, "quiz_details": self.quiz_details, "correct_answer": self.correct_answer}


# Get all quiz
@app.route("/quiz")
def get_all():
    quizlist = Quiz.query.all()
    if len(quizlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz": [quiz.json() for quiz in quizlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no quiz."
        }
    ), 404

#  Get details of one quiz in JSON form
@app.route("/quiz/<string:lesson_id>")
def find_by_id(lesson_id):
    quiz = Quiz.query.filter_by(lesson_id=lesson_id).first()
    if quiz:
        return jsonify(
            {
                "code": 200,
                "data": quiz.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    ), 404

#  POST > Insert a new quiz
@app.route("/quiz", methods=['POST'])
def create():

    data = request.get_json()
    quiz = Quiz(None, **data)

    try:
        db.session.add(quiz)
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
            "data": quiz.json()
        }
    ), 201

#Update a quiz
@app.route("/quiz/<string:quiz_id>", methods=['PUT'])
def update(quiz_id):
    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()
    print(quiz)
    if quiz:
        data = request.get_json()
        if data['quiz_name']:
            quiz.quiz_name = data['quiz_name']
        if data['quiz_type']:
            quiz.quiz_type = data['quiz_type']
        if data['quiz_description']:
            quiz.quiz_description = data['quiz_description']
        if data['passing_score']:
            quiz.passing_score = data['passing_score']
        if data['start_time']:
            quiz.start_time = data['start_time']
        if data['end_time']:
            quiz.end_time = data['end_time']
        if data['quiz_details']:
            quiz.quiz_details = data['quiz_details']
        if data['correct_answer']:
            quiz.correct_answer = data['correct_answer']    
        
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": quiz.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "quiz_id": quiz_id
            },
            "message": "Course is not found."
        }
    ), 404

#Delete a quiz 
@app.route("/quiz/<string:quiz_id>", methods=['DELETE'])
def delete(quiz_id):
    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()
    if quiz:
        db.session.delete(quiz)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "quiz_id": quiz_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "quiz_id": quiz_id
            },
            "message": "Course not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost:3306/lms_course"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)

#Create Quiz
class Quiz(db.Model):
    __tablename__ = 'quiz'

    quiz_id = db.Column(db.Integer, primary_key=True)
    quiz_type = db.Column(db.String(10), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.lesson_id'), nullable=False)
    quiz_question = db.Column(db.String(50), nullable=False)
    datetime_created = db.Column(db.DateTime, nullable=False)
    passing_score = db.Column(db.Integer, nullable=True)
    question_type = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)
    time_limit = db.Column(db.String(50), nullable=False)
    quiz_selection = db.Column(db.String(500), nullable=False)
   
    def __init__(self, quiz_id, quiz_type, lesson_id, quiz_question, datetime_created, passing_score, question_type, correct_answer,time_limit,quiz_selection):
        self.quiz_id = quiz_id
        self.quiz_type = quiz_type
        self.lesson_id =  lesson_id
        self.quiz_question = quiz_question
        self.datetime_created = datetime_created
        self.passing_score = passing_score
        self.question_type = question_type
        self.correct_answer = correct_answer
        self.time_limit = time_limit
        self.quiz_selection = quiz_selection

    def json(self):
        return {"quiz_id": self.quiz_id, "quiz_type": self.quiz_type, "lesson_id": self.lesson_id, "quiz_question": self.quiz_question, "datetime_created": self.datetime_created, "passing_score": self.passing_score, "question_type":self.question_type, "correct_answer":self.correct_answer, "time_limit":self.time_limit, "quiz_selection":self.quiz_selection}

# Get all quiz
@app.route("/quiz")
def get_all_quiz():
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
def find_by_id_quiz(lesson_id):
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
def create_quiz():

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
                "message": "An error occurred creating the quiz."
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
def update_quiz(quiz_id):
    quiz = Quiz.query.filter_by(quiz_id=quiz_id).first()
    print(quiz)
    if quiz:
        data = request.get_json()
        if data['quiz_type']:
            quiz.quiz_type = data['quiz_type']
        if data['quiz_question']:
            quiz.quiz_question = data['quiz_question']
        if data['passing_score']:
            quiz.passing_score = data['passing_score']
        if data['question_type']:
            quiz.question_type = data['question_type']
        if data['correct_answer']:
            quiz.correct_answer = data['correct_answer']    
        if data['time_limit']:
            quiz.time_limit = data['time_limit']
        if data['quiz_selection']:
            quiz.quiz_selection = data['quiz_selection']
        
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
def delete_quiz(quiz_id):
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

#Lesson
class Lesson(db.Model):
    __tablename__ = 'lesson'

    lesson_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, nullable=False)
    quiz_id = db.Column(db.Integer, nullable=False)
    lesson_descriptions = db.Column(db.String(50), nullable=False)
    lesson_name = db.Column(db.String(50), nullable=False)
    quiz_type = db.Column(db.String(50), nullable=False)
    lesson_material = db.Column(db.String(100), nullable=True)
    created_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, lesson_id, class_id, course_id, quiz_id, lesson_descriptions,lesson_name,quiz_type,lesson_material,created_on):
        self.lesson_id = lesson_id
        self.class_id = class_id
        self.course_id = course_id
        self.quiz_id = quiz_id
        self.lesson_descriptions = lesson_descriptions
        self.lesson_name = lesson_name
        self.quiz_type = quiz_type
        self.lesson_material = lesson_material
        self.created_on = created_on

    def json(self):
        return {"lesson_id": self.lesson_id, "class_id": self.class_id, "course_id": self.course_id, "quiz_id": self.quiz_id, "lesson_descriptions": self.lesson_descriptions, "lesson_name": self.lesson_name, "quiz_type": self.quiz_type, "lesson_material": self.lesson_material, "created_on": self.created_on}

# Get All Classes
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
def find_by_class_id_lessons(class_id):
    lesson = Lesson.query.filter_by(class_id=class_id).all()
    if len(lesson):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lessons": [lessons.json() for lessons in lesson]
                }
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
    lesson = Lesson(None,**data)

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
def update_lesson(lesson_id):
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
def get_all_classes():
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
            "message": "There are no class."
        }
    ), 404

#  Get details of one class in JSON form by class id
@app.route("/quiz/<string:class_id>")
def find_by_classid(class_id):
    a_class = Class.query.filter_by(class_id=class_id).first()
    if a_class:
        return jsonify(
            {
                "code": 200,
                "data": a_class.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Class not found."
        }
    ), 404

#  POST > Insert a new class
@app.route("/class", methods=['POST'])
def create_class():

    data = request.get_json()
    new_class = Class(None, **data)

    try:
        db.session.add(new_class)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                },
                "message": "An error occurred creating the class."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": new_class.json()
        }
    ), 201

# Update a class
@app.route("/class/<string:class_id>", methods=['PUT'])
def update_class(class_id):
    a_class = Class.query.filter_by(class_id=class_id).first()
    print(a_class)
    if a_class:
        data = request.get_json()
        if data['class_id']:
            a_class.class_id = data['class_id']
        if data['lesson_id']:
            a_class.lesson_id = data['lesson_id']
        if data['course_name']:
            a_class.course_namen = data['course_name']
        if data['start_date']:
            a_class.start_date = data['start_date']
        if data['end_date']:
            a_class.end_date = data['end_date']
        if data['start_time']:
            a_class.start_time = data['start_time']
        if data['end_time']:
            a_class.end_time = data['end_time']
        if data['class_size']:
            a_class.class_size = data['class_size']    
        if data['current_class_size']:
            a_class.current_class_size = data['current_class_size']   
        if data['employee_id']:
            a_class.employee_id = data['employee_id']   
        if data['duration_of_class']:
            a_class.duration_of_class = data['duration_of_class']   
        
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": a_class.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "class_id": class_id
            },
            "message": "Class is not found."
        }
    ), 404

# Delete a class
@app.route("/class/<string:class_id>", methods=['DELETE'])
def delete_class(class_id):
    a_class = Class.query.filter_by(class_id=class_id).first()
    if a_class:
        db.session.delete(a_class)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": {
                    "class_id": class_id
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "class_id": class_id
            },
            "message": "Class not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

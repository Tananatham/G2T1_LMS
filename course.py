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


class Employee(db.Model):
    __tablename__ = 'employee'

    employee_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, nullable=True)
    employee_name = db.Column(db.String(50), nullable=False)
    employee_role = db.Column(db.String(50), nullable=False)

    def __init__(self, employee_id, course_id, employee_name, employee_role):
        self.employee_id = employee_id
        self.course_id = course_id
        self.employee_name = employee_name
        self.employee_role = employee_role
    
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def json(self):
        return {"employee_id": self.employee_id, "course_id": self.course_id, "employee_name": self.employee_name, "employee_role": self.employee_role}


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

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def json(self):
        return {"course_id": self.course_id, "course_name": self.course_name, "total_no_of_class": self.total_no_of_class, "total_no_of_lesson": self.total_no_of_lesson, "class_id": self.class_id, "course_description": self.course_description, "course_prerequisite": self.course_prerequisite, "coursem_id": self.coursem_id, "employee_id": self.employee_id, "start_time":self.start_time, "end_time":self.end_time, "datetime_uploaded":self.datetime_uploaded}

# Class Class
class Class(db.Model):
    __tablename__ = 'class'

    class_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, nullable=False)
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

    def __init__(self, class_id, course_id, lesson_id, course_name, start_date, end_date, start_time, end_time, class_size, current_class_size, employee_id, duration_of_class):
        self.class_id = class_id
        self.course_id = course_id
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
    
    def class_enroll(self):
        """
        Add one to class size
        """
        if self.current_class_size < self.class_size:
            self.current_class_size += 1
        else:
            raise Exception("Class is now full.")

    def class_withdraw(self):
        """
        When a student finish or withdraw a class
        """
        if self.current_class_size >= 0:
            self.current_class_size -= 1
        else:
            raise Exception("Class size cannot be less than zero.")

    def json(self):
        return {"class_id": self.class_id, "course_id": self.course_id, "lesson_id": self.lesson_id, "course_name": self.course_name, "start_date": self.start_date, "end_date": self.end_date, "start_time": self.start_time, "end_time": self.end_time, "class_size": self.class_size, "current_class_size": self.current_class_size, "employee_id": self.employee_id, "duration_of_class": self.duration_of_class}

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
        return {"lesson_id": self.lesson_id, "class_id": self.class_id, "course_id": self.course_id, "quiz_id": self.quiz_id, "coursem_id": self.coursem_id, "lesson_descriptions": self.lesson_descriptions}

class Course_check(db.Model):
    __tablename__ = 'employee_enrolled'

    employee_id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, employee_id, course_id, class_id, status):
        self.employee_id = employee_id
        self.course_id = course_id
        self.class_id = class_id
        self.status = status
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def json(self):
        return {"employee_id": self.employee_id, "course_id": self.course_id, "class_id": self.class_id, "status": self.status}


class PrerequisiteCheck(db.Model):
    __tablename__ = 'course_prerequisite'

    course_id = db.Column(db.Integer, primary_key=True)
    prerequisite_course_id = db.Column(db.Integer, primary_key=True)

    def __init__(self, course_id, prerequisite_course_id):
        self.course_id = course_id
        self.prerequisite_course_id = prerequisite_course_id
    
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def json(self):
        return {"course_id": self.course_id, "prerequisite_course_id": self.prerequisite_course_id}


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


def employee_course_prerequisite_check(employee_id, course_id):
    employee_completed_course = Course_check.query.filter_by(employee_id=employee_id).filter_by(status="completed")
    employee_completed_json = [data.json() for data in employee_completed_course]
    employee_completed_array = []
    for json in employee_completed_json:
        employee_completed_array.append(json["course_id"])

    course_prerequisite = PrerequisiteCheck.query.filter_by(course_id=course_id)
    course_prerequisite_json = [course.json() for course in course_prerequisite]
    prerequisite_array = []
    for json in course_prerequisite_json:
        prerequisite_array.append(json["prerequisite_course_id"])

    if set(prerequisite_array).issubset(set(employee_completed_array)):
        return True
    else:
        return False

def course_prereq_okay_check(course_id, preq_course_id):
    if course_id == preq_course_id:
        return False
    
    course_prerequisite = PrerequisiteCheck.query.filter_by(course_id=course_id)
    course_prerequisite_json = [data.json() for data in course_prerequisite]
    course_prerequisite_array = []
    for json in course_prerequisite_json:
        course_prerequisite_array.append(json["prerequisite_course_id"])
    
    course_prerequisite_reverse = PrerequisiteCheck.query.filter_by(prerequisite_course_id=preq_course_id)
    course_prerequisite_reverse_json = [data.json() for data in course_prerequisite_reverse]
    course_prerequisite_reverse_array = []
    for json in course_prerequisite_reverse_json:
        course_prerequisite_reverse_array.append(json["prerequisite_course_id"])

    if preq_course_id in course_prerequisite_array or course_id in course_prerequisite_reverse_array:
        return False
    else:
        return True

@app.route("/employee_name_lookup")
def name_lookup_employee():
    search_name = request.args.get('name')
    if search_name:
        employee_list = Employee.query.filter(Employee.employee_name.contains(search_name))
    else:
        employee_list = Employee.query.all()
    return jsonify(
        {
            "data": [employee.to_dict() for employee in employee_list]
        }
    ), 200


#Create a course status
@app.route("/employee_course_status", methods=['POST'])
def create_status():
    data = request.get_json()

    employee_id = data["employee_id"]
    course_id = data["course_id"]
    if employee_course_prerequisite_check(employee_id, course_id):
        new_status = Course_check(**data)
        try:
            db.session.add(new_status)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                    },
                    "message": "An error occurred with enrollment. The employee may have already been enrolled or completed the course."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": new_status.json()
            }
        ), 201

    else:
        return jsonify(
            {
                "code": 500,
                "data": {},
                "message": "This ID has not completed all of the prerequisite courses!"
            }
        ), 500

    
@app.route("/set_course_prerequisite", methods=['POST'])
def set_course_prereq():
    data = request.get_json()

    course_id = data["course_id"]
    prerequisite_course_id = data["prerequisite_course_id"]

    if course_prereq_okay_check(course_id, prerequisite_course_id):
        new_status = PrerequisiteCheck(**data)
        try:
            db.session.add(new_status)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                    },
                    "message": "An error occurred with setting a prerequisite."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": new_status.json()
            }
        ), 201

    else:
        return jsonify(
            {
                "code": 500,
                "data": {},
                "message": "An error occured, the course is already a prerequisite, or it's the same course."
            }
        ), 500
    

#Find the course IDs that a student completed
@app.route("/employee_course_status/<string:employee_id>")
def find_status_by_id(employee_id):
    courselist = Course_check.query.filter_by(employee_id=employee_id).filter_by(status="completed")
    if courselist:
        course_json = [course.json() for course in courselist]
        completed_course_id = []
        for json in course_json:
            completed_course_id.append(json["course_id"])
        return jsonify(
            {
                "code": 201,
                "data": {
                    "course": completed_course_id
                }
                    
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Data not found."
        }
    ), 404


#Find the course IDs that a student is in progress
@app.route("/employee_course_status_progress/<string:employee_id>")
def find_employee_in_progress(employee_id):
    courselist = Course_check.query.filter_by(employee_id=employee_id).filter_by(status="in-progress")
    if courselist:
        course_json = [course.json() for course in courselist]
        completed_course_id = []
        for json in course_json:
            completed_course_id.append(json["course_id"])
        return jsonify(
            {
                "code": 201,
                "data": {
                    "course": completed_course_id
                }
                    
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Data not found."
        }
    ), 404

#Find all the prerequiste of a course
@app.route("/course_prerequisite/<string:course_id>")
def find_prerequisites_by_id(course_id):
    courselist = PrerequisiteCheck.query.filter_by(course_id=course_id)
    if courselist:
        course_json = [course.json() for course in courselist]
        prerequsities = []
        for json in course_json:
            prerequsities.append(json["prerequisite_course_id"])
        return jsonify(
            {
                "code": 201,
                "data": {
                    "prerequsities": prerequsities
                }
                    
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Data not found."
        }
    ), 404

#Find the course name
@app.route("/course_name/<string:course_id>")
def find_course_name_by_id(course_id):
    course = Course.query.filter_by(course_id=course_id).first()
    if course:
        course_name = course.course_name
        return jsonify(
            {
                "code": 200,
                "data": course_name
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Course not found."
        }
    ), 404


#Update a course status
@app.route("/employee_course_status/", methods=['PUT'])
def update_status():
    employee_id = request.args.get('employee_id',1,type=int)
    course_id = request.args.get('course_id',1,type=int)

    status_data = Course_check.query.filter_by(employee_id=employee_id).filter_by(course_id=course_id).first()

    if status_data:
        data = request.get_json()
        if data['status']:
            status_data.status = data['status']

        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": status_data.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "employee_id": employee_id
            },
            "message": "Data is not found."
        }
    ), 404

#Update a course status
@app.route("/class_enrollment/", methods=['PUT'])
def update_class_enrollment():
    employee_id = request.args.get('employee_id',1,type=int)
    course_id = request.args.get('course_id',1,type=int)

    status_data = Course_check.query.filter_by(employee_id=employee_id).filter_by(course_id=course_id).first()

    if status_data:
        data = request.get_json()
        if data['class_id']:
            status_data.class_id = data['class_id']
            class_data = Class.query.filter_by(class_id=data['class_id']).first()
            class_data.class_enroll()
        try:
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
                "code": 200,
                "data": status_data.json()
            }
        )
    
    return jsonify(
        {
            "code": 404,
            "data": {
                "employee_id": employee_id
            },
            "message": "An error occured, the class might be full."
        }
    ), 404

@app.route("/employee_course_status/", methods=['DELETE'])
def delete_status():
    employee_id = request.args.get('employee_id',1,type=int)
    course_id = request.args.get('course_id',1,type=int)

    status_data = Course_check.query.filter_by(employee_id=employee_id).filter_by(course_id=course_id).first()
    if status_data:
        db.session.delete(status_data)
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
            "message": "Status not found."
        }
    ), 404

# Get All course enrollment with pending
@app.route("/enrollment_pending")
def get_pending_enrollment():
    courselist = Course_check.query.filter_by(status="pending")
    if courselist:
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

# Get All course enrollment with in-progress
@app.route("/enrollment_in_progress")
def get_in_progress_enrollment():
    courselist = Course_check.query.filter_by(status="in-progress")
    if courselist:
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

#  Get All employee/learners 
@app.route("/employee")
def get_all_employees():
    employeelist = Employee.query.all()
    if len(employeelist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "employee":[employee.json() for employee in employeelist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Employee not found."
        }
    ), 404

#  Get details of one employee 
@app.route("/employee/<string:employee_id>")
def find_employee_by_id(employee_id):
    employee = Employee.query.filter_by(employee_id=employee_id).first()
    if employee:
        return jsonify(
            {
                "code": 200,
                "data": employee.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Employee not found."
        }
    ), 404

# Get All Courses
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

#  Get details of one course 
@app.route("/course/<string:course_id>")
def find_by_course_id(course_id):
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

#find lesson by class ID
@app.route("/lesson_by_class_id/<string:class_id>")
def find_lesson_by_class_id(class_id):
    lessonlist = Lesson.query.filter_by(class_id=class_id)
    if lessonlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "lesson": [lesson.json() for lesson in lessonlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Lessons not found for this course ID."
        }
    ), 404

#find classes by course ID
@app.route("/class_by_course_id/<string:course_id>")
def find_classes_by_course_id(course_id):
    classlist = Class.query.filter_by(course_id=course_id)
    if classlist:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "class": [classes.json() for classes in classlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Classes not found for this course ID."
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
    except Exception:
        return jsonify({
            "message": "The Class is probably full."
        }), 500

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
def find_by_lessonid(lesson_id):
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
            "message": "Quiz not found."
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

# Update a quiz
@app.route("/quiz/<string:quiz_id>", methods=['PUT'])
def update_quiz(quiz_id):
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
            "message": "Quiz is not found."
        }
    ), 404

# Delete a quiz 
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
            "message": "Quiz not found."
        }
    ), 404


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
    app.run(host='0.0.0.0', port=6900, debug=True)

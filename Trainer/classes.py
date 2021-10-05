from flask import Flask, request, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


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
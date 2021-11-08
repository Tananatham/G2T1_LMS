import unittest   
import flask_testing
import json
from datetime import datetime
from freezegun import freeze_time
from werkzeug.wrappers import request

from course import Course_check, app,db, Employee, Course, Class, Lesson,Quiz

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

#Author: Chelsea
class TestEmployee(TestApp):
    maxDiff = None
    def test_name_lookup_employee(self):
        e1 = Employee(employee_id=1, course_id=2, employee_name="Tom", employee_role="HR")

        db.session.add(e1)
        db.session.commit
    
        request_body = {
            "employee_name": "Tom"

        }

        response = self.client.get("/employee_name_lookup",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json['data'], { 
            "course_id": 2,
            "employee_id": 1,
            "employee_name": "Tom",
            "employee_role": "HR"
        })

     # line 508
    def test_find_status_by_id(self):
        C1 = Course_check(employee_id= 1, course_id= 4, class_id= 1, status= 'completed')

        db.session.add(C1)
        db.session.commit()

        response = self.client.get("/employee_course_status/1", content_type='application/json')
        self.assertEqual(response.json['code'], 201)
        self.assertEqual(response.json['data'], { 'course': [4]})

    # line 533
    def test_find_inprogress_class_id(self):
        e1 = Course_check(employee_id=1, course_id=5, class_id=2, status= 'in-progress')
        c2 = Class(class_id=2, course_id=5, lesson_id=1, course_name="something", start_date="01/01/2021", end_date="02/02/2021", start_time="12:00", end_time="3:00", class_size=10, current_class_size=2, employee_id="1", duration_of_class= 3)

        db.session.add(e1)
        db.session.add(c2)
        db.session.commit()

        response = self.client.get("/class_by_engineer_in_progress/1/5", content_type='application/json')
        self.assertEqual(response.json['code'], 201)
        self.assertEqual(response.json['data'], { 
            "class": [
                {
                    "class_id": 2, 
                    "course_id": 5, 
                    "lesson_id": 1, 
                    "course_name": "something", 
                    "start_date": "01/01/2021", 
                    "end_date": "02/02/2021", 
                    "start_time": "12:00", 
                    "end_time": "3:00", 
                    "class_size": 10, 
                    "current_class_size": 2, 
                    "employee_id": 1, 
                    "duration_of_class": 3
                }
            ]
        })
       
    #line 564   
    def test_find_employee_in_progress(self):
        C1 = Course_check(employee_id= 1, course_id= 4, class_id= 1, status= 'in-progress')

        db.session.add(C1)
        db.session.commit()

        response = self.client.get("/employee_course_status_progress/1", content_type='application/json')
        self.assertEqual(response.json['code'], 201)
        self.assertEqual(response.json['data'], { 'course': [4]})

    #line 633 wrong
    def test_delete_status(self):
        e1 = Course_check(employee_id=1, course_id=5, class_id=2, status= 'completed')
        c2 = Class(class_id=2, course_id=5, lesson_id=1, course_name="something", start_date="01/01/2021", end_date="02/02/2021", start_time="12:00", end_time="3:00", class_size=10, current_class_size=2, employee_id="1", duration_of_class= 3)

        db.session.add(e1)
        db.session.add(c2)
        db.session.commit()

        request_body = {
            "course_id": c2.course_id,
            "employee_id": c2.employee_id,
            "class_id": c2.class_id,
        }

        response = self.client.delete("/employee_course_status/",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json['code'], 200)
        self.assertEqual(response.json['data'], { 'course': 5})


#Author: Tantham 
class TestCourse(TestApp):

    def test_find_prerequisites_by_id(self):
        course1 = Course(course_id = 1, course_name = 'Chemical engineering', total_no_of_class = 1, total_no_of_lesson = 1, class_id = 1, course_description = 'This type of engineering concerns the use of chemical and biological processes to produce useful materials or substances. It’s a multidisciplinary subject, combining natural and experimental sciences (such as chemistry and physics), along with life sciences (such as biology, microbiology and biochemistry), plus mathematics and economics.', course_prerequisite = 5, coursem_id = 1, employee_id = 2, start_time = '1 July 2021', end_time = '1 December 2021', datetime_uploaded = '2021-06-23 00:00:00', start_enrol= '2021-06-23', end_enrol= '2021-06-23')
        db.session.add(course1)
        db.session.commit()
        response = self.client.get("/course_prerequisite/1")
        self.assertEqual(response.json['code'], 200)
        self.assertEqual(response.json['data'], 5)

    def test_find_course_name_by_id(self):
        course1 = Course(course_id = 1, course_name = 'Chemical engineering', total_no_of_class = 1, total_no_of_lesson = 1, class_id = 1, course_description = 'This type of engineering concerns the use of chemical and biological processes to produce useful materials or substances. It’s a multidisciplinary subject, combining natural and experimental sciences (such as chemistry and physics), along with life sciences (such as biology, microbiology and biochemistry), plus mathematics and economics.', course_prerequisite = 0, coursem_id = 1, employee_id = 2, start_time = '1 July 2021', end_time = '1 December 2021', datetime_uploaded = '2021-06-23 00:00:00', start_enrol= '2021-06-23', end_enrol= '2021-06-23')
        db.session.add(course1)
        db.session.commit()
        response = self.client.get("/course_name/1")
        self.assertEqual(response.json['code'], 200)
        self.assertEqual(response.json['data'], 'Chemical engineering')

    # def test_create(self):
    #     request_body = {
    #         'course_id': 3, 
    #         'course_name' : 'Chemical engineering',  
    #         'total_no_of_class' : 1,
    #         'total_no_of_lesson' : 1,
    #         'class_id' : 1,
    #         'course_description' : 'This type of engineering concerns the use of chemical and biological processes to produce useful materials or substances. It’s a multidisciplinary subject, combining natural and experimental sciences (such as chemistry and physics), along with life sciences (such as biology, microbiology and biochemistry), plus mathematics and economics.',
    #         'course_prerequisite' : 0,
    #         'coursem_id' : 1,
    #         'employee_id' : 2, 
    #         'start_time' : '1 July 2021', 
    #         'end_time' : '1 December 2021', 
    #         'datetime_uploaded' : '2021-06-23 00:00:00', 
    #         'start_enrol' : '2021-06-23', 
    #         'end_enrol'  : '2021-06-23'
    #     }

    #     response = self.client.post("/course",
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json')
    #     self.assertEqual(response.json['code'], 201)
    #     self.assertEqual(response.json['data'], {
    #         'course_id': 3, 
    #         'course_name' : 'Chemical engineering',  
    #         'total_no_of_class' : 1,
    #         'total_no_of_lesson' : 1,
    #         'class_id' : 1,
    #         'course_description' : 'This type of engineering concerns the use of chemical and biological processes to produce useful materials or substances. It’s a multidisciplinary subject, combining natural and experimental sciences (such as chemistry and physics), along with life sciences (such as biology, microbiology and biochemistry), plus mathematics and economics.',
    #         'course_prerequisite' : 0,
    #         'coursem_id' : 1,
    #         'employee_id' : 2, 
    #         'start_time' : '1 July 2021', 
    #         'end_time' : '1 December 2021', 
    #         'datetime_uploaded' : '2021-06-23 00:00:00', 
    #         'start_enrol' : '2021-06-23', 
    #         'end_enrol'  : '2021-06-23'
    #     })
    


#Author: Alina Tan 
class TestClass(TestApp):
    def test_create_status(self):
        e1 = Employee(employee_id = 10, course_id = 1, employee_name='Tom', employee_role='Engineer')
        c1 = Course(course_id = 1, course_name = 'Chemical engineering', total_no_of_class = 1, total_no_of_lesson = 1, class_id = 1, course_description = 'This type of engineering concerns the use of chemical and biological processes to produce useful materials or substances. It’s a multidisciplinary subject, combining natural and experimental sciences (such as chemistry and physics), along with life sciences (such as biology, microbiology and biochemistry), plus mathematics and economics.', course_prerequisite = 0, coursem_id = 1, employee_id = 2, start_time = '1 July 2021', end_time = '1 December 2021', datetime_uploaded = '2021-06-23 00:00:00', start_enrol= '2021-06-23', end_enrol= '2021-06-23')
        class2 = Class(class_id = 2, course_id=4, lesson_id = 3, course_name = 'Civil Engineer course', start_date = '01/09/2021', end_date = '01/12/2021', start_time = '14:00', end_time = '16:00', class_size = 10, current_class_size = 5, employee_id = 1, duration_of_class =2)
        db.session.add(e1)
        db.session.add(c1)
        db.session.add(class2)
        db.session.commit()

        request_body = {
            'employee_id': e1.employee_id,
            'course_id' : c1.course_id,
            'class_id' : class2.class_id
        }
        
        response = self.client.post("/employee_course_status",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
    
        self.assertEqual(response.json['code'], 201)            
        self.assertEqual(response.json['data']['status'], 'in-progress')      


    # def test_update_status(self):
    #     e1 = Employee(employee_id = 1, course_id = 4, employee_name='James', employee_role='Engineer')
    #     c1 = Course(course_id = 4, course_name = 'Chemical engineering', total_no_of_class = 3, total_no_of_lesson = 2, class_id = 2, course_description = 'Civil engineering is the professional practice of designing and developing infrastructure projects. This can be on a huge scale, such as the development of nationwide transport systems or water supply networks, or on a smaller scale, such as the development of single roads or buildings.', course_prerequisite = 0, coursem_id = 1, employee_id = 2, start_time = '5 August 2021', end_time = '1 December 2021', datetime_uploaded = '2021-08-17 00:00:00', start_enrol= '2021-06-23', end_enrol= '2021-06-23')
    #     class2 = Class(class_id = 2, course_id=4, lesson_id = 3, course_name = 'Civil Engineer course', start_date = '01/09/2021', end_date = '01/12/2021', start_time = '14:00', end_time = '16:00', class_size = 10, current_class_size = 5, employee_id = 1, duration_of_class =2)
    #     status = 'completed'
    #     db.session.commit()

    #     request_body = {
    #         'employee_id': e1.employee_id,
    #         'course_id' : c1.course_id,
    #         'class_id' : class2.class_id,
    #         'status' : status
    #     }
        
    #     response = self.client.put("/employee_course_status",
    #                                 data=json.dumps(request_body),
    #                                 content_type='application/json') 
    #     self.assertEqual(response.json['code'], 200)     
    #     self.assertEqual(response.json['data']['status'],     
    #     {
    #         'status': 'completed'
    #     })      

    # def test_find_classes_by_course_id(self):
    #     class2 = Class(class_id = 2, course_id=4, lesson_id = 3, course_name = 'Civil Engineer course', start_date = '01/09/2021', end_date = '01/12/2021', start_time = '14:00', end_time = '16:00', class_size = 10, current_class_size = 5, employee_id = 1, duration_of_class =2)
    #     db.session.add(class2)
    #     db.session.commit()
    #     response = self.client.get("/class_by_course_id/4")
    #     self.assertEqual(response.json['code'], 200)
    #     self.assertEqual(response.json['data']['class'], 
    #     [{'class_id': 2, 'course_id': 4,  'lesson_id' : 3,
    #         'course_name' : 'Civil Engineer course',
    #         'start_date': '01/09/2021',
    #         'end_date': '01/12/2021',
    #         'start_time': '14:00',
    #         'end_time': '16:00',
    #         'class_size': 10,
    #         'current_class_size': 5,
    #         'employee_id': 1,
    #         'duration_of_class': 2}
            
    #         ])

    def test_create_class(self):
        request_body = {
            'course_id': 2,
            'lesson_id' : 1,
            'course_name' : 'Civil Engineer course',
            'start_date': '01/09/2021',
            'end_date': '01/12/2021',
            'start_time': '14:00',
            'end_time': '16:00',
            'class_size': 10,
            'current_class_size': 2,
            'employee_id': 1,
            'duration_of_class': 2
        }

        response = self.client.post("/class",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json['code'], 201)
        self.assertEqual(response.json['data'], {
            'class_id': 1,
            'course_id': 2,
            'lesson_id' : 1,
            'course_name' : 'Civil Engineer course',
            'start_date': '01/09/2021',
            'end_date': '01/12/2021',
            'start_time': '14:00',
            'end_time': '16:00',
            'class_size': 10,
            'current_class_size': 2,
            'employee_id': 1,
            'duration_of_class': 2
        })
        
#Author: Brenda
class TestQuiz(TestApp):

    def test_find_quiz_by_lesson_id_invalid_lesson_id(self):
        self.maxDiff = None
        lesson = Lesson(lesson_id=20,lesson_name="lesson2",quiz_type="ungraded",lesson_material="https://drive.google.com/drive/folders/1OE3IzisueXHNK-91BjVofiy59H80Uht2?usp=sharing",created_on="11/7/2021 3:47:44 AM",class_id=12,course_id=4,quiz_id="",lesson_descriptions="lesson2 descriptions")
        db.session.add(lesson)
        db.session.commit()

        request_body = {
            "quiz_type":lesson.quiz_type,
            "question_type":"True/False",
            "quiz_question":"Electrons are larger than molecules",
            "quiz_selection":"True,False",
            "time_limit":"5 hours",
            "correct_answer":"True",
            "passing_score":'',
            "datetime_created":"11/7/2021 3:32:52 AM"
        }

        response = self.client.post("/quiz_by_lesson_id/23",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 405)


    def test_find_by_quizid(self):
        self.maxDiff = None
        quiz = Quiz(quiz_id=2,lesson_id=14,quiz_type='ungraded',question_type="True/False",quiz_question="Electrons are larger than molecules",quiz_selection="True,False",time_limit="5 hours",correct_answer="True",passing_score='',datetime_created="11/7/2021 3:32:52 AM")
        db.session.add(quiz)
        db.session.commit()

        response = self.client.get("/quizid/2",
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code": 200,
            'data': {
            "lesson_id":14,
            "quiz_type":"ungraded",
            "question_type":"True/False",
            "quiz_question":"Electrons are larger than molecules",
            "quiz_selection":"True,False",
            "time_limit":"5 hours",
            "correct_answer":"True",
            "passing_score":'',
            "datetime_created":"11/7/2021 3:32:52 AM",
            'quiz_id': 2
            }
        })

    def test_create_quiz(self):
        self.maxDiff = None
        lesson = Lesson(lesson_id=22,lesson_name="lesson2",quiz_type="ungraded",lesson_material="https://drive.google.com/drive/folders/1OE3IzisueXHNK-91BjVofiy59H80Uht2?usp=sharing",created_on="11/7/2021 3:47:44 AM",class_id=12,course_id=4,quiz_id="",lesson_descriptions="lesson2 descriptions")
        db.session.add(lesson)
        db.session.commit()

        request_body = {
            "lesson_id":lesson.lesson_id,
            "quiz_type":lesson.quiz_type,
            "question_type":"True/False",
            "quiz_question":"Electrons are larger than molecules",
            "quiz_selection":"True,False",
            "time_limit":"5 hours",
            "correct_answer":"True",
            "passing_score":'',
            "datetime_created":"11/7/2021 3:32:52 AM"
        }

        response = self.client.post("/quiz",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code": 201,
            'data': {
            "lesson_id":22,
            "quiz_type":"ungraded",
            "question_type":"True/False",
            "quiz_question":"Electrons are larger than molecules",
            "quiz_selection":"True,False",
            "time_limit":"5 hours",
            "correct_answer":"True",
            "passing_score":'',
            "datetime_created":"11/7/2021 3:32:52 AM",
            'quiz_id': 1
            }
        })

    def test_update_quiz(self):
        self.maxDiff = None
        quiz = Quiz(lesson_id=18,quiz_type="ungraded",question_type="True/False",quiz_question="Electrons are larger than molecules",quiz_selection="True,False",time_limit="5 hours",correct_answer="True",passing_score='',datetime_created="11/7/2021 3:32:52 AM",quiz_id= 3)
        db.session.add(quiz)
        db.session.commit()

        request_body = {
            "lesson_id":quiz.lesson_id,
            "quiz_type":quiz.quiz_type,
            "question_type":quiz.question_type,
            "quiz_question":quiz.quiz_question,
            "quiz_selection":quiz.quiz_selection,
            "time_limit":"5 minutes",
            "correct_answer":"False",
            "passing_score":quiz.passing_score,
            "datetime_created":quiz.datetime_created,
            'quiz_id': quiz.quiz_id
        }

        response = self.client.put("/quiz/3",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code": 200,
            'data': {
            "lesson_id":18,
            "quiz_type":"ungraded",
            "question_type":"True/False",
            "quiz_question":"Electrons are larger than molecules",
            "quiz_selection":"True,False",
            "time_limit":"5 minutes",
            "correct_answer":"False",
            "passing_score":'',
            "datetime_created":"11/7/2021 3:32:52 AM",
            'quiz_id': 3
            }
        })

    def test_delete_quiz(self):
        self.maxDiff = None
        quiz = Quiz(lesson_id=4,quiz_type="ungraded",question_type="True/False",quiz_question="Electrons are larger than molecules",quiz_selection="True,False",time_limit="5 hours",correct_answer="True",passing_score='',datetime_created="11/7/2021 3:32:52 AM",quiz_id= 7)
        db.session.add(quiz)
        db.session.commit()

        request_body = {
            "lesson_id":quiz.lesson_id,
            "quiz_type":quiz.quiz_type,
            "question_type":quiz.question_type,
            "quiz_question":quiz.quiz_question,
            "quiz_selection":quiz.quiz_selection,
            "time_limit":quiz.time_limit,
            "correct_answer":quiz.correct_answer,
            "passing_score":quiz.passing_score,
            "datetime_created":quiz.datetime_created,
            'quiz_id': quiz.quiz_id
        }

        response = self.client.delete("/quiz/7",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code": 200,
            'data': {
                'quiz_id': '7'
            }
        })


if __name__ == '__main__':
    unittest.main()
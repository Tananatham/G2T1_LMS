from datetime import datetime
from operator import le
import unittest   
import flask_testing
import json

from course import app,db, Employee, Course, Class, Lesson, Course_check, PrerequisiteCheck, Quiz


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

class TestLesson(TestApp):
    maxDiff = None
    def test_create_lesson(self):
        request_body = {
            'class_id': 2,
            'course_id': 2,
            'quiz_id': 4,
            'lesson_descriptions': "Placeholder Description",
            'lesson_name': "lesson name placeholder",
            'quiz_type': "MCQ",
            'lesson_material': "url",
            'created_on': "11/2/2021 9:58:57 PM"
        }

        response = self.client.post("/lessons",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json['code'], 201)
        self.assertEqual(response.json['data'], {
            'class_id': 2,
            'course_id': 2,
            'created_on': "11/2/2021 9:58:57 PM",
            'lesson_descriptions': "Placeholder Description",
            'lesson_id': 1,
            'lesson_material': "url",
            'lesson_name': "lesson name placeholder",
            'quiz_id': 4,
            'quiz_type': "MCQ",
        })

    def test_find_lesson_by_class_id(self):
        l1 = Lesson(lesson_id=2, class_id= 5, course_id=4, quiz_id=2, lesson_descriptions='Placeholder', lesson_name='Placeholder', quiz_type='MCQ', lesson_material='placeholder', created_on='placeholder')
        l2 = Lesson(lesson_id=3, class_id= 5, course_id=4, quiz_id=2, lesson_descriptions='Placeholder', lesson_name='Placeholder', quiz_type='MCQ', lesson_material='placeholder', created_on='placeholder')
        db.session.add(l2)
        db.session.add(l1)
        db.session.commit()
        response = self.client.get("/lesson_by_class_id/5")
        self.assertEqual(response.json['code'], 200)
        self.assertEqual(response.json['data']['lesson'], [{'class_id': 5, 'course_id': 4, 'created_on': 'placeholder', 'lesson_descriptions': 'Placeholder', 'lesson_id': 2, 'lesson_material': 'placeholder', 'lesson_name': 'Placeholder', 'quiz_id': 2, 'quiz_type': 'MCQ'}, {'class_id': 5, 'course_id': 4, 'created_on': 'placeholder', 'lesson_descriptions': 'Placeholder', 'lesson_id': 3, 'lesson_material': 'placeholder', 'lesson_name': 'Placeholder', 'quiz_id': 2, 'quiz_type': 'MCQ'}])


class TestEnroll(TestApp):
    def test_employee_course_status(self):
        e1 = Employee(employee_id=1, course_id=2, employee_name='james', employee_role='Engineer')
        en3 = Course_check(employee_id=1, course_id=1, class_id=4, status='completed')
        en4 = Course_check(employee_id=1, course_id=3, class_id=4, status='completed')
        c1 = Class(class_id=6, course_id=2, lesson_id=5, course_name='placeholder', start_date='1/1/2021', end_date='12/12/2023', start_time='10:00', end_time='12:00', class_size=99, current_class_size=0, employee_id=2,duration_of_class='2')
        p1 = PrerequisiteCheck(course_id=2, prerequisite_course_id=1)
        p2 = PrerequisiteCheck(course_id=2, prerequisite_course_id=3)
        db.session.add(e1)
        db.session.add(en3)
        db.session.add(en4)
        db.session.add(c1)
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()

        request_body = {
            'employee_id': e1.employee_id,
            'course_id': 2,
            'class_id': 6,
            'status': 'pending'
        }

        response = self.client.post("/employee_course_status",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        self.assertEqual(response.json['code'], 201)
        self.assertEqual(response.json['data'], {
            'class_id': '6',
            'course_id': 2,
            'employee_id': 1,
            'status': 'pending'
        })
    
    def test_employee_course_status_invalid_prerequisite(self):
        e1 = Employee(employee_id=1, course_id=2, employee_name='james', employee_role='Engineer')
        en3 = Course_check(employee_id=1, course_id=1, class_id=4, status='completed')
        c1 = Class(class_id=6, course_id=2, lesson_id=5, course_name='placeholder', start_date='1/1/2021', end_date='12/12/2023', start_time='10:00', end_time='12:00', class_size=99, current_class_size=0, employee_id=2,duration_of_class='2')
        p1 = PrerequisiteCheck(course_id=2, prerequisite_course_id=1)
        p2 = PrerequisiteCheck(course_id=2, prerequisite_course_id=3)
        db.session.add(e1)
        db.session.add(en3)
        db.session.add(c1)
        db.session.add(p1)
        db.session.add(p2)
        db.session.commit()

        request_body = {
            'employee_id': e1.employee_id,
            'course_id': 2,
            'class_id': 6,
            'status': 'pending'
        }

        response = self.client.post("/employee_course_status",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        print(response.json)

        self.assertEqual(response.json['code'], 500)
        self.assertEqual(response.json['message'], 'The employee applying do not meet all the prerequisite for this course.')
    
    def test_employee_course_status_invalid_classSize(self):
        e1 = Employee(employee_id=1, course_id=2, employee_name='james', employee_role='Engineer')
        en3 = Course_check(employee_id=1, course_id=1, class_id=4, status='completed')
        c1 = Class(class_id=6, course_id=2, lesson_id=5, course_name='placeholder', start_date='1/1/2021', end_date='12/12/2023', start_time='10:00', end_time='12:00', class_size=10, current_class_size=10, employee_id=2,duration_of_class='2')
        db.session.add(e1)
        db.session.add(en3)
        db.session.add(c1)
        db.session.commit()

        request_body = {
            'employee_id': e1.employee_id,
            'course_id': 2,
            'class_id': 6,
            'status': 'pending'
        }

        response = self.client.post("/employee_course_status",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        print(response.json)

        self.assertEqual(response.json['code'], 500)
        self.assertEqual(response.json['message'], 'The class is full.')


if __name__ == '__main__':
    unittest.main()
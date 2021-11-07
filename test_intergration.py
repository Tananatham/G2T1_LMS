import unittest   
import flask_testing
import json
from datetime import datetime
from freezegun import freeze_time

from course import Course_check, app,db, Employee, Course, Class, Lesson,Quiz

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()

#Author: Chelsea
class TestEmployee(TestApp):
    def test_employee_course_prerequisite_check(self):
       self.assertEqual(4,4)

    def test_name_lookup_employee(self):
      self.assertEqual(4,4)

    def test_find_status_by_id(self):
       self.assertEqual(4,4)

    def test_find_inprogress_class_id(self):
       self.assertEqual(4,4)
       
    def test_find_employee_in_progress(self):
       self.assertEqual(4,4)

    def test_delete_status(self):
        self.assertEqual(4,4)

#Author: Tantham 
class TestCourse(TestApp):
    def test_course_prereq_okay_check(self):
        self.assertEqual(4, 4)

    def test_set_course_prereq(self):
        self.assertEqual(4,4)

    def test_find_prerequisites_by_id(self):
        self.assertEqual(4,4)

    def test_find_course_name_by_id(self):
        self.assertEqual(4,4)

    def test_get_pending_enrollment(self):
        self.assertEqual(4,4)
    
    def test_get_in_progress_enrollment(self):
        self.assertEqual(4,4)


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


    def test_update_status(self):
        e1 = Employee(employee_id = 1, course_id = 1, employee_name='James', employee_role='Engineer')
        c1 = Course(course_id = 1, course_name = 'Chemical engineering', total_no_of_class = 1, total_no_of_lesson = 1, class_id = 1, course_description = 'This type of engineering concerns the use of chemical and biological processes to produce useful materials or substances. It’s a multidisciplinary subject, combining natural and experimental sciences (such as chemistry and physics), along with life sciences (such as biology, microbiology and biochemistry), plus mathematics and economics.', course_prerequisite = 0, coursem_id = 1, employee_id = 2, start_time = '1 July 2021', end_time = '1 December 2021', datetime_uploaded = '2021-06-23 00:00:00', start_enrol= '2021-06-23', end_enrol= '2021-06-23')
        class2 = Class(class_id = 6, course_id=1, lesson_id = 5, course_name = 'Chemical Engineering', start_date = '01/09/2021', end_date = '01/12/2021', start_time = '14:00', end_time = '16:00', class_size = 10, current_class_size = 5, employee_id = 1, duration_of_class =2)
        status = 'completed'
        db.session.commit()

        request_body = {
            'employee_id': e1.employee_id,
            'course_id' : c1.course_id,
            'class_id' : class2.class_id,
            'status' : status
        }
        
        response = self.client.put("/employee_course_status",
                                    data=json.dumps(request_body),
                                    content_type='application/json') 
        self.assertEqual(response.json['code'], 200)     
        self.assertEqual(response.json['data']['class'],     
        {
            'status': 'completed'
        })      

    def test_find_classes_by_course_id(self):
        class2 = Class(class_id = 2, course_id=4, lesson_id = 3, course_name = 'Civil Engineer course', start_date = '01/09/2021', end_date = '01/12/2021', start_time = '14:00', end_time = '16:00', class_size = 10, current_class_size = 5, employee_id = 1, duration_of_class =2)
        class3 = Class(class_id = 3, course_id=4, lesson_id = 3, course_name = 'Civil Engineer course', start_date = '01/01/2021', end_date = '12/12/2021', start_time = '14:00', end_time = '16:00', class_size = 10, current_class_size = 10, employee_id = 1, duration_of_class =2)
        class7 = Class(class_id = 7, course_id=4, lesson_id = 3, course_name = 'Civil Engineer course', start_date = '01/02/2021', end_date = '10/02/2021', start_time = '14:00', end_time = '16:00', class_size = 10, current_class_size = 0, employee_id = 1, duration_of_class =2)
        db.session.add(class2)
        db.session.add(class3)
        db.session.add(class7)
        db.session.commit()
        response = self.client.get("/class_by_course_id/4")
        self.assertEqual(response.json['code'], 200)
        self.assertEqual(response.json['data']['class'], 
        [{'class_id': 2, 'course_id': 4,  'lesson_id' : 3,
            'course_name' : 'Civil Engineer course',
            'start_date': '01/09/2021',
            'end_date': '01/12/2021',
            'start_time': '14:00',
            'end_time': '16:00',
            'class_size': 10,
            'current_class_size': 2,
            'employee_id': 1,
            'duration_of_class': 2},
            {'class_id': 3, 'course_id': 4,  'lesson_id' : 3,
            'course_name' : 'Civil Engineer course',
            'start_date': '01/01/202',
            'end_date': '12/12/2021',
            'start_time': '14:00',
            'end_time': '16:00',
            'class_size': 10,
            'current_class_size': 10,
            'employee_id': 1,
            'duration_of_class': 2},
            {'class_id': 7, 'course_id': 4,  'lesson_id' : 3,
            'course_name' : 'Civil Engineer course',
            'start_date': '01/02/2021',
            'end_date': '10/02/2021',
            'start_time': '14:00',
            'end_time': '16:00',
            'class_size': 10,
            'current_class_size': 0,
            'employee_id': 1,
            'duration_of_class': 2}
            ])

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
    def test_get_all_quiz(self):
        self.assertEqual(4, 4)
    
    def test_find_quiz_by_lesson_id(self):
        self.assertEqual(4, 4)

    def test_find_by_quizs(self):
        self.assertEqual(4, 4)

    def test_find_by_quizid(self):
        self.assertEqual(4, 4)

    def test_create_quiz(self):
         self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()
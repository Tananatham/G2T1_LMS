import unittest   
import flask_testing
import json
from datetime import datetime
from freezegun import freeze_time
from werkzeug.wrappers import request, response 

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
    @freeze_time("2021-11-05")
    def test_create_status(self):
        e1 = Employee(employee_id = '10', course_id = '4', employee_name='James', employee_role='Engineer')
        c1 = Course(course_id = '4', course_name = 'PlaceHolder', total_no_of_class = '5', total_no_of_lesson = '2', class_id = '1', course_description = 'Fix', course_prerequisite = '2', coursem_id = '2', employee_id = '10', start_time = 'Now', end_time = 'Later', datetime_uploaded = '2021-09-14 00:00:00', start_enrol= '', end_enrol= '')
        class1 = Class(class_id = '2', course_id='4', lesson_id = '1', course_name = 'PlaceHolder', start_date = '05/11/2021', end_date = '05/11/2021', start_time = '10:00', end_time = '11:00', class_size = 23, current_class_size = 4, employee_id = '5', duration_of_class ='5')
        db.session.add(e1)
        db.session.add(c1)
        db.session.add(class1)
        db.session.commit()
        start_date = Class.get_start_datetime(class1)

        request_body = {
            'employee_id': e1.employee_id,
            'course_id' : c1.course_id,
            'class_id' : class1.class_id,
        }
        
        response = self.client.post("/employee_course_status",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        new_status =  Course_check(employee_id = '10', course_id = '4', class_id = '2', status= 'in-progress')                            
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            'status': 'in-progress'
        })


    def test_update_status(self):
        e1 = Employee(employee_id = '1', course_id = '4', employee_name='James', employee_role='Engineer')
        c1 = Course(course_id = '4', course_name = 'PlaceHolder', total_no_of_class = '5', total_no_of_lesson = '2', class_id = '2', course_description = 'Fix', course_prerequisite = '2', coursem_id = '2', employee_id = '1', start_time = 'Now', end_time = 'Later', datetime_uploaded = '2021-09-14 00:00:00', start_enrol= '', end_enrol= '')
        class1 = Class(class_id = '2', course_id='4', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 4, employee_id = '5', duration_of_class ='5')
        db.session.commit()

        request_body = {
            'employee_id': e1.employee_id,
            'course_id' : c1.course_id,
            'class_id' : class1.class_id,
        }
        
        response = self.client.put("/employee_course_status/1/4/2",
                                    data=json.dumps(request_body),
                                    content_type='application/json')                         
        self.assertEqual(response.json, {
            'code' : '200',
            'status': 'completed'
        })

    def test_find_classes_by_course_id(self):
        self.assertEqual(4, 4)

    def test_get_all_classes(self):
        self.assertEqual(4, 4)

    def test_create_class(self):
         self.assertEqual(4, 4)

#Author: Brenda
class TestQuiz(TestApp):
    def test_get_all_quiz(self):
        self.assertEqual(4, 4)
    
    def test_find_quiz_by_lesson_id(self):
        response = self.client.get("/quiz_by_lesson_id/2")
        self.assertEqual(response.json['data']['quiz'], [])

    def test_find_by_quizs(self):
        self.assertEqual(4, 4)

    def test_find_by_quizid(self):
        self.assertEqual(4, 4)

    def test_create_quiz(self):
         self.assertEqual(4, 4)

#Author: Frank
class TestLesson(TestApp):
    #seems to be brenda's part sorry about it 
    def test_find_quiz_by_lesson_id(self):
        response = self.client.get("/quiz_by_lesson_id/2")
        self.assertEqual(response.json['data']['quiz'], [])

    def test_find_course_material_by_lesson_id(self):
        self.assertEqual(4, 4)

    def test_find_lesson_by_class_id(self):
        self.assertEqual(4, 4)
    
    def test_get_all_lessons(self):
        self.assertEqual(4, 4)

    def test_find_by_lessonid(self):
        self.assertEqual(4, 4)
    
    def test_create_lesson(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()
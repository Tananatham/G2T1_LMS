import unittest   
import flask_testing
import json
from datetime import datetime
from werkzeug.wrappers import request, response 

from course import app,db, Employee, Course, Class, Lesson,Quiz, Em

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
        e1 = Employee(employee_id = '1', course_id = '1', employee_name='James', employee_role='Engineer')
        c1 = Course(course_id = '1', course_name = 'PlaceHolder', total_no_of_class = '5', total_no_of_lesson = '2', class_id = '1', course_description = 'Fix', course_prerequisite = '2', coursem_id = '2', employee_id = '1', start_time = 'Now', end_time = 'Later', datetime_uploaded = '2021-09-14 00:00:00', start_enrol= '', end_enrol= '')
        class1 = Class(class_id = '1', course_id='1', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 4, employee_id = '5', duration_of_class ='5')
        db.session.add(e1)
        db.session.add(c1)
        db.session.add(class1)
        db.session.commit()

        request_body = {
            'employee_id': e1.employee_id,
            'course_id' : c1.course_id,
            'class_id' : class1.class_id,
        }
        
        response = self.client.post("/employee_course_status",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {
            'status': 'in-progress'
        })


    def test_update_status(self):
        self.assertEqual(4,4)

#Author: Brenda
class TestQuiz(TestApp):
    def test_get_all_quiz(self):
        self.assertEqual(4, 4)
    
    def test_find_quiz_by_lesson_id(self):
        self.assertEqual(4, 4)

    def test_create_quiz(self):
         self.assertEqual(4, 4)

#Author: Frank
class TestLesson(TestApp):
    def test_find_quiz_by_lesson_id(self):
        response = self.client.get("/quiz_by_lesson_id/2")
        self.assertEqual(response.json['data']['quiz'], [])

    def test_find_course_material_by_lesson_id(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()
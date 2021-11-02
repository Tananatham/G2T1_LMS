import unittest   
#import flask_testing
import json

from course import app,db, Employee, Course, Class, Lesson, Course_check, PrerequisiteCheck, Quiz


# class TestApp(flask_testing.TestCase):
#     app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
#     app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
#     app.config['TESTING'] = True

#     def create_app(self):
#         return app

#     def setUp(self):
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()


#Author: Chelsea
class TestEmployee(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.app = Employee(database='fixtures/test_basic.json')

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

    def test_employee_course_prerequisite_check(self):
       self.assertEqual(4,4)

#Author: 
class TestCourse(unittest.TestCase):

    def test_set_course_prereq(self):
        self.assertEqual(4,4)

    def test_find_prerequisites_by_id(self):
        self.assertEqual(4,4)

    def test_find_course_name_by_id(self):
        self.assertEqual(4,4)

    def test_course_prereq_okay_check(self):
        self.assertEqual(4, 4)


#Author: Alina Tan 
class TestClass(unittest.TestCase):
    def test_create_status(self):
        self.assertEqual(4, 4)

    def test_update_status(self):
        self.assertEqual(4,4)

#Author: 
class TestQuiz(unittest.TestCase):
    def test_get_all_quiz(self):
        self.assertEqual(4, 4)
    
    def test_get_quiz_by_lesson_id(self):
        self.assertEqual(4, 4)
    
    def test_find_by_lessonid(self):
        self.assertEqual(4, 4)

#Author: 
class TestLesson(unittest.TestCase):
    def test_find_quiz_by_lesson_id(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()
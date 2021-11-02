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
    def test_find_quiz_by_lesson_id(self):
        response = self.client.get("/quiz_by_lesson_id/2")
        self.assertEqual(response.json['data']['quiz'], [])



if __name__ == '__main__':
    unittest.main()
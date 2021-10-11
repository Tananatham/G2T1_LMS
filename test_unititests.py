import unittest   # The test framework

from course import Employee, Course, Class, Lesson, Course_check, PrerequisiteCheck, Quiz

class TestPerson(unittest.TestCase):
    def test_to_dict(self):
        e1 = Employee(employee_id = '1', course_id = '1', employee_name='James', employee_role='HR')
        self.assertEqual(e1.to_dict(), {
            'employee_id': '1',
            'course_id': '1',
            'employee_name': 'James',
            'employee_role': 'HR'}
        )

if __name__ == '__main__':
    unittest.main()
import unittest   # The test framework

from course import Employee, Course, Class, Lesson, Course_check, PrerequisiteCheck, Quiz

class TestPerson(unittest.TestCase):
    def test_to_dict(self):
        e1 = Employee(employee_id = '1', course_id = '1', employee_name='James', employee_role='Engineer')
        self.assertEqual(e1.to_dict(), {
            'employee_id': '1',
            'course_id': '1',
            'employee_name': 'James',
            'employee_role': 'Engineer'}
        )

class TestCourse(unittest.TestCase):
     def test_to_dict(self):
        c1 = Course(course_id = '1', course_name = 'PlaceHolder', total_no_of_class = '5', total_no_of_lesson = '2', class_id = '1', course_description = 'Fix', course_prerequisite = '2', coursem_id = '2', employee_id = '1', start_time = 'Now', end_time = 'Later', datetime_uploaded = '2021-09-14 00:00:00')
        self.assertEqual(c1.to_dict(), {
            'course_id': '1',
            'course_name': 'PlaceHolder',
            'total_no_of_class' : '5',
            'total_no_of_lesson' : '2',
            'class_id': '1',
            'course_description': 'Fix',
            'course_prerequisite': '2',
            'coursem_id': '2',
            'employee_id': '1',
            'start_time': 'Now',
            'end_time': 'Later',
            'datetime_uploaded': '2021-09-14 00:00:00'}
        )

class TestClass(unittest.TestCase):
    def test_class_enrol(self):
        class1 = Class(class_id = '1', course_id='1', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 4, employee_id = '5', duration_of_class ='5')
        class1.class_enroll()
        self.assertEqual(class1.current_class_size,5)

    def test_class_enrol_negative(self):
        class1 = Class(class_id = '1', course_id='1', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 23, employee_id = '5', duration_of_class ='5')
        self.assertEqual(class1.class_size, 23)
        try:
            class1.class_enroll()
        except Exception as e:
            self.assertEqual(str(e), 'Class is now full.')
            self.assertEqual(class1.class_size, 23)

if __name__ == '__main__':
    unittest.main()
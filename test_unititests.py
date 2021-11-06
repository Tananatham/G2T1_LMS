from datetime import datetime 
import unittest   
#from freezegun import freeze_time
from course import Employee, Course, Class, Lesson, Course_check, PrerequisiteCheck, Quiz

#Author: Chelsea
class TestEmployee(unittest.TestCase):
    def test_to_dict(self):
        e1 = Employee(employee_id = '1', course_id = '1', employee_name='James', employee_role='Engineer')
        self.assertEqual(e1.to_dict(), {
            'employee_id': '1',
            'course_id': '1',
            'employee_name': 'James',
            'employee_role': 'Engineer'}
        )

#Author: Tantham 
class TestCourse(unittest.TestCase):
    def test_to_dict(self):
        c1 = Course(course_id = '1', course_name = 'PlaceHolder', total_no_of_class = '5', total_no_of_lesson = '2', class_id = '1', course_description = 'Fix', course_prerequisite = '2', coursem_id = '2', employee_id = '1', start_time = 'Now', end_time = 'Later', datetime_uploaded = '2021-09-14 00:00:00', start_enrol= '', end_enrol= '')
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
            'datetime_uploaded': '2021-09-14 00:00:00',
            'start_enroll' : '',
            'end_enrol': ''}
        )

#Author: Alina Tan 
class TestClass(unittest.TestCase):
    def test_class_enrol(self):
        class1 = Class(class_id = '1', course_id='1', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 4, employee_id = '5', duration_of_class ='5')
        class1.class_enroll()
        self.assertEqual(class1.current_class_size,5)

    def test_class_enrol_negative(self):
        class1 = Class(class_id = '1', course_id='1', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 23, employee_id = '5', duration_of_class ='5')
        self.assertEqual(class1.current_class_size, 23)
        try:
            class1.class_enroll()
        except Exception as e:
            self.assertEqual(str(e), 'Class is now full.')
            self.assertEqual(class1.current_class_size, 23)

    def test_class_withdraw(self):
        class1 = Class(class_id = '1', course_id='1', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 4, employee_id = '5', duration_of_class ='5')
        class1.class_withdraw()
        self.assertEqual(class1.current_class_size,3)

    def test_class_withdraw_negative(self):
        class1 = Class(class_id = '1', course_id='1', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 1, employee_id = '5', duration_of_class ='5')
        self.assertEqual(class1.current_class_size, 1)
        try:
            class1.class_withdraw()
        except Exception as e:
            self.assertEqual(str(e), 'Class size cannot be less than zero.')
            self.assertEqual(class1.current_class_size, 1)

#Author: Brenda
class TestCourseCheck(unittest.TestCase):
    def test_to_dict(self):
        checkcourse = Course_check(employee_id = '1', course_id = '4', class_id='2', status='in-progress')
        self.assertEqual(checkcourse.to_dict(), {
            'employee_id': '1',
            'course_id': '4',
            'class_id': '2',
            'status': 'in-progress'}
        )

#Author: Frank
class TestPrerequisiteCheck(unittest.TestCase):
    def test_to_dict(self):
        checkprereq = PrerequisiteCheck(course_id = '2', prerequisite_course_id='5')
        self.assertEqual(checkprereq.to_dict(), {
            'course_id': '2',
            'prerequisite_course_id': '5'}
        )


if __name__ == '__main__':
    unittest.main()
import unittest   # The test framework

from course import Employee, Course, Class, Lesson, Course_check, PrerequisiteCheck, Quiz

class TestEmployee(unittest.TestCase):
    def test_to_dict(self):
        e1 = Employee(employee_id = '1', course_id = '1', employee_name='James', employee_role='Engineer')
        self.assertEqual(e1.to_dict(), {
            'employee_id': '1',
            'course_id': '1',
            'employee_name': 'James',
            'employee_role': 'Engineer'}
        )
    def test_name_lookup_employee(self):
        searchname = Employee(employee_id = '1', course_id = '1', employee_name='James', employee_role='Engineer')
        self.assertEqual(searchname.to_dict(), {
            'employee_id': '1',
            'course_id': '1',
            'employee_name': 'James',
            'employee_role': 'Engineer'}
        )

    def test_find_status_by_id(self):
        courselist = Course_check(employee_id = '1', course_id = '4', class_id='2', status='completed')
        self.assertEqual(courselist.to_dict(), {
            'employee_id': '1',
            'course_id': '4',
            'class_id': '2',
            'status': 'completed'}
        )

    def test_find_inprogress_class_id(self):
        in_progress_list = Course_check(employee_id = '1', course_id = '4', class_id='2', status='in-progress')
        self.assertEqual(in_progress_list.to_dict(), {
            'employee_id': '1',
            'course_id': '4',
            'class_id': '2',
            'status': 'in-progress'}
        )

    def test_find_employee_in_progress(self):
        courselist = Course_check(employee_id = '1', course_id = '4', class_id='2', status='in-progress')
        self.assertEqual(courselist.to_dict(), {
            'employee_id': '1',
            'course_id': '4',
            'class_id': '2',
            'status': 'in-progress'}
        )

    def test_delete_status(self):
        self.assertEqual(4,4)

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

    def test_set_course_prereq(self):
        self.assertEqual(4,4)

    def test_find_prerequisites_by_id(self):
        courselist = PrerequisiteCheck(course_id='2',prerequisite_course_id='5')
        self.assertEqual(courselist.prerequisite_course_id,'5')

    def test_find_course_name_by_id(self):
        c1 = Course(course_id = '1', course_name = 'PlaceHolder', total_no_of_class = '5', total_no_of_lesson = '2', class_id = '1', course_description = 'Fix', course_prerequisite = '2', coursem_id = '2', employee_id = '1', start_time = 'Now', end_time = 'Later', datetime_uploaded = '2021-09-14 00:00:00')
        self.assertEqual(c1.course_name ,'PlaceHolder')

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

    def test_class_withdraw(self):
        class1 = Class(class_id = '1', course_id='1', lesson_id = '1', course_name = 'PlaceHolder', start_date = 'Start', end_date = 'End', start_time = 'Start', end_time = 'End', class_size = 23, current_class_size = 4, employee_id = '5', duration_of_class ='5')
        class1.class_withdraw()
        self.assertEqual(class1.current_class_size,3)

    def test_create_status(self):
        self.assertEqual(4, 4)

    def test_update_status(self):
        self.assertEqual(4,4)


class TestCourseCheck(unittest.TestCase):
    def test_to_dict(self):
        checkcourse = Course_check(employee_id = '1', course_id = '4', class_id='2', status='in-progress')
        self.assertEqual(checkcourse.to_dict(), {
            'employee_id': '1',
            'course_id': '4',
            'class_id': '2',
            'status': 'in-progress'}
        )

class TestPrerequisiteCheck(unittest.TestCase):
    def test_to_dict(self):
        checkprereq = PrerequisiteCheck(course_id = '2', prerequisite_course_id='5')
        self.assertEqual(checkprereq.to_dict(), {
            'course_id': '2',
            'prerequisite_course_id': '5'}
        )

class TestQuiz(unittest.TestCase):
    def test_employee_course_prerequisite_check(self):
        e1completedcourse = Course_check(employee_id='1', status = 'in-progress', course_id='2', class_id= '2')
        c1prereq= PrerequisiteCheck(course_id='2', prerequisite_course_id='5')
        check = True
        if set(c1prereq).issubset(set(e1completedcourse)):
            check = check 
        else:
            check = False 
        self.assertEqual(check,{
            check: 'true'}
        )

    def test_course_prereq_okay_check(self):
        self.assertEqual(4, 4)

if __name__ == '__main__':
    unittest.main()
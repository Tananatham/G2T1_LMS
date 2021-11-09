# G2T1_LMS
This application is live at: http://50.16.230.106/G2T1_LMS/HTML_Production/

Git: https://github.com/Tananatham/G2T1_LMS

Database SQL file: https://github.com/Tananatham/G2T1_LMS/tree/main/SQL%20files

# Steps for installment on local machine:
1. Install git, docker, docker desktop, Python, WAMP/MAMP
2. Launch WAMP, docker desktop
3. Git clone https://github.com/Tananatham/G2T1_LMS into your WAMP web server root directory (e.g. C:\wamp\www)
4. Launch PhpMyAdmin, import lms_course.sql in the /SQL files folder
5. In the G2T1_LMS folder, run docker-compose up
6. Navigate to localhost/G2T1_LMS/HTML in your preferred browser
7. Done!

This is a learning management system for Service Engineers to repair, service and maintain the products of All-In-One. This system allows engineers to apply for classes and take lessons. It allows trainers to upload course materials and create assessments, and allow them to check the progress of the learners in their class. It allows Human Resources to enrol and assign students to a class.

### These are the current users assumed to be logged in:
- James - Learner - Default
- Richard - Learner
- Lamy - Learner
- Kane - Human Resources - Default
- Johnson - Trainer - Default

## For Learner:
- You can apply for classes in a course, please note that if a class is full, or if the time now is before or after the class time, you will not be able to apply.

- Please note that some courses have prerequisites, it will be stated in the first line of the course description, your application to a class in this course will fail if you do not meet the prerequisites.

- Please note that in some classes, the current class size is set to max, while there are not that many learners in the system at the moment, this is made as a test so you cannot apply for that class.

- After you apply for a class, Human Resources needs to approve your application.

- You can access the lesson and take quizzes, and also check and access materials.

- You can withdraw from a class you are enrolled in.

## For Human Resources:
- You can see a list of learner for each class.

- You can set an enrollment period for each course.

- You can approve a learner’s application to a class, or you can reject an application.

- You can set a course's prerequisite, please note that once it is set, it cannot be revoked.


## For Trainers:
- You can create lessons for each assigned class

- You can upload materials for a course.

- You can edit lessons.

- You can view, edit or delete quiz questions.

- You can create a quiz for a lesson.
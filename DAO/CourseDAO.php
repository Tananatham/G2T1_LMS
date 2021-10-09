<?php

require_once 'Course.php';
require_once 'ConnectionManager.php';

class CourseDAO {
    public function getCourse() {
        
        $connMgr = new ConnectionManager();
        $pdo = $connMgr->connect(); // PDO object
        
        $sql = "SELECT
                `course_id`, `course_name`, `total_no_of_class`, `total_no_of_lesson`, `class_id`, `course_description`, `course_prerequisite`, `coursem_id`, `employee_id`, `start_time`, `end_time`, `datetime_uploaded` 
                FROM
                `course` ";
        $stmt = $pdo->prepare($sql); 
        
        $stmt->execute(); 
        $stmt->setFetchMode(PDO::FETCH_ASSOC);
        $contacts = [];
        while ( $row = $stmt->fetch() ) {
            $contact = new Course( 
                        $row['course_id'], 
                        $row['course_name'], 
                        $row['total_no_of_class'], 
                        $row['total_no_of_lesson'],
                        $row['class_id'],
                        $row['course_description'],
                        $row['course_prerequisite'],
                        $row['coursem_id'],
                        $row['employee_id'],
                        $row['start_time'],
                        $row['end_time'],
                        $row['datetime_uploaded']
                    ); 
            $contacts[] = $contact;
        }
        
        // STEP 5
        $stmt = null; // clear memory
        $pdo = null; // clear memory
        
        // STEP 6
        return $contacts;
    }

    public function getCoursebyID($course_id) {
        
        $connMgr = new ConnectionManager();
        $pdo = $connMgr->connect(); // PDO object
        
        $sql = "SELECT
                    `course_id`, `course_name`, `total_no_of_class`, `total_no_of_lesson`, `class_id`, `course_description`, `course_prerequisite`, `coursem_id`, `employee_id`, `start_time`, `end_time`, `datetime_uploaded` 
                FROM
                    `course` 
                WHERE
                    course_id = :course_id";
        $stmt = $pdo->prepare($sql); 
        $stmt->bindParam('course_id', $course_id, PDO::PARAM_STR);
        
        $stmt->execute(); // RUN SQL
        $stmt->setFetchMode(PDO::FETCH_ASSOC);
        $contacts = [];
        while ( $row = $stmt->fetch() ) {
            $contact = new Course( 
                        $row['course_id'], 
                        $row['course_name'], 
                        $row['total_no_of_class'], 
                        $row['total_no_of_lesson'],
                        $row['class_id'],
                        $row['course_description'],
                        $row['course_prerequisite'],
                        $row['coursem_id'],
                        $row['employee_id'],
                        $row['start_time'],
                        $row['end_time'],
                        $row['datetime_uploaded']
                    ); 
            $contacts[] = $contact;
        }
        
        // STEP 5
        $stmt = null; // clear memory
        $pdo = null; // clear memory
        
        // STEP 6
        return $contacts;
    }

    public function add($course_name, $total_no_of_class, $total_no_of_lesson, $class_id, $course_description, $course_prerequisite, $coursem_id, $employee_id, $start_time, $end_time, $datetime_uploaded) {    

        $connMgr = new ConnectionManager();
        $pdo = $connMgr->connect();
        
        $sql = "INSERT INTO `course`(`course_id`, `course_name`, `total_no_of_class`, `total_no_of_lesson`, `class_id`, `course_description`, `course_prerequisite`, `coursem_id`, `employee_id`, `start_time`, `end_time`, `datetime_uploaded`) VALUES (NULL,:course_name,:total_no_of_class,:total_no_of_lesson,:class_id,:course_description,:course_prerequisite,:coursem_id,:employee_id,:start_time,:end_time,:datetime_uploaded)";
        

        $stmt = $pdo->prepare($sql);
        $stmt->bindParam('course_name', $course_name, PDO::PARAM_STR);
        $stmt->bindParam('total_no_of_class', $total_no_of_class, PDO::PARAM_INT);
        $stmt->bindParam('total_no_of_lesson', $total_no_of_lesson, PDO::PARAM_INT);
        $stmt->bindParam('class_id', $class_id, PDO::PARAM_INT);
        $stmt->bindParam('course_description', $course_description, PDO::PARAM_STR);
        $stmt->bindParam('course_prerequisite', $course_prerequisite, PDO::PARAM_STR);
        $stmt->bindParam('coursem_id', $coursem_id, PDO::PARAM_INT);
        $stmt->bindParam('employee_id', $employee_id, PDO::PARAM_INT);
        $stmt->bindParam('start_time', $start_time, PDO::PARAM_STR);
        $stmt->bindParam('end_time', $end_time, PDO::PARAM_STR);
        $stmt->bindParam('datetime_uploaded', $datetime_uploaded, PDO::PARAM_STR);

        $status = $stmt->execute();

        $stmt->closeCursor();
        $pdo = null;

        return $status;
    }

    public function delete($course_id) {        

        $connMgr = new ConnectionManager();
        $pdo = $connMgr->connect();
        
        $sql = "DELETE FROM course WHERE course_id = :course_id";
        

        $stmt = $pdo->prepare($sql);
        $stmt->bindParam('course_id', $course_id, PDO::PARAM_STR);

        $status = $stmt->execute();
        
        $stmt->closeCursor();
        $pdo = null;
        return $status;
    }

    public function edit($course_id, $course_name, $total_no_of_class, $total_no_of_lesson, $class_id, $course_description, $course_prerequisite, $coursem_id, $employee_id, $start_time, $end_time, $datetime_uploaded) {   
        $connMgr = new ConnectionManager();
        $pdo = $connMgr->connect();
        $sql = "UPDATE `course` SET `course_name`=:course_name,`total_no_of_class`=:total_no_of_class,`total_no_of_lesson`=:total_no_of_lesson,`class_id`=:class_id,`course_description`=:course_description`course_prerequisite`=:course_prerequisite,`coursem_id`=:coursem_id,`employee_id`=:employee_id,`start_time`=:start_time,`end_time`=:end_time,`datetime_uploaded`=:datetime_uploaded";
        

        $stmt = $pdo->prepare($sql);
        $stmt->bindParam('course_id', $course_id, PDO::PARAM_INT);
        $stmt->bindParam('course_name', $course_name, PDO::PARAM_STR);
        $stmt->bindParam('total_no_of_class', $total_no_of_class, PDO::PARAM_INT);
        $stmt->bindParam('total_no_of_lesson', $total_no_of_lesson, PDO::PARAM_INT);
        $stmt->bindParam('class_id', $class_id, PDO::PARAM_INT);
        $stmt->bindParam('course_description', $course_description, PDO::PARAM_STR);
        $stmt->bindParam('course_prerequisite', $course_prerequisite, PDO::PARAM_STR);
        $stmt->bindParam('coursem_id', $coursem_id, PDO::PARAM_INT);
        $stmt->bindParam('employee_id', $employee_id, PDO::PARAM_INT);
        $stmt->bindParam('start_time', $start_time, PDO::PARAM_STR);
        $stmt->bindParam('end_time', $end_time, PDO::PARAM_STR);
        $stmt->bindParam('datetime_uploaded', $datetime_uploaded, PDO::PARAM_STR);


        $status = $stmt->execute();
        

        $stmt->closeCursor();
        $pdo = null;


        return $status;
    }

}





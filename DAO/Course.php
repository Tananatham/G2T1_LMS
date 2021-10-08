<?php

class Course {

    private $course_id;
    private $course_name;
    private $total_no_of_class;
    private $total_no_of_lesson;
    private $class_id;
    private $course_description;
    private $course_prerequisite;
    private $coursem_id;
    private $employee_id;
    private $start_time;
    private $end_time;
    private $datetime_uploaded;

    public function __construct($course_id, $course_name, $total_no_of_class, $total_no_of_lesson, $class_id, $course_description, $course_prerequisite, $coursem_id, $employee_id, $start_time, $end_time, $datetime_uploaded) {
        $this->course_id = $course_id;
        $this->course_name = $course_name;
        $this->total_no_of_class = $total_no_of_class;
        $this->total_no_of_lesson = $total_no_of_lesson;
        $this->class_id = $class_id;
        $this->course_description = $course_description;
        $this->course_prerequisite = $course_prerequisite;
        $this->coursem_id = $coursem_id;
        $this->employee_id = $employee_id;
        $this->start_time = $start_time;
        $this->end_time = $end_time;
        $this->datetime_uploaded = $datetime_uploaded;
    }

    public function getcourse_id() {
        return $this->course_id;
    }

    public function getcourse_name() {
        return $this->course_name;
    }

    public function gettotal_no_of_class() {
        return $this->total_no_of_class;
    }

    public function gettotal_no_of_lesson() {
        return $this->total_no_of_lesson;
    }

    public function getclass_id() {
        return $this->class_id;
    }

    public function getcourse_description() {
        return $this->course_description;
    }

    public function getcourse_prerequisite() {
        return $this->course_prerequisite;
    }

    public function getcoursem_id() {
        return $this->coursem_id;
    }

    public function getemployee_id() {
        return $this->employee_id;
    }

    public function getstart_time() {
        return $this->start_time;
    }
    
    public function getend_time() {
        return $this->end_time;
    }
    
    public function getdatetime_uploaded() {
        return $this->datetime_uploaded;
    }
}

?>
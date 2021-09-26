-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Sep 22, 2021 at 09:05 AM
-- Server version: 8.0.18
-- PHP Version: 7.4.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lms_course`
--

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS `class` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `lesson_id` int(11) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  `start_date` varchar(50) NOT NULL,
  `end_date` varchar(50) NOT NULL,
  `start_time` varchar(50) NOT NULL,
  `end_time` varchar(50) NOT NULL,
  `class_size` int(11) NOT NULL,
  `current_class_size` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `duration_of_class` int(11) NOT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`class_id`, `lesson_id`, `course_name`, `start_date`, `end_date`, `start_time`, `end_time`, `class_size`, `current_class_size`, `employee_id`, `duration_of_class`) VALUES
(1, 1, 'PlaceHolder', 'Start', 'Ebd', 'Start', 'End', 23, 4, 5, 5);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) NOT NULL,
  `total_no_of_class` int(11) NOT NULL,
  `total_no_of_lesson` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `course_description` varchar(50) NOT NULL,
  `course_prerequisite` int(11) NOT NULL,
  `coursem_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `start_time` varchar(50) NOT NULL,
  `end_time` varchar(50) NOT NULL,
  `datetime_uploaded` datetime NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `total_no_of_class`, `total_no_of_lesson`, `class_id`, `course_description`, `course_prerequisite`, `coursem_id`, `employee_id`, `start_time`, `end_time`, `datetime_uploaded`) VALUES
(1, 'Fix', 2, 0, 4, 'Fix', 0, 2, 1, 'Now', 'Later', '2021-09-14 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `employee_enrolled`
--

DROP TABLE IF EXISTS `employee_enrolled`;
CREATE TABLE IF NOT EXISTS `employee_enrolled` (
  `employee_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`employee_id`,`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `employee_enrolled`
--

INSERT INTO `employee_enrolled` (`employee_id`, `course_id`, `status`) VALUES
(1, 1, 'pending'),
(1, 2, 'pending'),
(2, 1, 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
CREATE TABLE IF NOT EXISTS `lesson` (
  `lesson_id` int(11) NOT NULL AUTO_INCREMENT,
  `class_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `quiz_id` int(11) NOT NULL,
  `coursem_id` int(11) NOT NULL,
  `lesson_descriptions` varchar(50) NOT NULL,
  PRIMARY KEY (`lesson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`lesson_id`, `class_id`, `course_id`, `quiz_id`, `coursem_id`, `lesson_descriptions`) VALUES
(1, 5, 5, 6, 2, 'Korem Ipsum');

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
CREATE TABLE IF NOT EXISTS `1uiz` (
  `quiz_id` int(11) NOT NULL AUTO_INCREMENT,
  `quiz_name` varchar(50) NOT NULL,
  `quiz_type` varchar(10) NOT NULL,
  `quizq_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `quiz_descriptions` varchar(50) NOT NULL,
  `datetime_created` datetime NOT NULL,
  `passing_score` int(3) NOT NULL,
  `start_time` varchar(10) NOT NULL,
  `end_time` varchar(10) NOT NULL,
  `quiz_details` varchar(100) NOT NULL,
  `correct_answer` varchar(100) NOT NULL,
  PRIMARY KEY (`quiz_id`)
  FOREIGN KEY (`lesson_id`) REFERENCES lesson(`lesson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`quiz_id`, `quiz_name`, `quiz_type`, `quizq_id`, `lesson_id`, `quiz_descriptions`, `datetime_created`, `passing_score`,`start_time`, `end_time`, `quiz_details`, `correct_answer`) VALUES
(1, 'E02Quiz1', 'MCQ', 5, 5,'E02', '2021-09-26 00:00:00', 85, '00:00:000', '00:00:30', 'E02', 'Pear');


-- --------------------------------------------------------

--
-- Table structure for table `quizques`
--

-- DROP TABLE IF EXISTS `quizq`;
-- CREATE TABLE IF NOT EXISTS `1uiz` (
--   `quizq_id` int(11) NOT NULL AUTO_INCREMENT,
--   `quiz_id` int(11) NOT NULL,
--   `quiz_name` varchar(10) NOT NULL,
--   `lesson_id` int(11) NOT NULL,
--   `quiz_details` varchar(100) NOT NULL,
--   `correct_answer` varchar(100) NOT NULL,
--   PRIMARY KEY (`quizq_id`)
--   FOREIGN KEY (`quiz_id`) REFERENCES quiz(`quiz_id`)
-- ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --
-- -- Dumping data for table `quizq`
-- --

-- INSERT INTO `quizq` (`quizq_id`, `quiz_id`, `quiz_name`, `lesson_id`, `quiz_details`, `correct_answer`) VALUES
-- (1, 1, 'E02Quiz1', 5, 'E02', 'Pear');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 02, 2021 at 02:02 PM
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
DROP DATABASE IF EXISTS lms_course;
CREATE DATABASE IF NOT EXISTS `lms_course` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `lms_course`;
-- --------------------------------------------------------

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
CREATE TABLE IF NOT EXISTS `class` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `course_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `start_date` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `end_date` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `start_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `end_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `class_size` int(11) NOT NULL,
  `current_class_size` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `duration_of_class` int(11) NOT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`class_id`, `course_id`, `lesson_id`, `course_name`, `start_date`, `end_date`, `start_time`, `end_time`, `class_size`, `current_class_size`, `employee_id`, `duration_of_class`) VALUES
(2, 4, 3, 'Civil Engineer course', '01/09/2021', '01/12/2021', '14:00', '16:00', 10, 5, 1, 2),
(3, 4, 3, 'Civil Engineer course', '01/01/2021', '12/12/2021', '14:00', '16:00', 10, 10, 1, 2),
(4, 6, 4, 'Computer Engineering Class', '09/09/2022', '25/10/2022', '14:00', '16:00', 10, 0, 1, 2),
(5, 6, 4, 'Computer Engineering Class', '10/01/2020', '15/01/2020', '14:00', '16:00', 10, 0, 1, 2),
(6, 1, 5, 'Chemical engineering', '16/01/2020', '20/02/2020', '14:00', '16:00', 10, 10, 1, 2),
(7, 4, 3, 'Civil Engineer course', '01/02/2021', '10/02/2021', '14:00', '16:00', 10, 0, 1, 2),
(12, 4, 3, 'Civil Engineer course', '4/4/694', '4/20/69', '14:00', '16:00', 10, 0, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `total_no_of_class` int(11) NOT NULL,
  `total_no_of_lesson` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `course_description` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `course_prerequisite` int(11) NOT NULL,
  `coursem_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `start_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `end_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `datetime_uploaded` datetime NOT NULL,
  `start_enrol` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `end_enrol` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `total_no_of_class`, `total_no_of_lesson`, `class_id`, `course_description`, `course_prerequisite`, `coursem_id`, `employee_id`, `start_time`, `end_time`, `datetime_uploaded`, `start_enrol`, `end_enrol`) VALUES
(1, 'Chemical engineering', 1, 1, 1, 'This type of engineering concerns the use of chemical and biological processes to produce useful materials or substances. It’s a multidisciplinary subject, combining natural and experimental sciences (such as chemistry and physics), along with life sciences (such as biology, microbiology and biochemistry), plus mathematics and economics.', 0, 1, 2, '1 July 2021', '1 December 2021', '2021-06-23 00:00:00', '2021-06-23', '2021-06-23'),
(4, 'Civil Engineer', 3, 2, 2, 'Civil engineering is the professional practice of designing and developing infrastructure projects. This can be on a huge scale, such as the development of nationwide transport systems or water supply networks, or on a smaller scale, such as the development of single roads or buildings.', 0, 1, 2, '5 August 2021', '1 December 2021', '2021-08-17 00:00:00', '2021-06-23', '2021-06-23'),
(5, 'Electrical/electronic engineering', 1, 2, 5, 'Electrical and electronics engineering both focus on applications of electrical power. The two fields differ in that electrical engineers chiefly focus on the large-scale production and supply of electrical power, while electronics engineers focus on much smaller electronic circuits, such as those used in computers.', 0, 1, 1, '5 July 2021', '1 December 2021', '2021-09-14 00:00:00', '2021-09-14', '2021-09-14'),
(6, 'Computer Engineering', 2, 1, 5, '*This course has a prerequisite of Electrical Engineering*\r\nComputer engineering concerns the design and prototyping of computing hardware and software. This subject merges electrical engineering with computer science, and you may prefer to study computer engineering alongside one of these similar subjects.', 0, 1, 1, '8 September 2021', '18 September 2021', '2021-07-13 00:00:00', '2021-07-13', '2021-07-13');

-- --------------------------------------------------------

--
-- Table structure for table `course_material`
--

DROP TABLE IF EXISTS `course_material`;
CREATE TABLE IF NOT EXISTS `course_material` (
  `coursem_id` int(11) NOT NULL,
  `coursem_description` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `course_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `datetime_uploaded` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `course_prerequisite`
--

DROP TABLE IF EXISTS `course_prerequisite`;
CREATE TABLE IF NOT EXISTS `course_prerequisite` (
  `course_id` int(11) NOT NULL,
  `prerequisite_course_id` int(11) NOT NULL,
  PRIMARY KEY (`course_id`,`prerequisite_course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course_prerequisite`
--

INSERT INTO `course_prerequisite` (`course_id`, `prerequisite_course_id`) VALUES
(1, 5),
(2, 5),
(2, 6),
(3, 7),
(3, 8),
(6, 5),
(45, 46);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE IF NOT EXISTS `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) NOT NULL,
  `employee_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `employee_role` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_id`, `course_id`, `employee_name`, `employee_role`) VALUES
(1, 1, 'James', 'Engineer'),
(2, 2, 'Richard', 'Engineer'),
(3, 3, 'Lamy', 'Engineer'),
(4, 4, 'Kane', 'Human Resource');

-- --------------------------------------------------------

--
-- Table structure for table `employee_enrolled`
--

DROP TABLE IF EXISTS `employee_enrolled`;
CREATE TABLE IF NOT EXISTS `employee_enrolled` (
  `employee_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `class_id` int(11) DEFAULT NULL,
  `status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`employee_id`,`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee_enrolled`
--

INSERT INTO `employee_enrolled` (`employee_id`, `course_id`, `class_id`, `status`) VALUES
(1, 4, 2, 'in-progress');

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
  `lesson_descriptions` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lesson_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `quiz_type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `lesson_material` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `created_on` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`lesson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`lesson_id`, `class_id`, `course_id`, `quiz_id`, `lesson_descriptions`, `lesson_name`, `quiz_type`, `lesson_material`, `created_on`) VALUES
(10, 5, 6, 0, 'Lesson 1 Descriptions', 'Lesson1', 'ungraded', 'https://drive.google.com/drive/folders/1D4aDjMm1LxaD6187eLMj70i6lG4QfAI7?usp=sharing', '11/2/2021 9:14:35 PM'),
(11, 5, 6, 0, 'Lesson 2 Descriptions', 'Lesson2', 'ungraded', 'https://drive.google.com/drive/folders/1D4aDjMm1LxaD6187eLMj70i6lG4QfAI7?usp=sharing', '11/2/2021 9:15:28 PM'),
(12, 5, 6, 0, 'Lesson 3 Descriptions', 'Lesson3', 'ungraded', 'https://drive.google.com/drive/folders/1D4aDjMm1LxaD6187eLMj70i6lG4QfAI7?usp=sharing', '11/2/2021 9:17:10 PM'),
(13, 5, 6, 0, 'Final Quiz Descriptions', 'FinalQuiz', 'graded', 'https://drive.google.com/drive/folders/1D4aDjMm1LxaD6187eLMj70i6lG4QfAI7?usp=sharing', '11/2/2021 9:17:21 PM'),
(14, 2, 4, 3, 'Lesson 1 Descriptions', 'Lesson1', 'ungraded', 'https://drive.google.com/drive/folders/1D4aDjMm1LxaD6187eLMj70i6lG4QfAI7?usp=sharing', '11/2/2021 9:58:57 PM'),
(15, 2, 4, 0, 'Lesson 2 Descriptions', 'Lesson2', 'ungraded', 'https://drive.google.com/drive/folders/1D4aDjMm1LxaD6187eLMj70i6lG4QfAI7?usp=sharing', '11/2/2021 9:59:09 PM'),
(16, 2, 4, 0, 'Lesson 3 Descriptions\r\n', 'Lesson3', 'ungraded', 'https://drive.google.com/drive/folders/1D4aDjMm1LxaD6187eLMj70i6lG4QfAI7?usp=sharing', '11/2/2021 9:59:18 PM'),
(17, 2, 4, 0, 'Final Quiz Descriptions', 'FinalQuiz', 'ungraded', 'https://drive.google.com/drive/folders/1D4aDjMm1LxaD6187eLMj70i6lG4QfAI7?usp=sharing', '11/2/2021 9:59:28 PM');

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
CREATE TABLE IF NOT EXISTS `quiz` (
  `quiz_id` int(11) NOT NULL AUTO_INCREMENT,
  `quiz_type` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `quiz_question` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `datetime_created` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `passing_score` int(3) DEFAULT NULL,
  `correct_answer` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `question_type` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `time_limit` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `quiz_selection` varchar(500) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`quiz_id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`quiz_id`, `quiz_type`, `lesson_id`, `quiz_question`, `datetime_created`, `passing_score`, `correct_answer`, `question_type`, `time_limit`, `quiz_selection`) VALUES
(2, 'ungraded', 14, 'Electrons are larger than molecules', '11/2/2021 9:59:46 PM', 0, 'True', 'True/False', '30 minutes', 'True,False'),
(3, 'ungraded', 14, 'What\'s the biggest animal in the world?', '11/2/2021 9:59:46 PM', 0, 'Whale', 'MCQ', '30 minutes', 'Tiger,Cow,Whale'),
(4, 'ungraded', 14, 'Sharks are mammals', '11/2/2021 9:59:46 PM', 0, 'True', 'True/False', '30 minutes', 'True,False');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `quiz`
--
ALTER TABLE `quiz`
  ADD CONSTRAINT `quiz_ibfk_1` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`lesson_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

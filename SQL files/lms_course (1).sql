-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 20, 2021 at 08:55 AM
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
CREATE DATABASE IF NOT EXISTS `lms_course` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
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
  `course_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `start_date` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `end_date` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `start_time` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `end_time` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `class_size` int(11) NOT NULL,
  `current_class_size` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `duration_of_class` int(11) NOT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`class_id`, `course_id`, `lesson_id`, `course_name`, `start_date`, `end_date`, `start_time`, `end_time`, `class_size`, `current_class_size`, `employee_id`, `duration_of_class`) VALUES
(2, 4, 3, 'Civil Engineer course', '1 September 2021', '1 December 2021', '14:00', '16:00', 10, 4, 1, 2),
(3, 4, 3, 'Civil Engineer course', '1 January 2021', '25 October 2022', '14:00', '16:00', 10, 10, 1, 2),
(4, 6, 4, 'Computer Engineering Class', '25 October 2021', '25 October 2022', '14:00', '16:00', 10, 0, 1, 2),
(5, 6, 4, 'Computer Engineering Class', '1 January 2020', '20 January 2020', '14:00', '16:00', 10, 0, 1, 2),
(6, 1, 5, 'Chemical engineering', '1 January 2020', '20 January 2020', '14:00', '16:00', 10, 10, 1, 2),
(7, 4, 3, 'Civil Engineer course', '1 January 2021', '10 February 2021', '14:00', '16:00', 10, 0, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE IF NOT EXISTS `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `total_no_of_class` int(11) NOT NULL,
  `total_no_of_lesson` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `course_description` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `course_prerequisite` int(11) NOT NULL,
  `coursem_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `start_time` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `end_time` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `datetime_uploaded` datetime NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `total_no_of_class`, `total_no_of_lesson`, `class_id`, `course_description`, `course_prerequisite`, `coursem_id`, `employee_id`, `start_time`, `end_time`, `datetime_uploaded`) VALUES
(1, 'Chemical engineering', 1, 1, 1, 'This type of engineering concerns the use of chemical and biological processes to produce useful materials or substances. It’s a multidisciplinary subject, combining natural and experimental sciences (such as chemistry and physics), along with life sciences (such as biology, microbiology and biochemistry), plus mathematics and economics.', 0, 1, 2, '1 July 2021', '1 December 2021', '2021-06-23 00:00:00'),
(4, 'Civil Engineer', 1, 1, 1, 'Civil engineering is the professional practice of designing and developing infrastructure projects. This can be on a huge scale, such as the development of nationwide transport systems or water supply networks, or on a smaller scale, such as the development of single roads or buildings.', 0, 1, 2, '5 August 2021', '1 December 2021', '2021-08-17 00:00:00'),
(5, 'Electrical/electronic engineering', 1, 2, 5, 'Electrical and electronics engineering both focus on applications of electrical power. The two fields differ in that electrical engineers chiefly focus on the large-scale production and supply of electrical power, while electronics engineers focus on much smaller electronic circuits, such as those used in computers.', 0, 1, 1, '5 July 2021', '1 December 2021', '2021-09-14 00:00:00'),
(6, 'Computer Engineering', 1, 1, 5, '*This course has a prerequisite of Electrical Engineering*\r\nComputer engineering concerns the design and prototyping of computing hardware and software. This subject merges electrical engineering with computer science, and you may prefer to study computer engineering alongside one of these similar subjects.', 0, 1, 1, '8 September 2021', '18 September 2021', '2021-07-13 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `course_material`
--

DROP TABLE IF EXISTS `course_material`;
CREATE TABLE IF NOT EXISTS `course_material` (
  `coursem_id` int(11) NOT NULL,
  `coursem_description` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
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
  `employee_name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `employee_role` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
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
  `status` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
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
  `coursem_id` int(11) NOT NULL,
  `lesson_descriptions` mediumtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`lesson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`lesson_id`, `class_id`, `course_id`, `quiz_id`, `coursem_id`, `lesson_descriptions`) VALUES
(1, 5, 5, 6, 2, 'Korem Ipsum'),
(2, 5, 5, 2, 2, 'Placeholder'),
(3, 3, 4, 1, 2, 'This program prepares students for employment as a CIVIL ENGINEERING DRAFTER or DESIGNER, or in the architecture or construction fields.  Civil drafters create detailed technical drawings of buildings, structures, and various construction projects designed by architects and civil engineers.  Civil drafters must be proficient in CAD software commonly used in industry (AutoCAD, Civil 3D, REVIT) and have knowledge of current industry drafting practices.  Employment is available in private industry '),
(4, 3, 4, 2, 2, 'A standard range of conventions and symbols are used to understand and read the engineering drawings. The engineering drawings, at first glance, look incomprehensible, they need to be comprehended by means of specific types of symbols and codes. Engineering drawings are prepared on the basis of technical standards and professional codes, in order to be read by anyone without any difficulty and misinterpretation. Following elements are required to comprehend for reading an engineering drawing. Th');

-- --------------------------------------------------------

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
CREATE TABLE IF NOT EXISTS `quiz` (
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
  PRIMARY KEY (`quiz_id`),
  KEY `lesson_id` (`lesson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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

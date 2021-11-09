-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 09, 2021 at 11:56 AM
-- Server version: 10.2.38-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lms_course`
--
CREATE DATABASE IF NOT EXISTS `lms_course` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `lms_course`;

-- --------------------------------------------------------

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
CREATE TABLE `class` (
  `class_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `course_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `start_date` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `end_date` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `start_time` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `end_time` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `class_size` int(11) NOT NULL,
  `current_class_size` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `duration_of_class` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`class_id`, `course_id`, `lesson_id`, `course_name`, `start_date`, `end_date`, `start_time`, `end_time`, `class_size`, `current_class_size`, `employee_id`, `duration_of_class`) VALUES
(2, 4, 3, 'Basic Printer Repair', '01/09/2021', '01/12/2021', '14:00', '16:00', 10, 1, 1, 2),
(3, 4, 3, 'Basic Printer Repair', '01/01/2021', '12/12/2021', '14:00', '16:00', 10, 10, 1, 2),
(4, 6, 4, 'Computer Engineering Class', '09/09/2022', '25/10/2022', '14:00', '16:00', 10, 0, 1, 2),
(5, 6, 4, 'Computer Engineering Class', '10/01/2020', '15/01/2020', '14:00', '16:00', 10, 0, 1, 2),
(6, 1, 5, 'Clearing Errors for Brother Printers', '16/01/2020', '20/02/2020', '14:00', '16:00', 10, 10, 1, 2),
(7, 4, 3, 'Basic Printer Repair', '01/02/2021', '10/02/2021', '14:00', '16:00', 10, 0, 1, 2),
(13, 5, 3, 'Electrical/electronic engineering', '01/02/2021', '12/12/2022', '14:00', '16:00', 10, 0, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `course_id` int(11) NOT NULL,
  `course_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `total_no_of_class` int(11) NOT NULL,
  `total_no_of_lesson` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `course_description` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `course_prerequisite` int(11) NOT NULL,
  `coursem_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  `start_time` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `end_time` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime_uploaded` datetime NOT NULL,
  `start_enrol` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `end_enrol` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `total_no_of_class`, `total_no_of_lesson`, `class_id`, `course_description`, `course_prerequisite`, `coursem_id`, `employee_id`, `start_time`, `end_time`, `datetime_uploaded`, `start_enrol`, `end_enrol`) VALUES
(1, 'Clearing Errors for Brother Printers', 1, 1, 1, 'Experiencing a paper jam can be a frustrating interruption to your work day, but there are easy steps to follow to clear them quickly and safely when a paper jam error pops up on your Brother printer’s display screen. The course mentions a specific printer model; however, the process is the same for most Brother printers.', 0, 1, 2, '01/07/2021 9:00', '01/07/2022 18:00', '2021-06-23 00:00:00', '01/07/2021', '01/07/2022'),
(4, 'Basic Printer Repair', 3, 2, 1, 'A computer printer is an electronic component that gets data from a computer through a cable and converts the data into a series of small dots that form letters or images on paper.\r\n\r\nThere are three types of computer printers used by consumers: the older dot-matrix and the newer ink-jet and laser printers. Each prints differently. This course will go through the basics of repairing', 0, 1, 2, '01/12/2021 12:00', '15/05/2022 12:00', '2021-08-17 00:00:00', '01/12/2021', '15/05/2022'),
(5, 'Electrical/electronic engineering', 1, 2, 5, 'Electrical and electronics engineering both focus on applications of electrical power. The two fields differ in that electrical engineers chiefly focus on the large-scale production and supply of electrical power, while electronics engineers focus on much smaller electronic circuits, such as those used in computers.', 0, 1, 1, '12/01/2020 12:00', '12/02/2021 12:00', '2021-09-14 00:00:00', '12/01/2020', '12/02/2021'),
(6, 'Computer Engineering', 2, 1, 5, '*This course has a prerequisite of Electrical Engineering*\r\nComputer engineering concerns the design and prototyping of computing hardware and software. This subject merges electrical engineering with computer science, and you may prefer to study computer engineering alongside one of these similar subjects.', 0, 1, 1, '01/09/2021 12:00', '12/12/2022 12:00', '2021-07-13 00:00:00', '01/09/2021', '12/12/2022');

-- --------------------------------------------------------

--
-- Table structure for table `course_prerequisite`
--

DROP TABLE IF EXISTS `course_prerequisite`;
CREATE TABLE `course_prerequisite` (
  `course_id` int(11) NOT NULL,
  `prerequisite_course_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `course_prerequisite`
--

INSERT INTO `course_prerequisite` (`course_id`, `prerequisite_course_id`) VALUES
(6, 5);

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `employee_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employee_role` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`employee_id`, `course_id`, `employee_name`, `employee_role`) VALUES
(1, 1, 'James', 'Engineer'),
(2, 2, 'Richard', 'Engineer'),
(3, 3, 'Lamy', 'Engineer'),
(4, 4, 'Kane', 'Human Resource'),
(5, 5, 'Johnson', 'Trainer');

-- --------------------------------------------------------

--
-- Table structure for table `employee_enrolled`
--

DROP TABLE IF EXISTS `employee_enrolled`;
CREATE TABLE `employee_enrolled` (
  `employee_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `class_id` int(11) DEFAULT NULL,
  `status` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
CREATE TABLE `lesson` (
  `lesson_id` int(11) NOT NULL,
  `class_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `quiz_id` int(11) NOT NULL,
  `lesson_descriptions` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `lesson_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quiz_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `lesson_material` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_on` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
CREATE TABLE `quiz` (
  `quiz_id` int(11) NOT NULL,
  `quiz_type` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `quiz_question` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `datetime_created` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `passing_score` int(3) DEFAULT NULL,
  `correct_answer` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `question_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `time_limit` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quiz_selection` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`quiz_id`, `quiz_type`, `lesson_id`, `quiz_question`, `datetime_created`, `passing_score`, `correct_answer`, `question_type`, `time_limit`, `quiz_selection`) VALUES
(2, 'ungraded', 14, 'Electrons are larger than molecules', '11/2/2021 9:59:46 PM', 0, 'True', 'True/False', '30 minutes', 'True,False'),
(3, 'ungraded', 14, 'What\'s the biggest animal in the world?', '11/2/2021 9:59:46 PM', 0, 'Whale', 'MCQ', '30 minutes', 'Tiger,Cow,Whale'),
(4, 'ungraded', 14, 'Sharks are mammals', '11/2/2021 9:59:46 PM', 0, 'True', 'True/False', '30 minutes', 'True,False');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`class_id`);

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `course_prerequisite`
--
ALTER TABLE `course_prerequisite`
  ADD PRIMARY KEY (`course_id`,`prerequisite_course_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`employee_id`);

--
-- Indexes for table `employee_enrolled`
--
ALTER TABLE `employee_enrolled`
  ADD PRIMARY KEY (`employee_id`,`course_id`);

--
-- Indexes for table `lesson`
--
ALTER TABLE `lesson`
  ADD PRIMARY KEY (`lesson_id`);

--
-- Indexes for table `quiz`
--
ALTER TABLE `quiz`
  ADD PRIMARY KEY (`quiz_id`),
  ADD KEY `lesson_id` (`lesson_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `class`
--
ALTER TABLE `class`
  MODIFY `class_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `employee_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `lesson`
--
ALTER TABLE `lesson`
  MODIFY `lesson_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `quiz`
--
ALTER TABLE `quiz`
  MODIFY `quiz_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

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

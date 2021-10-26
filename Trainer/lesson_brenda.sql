-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Oct 23, 2021 at 08:46 AM
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
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
CREATE TABLE IF NOT EXISTS `lesson` (
  `lesson_id` int(11) NOT NULL AUTO_INCREMENT,
  `class_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `quiz_id` int(11) NOT NULL,
  `lesson_descriptions` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `lesson_name` varchar(50) NOT NULL,
  `quiz_type` varchar(50) NOT NULL,
  `lesson_material` varchar(100) DEFAULT NULL,
  `created_on` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`lesson_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lesson` (`lesson_id`, `class_id`, `course_id`, `quiz_id`, `lesson_descriptions`, `lesson_name`, `quiz_type`, `lesson_material`, `created_on`) VALUES
(1, 5, 5, 6, 'Korem Ipsum', 'apple', 'Ungraded', NULL, '2021-10-05 21:35:50'),
(3, 0, 0, 0, '', '', '', '', '0000-00-00 00:00:00'),
(4, 2, 3, 4, 'testing', 'testing', 'ungraded', '', '0000-00-00 00:00:00'),
(5, 2, 3, 4, 'testing', 'testing', 'ungraded', '', '0000-00-00 00:00:00'),
(6, 2, 3, 4, 'testing', 'testing', 'ungraded', '', '0000-00-00 00:00:00'),
(7, 3487, 3487, 3487, 'w', 'w', 'graded', '3487', '0000-00-00 00:00:00'),
(8, 3487, 3487, 3487, 'w', 'w', 'graded', '', '0000-00-00 00:00:00'),
(9, 3487, 3487, 3487, 'test', 'test', 'graded', '', '0000-00-00 00:00:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

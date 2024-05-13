-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 29, 2024 at 02:15 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2vehicledamageinsdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `cregtb`
--

CREATE TABLE `cregtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `cregtb`
--

INSERT INTO `cregtb` (`id`, `Name`, `Mobile`, `Email`, `UserName`, `Password`) VALUES
(3, 'ICIC', '9486365535', 'sangeeth5535@gmail.com', 'ICIC', 'ICIC');

-- --------------------------------------------------------

--
-- Table structure for table `insurtb`
--

CREATE TABLE `insurtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Body` varchar(250) NOT NULL,
  `Level` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Cname` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `insurtb`
--

INSERT INTO `insurtb` (`id`, `UserName`, `Body`, `Level`, `Amount`, `Status`, `Cname`) VALUES
(1, 'san', '0001.jpeg', '0001.JPEG', '30000 - 50000 INR', 'Approved', 'ICIC'),
(2, 'san', '1280.png', '2440.png', '60000- 80000 INR', 'Reject', 'ICIC'),
(3, 'dharani', '4327.png', '4217.png', '60000- 80000 INR', 'Approved', 'ICIC');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `VehicleNo` varchar(50) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Mobile`, `Email`, `VehicleNo`, `UserName`, `Password`) VALUES
(2, 'jai', '9486365535', 'sangeeth5535@gmail.com', '21BH2345AA', 'jai', 'jai'),
(3, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'TN48AL5535', 'san', 'san'),
(4, 'dharani', '9597610859', 'dharani@gmail.com', 'TN48AL5589', 'dharani', 'dharani');

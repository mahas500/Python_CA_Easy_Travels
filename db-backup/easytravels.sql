﻿--
-- Script was generated by Devart dbForge Studio for MySQL, Version 8.0.40.0
-- Product home page: http://www.devart.com/dbforge/mysql/studio
-- Script date 27-12-2019 01:05:24 AM
-- Server version: 5.6.45-log
-- Client version: 4.1
--

-- 
-- Disable foreign keys
-- 
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;

-- 
-- Set SQL mode
-- 
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- 
-- Set character set the client will use to send SQL statements to the server
--
SET NAMES 'utf8';

--
-- Set default database
--
USE easytravels;

--
-- Drop table `employee_role_mapping`
--
DROP TABLE IF EXISTS employee_role_mapping;

--
-- Drop table `employee`
--
DROP TABLE IF EXISTS employee;

--
-- Drop table `employee_role`
--
DROP TABLE IF EXISTS employee_role;

--
-- Set default database
--
USE easytravels;

--
-- Create table `employee_role`
--
CREATE TABLE employee_role (
  role_id int(11) NOT NULL,
  role_name varchar(30) NOT NULL,
  PRIMARY KEY (role_id)
)
ENGINE = INNODB,
AVG_ROW_LENGTH = 3276,
CHARACTER SET utf8,
COLLATE utf8_general_ci;

--
-- Create table `employee`
--
CREATE TABLE employee (
  employee_id varchar(40) NOT NULL,
  name varchar(50) NOT NULL,
  username varchar(20) NOT NULL,
  password varchar(20) NOT NULL,
  email varchar(50) NOT NULL,
  contact_no varchar(15) NOT NULL,
  session_id varchar(40) DEFAULT NULL,
  created_on datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (employee_id)
)
ENGINE = INNODB,
CHARACTER SET utf8,
COLLATE utf8_general_ci;

--
-- Create table `employee_role_mapping`
--
CREATE TABLE employee_role_mapping (
  mapping_id varchar(40) NOT NULL,
  employee_id varchar(40) NOT NULL,
  role_id int(11) NOT NULL,
  created_on datetime DEFAULT NULL,
  PRIMARY KEY (mapping_id)
)
ENGINE = INNODB,
CHARACTER SET utf8,
COLLATE utf8_general_ci;

--
-- Create foreign key
--
ALTER TABLE employee_role_mapping
ADD CONSTRAINT employee_id_fk2 FOREIGN KEY (employee_id)
REFERENCES employee (employee_id);

--
-- Create foreign key
--
ALTER TABLE employee_role_mapping
ADD CONSTRAINT role_id_fk FOREIGN KEY (role_id)
REFERENCES employee_role (role_id);

-- 
-- Dumping data for table employee_role
--
INSERT INTO employee_role VALUES
(1, 'HR'),
(2, 'OPERATION'),
(3, 'ADMIN'),
(4, 'SALES'),
(5, 'OPERATION HEAD');

-- 
-- Dumping data for table employee
--
INSERT INTO employee VALUES
('f8bc75b0-7b89-4a56-942e-139426b77483', 'Saurabh Devade', 'saurabh_123', 'pass@123', 'saurabh.devade21@gmail.com', '897646767', '58264184-51d0-4365-857d-261517febe4f', '2019-12-09 20:44:02');

-- 
-- Dumping data for table employee_role_mapping
--
-- Table easytravels.employee_role_mapping does not contain any data (it is empty)

-- 
-- Restore previous SQL mode
-- 
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;

-- 
-- Enable foreign keys
-- 
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
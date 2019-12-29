-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: easytravels
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `booking` (
  `booking_id` varchar(40) NOT NULL,
  `customer_id` varchar(40) NOT NULL,
  `package_id` varchar(40) NOT NULL,
  `created_on` datetime NOT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `booking_ibfk_1` (`customer_id`),
  KEY `booking_ibfk_4` (`package_id`),
  CONSTRAINT `booking_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `booking_ibfk_4` FOREIGN KEY (`package_id`) REFERENCES `package` (`package_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES ('7bc3ba6d-b35f-4f97-a6a4-acf4a3fd3ead','ee3c1ac0-9c7f-4353-bd78-a72c3d2225b1','b7c12385-856d-46b4-bd05-954a531c7444','2019-12-17 15:12:00'),('cfaa8810-cd66-4450-bed4-9b4414490e5f','45b83100-e7aa-448e-8447-d023c949e799','10ddc398-4405-48ad-ab5f-95322451eff3','2019-12-17 14:16:22');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `customer_id` varchar(40) NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact_no` varchar(15) NOT NULL,
  `session_id` varchar(40) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('27782282-79a5-4db5-8152-4869397a8b37','Manik','manik325','manik123','manik@gmail.com','98453443573','5c033fba-e13b-401b-a2e6-c6904d3d950e',NULL),('450a65f9-d24c-4b19-8466-79b874c1c854','mahas5000120','Florence','Italy','mahasha@gmail.com','22634634','dd95defc-e392-4146-ac64-d9ca2d3b47cd',NULL),('45b83100-e7aa-448e-8447-d023c949e799','Aatmaj Deshmukh','atdeshmukh89','89deshaat','aatmaj@intel.co.in','65655656454',NULL,'2019-12-13 23:23:58'),('643aff20-b59e-45d5-8746-64af662b6204','mahas5000','Florence','Italy','mahasha@gmail.com','22634634','67a18907-876b-49dd-b21f-ad9c715aeeee',NULL),('9b84c0e9-b566-4dd4-b57b-77a8f9035290','manik123','Florence','Italy','mahasha@gmail.com','22634634','b33631cc-24dd-4183-9ad8-f8c6b7e6d98b',NULL),('aa989f57-5f8e-425d-b257-8a989de1e6dc','manik123','Florence','Italy','mahasha@gmail.com','22634634','f5e08c5d-3e3c-4618-9009-1f14b294fe76',NULL),('c051433b-3e07-4789-a122-bc029b59e74f','mahas500','Florence','Italy','mahasha@gmail.com','22634634','9255b16f-964c-4718-b146-911cf6e3f46f',NULL),('c4367e13-41be-496a-9638-1e3acafa1a58','manik123','Florence','Italy','mahasha@gmail.com','22634634','c3c4f714-8fe9-4a4f-b1db-eba036cb977e',NULL),('ee3c1ac0-9c7f-4353-bd78-a72c3d2225b1','Avdhoot Hande','avd@1234','23123212','avd@hnade.com','51231231531',NULL,'2019-12-17 15:11:28');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `employee_id` varchar(40) NOT NULL,
  `name` varchar(50) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact_no` varchar(15) NOT NULL,
  `session_id` varchar(80) DEFAULT NULL,
  `created_on` datetime DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('02b10ba6-4853-4442-b5a3-5697367fd122','Pratik Yadav','psy_1234','ydava@pratik','ypyadav@gmail.com','9898956556',NULL,'2019-12-17 14:10:53'),('6848be80-5c58-4d4f-b11f-d1e76f6c92b5','Manik Mahashabde','manik_123','man@1991','manik@mydbs.ie','867866545','fa0b17b3-ca91-4934-9f79-12b0a481c96d','2019-12-09 20:51:27'),('9eb496f7-449a-4db4-8cf4-1f9c02ddec3f','Sagar Patil','patil_sagar','sg@1995','sagar.patil@gmail.com','5645345454',NULL,'2019-12-17 14:09:04'),('a3444f02-3272-44bb-8507-4f96d6573f8f','Sabitha Maram','sabitha@1997','sab_maram','sabitha@gmail.com','9565968595',NULL,'2019-12-09 20:52:28'),('f8bc75b0-7b89-4a56-942e-139426b77483','Saurabh Devade','saurabh_123','pass@123','saurabh.devade21@gmail.com','897646767','f8bc75b0-7b89-4a56-942e-139426b774831576433659993','2019-12-09 20:44:02');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_role`
--

DROP TABLE IF EXISTS `employee_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_role` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(30) NOT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_role`
--

LOCK TABLES `employee_role` WRITE;
/*!40000 ALTER TABLE `employee_role` DISABLE KEYS */;
INSERT INTO `employee_role` VALUES (1,'HR'),(2,'OPERATION'),(3,'ADMIN'),(4,'SALES'),(5,'OPERATION HEAD');
/*!40000 ALTER TABLE `employee_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_role_mapping`
--

DROP TABLE IF EXISTS `employee_role_mapping`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_role_mapping` (
  `mapping_id` varchar(40) NOT NULL,
  `employee_id` varchar(40) NOT NULL,
  `role_id` int(11) NOT NULL,
  `created_on` datetime NOT NULL,
  PRIMARY KEY (`mapping_id`),
  KEY `employee_role_mapping_ibfk_1` (`employee_id`),
  KEY `employee_role_mapping_ibfk_2` (`role_id`),
  CONSTRAINT `employee_role_mapping_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `employee_role_mapping_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `employee_role` (`role_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_role_mapping`
--

LOCK TABLES `employee_role_mapping` WRITE;
/*!40000 ALTER TABLE `employee_role_mapping` DISABLE KEYS */;
INSERT INTO `employee_role_mapping` VALUES ('4af729be-7089-43f6-bc19-9fca6d3726ee','6848be80-5c58-4d4f-b11f-d1e76f6c92b5',4,'2019-12-13 23:17:48'),('a3c5f7a9-5c63-4788-a4b9-5d2652354031','02b10ba6-4853-4442-b5a3-5697367fd122',1,'2019-12-17 14:12:28'),('a8b0ac6a-8c0b-4480-a9c3-ef86479df89f','9eb496f7-449a-4db4-8cf4-1f9c02ddec3f',3,'2019-12-17 14:12:54'),('ad521239-9107-43ef-8c9e-c6f6d6c5118e','a3444f02-3272-44bb-8507-4f96d6573f8f',5,'2019-12-17 15:13:48'),('ff3a7226-49a3-42ff-a842-1a7be63fc1b0','f8bc75b0-7b89-4a56-942e-139426b77483',2,'2019-12-09 20:56:25');
/*!40000 ALTER TABLE `employee_role_mapping` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enquiry`
--

DROP TABLE IF EXISTS `enquiry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `enquiry` (
  `enquiry_id` varchar(40) NOT NULL,
  `employee_id` varchar(40) NOT NULL,
  `customer_id` varchar(40) NOT NULL,
  `enquiry_detail` text NOT NULL,
  `enquiry_type` varchar(20) NOT NULL,
  `created_on` datetime DEFAULT NULL,
  `required_days` int(11) DEFAULT NULL,
  `required_nights` int(11) DEFAULT NULL,
  `required_country` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`),
  KEY `customer_id` (`customer_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `enquiry_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `enquiry_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enquiry`
--

LOCK TABLES `enquiry` WRITE;
/*!40000 ALTER TABLE `enquiry` DISABLE KEYS */;
INSERT INTO `enquiry` VALUES ('4cd27bba-88d8-4d2c-8ee1-86d2ca66e615','6848be80-5c58-4d4f-b11f-d1e76f6c92b5','45b83100-e7aa-448e-8447-d023c949e799','Looking for 5 dayl holiday package in North Indian','DOMESTIC','2019-12-13 23:30:59',5,4,'India'),('6da738d0-c680-4df9-8080-769d2e889f44','6848be80-5c58-4d4f-b11f-d1e76f6c92b5','ee3c1ac0-9c7f-4353-bd78-a72c3d2225b1','Kanaykumari 9 days','DOMESTIC','2019-12-17 15:37:20',9,8,'India');
/*!40000 ALTER TABLE `enquiry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `package`
--

DROP TABLE IF EXISTS `package`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `package` (
  `package_id` varchar(40) NOT NULL,
  `employee_id` varchar(40) NOT NULL,
  `package_display_name` varchar(100) NOT NULL,
  `unique_url_name` varchar(50) NOT NULL,
  `days` int(11) NOT NULL,
  `night` int(11) NOT NULL,
  `charges` varchar(30) NOT NULL,
  `country` varchar(30) NOT NULL,
  `city` varchar(30) NOT NULL,
  `valid` datetime NOT NULL,
  `created_on` datetime NOT NULL,
  PRIMARY KEY (`package_id`),
  UNIQUE KEY `unique_url_name` (`unique_url_name`),
  KEY `package_ibfk_1` (`employee_id`),
  CONSTRAINT `package_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee` (`employee_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `package`
--

LOCK TABLES `package` WRITE;
/*!40000 ALTER TABLE `package` DISABLE KEYS */;
INSERT INTO `package` VALUES ('10ddc398-4405-48ad-ab5f-95322451eff3','f8bc75b0-7b89-4a56-942e-139426b77483','Bali Escape','bali-escape',6,5,'50,000','Indonesia','Baturiti','2020-01-01 00:00:00','2019-12-13 21:06:16'),('50fe2bda-706c-40e9-902a-63a3b76d6b0e','f8bc75b0-7b89-4a56-942e-139426b77483','Spectacular Thailand','Spectacular Thailand',6,5,'1525296','Thailand','Phuket','2019-12-27 14:49:31','2019-12-17 14:30:49'),('a13ad548-639c-4462-83d0-d858b23b341c','f8bc75b0-7b89-4a56-942e-139426b77483','Singapore Sentosa Getaway','singapore-sentosa-getaway',4,3,'100000','Singapore','Sentosa','2019-12-19 14:28:42','2019-10-23 13:20:19'),('b7c12385-856d-46b4-bd05-954a531c7444','f8bc75b0-7b89-4a56-942e-139426b77483','Australia\'s Northern Territory','australia',8,7,'1022201','Australia','Sydney','2019-12-19 15:07:33','2019-12-17 15:07:34'),('bc6637bf-21f6-4bac-84b3-fa016321b89b','f8bc75b0-7b89-4a56-942e-139426b77483','Glimpses of Muscat','glimpses-of-muscat',4,3,'120000','Oman','Muscat ','2019-12-12 14:58:07','2019-12-17 14:58:09');
/*!40000 ALTER TABLE `package` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-29 15:28:24

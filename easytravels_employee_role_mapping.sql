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
  PRIMARY KEY (`mapping_id`)
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
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-26 22:26:56

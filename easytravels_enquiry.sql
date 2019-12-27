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
  `created_on` datetime NOT NULL,
  `required_days` int(11) DEFAULT NULL,
  `required_nights` int(11) DEFAULT NULL,
  `required_country` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`enquiry_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enquiry`
--

LOCK TABLES `enquiry` WRITE;
/*!40000 ALTER TABLE `enquiry` DISABLE KEYS */;
INSERT INTO `enquiry` VALUES ('02507b42-a023-4271-929d-4d5abecb620b','6848be80-5c58-4d4f-b11f-d1e76f6c92b5','a81230ab-1510-46e2-b9b4-64fd62fc9911','Urgent requirement for Portugal','INTERNATIONAL','2019-12-17 15:35:59',5,4,'Portugal'),('4cd27bba-88d8-4d2c-8ee1-86d2ca66e615','6848be80-5c58-4d4f-b11f-d1e76f6c92b5','45b83100-e7aa-448e-8447-d023c949e799','Looking for 5 dayl holiday package in North Indian','DOMESTIC','2019-12-13 23:30:59',5,4,'India'),('6da738d0-c680-4df9-8080-769d2e889f44','6848be80-5c58-4d4f-b11f-d1e76f6c92b5','ee3c1ac0-9c7f-4353-bd78-a72c3d2225b1','Kanaykumari 9 days','DOMESTIC','2019-12-17 15:37:20',9,8,'India'),('b31cd01b-f3d0-4156-b5b7-2896023b8765','6848be80-5c58-4d4f-b11f-d1e76f6c92b5','a81230ab-1510-46e2-b9b4-64fd62fc9911','Want to visit to Singapore in this winter','INTERNATIONAL','2019-12-13 23:19:40',5,4,'Singapore'),('c90011b2-2082-4cf6-9dc5-62ad6bbd54d3','6848be80-5c58-4d4f-b11f-d1e76f6c92b5','4bbfe99e-c7fa-46c5-bd84-62bd1b488611','Have to visit to london for office work','INTERNATIONAL','2019-12-13 23:28:46',3,2,'England');
/*!40000 ALTER TABLE `enquiry` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-26 22:26:58

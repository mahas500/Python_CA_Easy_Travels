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
  UNIQUE KEY `unique_url_name` (`unique_url_name`)
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

-- Dump completed on 2019-12-26 22:26:58

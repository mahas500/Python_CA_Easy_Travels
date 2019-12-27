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
  PRIMARY KEY (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking`
--

LOCK TABLES `booking` WRITE;
/*!40000 ALTER TABLE `booking` DISABLE KEYS */;
INSERT INTO `booking` VALUES ('4c724dbc-98f3-4356-8851-949706719eba','a81230ab-1510-46e2-b9b4-64fd62fc9911','10ddc398-4405-48ad-ab5f-95322451eff3','2019-12-13 22:05:44'),('7b0c4caf-e020-43d7-99fa-7fb1aac9cfe5','4bbfe99e-c7fa-46c5-bd84-62bd1b488611','50fe2bda-706c-40e9-902a-63a3b76d6b0e','2019-12-27 15:09:06'),('7bc3ba6d-b35f-4f97-a6a4-acf4a3fd3ead','ee3c1ac0-9c7f-4353-bd78-a72c3d2225b1','b7c12385-856d-46b4-bd05-954a531c7444','2019-12-17 15:12:00'),('a6f9974d-55d6-4971-b7d8-873f51471400','4bbfe99e-c7fa-46c5-bd84-62bd1b488611','a13ad548-639c-4462-83d0-d858b23b341c','2019-12-17 15:10:27'),('ccf59898-ea33-47b6-a619-492741778ba2','a81230ab-1510-46e2-b9b4-64fd62fc9911','bc6637bf-21f6-4bac-84b3-fa016321b89b','2019-12-17 15:12:29'),('cfaa8810-cd66-4450-bed4-9b4414490e5f','45b83100-e7aa-448e-8447-d023c949e799','10ddc398-4405-48ad-ab5f-95322451eff3','2019-12-17 14:16:22');
/*!40000 ALTER TABLE `booking` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-26 22:26:59

-- MySQL dump 10.13  Distrib 8.0.13, for macos10.14 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Event`
--

DROP TABLE IF EXISTS `Event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` varchar(100) DEFAULT NULL,
  `unit` varchar(100) DEFAULT NULL,
  `lang` varchar(45) DEFAULT NULL,
  `url` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `person` varchar(45) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `iden` varchar(100) DEFAULT NULL,
  `title` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event`
--

LOCK TABLES `Event` WRITE;
/*!40000 ALTER TABLE `Event` DISABLE KEYS */;
INSERT INTO `Event` VALUES (1,'2018-10-24T00:00:00+08:00to2018-10-24T00:00:00+08:00','Honours College','English','http://news.umac.mo/nrs/binary?id=1UAuCm9daJHtE998wpdYhj3PuY9Z2yffLEh5FZyEUvU_3D','8822 4972','Ms. Amy Tong','E12-G025, G/F, Faculty of Health Sciences','5bce9968067a7dc72111132e','News Discussion Forum by Larry Qingning LIANG '),(2,'2018-10-24T00:00:00+08:00to2018-10-24T00:00:00+08:00','Institute of Applied Physics and Materials Engineering ','English','http://news.umac.mo/nrs/binary?id=YmOBvZe5RU3ur_2FLuzXH7BazX0v4g9MbrdQelX0OfIeE_3D','88224097','Prof. Huaiyui SHAO','E12-G004, Faculty of Health Sciences','5bcd9c44067a7dc72103ae23','IAPME Seminar: Different Processing Routes to Produce Mg-based Materials for Hydrogen Storage by Prof. Walter J. Botta'),(3,'2018-10-12T00:00:00+08:00to2018-10-22T00:00:00+08:00','University Library','English','http://news.umac.mo/nrs/binary?id=Cf_2BQFu9wdsZ5nmWWAig00kYsKLgm0KxjkKjcV1dEc_2FU_3D','88228170','Ms. Lei','E2, UM Wu Yee Sun Library, 5/F, Exhibition Hall','5bc0512102a5a36c87babd50','Library Exhibition -- “Macao: A Gateway to the Cultural Interaction between China and the West – Guangdong-Hong Kong-Macao Rare Collections Exhibition”'),(4,'2018-09-06T00:00:00+08:00to2018-10-31T00:00:00+08:00','University Library','English','http://news.umac.mo/nrs/binary?id=q7kcnpLikbojQDpthla_2BfNsUxF4WTr5BEbEJCX0_2BYZQ_3D','88228170','Ms. Lei','E1 University Gallery','5bbc1e5ac95d94eef5b0d856','Library Activity: “Chapas Sinicas” Exhibition'),(5,'2018-10-24T00:00:00+08:00to2018-10-24T00:00:00+08:00','Honours College','English','http://news.umac.mo/nrs/binary?id=1UAuCm9daJHtE998wpdYhj3PuY9Z2yffLEh5FZyEUvU_3D','8822 4972','Ms. Amy Tong','E12-G025, G/F, Faculty of Health Sciences','5bce9968067a7dc72111132e','News Discussion Forum by Larry Qingning LIANG ');
/*!40000 ALTER TABLE `Event` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-27 14:01:42

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
-- Table structure for table `Event_His`
--

DROP TABLE IF EXISTS `Event_His`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Event_His` (
  `identify` varchar(100) NOT NULL,
  `like` int(11) DEFAULT '100',
  `orgnizer` varchar(200) DEFAULT NULL,
  `comments` varchar(100) DEFAULT 'I love it!',
  `select` int(11) DEFAULT '50',
  `score` int(11) DEFAULT '8',
  PRIMARY KEY (`identify`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Event_His`
--

LOCK TABLES `Event_His` WRITE;
/*!40000 ALTER TABLE `Event_His` DISABLE KEYS */;
INSERT INTO `Event_His` VALUES ('5bbc1e59c95d94eef5b0d4aa',100,'Chinese Portuguese Bilingual Teaching and Training Centre (CPC) ','I love it!',50,8),('5bbc1e59c95d94eef5b0d4b4',100,'University Library','I love it!',50,8),('5bbc1e59c95d94eef5b0d4be',100,'University Library','I love it!',50,8),('5bbc1e59c95d94eef5b0d767',100,'Alumni and Development Office','I love it!',50,8),('5bbc1e59c95d94eef5b0d785',100,'Student Affairs Office and Macau Pass','I love it!',50,8),('5bbc1e59c95d94eef5b0d78f',100,'Student Affairs Office','I love it!',50,8),('5bbc1e59c95d94eef5b0d799',100,'Student Affairs Office','I love it!',50,8),('5bbc1e59c95d94eef5b0d7a3',100,'Student Affairs Office','I love it!',50,8),('5bbc1e59c95d94eef5b0d7ad',100,'Student Affairs Office','I love it!',50,8),('5bbc1e59c95d94eef5b0d7cb',100,'Student Affairs Office and Macau Pass','I love it!',50,8),('5bbc1e59c95d94eef5b0d7d7',100,'Student Affairs Office','I love it!',50,8),('5bbc1e59c95d94eef5b0d7dd',100,'Student Affairs Office','I love it!',50,8),('5bbc1e59c95d94eef5b0d7e3',100,'Student Affairs Office','I love it!',50,8),('5bbc1e5ac95d94eef5b0d80f',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0d819',100,'Student Affairs Office','I love it!',50,8),('5bbc1e5ac95d94eef5b0d856',100,'University Library','I love it!',51,8),('5bbc1e5ac95d94eef5b0d9ab',100,'Cheong Kun Lun College','I love it!',50,8),('5bbc1e5ac95d94eef5b0da4b',100,'Registry','I love it!',50,8),('5bbc1e5ac95d94eef5b0da55',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0da5f',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0da69',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0da73',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0da7d',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0da87',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0da91',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0da9b',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0daa5',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0daaf',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0dab9',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0dac3',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0dacd',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0dad7',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0dae1',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0daf5',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0db13',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0db1d',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0db27',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0db31',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0db3b',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0db45',100,'University Library','I love it!',50,8),('5bbc1e5ac95d94eef5b0db4f',100,'Global Affairs Office','I love it!',50,8),('5bbc1e5ac95d94eef5b0db81',100,'Faculty of Health Sciences','I love it!',50,8),('5bbc1e5ac95d94eef5b0db8b',100,'Philosophy and Religious Studies Programme, FAH','I love it!',50,8),('5bbc1e5ac95d94eef5b0db95',100,'FSS-Department of Psychology','I love it!',50,8),('5bbc1e5ac95d94eef5b0dbd8',100,'Faculty of Education','I love it!',50,8),('5bbc1e5ac95d94eef5b0dbe2',100,'Shiu Pong College','I love it!',50,8),('5bbc1e5ac95d94eef5b0dbec',100,'Faculty of Health Sciences','I love it!',50,8),('5bbc1e5ac95d94eef5b0dbf6',100,'FAH - Department of Chinese Language and Literature','I love it!',50,8),('5bbc1e5ac95d94eef5b0dc00',100,'Faculty of Health Sciences','I love it!',50,8),('5bbc1e5ac95d94eef5b0dc0a',100,'Communications Office','I love it!',50,8),('5bbc1e5ac95d94eef5b0dc1e',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5ac95d94eef5b0dc24',100,'Office of Vice Rector (Academic Affairs)','I love it!',50,8),('5bbc1e5ac95d94eef5b0dc2a',100,'Ma Man Kei and Lo Pak Sam College','I love it!',50,8),('5bbc1e5ac95d94eef5b0dc30',100,'SAO-Student Counselling Section ','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc3b',100,'Henry Fok Pearl Jubilee College','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc47',100,'Communications Office','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc4e',100,'SAO-SCS','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc58',100,'College on Inter-College Activities (CICA) ','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc60',100,'University Library','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc6d',100,'FSS - Department of Psychology','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc74',100,'Philosophy and Religious Studies Programme, FAH','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc7e',100,'Department of Economics, FSS','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc87',100,'SAO-SCS','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc8d',100,'Ma Man Kei and Lo Pak Sam College','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc92',100,'University Library','I love it!',50,8),('5bbc1e5bc95d94eef5b0dc9b',100,'Centre for Law Studies, Faculty of Law, University of Macau','I love it!',50,8),('5bbc1e5bc95d94eef5b0dcac',100,'Shiu Pong College','I love it!',50,8),('5bbc1e5bc95d94eef5b0dcb1',100,'Institute of Applied Physics and Materials Engineering ','I love it!',50,8),('5bbc1e5bc95d94eef5b0dcbf',100,'Institute of Applied Physics and Materials Engineering ','I love it!',50,8),('5bbc1e5bc95d94eef5b0dccc',100,'Communications Office','I love it!',50,8),('5bbc1e5bc95d94eef5b0dcd6',100,'Communications Office','I love it!',50,8),('5bbc1e5bc95d94eef5b0dce0',100,'Centre for Teaching and Learning Enhancement','I love it!',50,8),('5bbc1e5bc95d94eef5b0dcea',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5bc95d94eef5b0dcf4',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5bc95d94eef5b0dcfe',100,'Department of Communication, Faculty of Social Sciences','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd08',100,'Ma Man Kei and Lo Pak Sam College','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd12',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd1c',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd26',100,'University Library','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd30',100,'Choi Kai Yau College','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd3a',100,'Chao Kuang Piu College','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd44',100,'ICI, Centre for Innovation','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd4e',100,'Department of Economics, FSS','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd58',100,'University Library','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd62',100,'University Library','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd6c',100,'University Library','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd76',100,'Faculty of Business Administration','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd80',100,'Communications Office','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd8a',100,'Cheong Kun Lun College','I love it!',50,8),('5bbc1e5bc95d94eef5b0dd9c',100,'Faculty of Business Administration','I love it!',50,8),('5bbc1e5bc95d94eef5b0dda6',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5bc95d94eef5b0ddb0',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5bc95d94eef5b0ddba',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5bc95d94eef5b0ddc4',100,'SAO-Career Development Centre','I love it!',50,8),('5bbc1e5bc95d94eef5b0ddce',100,'Functional Genomics Informatics and Systems Biology Branch of the Chinese Society of Cell Biology, Faculty of Health Sciences, University of Macau ','I love it!',50,8),('5bbc1e5bc95d94eef5b0ddd8',100,'Philosophy and Religious Studies Programme, FAH','I love it!',50,8),('5bbc1e5bc95d94eef5b0dde2',100,'Ma Man Kei and Lo Pak Sam College ','I love it!',50,8),('5bbc1e5bc95d94eef5b0dded',100,'Cheong Kun Lun College','I love it!',50,8),('5bbc1e5bc95d94eef5b0ddf7',100,'Ma Man Kei and Lo Pak Sam College ','I love it!',50,8),('5bbc1e5bc95d94eef5b0de01',100,'Faculty of Arts and Humanities','I love it!',50,8),('5bbc2beec95d94eef5b162f5',100,'Student Affairs Office ','I love it!',50,8),('5bbc559dc95d94eef5b2b777',100,'Department of Government and Public Administration, FSS','I love it!',50,8),('5bbc7fcec95d94eef5b3e979',100,'Faculty of Health Sciences','I love it!',50,8),('5bbc7fcec95d94eef5b3e983',100,'China Mainland Students\' Association, UMSU','I love it!',50,8),('5bbc7fcec95d94eef5b3e98d',100,'FAH-English Language Centre','I love it!',50,8),('5bbc7fcec95d94eef5b3e997',100,'Centre for Teaching and Learning Enhancement','I love it!',50,8),('5bbd60ce02a5a36c878f1a43',100,'Faculty of Health Sciences','I love it!',50,8),('5bbd60ce02a5a36c878f1a4b',100,'Faculty of Business Administration','I love it!',50,8),('5bbd807402a5a36c8790026e',100,'Faculty of Business Administration','I love it!',50,8),('5bbdb52f02a5a36c8791795b',100,'Student Affairs Office','I love it!',50,8),('5bbdb52f02a5a36c87917967',100,'Ma Man Kei and Lo Pak Sam College ','I love it!',50,8),('5bbeb23202a5a36c87a32c07',100,'The Chinese-Portuguese Bilingual Teaching and Training Centre','I love it!',50,8),('5bbeb23202a5a36c87a32c13',100,'Student Affairs Office','I love it!',50,8),('5bbef19402a5a36c87a5032f',100,'Faculty of Education','I love it!',50,8),('5bbef51102a5a36c87a515d5',100,'Committee on Gender Equity (CGE)','I love it!',50,8),('5bc026df02a5a36c87b98128',100,'Communications Office','I love it!',50,8),('5bc026df02a5a36c87b9812f',100,'Communications Office','I love it!',50,8),('5bc0512102a5a36c87babd50',101,'University Library','I love it!',51,8),('5bc0512102a5a36c87babd5c',100,'FAH-English Language Centre','I love it!',50,8),('5bc06d2a02a5a36c87bb7cbb',100,'Department of Communication, Faculty of Social Sciences','I love it!',50,8),('5bc06d2a02a5a36c87bb7cc6',100,'Department of Communication, Faculty of Social Sciences','I love it!',50,8),('5bc417e8067a7dc7215741f8',100,'FAH - Department of English','I love it!',50,8),('5bc417e8067a7dc721574207',100,'Henry Fok Pearl Jubilee College','I love it!',50,8),('5bc41b6b067a7dc7215762dc',100,'Philosophy and Religious Studies Programme, FAH','I love it!',50,8),('5bc46542067a7dc72159f53d',100,'FAH - Confucius Institute','I love it!',50,8),('5bc46542067a7dc72159f548',100,'FAH - Department of English','I love it!',50,8),('5bc46542067a7dc72159f552',100,'FAH - Department of English','I love it!',50,8),('5bc47353067a7dc7215a8222',100,'FAH-English Language Centre','I love it!',50,8),('5bc4b61e067a7dc7215cc393',100,'Centre for Teaching and Learning Enhancement','I love it!',50,8),('5bc565e6067a7dc7216f8ec0',100,'Faculty of Business Administration','I love it!',50,8),('5bc565e6067a7dc7216f8ec5',100,'Faculty of Health Sciences','I love it!',50,8),('5bc5c84f067a7dc72173000d',100,'Faculty of Arts and Humanities','I love it!',50,8),('5bc5c84f067a7dc721730019',100,'Faculty of Health Sciences','I love it!',50,8),('5bc5c84f067a7dc721730026',100,'Faculty of Health Sciences','I love it!',50,8),('5bc5c84f067a7dc721730030',100,'Faculty of Health Sciences','I love it!',50,8),('5bc5c84f067a7dc72173003d',100,'Centre for Law Studies, Faculty of Law, University of Macau','I love it!',50,8),('5bc5c84f067a7dc721730048',100,'Centre for Law Studies, Faculty of Law, University of Macau','I love it!',50,8),('5bc5c84f067a7dc721730052',100,'Student Affairs Office','I love it!',50,8),('5bc82185067a7dc721a14d9f',100,'Faculty of Arts and Humanities','I love it!',50,8),('5bc82185067a7dc721a14dad',100,'Centre for Teaching and Learning Enhancement','I love it!',50,8),('5bc82508067a7dc721a17457',100,'Office of Sports Affairs','I love it!',50,8),('5bc84f3a067a7dc721a300d0',100,'Department of Sociology, FSS','I love it!',50,8),('5bc85642067a7dc721a33dad',100,'Office of Vice Rector (Academic Affairs)','I love it!',50,8),('5bc85642067a7dc721a33db7',100,'Communications Office','I love it!',50,8),('5bc93ac2067a7dc721b800bf',100,'CKYC','I love it!',50,8),('5bc941c3067a7dc721b84223',100,'Faculty of Health Sciences','I love it!',50,8),('5bc941c3067a7dc721b8422e',100,'Faculty of Health Sciences','I love it!',50,8),('5bc941c3067a7dc721b84232',100,'FAH-Department of Portuguese ','I love it!',50,8),('5bc941c3067a7dc721b84239',100,'FAH-Department of Portuguese ','I love it!',50,8),('5bc9454f067a7dc721b85fa6',100,'Ma Man Kei and Lo Pak Sam College ','I love it!',50,8),('5bc9454f067a7dc721b85fb1',100,'Ma Man Kei and Lo Pak Sam College ','I love it!',50,8),('5bc95a67067a7dc721b9382c',100,'Faculty of Health Sciences','I love it!',50,8),('5bc95a67067a7dc721b93844',100,'Ma Man Kei and Lo Pak Sam College ','I love it!',50,8),('5bc9616f067a7dc721b971e0',100,'Department of Communication, Faculty of Social Sciences','I love it!',50,8),('5bc9616f067a7dc721b971ee',100,'Choi Kai Yau College','I love it!',50,8),('5bc9616f067a7dc721b971fa',100,'Ma Man Kei and Lo Pak Sam College ','I love it!',50,8),('5bc9a7c4067a7dc721bbf0ee',100,'Communications Office','I love it!',50,8),('5bc9a7c4067a7dc721bbf0f4',100,'Department of English, FAH','I love it!',50,8),('5bc9bcdc067a7dc721bcbedc',100,'Communications Office','I love it!',50,8),('5bcd2bc0067a7dc721009d30',100,'Institute of Applied Physics and Materials Engineering ','I love it!',50,8),('5bcd40da067a7dc721015b80',100,'Institute of Applied Physics and Materials Engineering ','I love it!',50,8),('5bcd40da067a7dc721015b84',100,'Communications Office','I love it!',50,8),('5bcd98b9067a7dc721039942',100,'Henry Fok Pearl Jubilee College','I love it!',50,8),('5bcd9c44067a7dc72103ae23',100,'Institute of Applied Physics and Materials Engineering ','I love it!',50,8),('5bce87d3067a7dc72110a822',100,'University Library','I love it!',50,8),('5bce8b55067a7dc72110bc7e',100,'CKYC','I love it!',50,8),('5bce8b55067a7dc72110bc84',100,'Chao Kuang Piu College','I love it!',50,8),('5bce9968067a7dc721111321',100,'Choi Kai Yau College','I love it!',50,8),('5bce9968067a7dc721111329',100,'Communications Office','I love it!',50,8),('5bce9968067a7dc72111132e',101,'Honours College','I love it!',51,8),('5bceae78067a7dc72111d154',100,'Department of Sociology, FSS','I love it!',50,8),('5bceea35067a7dc72113500f',100,'FAH-English Language Centre','I love it!',50,8),('5bceea35067a7dc721135019',100,'FSS-Centre for Chinese History and Culture','I love it!',50,8),('5bceedb9067a7dc72113659b',100,'Communications Office','I love it!',50,8),('5bceedb9067a7dc7211365a5',100,'Communications Office','I love it!',50,8),('5bcef145067a7dc721137d9f',100,'Communications Office','I love it!',50,8),('5bcef84e067a7dc72113b0e5',100,'Student Affairs Office','I love it!',50,8),('5bcff8ef067a7dc72133029c',100,'University Library','I love it!',50,8),('5bcff8ef067a7dc7213302a2',100,'University Library','I love it!',50,8),('5bcff8ef067a7dc7213302a6',100,'Student Affairs Office','I love it!',50,8),('5bd01f9b067a7dc7213b3ba5',100,'Cheong Kun Lun College','I love it!',50,8),('5bd01f9b067a7dc7213b3bad',100,'Cheong Kun Lun College','I love it!',50,8),('5bd03bbb067a7dc72141b39d',100,'Macao Orchestra','I love it!',50,8),('5bd03bbb067a7dc72141b3a6',100,'Macao Orchestra','I love it!',50,8),('5bd049c4067a7dc721875f98',100,'FAH-Department of Portuguese ','I love it!',50,8),('5bd13557067a7dc721783755',100,'Cheong Kun Lun College','I love it!',50,8),('5bd13c69067a7dc7218098fe',100,'Macao Orchestra','I love it!',50,8),('5bd13c69067a7dc72180990d',100,'Cheong Kun Lun College','I love it!',50,8),('5bd13c69067a7dc72180991a',100,'Institute of Chinese Medical Sciences / State Key Laboratory of Quality Research in Chinese Medicine','I love it!',50,8),('5bd14dfc067a7dc721239918',100,'Communications Office','I love it!',50,8),('5bd14dfc067a7dc721239928',100,'Communications Office','I love it!',50,8),('5bd14dfc067a7dc72123993e',100,'CKLC House Association ','I love it!',50,8),('5bd15504067a7dc721661986',100,'CKLC House Association ','I love it!',50,8),('5bd190c9067a7dc7218a3b84',100,'ADMO-Human Resources Services Section ','I love it!',50,8),('5bd1945c067a7dc721ab47f0',100,'UM Choir','I love it!',50,8),('5bd1945c067a7dc721ab4802',100,'UM Choir','I love it!',50,8),('5bd294ee067a7dc7217e7b0f',100,'Institute of Applied Physics and Materials Engineering ','I love it!',50,8),('5bd294ee067a7dc7217e7b12',100,'Honours College','I love it!',50,8),('5bd294ee067a7dc7217e7b15',100,'UM Choir','I love it!',50,8),('5bd294ee067a7dc7217e7b18',100,'Office of Vice Rector (Academic Affairs), University of Macau','I love it!',50,8);
/*!40000 ALTER TABLE `Event_His` ENABLE KEYS */;
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

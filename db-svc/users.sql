-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: users
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu18.04.1

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
-- Table structure for table `audit_event`
--

DROP TABLE IF EXISTS `audit_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `audit_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `event` varchar(30) NOT NULL,
  `userid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userid` (`userid`),
  CONSTRAINT `audit_event_ibfk_1` FOREIGN KEY (`userid`) REFERENCES `credentials` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_event`
--

LOCK TABLES `audit_event` WRITE;
/*!40000 ALTER TABLE `audit_event` DISABLE KEYS */;
INSERT INTO `audit_event` VALUES (1,'2018-06-04 23:12:43','Correct Register',1),(2,'2018-06-04 23:12:50','Correct Login',1),(3,'2018-06-04 23:17:15','Correct Login',1),(4,'2018-06-04 23:21:54','Correct Login',1),(5,'2018-06-04 23:26:32','Correct Login',1),(6,'2018-06-11 21:42:16','Correct Login',1),(7,'2018-06-11 21:43:35','Correct Login',1),(8,'2018-06-11 21:57:46','Correct Logout',NULL),(9,'2018-06-11 22:47:37','Correct Login',1),(10,'2018-06-11 22:54:19','Correct Login',1),(11,'2018-06-18 19:44:55','Correct Login',1),(12,'2018-06-18 19:59:49','Correct Login',1),(13,'2018-06-18 19:59:51','Correct Logout',NULL),(14,'2018-06-18 20:02:27','Correct Login',1),(15,'2018-06-18 20:18:12','Correct Logout',NULL),(16,'2018-06-18 20:40:13','Correct Login',1),(17,'2018-06-18 20:42:32','Correct Logout',NULL),(18,'2018-06-18 20:42:57','Correct Login',1),(19,'2018-06-18 20:48:38','Correct Logout',NULL),(20,'2018-06-18 20:49:36','Correct Login',1),(21,'2018-06-18 21:33:54','Correct Logout',NULL),(22,'2018-06-18 21:34:18','Correct Login',1),(23,'2018-06-18 21:36:36','Correct Login',1),(24,'2018-06-18 21:38:26','Correct Login',1),(25,'2018-06-18 21:39:45','Correct Login',1),(26,'2018-06-18 21:45:26','Correct Login',1),(27,'2018-06-18 21:49:58','Correct Login',1),(28,'2018-06-18 21:50:38','Correct Login',1),(29,'2018-06-18 21:51:09','Correct Login',1),(30,'2018-06-18 22:22:02','Correct Login',1),(31,'2018-06-18 22:22:36','Correct Logout',NULL),(32,'2018-06-18 22:22:44','Correct Login',1),(33,'2018-06-18 22:27:30','Correct Logout',NULL),(34,'2018-06-18 22:28:57','Wrong Login',NULL),(35,'2018-06-18 22:29:09','Correct Login',1),(36,'2018-06-18 22:29:14','Correct Logout',NULL),(37,'2018-06-18 22:29:24','Correct Register',2),(38,'2018-06-18 22:29:48','Correct Login',2),(39,'2018-06-18 22:46:21','Correct Login',1),(40,'2018-06-18 22:49:23','Correct Login',1),(41,'2018-06-18 22:51:18','Correct Login',1),(42,'2018-06-18 23:02:04','Correct Login',1),(43,'2018-06-18 23:08:23','Correct Login',1),(44,'2018-06-25 05:47:05','Correct Login',1),(45,'2018-06-25 05:48:07','Correct Logout',NULL),(46,'2018-06-25 05:48:29','Correct Login',2),(47,'2018-06-25 05:48:32','Correct Logout',NULL),(48,'2018-06-25 19:31:22','Correct Login',1),(49,'2018-06-25 19:31:27','Correct Logout',NULL),(50,'2018-06-25 19:39:08','Correct Login',1),(51,'2018-06-25 19:40:56','Correct Login',1),(52,'2018-06-25 19:40:59','Correct Logout',1),(53,'2018-06-25 20:22:10','Correct Login',1),(54,'2018-06-25 20:23:37','Correct Logout',1),(55,'2018-06-25 20:24:11','Correct Login',1),(56,'2018-06-25 20:29:00','Correct Login',1),(57,'2018-06-25 20:34:47','Correct Logout',1),(58,'2018-06-25 20:34:52','Correct Login',1),(59,'2018-06-25 20:36:53','Correct Login',1),(60,'2018-06-25 20:40:59','Wrong Login',NULL),(61,'2018-06-25 20:41:13','Correct Login',1),(62,'2018-06-25 20:49:46','Correct Login',1),(63,'2018-06-25 20:52:39','Wrong Login',NULL),(64,'2018-06-25 20:52:43','Correct Login',1),(65,'2018-06-25 20:54:50','Correct Login',1),(66,'2018-06-25 21:01:21','Correct Login',1),(67,'2018-06-25 21:01:59','Correct Login',1),(68,'2018-06-25 21:06:25','Correct Login',1),(69,'2018-06-25 21:17:48','Correct Login',1),(70,'2018-06-25 21:19:04','Correct Login',1),(71,'2018-06-25 21:26:04','Correct Login',1),(72,'2018-06-25 21:31:51','Correct Login',1),(73,'2018-06-25 21:35:10','Correct Login',1),(74,'2018-06-25 21:41:21','Correct Login',1),(75,'2018-06-25 21:42:23','Correct Login',1),(76,'2018-06-25 21:49:51','Correct Login',1),(77,'2018-06-25 21:50:41','Correct Login',1),(78,'2018-06-25 21:53:08','Correct Login',1),(79,'2018-06-25 21:56:07','Correct Login',1),(80,'2018-06-25 21:57:32','Correct Login',1),(81,'2018-06-25 21:59:09','Correct Login',1),(82,'2018-06-25 22:02:55','Correct Login',1),(83,'2018-06-25 22:13:17','Correct Login',1),(84,'2018-06-25 22:15:46','Correct Login',1),(85,'2018-06-25 22:24:03','Correct Login',1),(86,'2018-06-25 22:25:35','Correct Login',1),(87,'2018-06-25 22:26:34','Correct Login',1),(88,'2018-06-25 22:30:31','Correct Login',1),(89,'2018-06-25 22:35:50','Correct Login',1),(90,'2018-06-25 22:56:37','Correct Login',1),(91,'2018-06-25 23:46:07','Correct Login',1),(92,'2018-06-26 00:31:41','Correct Login',1),(93,'2018-06-26 00:33:12','Correct Login',1),(94,'2018-06-26 00:37:00','Correct Login',1),(95,'2018-06-26 00:37:54','Correct Login',1),(96,'2018-06-26 00:40:58','Correct Login',1),(97,'2018-06-26 00:42:33','Correct Login',1),(98,'2018-06-26 00:58:16','Correct Login',1),(99,'2018-06-26 01:00:14','Correct Login',1),(100,'2018-06-26 01:00:49','Correct Login',1),(101,'2018-06-26 01:03:09','Correct Login',1),(102,'2018-06-26 01:03:27','Correct Login',1),(103,'2018-06-26 01:04:20','Correct Login',1),(104,'2018-06-26 01:15:39','Correct Login',1),(105,'2018-06-26 01:18:54','Correct Login',1),(106,'2018-06-26 01:23:05','Correct Logout',1),(107,'2018-06-26 01:23:11','Correct Login',1),(108,'2018-06-26 01:32:08','Correct Login',1),(109,'2018-06-26 01:33:27','Correct Login',1),(110,'2018-06-26 01:34:04','Correct Login',1),(111,'2018-06-26 01:36:43','Correct Logout',1),(112,'2018-06-26 01:37:02','Correct Login',1),(113,'2018-06-26 02:31:44','Correct Login',1),(114,'2018-06-26 02:46:49','Correct Login',1),(115,'2018-06-26 02:57:00','Correct Login',1),(116,'2018-06-26 03:26:10','Correct Login',1),(117,'2018-06-26 03:28:18','Correct Logout',1),(118,'2018-06-26 03:28:36','Correct Login',2),(119,'2018-06-26 03:35:17','Correct Logout',2),(120,'2018-06-26 03:35:25','Correct Login',2),(121,'2018-06-26 05:03:50','Correct Login',1),(122,'2018-06-26 05:04:33','Correct Register',3),(123,'2018-06-26 05:05:03','Wrong Login',NULL),(124,'2018-06-26 05:05:24','Correct Login',3),(125,'2018-06-26 05:05:33','Correct Logout',3),(126,'2018-06-26 05:05:51','Correct Register',4),(127,'2018-06-26 05:34:39','Correct Register',6),(128,'2018-06-26 05:34:55','Correct Login',6),(129,'2018-06-26 05:36:57','Correct Logout',6),(130,'2018-06-26 05:37:16','Wrong Register',NULL),(131,'2018-06-26 05:37:24','Wrong Register',NULL),(132,'2018-06-26 05:38:02','Correct Login',3),(133,'2018-06-26 05:38:15','Correct Logout',3),(134,'2018-06-26 05:38:24','Correct Login',6),(135,'2018-06-26 05:41:39','Correct Login',1),(136,'2018-06-26 05:41:50','Correct Logout',1),(137,'2018-06-26 05:42:02','Correct Login',2),(138,'2018-06-26 05:42:18','Correct Logout',2);
/*!40000 ALTER TABLE `audit_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credentials`
--

DROP TABLE IF EXISTS `credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credentials` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `rol` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credentials`
--

LOCK TABLES `credentials` WRITE;
/*!40000 ALTER TABLE `credentials` DISABLE KEYS */;
INSERT INTO `credentials` VALUES (1,'pepe','pepe123','admin'),(2,'cacho','cacho123','normal'),(3,'diego','belgrano123','normal'),(4,'pipo','pipo123','normal'),(6,'ema','ema123','admin');
/*!40000 ALTER TABLE `credentials` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-26 19:59:40

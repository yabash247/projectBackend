-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: projects
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_user'),(22,'Can change user',6,'change_user'),(23,'Can delete user',6,'delete_user'),(24,'Can view user',6,'view_user'),(25,'Can add profile',7,'add_profile'),(26,'Can change profile',7,'change_profile'),(27,'Can delete profile',7,'delete_profile'),(28,'Can view profile',7,'view_profile'),(29,'Can add company',8,'add_company'),(30,'Can change company',8,'change_company'),(31,'Can delete company',8,'delete_company'),(32,'Can view company',8,'view_company'),(33,'Can add my projects',9,'add_myprojects'),(34,'Can change my projects',9,'change_myprojects'),(35,'Can delete my projects',9,'delete_myprojects'),(36,'Can view my projects',9,'view_myprojects'),(37,'Can add ponds',10,'add_ponds'),(38,'Can change ponds',10,'change_ponds'),(39,'Can delete ponds',10,'delete_ponds'),(40,'Can view ponds',10,'view_ponds'),(41,'Can add project',11,'add_project'),(42,'Can change project',11,'change_project'),(43,'Can delete project',11,'delete_project'),(44,'Can view project',11,'view_project'),(45,'Can add stocking',12,'add_stocking'),(46,'Can change stocking',12,'change_stocking'),(47,'Can delete stocking',12,'delete_stocking'),(48,'Can view stocking',12,'view_stocking'),(49,'Can add blacklisted token',13,'add_blacklistedtoken'),(50,'Can change blacklisted token',13,'change_blacklistedtoken'),(51,'Can delete blacklisted token',13,'delete_blacklistedtoken'),(52,'Can view blacklisted token',13,'view_blacklistedtoken'),(53,'Can add outstanding token',14,'add_outstandingtoken'),(54,'Can change outstanding token',14,'change_outstandingtoken'),(55,'Can delete outstanding token',14,'delete_outstandingtoken'),(56,'Can view outstanding token',14,'view_outstandingtoken'),(57,'Can add pondsto do list',15,'add_pondstodolist'),(58,'Can change pondsto do list',15,'change_pondstodolist'),(59,'Can delete pondsto do list',15,'delete_pondstodolist'),(60,'Can view pondsto do list',15,'view_pondstodolist'),(61,'Can add sales',16,'add_sales'),(62,'Can change sales',16,'change_sales'),(63,'Can delete sales',16,'delete_sales'),(64,'Can view sales',16,'view_sales'),(65,'Can add feeding',17,'add_feeding'),(66,'Can change feeding',17,'change_feeding'),(67,'Can delete feeding',17,'delete_feeding'),(68,'Can view feeding',17,'view_feeding'),(69,'Can add water change',18,'add_waterchange'),(70,'Can change water change',18,'change_waterchange'),(71,'Can delete water change',18,'delete_waterchange'),(72,'Can view water change',18,'view_waterchange'),(73,'Can add activities images',19,'add_activitiesimages'),(74,'Can change activities images',19,'change_activitiesimages'),(75,'Can delete activities images',19,'delete_activitiesimages'),(76,'Can view activities images',19,'view_activitiesimages'),(77,'Can add activity names',20,'add_activitynames'),(78,'Can change activity names',20,'change_activitynames'),(79,'Can delete activity names',20,'delete_activitynames'),(80,'Can view activity names',20,'view_activitynames'),(81,'Can add followup task',21,'add_followuptask'),(82,'Can change followup task',21,'change_followuptask'),(83,'Can delete followup task',21,'delete_followuptask'),(84,'Can view followup task',21,'view_followuptask'),(85,'Can add followup task suggestion',22,'add_followuptasksuggestion'),(86,'Can change followup task suggestion',22,'change_followuptasksuggestion'),(87,'Can delete followup task suggestion',22,'delete_followuptasksuggestion'),(88,'Can view followup task suggestion',22,'view_followuptasksuggestion'),(89,'Can add stock source',23,'add_stocksource'),(90,'Can change stock source',23,'change_stocksource'),(91,'Can delete stock source',23,'delete_stocksource'),(92,'Can view stock source',23,'view_stocksource'),(93,'Can add staff',24,'add_staff'),(94,'Can change staff',24,'change_staff'),(95,'Can delete staff',24,'delete_staff'),(96,'Can view staff',24,'view_staff'),(97,'Can add contacts',25,'add_contacts'),(98,'Can change contacts',25,'change_contacts'),(99,'Can delete contacts',25,'delete_contacts'),(100,'Can view contacts',25,'view_contacts'),(101,'Can add expenses',26,'add_expenses'),(102,'Can change expenses',26,'change_expenses'),(103,'Can delete expenses',26,'delete_expenses'),(104,'Can view expenses',26,'view_expenses'),(105,'Can add expenses disbursement',27,'add_expensesdisbursement'),(106,'Can change expenses disbursement',27,'change_expensesdisbursement'),(107,'Can delete expenses disbursement',27,'delete_expensesdisbursement'),(108,'Can view expenses disbursement',27,'view_expensesdisbursement'),(109,'Can add items group',28,'add_itemsgroup'),(110,'Can change items group',28,'change_itemsgroup'),(111,'Can delete items group',28,'delete_itemsgroup'),(112,'Can view items group',28,'view_itemsgroup'),(113,'Can add expense',29,'add_expense'),(114,'Can change expense',29,'change_expense'),(115,'Can delete expense',29,'delete_expense'),(116,'Can view expense',29,'view_expense'),(117,'Can add expense item table link',30,'add_expenseitemtablelink'),(118,'Can change expense item table link',30,'change_expenseitemtablelink'),(119,'Can delete expense item table link',30,'delete_expenseitemtablelink'),(120,'Can view expense item table link',30,'view_expenseitemtablelink'),(121,'Can add item parent',31,'add_itemparent'),(122,'Can change item parent',31,'change_itemparent'),(123,'Can delete item parent',31,'delete_itemparent'),(124,'Can view item parent',31,'view_itemparent'),(125,'Can add purchase delivery',32,'add_purchasedelivery'),(126,'Can change purchase delivery',32,'change_purchasedelivery'),(127,'Can delete purchase delivery',32,'delete_purchasedelivery'),(128,'Can view purchase delivery',32,'view_purchasedelivery'),(129,'Can add items',33,'add_items'),(130,'Can change items',33,'change_items'),(131,'Can delete items',33,'delete_items'),(132,'Can view items',33,'view_items');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-08-16 03:29:30.855168','1','Profile object (1)',2,'[{\"changed\": {\"fields\": [\"Verified\"]}}]',7,1),(2,'2024-08-16 03:30:58.446894','1','Profile object (1)',2,'[{\"changed\": {\"fields\": [\"Full name\", \"Bio\"]}}]',7,1),(3,'2024-08-18 00:14:35.398501','2','Profile object (2)',2,'[{\"changed\": {\"fields\": [\"Verified\"]}}]',7,1),(4,'2024-08-18 01:50:19.781648','2','Profile object (2)',2,'[{\"changed\": {\"fields\": [\"Title\", \"Image ProfileLarge\", \"Image ProfileSmall\", \"Image\", \"Instagram\", \"Twiter\", \"Tiktok\", \"OtherOnline\", \"Fb\", \"Website\", \"Phone\", \"Birthday\"]}}]',7,1),(5,'2024-08-20 02:38:05.826309','3','Profile object (3)',2,'[{\"changed\": {\"fields\": [\"Verified\"]}}]',7,3),(6,'2024-08-21 00:25:10.263245','5','Profile object (5)',2,'[{\"changed\": {\"fields\": [\"Verified\"]}}]',7,4),(7,'2024-08-21 00:25:10.265244','4','Profile object (4)',2,'[{\"changed\": {\"fields\": [\"Verified\"]}}]',7,4),(8,'2024-08-27 02:26:00.787022','6','Profile object (6)',2,'[{\"changed\": {\"fields\": [\"Verified\"]}}]',7,6),(9,'2024-08-27 02:27:53.571169','5','Profile object (5)',2,'[{\"changed\": {\"fields\": [\"Full name\", \"Title\", \"Bio\", \"Image ProfileLarge\", \"Image ProfileSmall\", \"Image\", \"Instagram\", \"Twiter\", \"Tiktok\", \"OtherOnline\", \"Fb\", \"Website\", \"Phone\", \"Birthday\"]}}]',7,6),(10,'2024-08-27 04:42:09.253512','5','Project object (5)',1,'[{\"added\": {}}]',11,6),(11,'2024-08-27 04:50:34.446270','5','Project object (5)',3,'',11,6);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(19,'projects','activitiesimages'),(20,'projects','activitynames'),(8,'projects','company'),(25,'projects','contacts'),(29,'projects','expense'),(30,'projects','expenseitemtablelink'),(26,'projects','expenses'),(27,'projects','expensesdisbursement'),(17,'projects','feeding'),(21,'projects','followuptask'),(22,'projects','followuptasksuggestion'),(31,'projects','itemparent'),(33,'projects','items'),(28,'projects','itemsgroup'),(9,'projects','myprojects'),(10,'projects','ponds'),(15,'projects','pondstodolist'),(11,'projects','project'),(32,'projects','purchasedelivery'),(16,'projects','sales'),(24,'projects','staff'),(12,'projects','stocking'),(23,'projects','stocksource'),(18,'projects','waterchange'),(5,'sessions','session'),(13,'token_blacklist','blacklistedtoken'),(14,'token_blacklist','outstandingtoken'),(7,'users','profile'),(6,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-12 12:49:27.091819'),(2,'contenttypes','0002_remove_content_type_name','2024-08-12 12:49:27.128823'),(3,'auth','0001_initial','2024-08-12 12:49:27.265790'),(4,'auth','0002_alter_permission_name_max_length','2024-08-12 12:49:27.297035'),(5,'auth','0003_alter_user_email_max_length','2024-08-12 12:49:27.312647'),(6,'auth','0004_alter_user_username_opts','2024-08-12 12:49:27.312647'),(7,'auth','0005_alter_user_last_login_null','2024-08-12 12:49:27.312647'),(8,'auth','0006_require_contenttypes_0002','2024-08-12 12:49:27.312647'),(9,'auth','0007_alter_validators_add_error_messages','2024-08-12 12:49:27.328270'),(10,'auth','0008_alter_user_username_max_length','2024-08-12 12:49:27.328270'),(11,'auth','0009_alter_user_last_name_max_length','2024-08-12 12:49:27.328270'),(12,'auth','0010_alter_group_name_max_length','2024-08-12 12:49:27.344303'),(13,'auth','0011_update_proxy_permissions','2024-08-12 12:49:27.344303'),(14,'auth','0012_alter_user_first_name_max_length','2024-08-12 12:49:27.344303'),(15,'users','0001_initial','2024-08-12 12:49:27.552430'),(16,'admin','0001_initial','2024-08-12 12:49:27.641066'),(17,'admin','0002_logentry_remove_auto_add','2024-08-12 12:49:27.646571'),(18,'admin','0003_logentry_add_action_flag_choices','2024-08-12 12:49:27.646571'),(19,'projects','0001_initial','2024-08-12 12:49:27.820081'),(20,'sessions','0001_initial','2024-08-12 12:49:27.851734'),(21,'token_blacklist','0001_initial','2024-08-12 12:49:27.941705'),(22,'token_blacklist','0002_outstandingtoken_jti_hex','2024-08-12 12:49:27.959035'),(23,'token_blacklist','0003_auto_20171017_2007','2024-08-12 12:49:27.959035'),(24,'token_blacklist','0004_auto_20171017_2013','2024-08-12 12:49:28.016143'),(25,'token_blacklist','0005_remove_outstandingtoken_jti','2024-08-12 12:49:28.044716'),(26,'token_blacklist','0006_auto_20171017_2113','2024-08-12 12:49:28.056353'),(27,'token_blacklist','0007_auto_20171017_2214','2024-08-12 12:49:28.176844'),(28,'token_blacklist','0008_migrate_to_bigautofield','2024-08-12 12:49:28.290379'),(29,'token_blacklist','0010_fix_migrate_to_bigautofield','2024-08-12 12:49:28.306027'),(30,'token_blacklist','0011_linearizes_history','2024-08-12 12:49:28.306027'),(31,'token_blacklist','0012_alter_outstandingtoken_user','2024-08-12 12:49:28.319983'),(32,'projects','0002_alter_stocking_followuptaskduedate_and_more','2024-08-13 05:28:01.104275'),(33,'projects','0003_pondstodolist','2024-08-14 03:39:37.619088'),(34,'projects','0004_alter_pondstodolist_assignedtoid_and_more','2024-08-14 03:42:59.329324'),(35,'projects','0005_alter_pondstodolist_completedate_and_more','2024-08-14 04:26:59.250861'),(36,'projects','0006_alter_pondstodolist_createdate','2024-08-14 04:27:40.376559'),(37,'projects','0007_pondstodolist_projectid','2024-08-14 04:32:55.985816'),(38,'projects','0008_sales','2024-08-14 15:47:15.816831'),(39,'projects','0009_sales_weight_alter_sales_amount','2024-08-14 17:20:27.466038'),(40,'users','0002_profile_birthday_profile_fb_and_more','2024-08-18 01:45:36.273975'),(41,'projects','0010_feeding_waterchange','2024-08-28 22:17:24.741390'),(42,'projects','0011_activitiesimages_activitynames_followuptask_and_more','2024-09-06 20:08:01.864845'),(43,'projects','0012_activitynames_creatorid','2024-09-08 03:43:20.882032'),(44,'projects','0013_stocksource','2024-09-14 18:21:53.551085'),(45,'projects','0014_rename_pondid_stocking_frompondid_and_more','2024-09-15 00:27:25.871904'),(46,'projects','0015_rename_added_stocking_addedquantity','2024-09-15 00:34:55.388410'),(47,'projects','0016_staff_stocking_addedimage','2024-09-16 21:38:14.607633'),(48,'projects','0017_staff_email_staff_farmid_staff_homeaddress_and_more','2024-09-16 23:38:10.798888'),(49,'projects','0018_alter_staff_firstname_alter_staff_lastname_and_more','2024-09-16 23:57:03.607475'),(50,'projects','0019_alter_staff_farmid_alter_staff_phonemain','2024-09-16 23:58:18.114914'),(51,'projects','0020_alter_staff_phonemain','2024-09-17 03:03:54.506571'),(52,'projects','0021_alter_staff_phonesecondary','2024-09-17 03:23:48.442035'),(53,'projects','0022_alter_staff_dateofbirth','2024-09-17 03:24:27.983940'),(54,'projects','0023_stocking_pondid','2024-09-17 09:51:58.126493'),(55,'projects','0024_alter_stocking_frompondid_and_more','2024-09-17 10:24:08.036597'),(56,'projects','0025_alter_pondstodolist_pomdname_and_more','2024-09-19 19:45:31.730825'),(57,'projects','0026_rename_projectid_pondstodolist_farmid','2024-09-19 19:49:42.964377'),(58,'projects','0027_contacts_expenses_expensesdisbursement_itemsgroup','2024-09-22 20:14:03.624980'),(59,'projects','0028_rename_contactid_expenses_paymenttoid_and_more','2024-09-22 20:24:52.312928'),(60,'projects','0029_rename_contactid_expenses_paymenttoid_and_more','2024-09-22 21:00:03.222736'),(61,'projects','0028_expense','2024-09-23 01:06:10.686944'),(62,'projects','0029_delete_expenses','2024-09-23 01:07:06.892587'),(63,'projects','0030_expensesdisbursement_cost','2024-09-23 02:20:46.132016'),(64,'projects','0031_alter_expensesdisbursement_itemsgroupid_and_more','2024-09-23 03:29:38.612130'),(65,'projects','0002_items','2024-09-29 16:36:33.178856');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0tn3syb4yd3qqljkl1b2z3x1x80r0e9y','.eJxVjDsOwjAQBe_iGln-xD9Kes5g7dpeHEC2FCcV4u4QKQW0b2bei0XY1hq3UZY4Z3Zmkp1-N4T0KG0H-Q7t1nnqbV1m5LvCDzr4tefyvBzu30GFUb91CXkih1CS9Dagt0Zoj2oSBjKpoikEcChIe0LrnEopWKvJSCsVSkrs_QHzYTgV:1seneN:IVrEget9Q3hxMplNLSXkSsDJY5YsqSU7kan86cXk2lI','2024-08-30 03:29:15.025732'),('309nungtx6b944fqwjeuep0mqg2wjwyg','.eJxVjDsOwjAQBe_iGllOsv5R0nMGa9de4wCypTipEHeHSCmgfTPzXiLgtpawdV7CnMRZGHH63Qjjg-sO0h3rrcnY6rrMJHdFHrTLa0v8vBzu30HBXr61ykYZtolBjWrirDOMHtB4r8mBj8oDOHIObQQayCIOLmavI0MiVpN4fwDU9Dfl:1siltz:Q1wadgPzyUPYeNMH_O03kc9C8Xd6NIhtITkqgTvXvN8','2024-09-10 02:25:47.583377'),('5a01sarqi1i0t6zbu6evp7gp2gveim69','.eJxVjMsOwiAQRf-FtSFAKTO4dO83kOExUjU0Ke3K-O_apAvd3nPOfYlA21rD1ssSpizOworT7xYpPUrbQb5Tu80yzW1dpih3RR60y-ucy_NyuH8HlXr91h4IVdHRIQ_WWEeIyTPCSC4x6JJVZFAeXQQGXwZvRgcqJUbPYDSK9wfZozd_:1sgZ8T:gAHHqS9t_zdwZ81d_LcMFeQmUOujRtgE0Qti4F95SMk','2024-09-04 00:23:37.977855'),('c69k06al6pu04ea3nz7lj5sa4ylsmzl9','.eJxVjDsOwjAQBe_iGllOsv5R0nMGa9de4wCypTipEHeHSCmgfTPzXiLgtpawdV7CnMRZGHH63Qjjg-sO0h3rrcnY6rrMJHdFHrTLa0v8vBzu30HBXr61ykYZtolBjWrirDOMHtB4r8mBj8oDOHIObQQayCIOLmavI0MiVpN4fwDU9Dfl:1srC6X:Ktl4WgulZ7XS86J-zdj_nCCIbu-pukzc4XLyknsUCv4','2024-10-03 08:01:33.821160'),('mncneyj1gp7sw0jpjndu8kkggqn1uw4c','.eJxVjDsOwyAQBe9CHSEDyy9lep8BsSwEJxGWjF1FuXuE5CJp38y8Nwvx2Gs4et7CQuzKFLv8bhjTM7cB6BHbfeVpbfu2IB8KP2nn80r5dTvdv4Maex21lCgNoJrQo_HJAEFRUrhJCfIAxRsrbUkelXOgJWmnhfDagjMEurDPF7zCNnE:1sgEkr:4qxcIpHRY9fApiCGMb-zGYQvv-C2FrkvzBW_-Fv4vcU','2024-09-03 02:37:53.999770');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_activitiesimages`
--

DROP TABLE IF EXISTS `projects_activitiesimages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_activitiesimages` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `activityId` int NOT NULL,
  `pondId` int NOT NULL,
  `projectId` int NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `src` varchar(100) DEFAULT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  `uploadDate` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_activitiesimages`
--

LOCK TABLES `projects_activitiesimages` WRITE;
/*!40000 ALTER TABLE `projects_activitiesimages` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_activitiesimages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_activitynames`
--

DROP TABLE IF EXISTS `projects_activitynames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_activitynames` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `creatorId` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_activitynames`
--

LOCK TABLES `projects_activitynames` WRITE;
/*!40000 ALTER TABLE `projects_activitynames` DISABLE KEYS */;
INSERT INTO `projects_activitynames` VALUES (2,'STOCKING','Adding of fish to a pond. This could be fish taken from another pond or fish gotten from breeder vendor (Internal / External)',2),(3,'FEEDING','Feeding activties for all fishes',2),(8,'TOP UP WATER','Increase water level in the pond',2),(10,'WATER CHANGE','Completly replace water in pond',2),(11,'DECONJEST OR DESTOCKING','Removing fish(es) to a pond',2),(12,'WEIGHING','WEIGHING  THE FISHES',2),(13,'PH LEVEL CHECK','PH LEVEL TESTING',2),(14,'BOOSTER APPLCATION','Adminsitering of booster to the fishes this can be done in many ways such as mixing with food, adding to water etc.',2);
/*!40000 ALTER TABLE `projects_activitynames` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_company`
--

DROP TABLE IF EXISTS `projects_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_company` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `creatorId` int NOT NULL,
  `contactName` varchar(100) NOT NULL,
  `contactPhone` int NOT NULL,
  `contactEmail` varchar(254) NOT NULL,
  `instagram` varchar(100) NOT NULL,
  `facebook` varchar(100) NOT NULL,
  `status` int NOT NULL,
  `Address` varchar(1000) NOT NULL,
  `City` varchar(100) NOT NULL,
  `State` varchar(100) NOT NULL,
  `Country` varchar(100) NOT NULL,
  `zipCode` int NOT NULL,
  `comments` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_company`
--

LOCK TABLES `projects_company` WRITE;
/*!40000 ALTER TABLE `projects_company` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_contacts`
--

DROP TABLE IF EXISTS `projects_contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_contacts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userId` int DEFAULT NULL,
  `firstName` varchar(100) DEFAULT NULL,
  `lastName` varchar(100) DEFAULT NULL,
  `creatorId` int DEFAULT NULL,
  `phoneOne` int DEFAULT NULL,
  `phoneTwo` int DEFAULT NULL,
  `emailOne` varchar(254) DEFAULT NULL,
  `emailTwo` varchar(254) DEFAULT NULL,
  `instagram` varchar(100) DEFAULT NULL,
  `facebook` varchar(100) DEFAULT NULL,
  `status` int DEFAULT NULL,
  `Address` varchar(1000) DEFAULT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_contacts`
--

LOCK TABLES `projects_contacts` WRITE;
/*!40000 ALTER TABLE `projects_contacts` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_expense`
--

DROP TABLE IF EXISTS `projects_expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_expense` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `farmId` int NOT NULL,
  `itemDescription` varchar(500) NOT NULL,
  `unitCost` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `totalcost` int NOT NULL,
  `expensesDate` datetime(6) NOT NULL,
  `paymentToId` int DEFAULT NULL,
  `shopId` int DEFAULT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_expense`
--

LOCK TABLES `projects_expense` WRITE;
/*!40000 ALTER TABLE `projects_expense` DISABLE KEYS */;
INSERT INTO `projects_expense` VALUES (1,8,'Gave Favour and Precious 4000NGN for the weekend',1,1,4000,'2024-09-22 01:20:00.000000',NULL,NULL,NULL),(3,8,'Fuel to change fish in Stock fIshId 5(10), 8(40), 9(50) . quantity in liters',1300,6,8100,'2024-09-23 01:20:00.000000',NULL,NULL,'Fuel to change fish in Stock fIshId 5(10), 8(40), 9(50) . quantity in liters'),(4,8,'Dog Feed, WAD TOLD IS ABOUT 1KG OFF FEED',4500,1,4500,'2024-09-22 04:20:00.000000',6,NULL,'Dog Feed, WAD TOLD IS ABOUT 1KG OFF FEE'),(5,8,'AIRTIME - NGN200 - TO CALL MANAGER - SENT TO FAVOUR 09046853465',200,1,200,'2024-09-28 00:00:00.000000',6,NULL,'AIRTIME'),(6,8,'WHEEL BARROW - RENTAL - FOR FEW HOURS - TRANSPORT SUBTRATES(MAGGORT FEED) FROM PP\'S HOUSE SIDE TOO FARM',1000,1,200,'2024-09-27 10:00:00.000000',6,NULL,'WHEEL BARROW - RENTAL'),(7,8,'WHEEL BARROW - RENTAL - FOR FEW HOURS - TRANSPORT SUBTRATES(MAGGORT FEED) FROM PP\'S HOUSE SIDE TOO FARM',1000,1,1000,'2024-09-28 10:00:00.000000',6,NULL,'WHEEL BARROW - RENTAL'),(8,8,'TRANSPORT - IN SEARCH OF BREAD WASTE - MARGGOT FEED - NO SUCESS',1000,1,1000,'2024-09-27 00:00:00.000000',6,NULL,'TRANSPORT - ERAND'),(9,8,'TRANSPORT - IN SEARCH OF BREAD WASTE - MARGGOT FEED - NO SUCESS',1000,1,1000,'2024-09-28 00:00:00.000000',6,NULL,'TRANSPORT - ERAND'),(10,8,'PETROL - WATER CHANGE - POND A6, A7, A8',1300,2,3000,'2024-09-28 00:00:00.000000',6,NULL,'FUEL  - WATER CHANGE IN POND'),(11,8,'STOCK FISH PURCHASE - JUVENILE - UMUAHIA',130,450,72000,'2024-09-26 00:00:00.000000',6,NULL,'transport: UMUAHIA LOCAL(9500) SHIPPING / 4000 PH LOCAL (PICKUP)'),(12,8,'STOCK FISH PURCHASE - JUVENILE - UMUAHIA',200,450,101000,'2024-09-28 00:00:00.000000',6,NULL,'transport: UMUAHIA LOCAL(8500) SHIPPING / 2500 PH LOCAL (PICKUP)'),(13,8,'STOCK FISH PURCHASE - JUMBO - UMUAHIA',210,450,105500,'2024-09-28 00:00:00.000000',6,NULL,'transport: UMUAHIA LOCAL(8500) SHIPPING / 2500 PH LOCAL (PICKUP)'),(14,8,'AIRTIME - NGN300 - TO CALL MANAGER - SENT TO FAVOUR 09046853465',300,1,300,'2024-09-27 00:00:00.000000',6,NULL,'AIRTIME');
/*!40000 ALTER TABLE `projects_expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_expenseitemtablelink`
--

DROP TABLE IF EXISTS `projects_expenseitemtablelink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_expenseitemtablelink` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `expenseId` int NOT NULL,
  `itemId` int NOT NULL,
  `itemTableName` varchar(1000) NOT NULL,
  `quantityPercentage` int NOT NULL,
  `costPercentage` int NOT NULL,
  `deliveryCostPercentage` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_expenseitemtablelink`
--

LOCK TABLES `projects_expenseitemtablelink` WRITE;
/*!40000 ALTER TABLE `projects_expenseitemtablelink` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_expenseitemtablelink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_expensesdisbursement`
--

DROP TABLE IF EXISTS `projects_expensesdisbursement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_expensesdisbursement` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `expenseId` int NOT NULL,
  `sharePecentage` int NOT NULL,
  `allocatedToId` int NOT NULL,
  `ItemsGroupId` int NOT NULL,
  `cost` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_expensesdisbursement`
--

LOCK TABLES `projects_expensesdisbursement` WRITE;
/*!40000 ALTER TABLE `projects_expensesdisbursement` DISABLE KEYS */;
INSERT INTO `projects_expensesdisbursement` VALUES (1,1,50,6,2,2000),(2,1,50,5,2,2000);
/*!40000 ALTER TABLE `projects_expensesdisbursement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_feeding`
--

DROP TABLE IF EXISTS `projects_feeding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_feeding` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pondId` int NOT NULL,
  `feedDateTime` datetime(6) NOT NULL,
  `quantity` int NOT NULL,
  `reaction` varchar(2) NOT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_feeding`
--

LOCK TABLES `projects_feeding` WRITE;
/*!40000 ALTER TABLE `projects_feeding` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_feeding` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_followuptask`
--

DROP TABLE IF EXISTS `projects_followuptask`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_followuptask` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `activityId` int NOT NULL,
  `notificationId` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_followuptask`
--

LOCK TABLES `projects_followuptask` WRITE;
/*!40000 ALTER TABLE `projects_followuptask` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_followuptask` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_followuptasksuggestion`
--

DROP TABLE IF EXISTS `projects_followuptasksuggestion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_followuptasksuggestion` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `activityNamesId` int NOT NULL,
  `followupNameId` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_followuptasksuggestion`
--

LOCK TABLES `projects_followuptasksuggestion` WRITE;
/*!40000 ALTER TABLE `projects_followuptasksuggestion` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_followuptasksuggestion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_itemparent`
--

DROP TABLE IF EXISTS `projects_itemparent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_itemparent` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `itemId` int DEFAULT NULL,
  `parentId` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_itemparent`
--

LOCK TABLES `projects_itemparent` WRITE;
/*!40000 ALTER TABLE `projects_itemparent` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_itemparent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_items`
--

DROP TABLE IF EXISTS `projects_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_items` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` varchar(1000) NOT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_items`
--

LOCK TABLES `projects_items` WRITE;
/*!40000 ALTER TABLE `projects_items` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_myprojects`
--

DROP TABLE IF EXISTS `projects_myprojects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_myprojects` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `projectId` int NOT NULL,
  `addedby_Id` int NOT NULL,
  `addedDate` date NOT NULL,
  `levels` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_myprojects`
--

LOCK TABLES `projects_myprojects` WRITE;
/*!40000 ALTER TABLE `projects_myprojects` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_myprojects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_ponds`
--

DROP TABLE IF EXISTS `projects_ponds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_ponds` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `projectId` int NOT NULL,
  `position_row` int NOT NULL,
  `position_col` int NOT NULL,
  `materialType` varchar(100) NOT NULL,
  `depth` int NOT NULL,
  `lenght` int NOT NULL,
  `width` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_ponds`
--

LOCK TABLES `projects_ponds` WRITE;
/*!40000 ALTER TABLE `projects_ponds` DISABLE KEYS */;
INSERT INTO `projects_ponds` VALUES (1,'A1',3,1,1,'Concrete',5,10,12),(3,'B1',3,1,3,'Concrete',5,15,15),(4,'B2',3,2,3,'Concrete',5,15,15),(5,'B10',3,1,4,'Concrete',5,15,15),(6,'B6',3,6,3,'Concrete',5,15,15),(7,'B3',3,3,3,'Concrete',5,15,15),(8,'A1',6,1,1,'Concrete',5,15,15),(9,'H1',6,2,2,'Concrete',5,15,15),(10,'A1',8,1,1,'Concrete',5,12,12),(11,'A2',8,2,1,'Concrete',5,12,12),(12,'A3',8,3,1,'Concrete',5,12,12),(13,'A4',8,4,1,'Concrete',5,12,12),(14,'A5',8,5,1,'Concrete',5,12,12),(15,'A6',8,6,1,'Concrete',5,12,12),(16,'C1',8,1,13,'Concrete',5,15,15),(17,'C2',8,2,3,'Concrete',5,15,15),(18,'C3',8,3,3,'Concrete',5,15,15),(19,'C4',8,4,3,'Concrete',5,15,15),(20,'C5',8,5,3,'Concrete',5,15,15),(21,'B1',8,1,3,'Concrete',5,15,15),(22,'B2',8,2,3,'Concrete',5,15,15),(23,'B3',8,3,3,'Concrete',5,15,15),(24,'B4',8,4,3,'Concrete',5,15,15),(25,'B5',8,5,3,'Concrete',5,15,15),(26,'B6',8,5,4,'Concrete',5,15,15),(27,'B7',8,4,4,'Concrete',5,15,15),(28,'B8',8,5,4,'Concrete',5,15,15),(29,'B9',8,6,4,'Concrete',5,15,15),(30,'B10',8,1,4,'Concrete',5,15,15);
/*!40000 ALTER TABLE `projects_ponds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_pondstodolist`
--

DROP TABLE IF EXISTS `projects_pondstodolist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_pondstodolist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pondId` int NOT NULL,
  `pomdName` varchar(100) DEFAULT NULL,
  `taskName` varchar(100) DEFAULT NULL,
  `taskId` int NOT NULL,
  `createDate` datetime(6) NOT NULL,
  `dueDate` datetime(6) NOT NULL,
  `urgency` int NOT NULL,
  `status` int NOT NULL,
  `completeDate` datetime(6) DEFAULT NULL,
  `requestorId` int NOT NULL,
  `assignedToId` int DEFAULT NULL,
  `taskDetails` varchar(1000) NOT NULL,
  `farmId` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_pondstodolist`
--

LOCK TABLES `projects_pondstodolist` WRITE;
/*!40000 ALTER TABLE `projects_pondstodolist` DISABLE KEYS */;
INSERT INTO `projects_pondstodolist` VALUES (4,4,'A2','Stocking',1,'2024-08-13 23:27:49.283141','2024-08-15 00:00:00.000000',4,3,NULL,1,NULL,'Pond has over 700 fishes weighing over 0.6grams each, need to share these amongts pond A1 which is currently empty.',3),(5,3,'A1','Stocking',1,'2024-08-13 23:51:23.837660','2024-08-15 00:00:00.000000',4,3,NULL,1,NULL,'Move half of dishes from A2 to this pond.',3),(6,5,'B10','Sales',2,'2024-08-13 23:54:01.112231','2024-08-15 00:00:00.000000',3,3,NULL,1,NULL,'Fishes not growing as reequired',3),(7,6,'B6','Sales',2,'2024-08-13 23:56:37.836364','2024-08-15 00:00:00.000000',3,3,NULL,1,NULL,'Fishes are more like grunts and needs to be sold immediately',3),(8,8,'A1','Sales',2,'2024-08-27 16:57:40.880621','2024-08-27 00:00:00.000000',3,3,NULL,1,NULL,'Fishes are more like grunts and needs to be sold immediately',6),(9,8,'A1','Water_TopUp',2,'2024-08-27 16:59:25.719603','2024-08-29 00:00:00.000000',3,3,NULL,2,NULL,'Pond is newly repaired and seem to be lossing water gradually, need to top up water at intervals.',6),(10,8,'A1','Change Water',2,'2024-08-27 17:00:32.475691','2024-09-03 00:00:00.000000',3,3,NULL,2,NULL,'Change water',6),(13,10,NULL,NULL,8,'2024-09-27 13:26:55.148326','2024-09-24 00:00:00.000000',5,3,NULL,2,NULL,'Top water in Pond A1, water level is currently very low.',8),(14,12,NULL,NULL,10,'2024-09-27 13:28:23.877786','2024-09-24 00:00:00.000000',1,3,NULL,2,NULL,'Need to chnage the water in a weeks time',8),(15,14,NULL,NULL,10,'2024-09-27 13:29:09.691448','2024-10-04 00:00:00.000000',3,3,NULL,2,NULL,'Need to chnage the water in a weeks time',8),(16,15,NULL,NULL,10,'2024-09-27 13:29:46.328639','2024-10-06 00:00:00.000000',4,3,NULL,2,NULL,'Need to switch the water in a weeks time',8),(17,17,NULL,NULL,12,'2024-09-27 13:31:50.980211','2024-10-06 00:00:00.000000',1,3,NULL,2,NULL,'This is a test task 5',8),(18,18,NULL,NULL,14,'2024-09-27 13:32:24.205208','2024-10-09 00:00:00.000000',5,3,NULL,2,NULL,'This is a test task 7',8),(19,19,NULL,NULL,12,'2024-09-27 13:33:11.200893','2024-10-03 00:00:00.000000',2,3,NULL,2,NULL,'This is a test task 9',8),(20,20,NULL,NULL,10,'2024-09-27 13:43:10.307260','2024-10-04 00:00:00.000000',1,3,NULL,2,NULL,'20 - This is a test task 920',8),(21,21,NULL,NULL,11,'2024-09-27 13:43:34.277783','2024-10-11 00:00:00.000000',2,3,NULL,2,NULL,'21 - This is a test task 920',8),(22,22,NULL,NULL,13,'2024-09-27 13:44:00.883151','2024-10-13 00:00:00.000000',3,3,NULL,2,NULL,'22 - This is a test task 920',8),(23,24,NULL,NULL,14,'2024-09-27 13:44:30.008944','2024-10-14 00:00:00.000000',4,3,NULL,2,NULL,'24 - This is a test task 654',8),(24,25,NULL,NULL,15,'2024-09-27 13:44:58.236317','2024-10-24 00:00:00.000000',5,3,NULL,2,NULL,'25 - This is a test task 453',8);
/*!40000 ALTER TABLE `projects_pondstodolist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_project`
--

DROP TABLE IF EXISTS `projects_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_project` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `summary` varchar(1000) DEFAULT NULL,
  `createdDate` date NOT NULL,
  `creatorId` int NOT NULL,
  `contactName` varchar(100) DEFAULT NULL,
  `contactPhone` bigint DEFAULT NULL,
  `contactEmail` varchar(254) NOT NULL,
  `country` varchar(100) DEFAULT NULL,
  `state` varchar(100) DEFAULT NULL,
  `zipCode` int NOT NULL,
  `fullsAddress` varchar(1000) DEFAULT NULL,
  `area` int DEFAULT NULL,
  `length` int DEFAULT NULL,
  `width` int DEFAULT NULL,
  `Status` int NOT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `instagram` varchar(100) DEFAULT NULL,
  `facebook` varchar(100) DEFAULT NULL,
  `tiktok` varchar(100) DEFAULT NULL,
  `otherOnline` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_project`
--

LOCK TABLES `projects_project` WRITE;
/*!40000 ALTER TABLE `projects_project` DISABLE KEYS */;
INSERT INTO `projects_project` VALUES (1,'UBAKALA FARM','Second Fish Farm of Yabash','2024-08-12',1,NULL,NULL,'','','',2134,'Umuahai, Ubakala',0,0,0,1,NULL,NULL,NULL,NULL,NULL,NULL),(3,'RUMUOKRO PH FARM','First Fish Farm of Yabash','2024-08-12',1,NULL,NULL,'','','',2134,'RUMUOKRO, Port Harcourt',0,0,0,1,NULL,NULL,NULL,NULL,NULL,NULL),(4,'TEST FARM','First Fish Farm of Yabash','2024-08-17',1,NULL,NULL,'','','',2134,'RUMUOKRO, Port Harcourt',0,0,0,1,NULL,NULL,NULL,NULL,NULL,NULL),(6,'TEST FARM TWO','First Fish Farm of Yabash','2024-08-27',2,NULL,NULL,'','','',2134,'RUMUOKRO, Port Harcourt',0,0,0,1,NULL,NULL,NULL,NULL,NULL,NULL),(7,'TEST FARM THREE','First Fish Farm of Yabash','2024-09-14',2,NULL,NULL,'','','',2134,'Ubkala Umuahaia',0,0,0,1,NULL,NULL,NULL,NULL,NULL,NULL),(8,'KETS PUNCATUS FARM','First Fish Farm of Yabash Integrated Farms','2024-09-19',2,NULL,NULL,'','','',2134,'Rukpurko, Rivers State, Nigeria',0,0,0,1,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `projects_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_purchasedelivery`
--

DROP TABLE IF EXISTS `projects_purchasedelivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_purchasedelivery` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `expenseId` int NOT NULL,
  `deliveryCost` int NOT NULL,
  `deliveryStatus` int NOT NULL,
  `shipperId` int DEFAULT NULL,
  `mainHandler` varchar(1000) NOT NULL,
  `secondaryHandler` varchar(1000) DEFAULT NULL,
  `shippingLocation` varchar(1000) DEFAULT NULL,
  `deliveryPickupLocation` varchar(1000) NOT NULL,
  `estimatedShipTime` datetime(6) NOT NULL,
  `estimatedDeliveryTime` datetime(6) NOT NULL,
  `receivierStaffId` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_purchasedelivery`
--

LOCK TABLES `projects_purchasedelivery` WRITE;
/*!40000 ALTER TABLE `projects_purchasedelivery` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_purchasedelivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_sales`
--

DROP TABLE IF EXISTS `projects_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_sales` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pondId` int NOT NULL,
  `projectId` int NOT NULL,
  `dateSold` datetime(6) NOT NULL,
  `amount` int DEFAULT NULL,
  `unitPrice` int NOT NULL,
  `fishId` int NOT NULL,
  `buyerId` int NOT NULL,
  `paid` int NOT NULL,
  `paymentBal` int NOT NULL,
  `status` int NOT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  `weight` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_sales`
--

LOCK TABLES `projects_sales` WRITE;
/*!40000 ALTER TABLE `projects_sales` DISABLE KEYS */;
INSERT INTO `projects_sales` VALUES (3,6,3,'2024-08-14 18:41:20.353662',NULL,1800,1,1,142200,0,1,'Fishes here weighed 5 to 6 for 1kg after 3plus months old',79),(4,5,3,'2024-08-14 18:52:05.403957',NULL,1800,1,1,352800,0,1,'Fishes here weighed 5 to 6 for 1kg after 3plus months old',196);
/*!40000 ALTER TABLE `projects_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_staff`
--

DROP TABLE IF EXISTS `projects_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_staff` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstName` varchar(100) NOT NULL,
  `lastName` varchar(100) NOT NULL,
  `position` varchar(100) NOT NULL,
  `managerId` int DEFAULT NULL,
  `dateOfBirth` datetime(6) DEFAULT NULL,
  `userId` int DEFAULT NULL,
  `dataCreated` datetime(6) NOT NULL,
  `employmentDate` datetime(6) DEFAULT NULL,
  `status` int NOT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  `email` varchar(1000) DEFAULT NULL,
  `farmId` int NOT NULL,
  `homeAddress` varchar(1000) DEFAULT NULL,
  `phoneMain` varchar(100) NOT NULL,
  `phoneSecondary` varchar(100) NOT NULL,
  `relationId` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_staff`
--

LOCK TABLES `projects_staff` WRITE;
/*!40000 ALTER TABLE `projects_staff` DISABLE KEYS */;
INSERT INTO `projects_staff` VALUES (3,'Favour','Aneiofiok','Staff II',2,'2001-09-03 00:00:00.000000',NULL,'2024-09-16 22:24:32.339666','2022-01-01 00:00:00.000000',1,'Technically sound worker.',NULL,6,NULL,'+234 904 685 3465','+234 704 301 0699',NULL),(4,'Precious','Manfred','Interm I',2,'2002-11-03 00:00:00.000000',NULL,'2024-09-16 22:28:51.221396','2024-08-01 00:00:00.000000',1,'Introduced by Favour, once worked for Pastor Prince and currently Pastor Prince\'s church member',NULL,6,NULL,'+234 904 685 xxxx','+234 704 301 0699',NULL),(5,'Precious','Manfred','Interm I',2,'2002-11-03 00:00:00.000000',NULL,'2024-09-19 03:38:54.160461','2024-08-01 00:00:00.000000',1,'Introduced by Favour, once worked for Pastor Prince and currently Pastor Prince\'s church member',NULL,8,NULL,'+234 904 685 xxxx','+234 704 301 0699',NULL),(6,'Favour','Aniefiok','Manager I',2,'2002-11-03 00:00:00.000000',NULL,'2024-09-19 03:41:21.340775','2022-01-01 00:00:00.000000',1,'Favour was introduced to Farm by former employee',NULL,8,NULL,'+234 904 685 3465','+234 704 301 0699',NULL);
/*!40000 ALTER TABLE `projects_staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_stocking`
--

DROP TABLE IF EXISTS `projects_stocking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_stocking` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fromPondId` int DEFAULT NULL,
  `waterLevel` int DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  `averageWeight` int DEFAULT NULL,
  `totalWeight` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `recordDate` datetime(6) NOT NULL,
  `fishId` int DEFAULT NULL,
  `leadByName` varchar(100) DEFAULT NULL,
  `assittedByName` varchar(100) DEFAULT NULL,
  `assittedById` int DEFAULT NULL,
  `followupTask` varchar(100) DEFAULT NULL,
  `followupTaskDueDate` datetime(6) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `addedQuantity` int DEFAULT NULL,
  `addedSize` int DEFAULT NULL,
  `addedWeight` int DEFAULT NULL,
  `removed` int DEFAULT NULL,
  `removedSize` int DEFAULT NULL,
  `removedWeight` int DEFAULT NULL,
  `comments` varchar(1000) DEFAULT NULL,
  `leadById` int DEFAULT NULL,
  `fromVendordId` int DEFAULT NULL,
  `toPondId` int NOT NULL,
  `toVendorId` int DEFAULT NULL,
  `addedimage` varchar(100) DEFAULT NULL,
  `pondId` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_stocking`
--

LOCK TABLES `projects_stocking` WRITE;
/*!40000 ALTER TABLE `projects_stocking` DISABLE KEYS */;
INSERT INTO `projects_stocking` VALUES (1,1,1,'Empty',NULL,NULL,NULL,'2024-08-13 00:00:00.000000',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,NULL,8),(2,1,1,'Empty',NULL,NULL,NULL,'2024-08-13 00:00:00.000000',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,NULL,8),(3,1,1,'Empty',NULL,NULL,NULL,'2024-08-13 00:32:52.851950',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,NULL,8),(4,1,0,'Empty',NULL,NULL,NULL,'2024-08-13 00:39:43.471781',NULL,NULL,NULL,NULL,'Check if pond still leaks water by adding water to pond and watching',NULL,'2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0,NULL,8),(5,4,4,'Smoking',NULL,318,718,'2024-08-13 00:53:02.523224',1,'2',NULL,NULL,'Deconjest',NULL,'2',718,NULL,NULL,0,NULL,NULL,'This pond needs to be deconjested ASAP',NULL,0,0,0,NULL,8),(6,4,4,'Smoking',NULL,318,717,'2024-08-13 00:56:18.987441',1,'2',NULL,NULL,'Deconjest',NULL,'2',0,NULL,NULL,1,NULL,NULL,'One fish died, probably due to prolonged satocking. Remedy: reduce stockiing time, supervise team to ensure effective stocking method and reduced exposure of fish to no water and stress during stocking, dont stock when the sun is out',NULL,0,0,0,NULL,8),(7,4,4,'Smoking',NULL,318,717,'2024-08-13 00:57:08.115828',1,'2',NULL,NULL,'Deconjest',NULL,'2',0,NULL,NULL,1,NULL,NULL,'One fish died, probably due to prolonged satocking. Remedy: reduce stockiing time, supervise team to ensure effective stocking method and reduced exposure of fish to no water and stress during stocking, dont stock when the sun is out',NULL,0,0,0,NULL,8),(8,7,3,'Table Size',NULL,90,200,'2024-08-15 23:45:29.730331',1,'3',NULL,NULL,NULL,NULL,'2',200,NULL,NULL,0,NULL,NULL,'added from Pond B2.',NULL,0,0,0,NULL,8),(9,4,4,'Smoking',NULL,228,517,'2024-08-15 23:51:28.690280',1,'2',NULL,NULL,'Deconjest',NULL,'2',0,NULL,NULL,200,NULL,NULL,'200fishes(90kg) where moved from this pond to Pond B3',NULL,0,0,0,NULL,8),(10,4,4,'Smoking',NULL,228,517,'2024-08-19 22:41:19.137231',1,'2',NULL,NULL,'Deconjest',NULL,'2',0,NULL,NULL,NULL,NULL,NULL,'200fishes(90kg) where moved from this pond to Pond B3',NULL,0,0,0,NULL,8),(11,8,4,'Smoking',NULL,228,517,'2024-09-14 17:50:13.654591',1,'2',NULL,NULL,'Deconjest',NULL,'2',0,NULL,NULL,NULL,NULL,NULL,'200fishes(90kg) where moved from this pond to Pond B3',NULL,0,0,0,NULL,8),(12,NULL,4,'Smoking',NULL,348,600,'2024-09-17 05:24:13.191147',1,'2',NULL,NULL,'Deconjest',NULL,'2',NULL,NULL,NULL,NULL,NULL,NULL,'200fishes(90kg) where moved from this pond to Pond B3',NULL,NULL,8,NULL,'',8),(13,NULL,4,'Smoking',NULL,348,800,'2024-09-17 05:24:29.009162',1,'2',NULL,NULL,'Deconjest',NULL,'2',NULL,NULL,NULL,NULL,NULL,NULL,'200fishes(90kg) where moved from this pond to Pond B3',NULL,NULL,8,NULL,'',8),(14,9,NULL,NULL,NULL,NULL,NULL,'2024-09-18 15:56:12.375576',1,NULL,NULL,NULL,NULL,NULL,NULL,700,NULL,448,NULL,NULL,NULL,'200fishes(90kg) where moved from this pond to Pond B3',NULL,NULL,8,NULL,'',9),(15,9,NULL,NULL,NULL,NULL,NULL,'2024-09-18 15:56:34.849141',1,NULL,NULL,NULL,NULL,NULL,NULL,700,NULL,448,NULL,NULL,NULL,'200fishes(90kg) where moved from this pond to Pond B3',NULL,NULL,8,NULL,'',8),(16,8,NULL,NULL,NULL,NULL,NULL,'2024-09-18 16:00:50.269983',3,NULL,NULL,NULL,NULL,NULL,NULL,5555,NULL,55,NULL,NULL,NULL,'uyujyj',NULL,NULL,9,NULL,'',9),(17,9,NULL,NULL,NULL,NULL,NULL,'2024-09-18 21:33:18.757830',2,NULL,NULL,NULL,NULL,NULL,NULL,200,NULL,190,NULL,NULL,NULL,'I know my name - testing',NULL,NULL,8,NULL,'',8),(18,9,NULL,NULL,NULL,NULL,NULL,'2024-09-18 21:34:00.231729',1,NULL,NULL,NULL,NULL,NULL,NULL,700,NULL,448,NULL,NULL,NULL,'200fishes(90kg) where moved from this pond to Pond B3',NULL,NULL,8,NULL,'',8),(19,8,NULL,NULL,NULL,NULL,NULL,'2024-09-18 21:42:53.839676',2,NULL,NULL,NULL,NULL,NULL,NULL,250,NULL,196,NULL,NULL,NULL,'Organize a testing party',NULL,NULL,9,NULL,'',9),(20,11,NULL,NULL,NULL,NULL,NULL,'2024-09-19 03:56:26.874219',1,NULL,NULL,NULL,NULL,NULL,NULL,558,NULL,16,NULL,NULL,NULL,'This was actually water change that was done',NULL,NULL,10,NULL,'',10),(21,10,NULL,NULL,NULL,NULL,NULL,'2024-09-19 03:56:39.478143',4,NULL,NULL,NULL,NULL,NULL,NULL,558,NULL,16,NULL,NULL,NULL,'Aclaimed first shooters from Tamborine bought in July 26th 2024 as 5weeks old fingerlins. Weighing around 2grams per fish',NULL,NULL,15,NULL,'',15),(22,10,NULL,NULL,NULL,NULL,NULL,'2024-09-19 03:58:00.690612',4,NULL,NULL,NULL,NULL,NULL,NULL,558,NULL,17,NULL,NULL,NULL,'Aclaimed first shooters from Tamborine bought in July 26th 2024 as 5weeks old fingerlins. Weighing around 2grams per fish',NULL,NULL,15,NULL,'',15),(23,15,NULL,NULL,NULL,NULL,NULL,'2024-09-19 04:02:03.374761',4,NULL,NULL,NULL,NULL,NULL,NULL,558,NULL,17,NULL,NULL,NULL,'Aclaimed first shooters from Tamborine bought in July 26th 2024 as 5weeks old fingerlins. Weighing around 2grams per fish',NULL,NULL,10,NULL,'',10),(24,15,NULL,NULL,NULL,NULL,NULL,'2024-09-19 04:06:01.662698',4,NULL,NULL,NULL,NULL,NULL,NULL,288,NULL,7,NULL,NULL,NULL,'Aclaimed Second grade from Tamborine bought in August 8th 2024 as 6weeks old fingerlins. Weighing around 2grams per fish',NULL,NULL,11,NULL,'',11),(25,15,NULL,NULL,NULL,NULL,NULL,'2024-09-19 04:08:05.154135',4,NULL,NULL,NULL,NULL,NULL,NULL,200,NULL,5,NULL,NULL,NULL,'Aclaimed First grade from Tamborine bought in July 26th 2024 as 5weeks old fingerlins. Weighing around 2grams per fish',NULL,NULL,12,NULL,'',12),(26,15,NULL,NULL,NULL,NULL,NULL,'2024-09-19 04:31:58.249237',6,NULL,NULL,NULL,NULL,NULL,NULL,341,NULL,10,NULL,NULL,NULL,'hybrids catfish bought from lagos',NULL,NULL,14,NULL,'',14),(27,10,NULL,NULL,NULL,NULL,NULL,'2024-09-19 09:08:46.628055',5,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,1,NULL,NULL,NULL,'test',NULL,NULL,15,NULL,'',15),(28,16,NULL,NULL,NULL,NULL,NULL,'2024-09-21 03:04:23.761509',8,NULL,NULL,NULL,NULL,NULL,NULL,500,NULL,43,NULL,NULL,NULL,'Part of deconjesting',NULL,NULL,16,NULL,'',16),(29,16,NULL,NULL,NULL,NULL,NULL,'2024-09-21 03:05:55.679631',8,NULL,NULL,NULL,NULL,NULL,NULL,315,NULL,27,NULL,NULL,NULL,'Part of deconjesting',NULL,NULL,16,NULL,'',16),(30,16,NULL,NULL,NULL,NULL,NULL,'2024-09-21 03:07:28.224438',8,NULL,NULL,NULL,NULL,NULL,NULL,315,NULL,27,NULL,NULL,NULL,'Part of deconjesting',NULL,NULL,17,NULL,'',17),(31,16,NULL,NULL,NULL,NULL,NULL,'2024-09-21 03:07:49.602901',8,NULL,NULL,NULL,NULL,NULL,NULL,500,NULL,45,NULL,NULL,NULL,'Part of deconjesting',NULL,NULL,16,NULL,'',16),(32,16,NULL,NULL,NULL,NULL,NULL,'2024-09-21 03:07:54.397729',8,NULL,NULL,NULL,NULL,NULL,NULL,500,NULL,45,NULL,NULL,NULL,'Part of deconjesting',NULL,NULL,16,NULL,'',16),(33,15,NULL,NULL,NULL,NULL,NULL,'2024-09-21 05:02:05.465919',8,NULL,NULL,NULL,NULL,NULL,NULL,513,NULL,48,NULL,NULL,NULL,'Fish from B10 was spread equally between ponds B10 and B3',NULL,NULL,23,NULL,'',23),(34,15,NULL,NULL,NULL,NULL,NULL,'2024-09-21 05:04:46.767853',8,NULL,NULL,NULL,NULL,NULL,NULL,513,NULL,48,NULL,NULL,NULL,'Fish from B10 was spread equally between ponds B10 and B3',NULL,NULL,30,NULL,'',30),(35,15,NULL,NULL,NULL,NULL,NULL,'2024-09-21 05:07:17.405417',8,NULL,NULL,NULL,NULL,NULL,NULL,500,NULL,43,NULL,NULL,NULL,'Fish from B1 was spread equally between ponds B1 and B2',NULL,NULL,21,NULL,'',21),(36,15,NULL,NULL,NULL,NULL,NULL,'2024-09-21 05:07:52.845940',8,NULL,NULL,NULL,NULL,NULL,NULL,315,NULL,27,NULL,NULL,NULL,'Fish from B1 was spread equally between ponds B1 and B2',NULL,NULL,22,NULL,'',22);
/*!40000 ALTER TABLE `projects_stocking` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_stocksource`
--

DROP TABLE IF EXISTS `projects_stocksource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_stocksource` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `PurchaseId` int NOT NULL,
  `farmId` int NOT NULL,
  `vendorId` int NOT NULL,
  `aveLength` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_stocksource`
--

LOCK TABLES `projects_stocksource` WRITE;
/*!40000 ALTER TABLE `projects_stocksource` DISABLE KEYS */;
INSERT INTO `projects_stocksource` VALUES (1,'NILLY FINGERLINGS MAY 2024','fish from nilly, supplied 2500 fingerlins in may 2024',1,7,2,NULL),(2,'KINGSO FINGERLINGS MAY 2024','fish from KINGSO, supplied 2500 fingerlins in may 2024',1,6,2,NULL),(3,'KINGSO FINGERLINGS AUG 2024','fish from KINGSO, supplied 4500 fingerlins in may 2024',1,6,2,NULL),(4,'TAMBORINE - JULY 26 - FINGERLINS','AMBORINE - JULY 26 - FINGERLINS - 4000 PICES',4,8,2,NULL),(5,'TAMBORINE - AUGUST 08 - FINGERLINS','TAMBORINE - AUGUST 08 - FINGERLINS - 3200 PICES - 2ND BATCH',5,8,2,NULL),(6,'862 HYBRIDS - ABIONDUN ADEYEMO - LAGOS - JULY 06 - POST FINGERLINS','ABIONDUN ADEYEMO - JULY 06 - POST FINGERLINS - 862 PICES - 1ST GRADE',6,8,3,NULL),(7,'862 HYBRIDS - ABIONDUN ADEYEMO - LAGOS - JULY 06 - POST FINGERLINS','ABIONDUN ADEYEMO - JULY 06 - POST FINGERLINS - 862 PICES - 1ST GRADE',6,8,3,NULL),(8,'MARYJAH - FINGERLINGS - JULY 5 - 2500','MARYJAH - JULY 06 - POST FINGERLINS - 2500 PICES - 1ST GRADE - 7WEEKS',8,8,4,NULL);
/*!40000 ALTER TABLE `projects_stocksource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects_waterchange`
--

DROP TABLE IF EXISTS `projects_waterchange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects_waterchange` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pondId` int NOT NULL,
  `eventDate` date NOT NULL,
  `depth` int NOT NULL,
  `preWaterColor` varchar(100) NOT NULL,
  `preWaterCond` varchar(600) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects_waterchange`
--

LOCK TABLES `projects_waterchange` WRITE;
/*!40000 ALTER TABLE `projects_waterchange` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects_waterchange` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_blacklistedtoken`
--

DROP TABLE IF EXISTS `token_blacklist_blacklistedtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_blacklistedtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blacklisted_at` datetime(6) NOT NULL,
  `token_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_id` (`token_id`),
  CONSTRAINT `token_blacklist_blacklistedtoken_token_id_3cc7fe56_fk` FOREIGN KEY (`token_id`) REFERENCES `token_blacklist_outstandingtoken` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_blacklistedtoken`
--

LOCK TABLES `token_blacklist_blacklistedtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` DISABLE KEYS */;
INSERT INTO `token_blacklist_blacklistedtoken` VALUES (1,'2024-08-12 12:54:16.590931',1),(2,'2024-08-17 19:50:26.066623',5);
/*!40000 ALTER TABLE `token_blacklist_blacklistedtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `token_blacklist_outstandingtoken`
--

DROP TABLE IF EXISTS `token_blacklist_outstandingtoken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `token_blacklist_outstandingtoken` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `token` longtext NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `expires_at` datetime(6) NOT NULL,
  `user_id` bigint DEFAULT NULL,
  `jti` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_blacklist_outstandingtoken_jti_hex_d9bdf6f7_uniq` (`jti`),
  KEY `token_blacklist_outs_user_id_83bc629a_fk_users_use` (`user_id`),
  CONSTRAINT `token_blacklist_outs_user_id_83bc629a_fk_users_use` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `token_blacklist_outstandingtoken`
--

LOCK TABLES `token_blacklist_outstandingtoken` WRITE;
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` DISABLE KEYS */;
INSERT INTO `token_blacklist_outstandingtoken` VALUES (1,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDMzMTIzMCwiaWF0IjoxNzIzNDY3MjMwLCJqdGkiOiJiM2RhMDgzMDFkNDM0MGEyYjY5YjlhNzFmNDBlMzNkMCIsInVzZXJfaWQiOjF9.MwoXZ98FsdSAZ94XdBIKUmTpteVUKlzVD-3jiWwlfZQ','2024-08-12 12:53:50.306794','2024-08-22 12:53:50.000000',1,'b3da08301d4340a2b69b9a71f40e33d0'),(2,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDMzMTI2MSwiaWF0IjoxNzIzNDY3MjYxLCJqdGkiOiJhODhkNTlmN2ExZTc0OGM1OWQ1MGVmMDJkOWIxMmVlNiIsInVzZXJfaWQiOjF9.B17PG7q3q_6lNQj4ApjfmnQrSXn-1_qt6XTmsYQjbOg','2024-08-12 12:54:21.340971','2024-08-22 12:54:21.000000',1,'a88d59f7a1e748c59d50ef02d9b12ee6'),(3,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDU1NTM0NywiaWF0IjoxNzIzNjkxMzQ3LCJqdGkiOiI3Y2EwYmQ2MWVmNzE0Y2U5OWY0MzQ3ZTU3ZDU0OTAxOSIsInVzZXJfaWQiOjF9.icHIN8b_aEnJwy4vzWulRU880avyNKJBQOUJ-tSnjGs','2024-08-15 03:09:07.294868','2024-08-25 03:09:07.000000',1,'7ca0bd61ef714ce99f4347e57d549019'),(4,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDY3NDgyMCwiaWF0IjoxNzIzODEwODIwLCJqdGkiOiJkMzE1ZThjNTUwYTk0N2M3ODM3ZThlYWY5ZGM4NDg5YyIsInVzZXJfaWQiOjF9.2KRke7Ov2X6LPBz0saInIiJFl-DttfO43gNyH5iBJUI','2024-08-16 12:20:20.758606','2024-08-26 12:20:20.000000',1,'d315e8c550a947c7837e8eaf9dc8489c'),(5,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDc4ODEwNCwiaWF0IjoxNzIzOTI0MTA0LCJqdGkiOiI0ZjliNDYyMzc4NDM0M2U5OGJhY2E0MDJmN2E4OTZkMyIsInVzZXJfaWQiOjF9.ftgR3k-hHm297LBLEg9N6yayhrD_3cQ8snZYVNSuVpU','2024-08-17 19:48:24.798787','2024-08-27 19:48:24.000000',1,'4f9b4623784343e98baca402f7a896d3'),(6,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDc4ODcxMSwiaWF0IjoxNzIzOTI0NzExLCJqdGkiOiJmZDg4NzBjNWNlOGM0ZTE0YTBkZGJjNDc0YmI5YTQzOCIsInVzZXJfaWQiOjF9.jUUayUTng3pir3Hb_9HUv93t1tqECkH_ZIWMtDO1Meg','2024-08-17 19:58:31.653477','2024-08-27 19:58:31.000000',1,'fd8870c5ce8c4e14a0ddbc474bb9a438'),(7,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDc4OTAwNCwiaWF0IjoxNzIzOTI1MDA0LCJqdGkiOiI4YWQwYjE2MzU4NWM0NTdkYjcyZGRjOTc5NjJmMzU0NCIsInVzZXJfaWQiOjF9.dSheWkGPfxujbqHaYq_xzid9gjvMkyiui2RV_e7e1P0','2024-08-17 20:03:24.466671','2024-08-27 20:03:24.000000',1,'8ad0b163585c457db72ddc97962f3544'),(8,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDgwNDEyOSwiaWF0IjoxNzIzOTQwMTI5LCJqdGkiOiI4NjVjMmRmZWE0OGI0NGI5OGMxZjRmZDVkODczOWNmMSIsInVzZXJfaWQiOjF9.dH_gb95NsnKBL2OWQAgirJvLgJUuY2jV7toWeP5IAyw','2024-08-18 00:15:29.369635','2024-08-28 00:15:29.000000',1,'865c2dfea48b44b98c1f4fd5d8739cf1'),(9,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDgwNjM5NCwiaWF0IjoxNzIzOTQyMzk0LCJqdGkiOiJjYjc4MGI0MjViNzc0ODRiOGI5Njg1YzE2MjY1ZGMwZiIsInVzZXJfaWQiOjJ9.lVTBlUg3P3XBDBpFmvjQTOhm01bHtS9S8wRHKVPYJ2k','2024-08-18 00:53:14.039626','2024-08-28 00:53:14.000000',2,'cb780b425b77484b8b9685c16265dc0f'),(10,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDgwNjQyNSwiaWF0IjoxNzIzOTQyNDI1LCJqdGkiOiJkMmQ0M2UxZGYzNjY0OTc1YjU5NDZmZjFhNGQzOGNjNiIsInVzZXJfaWQiOjJ9.RV-qpQJtnElI6jebI3H-jTAZvSbFeTW9k3XVSBZPslo','2024-08-18 00:53:45.756563','2024-08-28 00:53:45.000000',2,'d2d43e1df3664975b5946ff1a4d38cc6'),(11,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDk3NzY5MCwiaWF0IjoxNzI0MTEzNjkwLCJqdGkiOiI5YmRhOGIyNThkMDE0MTZjYjcwNDYxYzY1MmZhN2NmNCIsInVzZXJfaWQiOjJ9.G3HtSRMcz4TV88ARMVwM8jTx66KlDAXcM4vu1LuNPjs','2024-08-20 00:28:10.068698','2024-08-30 00:28:10.000000',2,'9bda8b258d01416cb70461c652fa7cf4'),(12,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDk4MzgwNywiaWF0IjoxNzI0MTE5ODA3LCJqdGkiOiJhMWY1OWU3NzE2MjM0MDQwOWNiOWU1ZTgzNzgyMGNkYiIsInVzZXJfaWQiOjF9.QTcGEbdX3g6bcbqqB1HhFXj2RMIrq5nWvk32_zub0o4','2024-08-20 02:10:07.257880','2024-08-30 02:10:07.000000',1,'a1f59e77162340409cb9e5e837820cdb'),(13,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNDk4NTU1NywiaWF0IjoxNzI0MTIxNTU3LCJqdGkiOiI2OTY2YzNkZjJiYjg0OTdkYmY4NjBhYjM4ZjM4ODFhZCIsInVzZXJfaWQiOjJ9.tSp7BftwepqwflNhXnc66wMDCMvsiwGb6o2xchQQ0Ig','2024-08-20 02:39:17.308543','2024-08-30 02:39:17.000000',2,'6966c3df2bb8497dbf860ab38f3881ad'),(14,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTA2Mzk1NCwiaWF0IjoxNzI0MTk5OTU0LCJqdGkiOiJlZTAzZjY1ZTBhMTU0NWYyOWRlZjY4ODI0MzkyZWY0NSIsInVzZXJfaWQiOjV9.n-WG-wetxtoeXhtv9TcD3jTrvheqpRofpXn2halb7QM','2024-08-21 00:25:54.277444','2024-08-31 00:25:54.000000',5,'ee03f65e0a1545f29def68824392ef45'),(15,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTA2NDk4NSwiaWF0IjoxNzI0MjAwOTg1LCJqdGkiOiJkOGNhZDc5ZDRmMWI0ZDY0YjFiNzhlZDc0YmE5ZjY1OCIsInVzZXJfaWQiOjV9.5KPOzPsjeoIhP4CFFAQlI-ay1tyVdbphxYu9MnaJgOc','2024-08-21 00:43:05.302824','2024-08-31 00:43:05.000000',5,'d8cad79d4f1b4d64b1b78ed74ba9f658'),(16,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTUyMDYxMiwiaWF0IjoxNzI0NjU2NjEyLCJqdGkiOiIwN2JkZTQ1ZmU2MWU0NjBhYjllYjFhZjM4OWViNDViZiIsInVzZXJfaWQiOjJ9.nCLfCKcbMRgzl53Wo_TUesCgA7X4ubcV7D4XJvTSzGE','2024-08-26 07:16:52.733514','2024-09-05 07:16:52.000000',2,'07bde45fe61e460ab9eb1af389eb45bf'),(17,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTUyMDgzNSwiaWF0IjoxNzI0NjU2ODM1LCJqdGkiOiIwMmMyNGQ2NDA5NmY0ZGNkYWM3ZTUyYjNiNzQ0YTM5NyIsInVzZXJfaWQiOjV9.287E32pFijCC4g9TjgtByDudjP8nvQdPsXnTD09R9ps','2024-08-26 07:20:35.214830','2024-09-05 07:20:35.000000',5,'02c24d64096f4dcdac7e52b3b744a397'),(18,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTUyMDg1OSwiaWF0IjoxNzI0NjU2ODU5LCJqdGkiOiJjODg4ZmE0ZjdhN2Q0NzI3YWEyN2FjNTAwMTY4ZGMyYSIsInVzZXJfaWQiOjV9.WVPWwyXu4ZOByycr4jRgXNBvBsYX2LQxoTl7JOIFj3g','2024-08-26 07:20:59.385892','2024-09-05 07:20:59.000000',5,'c888fa4f7a7d4727aa27ac500168dc2a'),(19,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU2MDcyNCwiaWF0IjoxNzI0Njk2NzI0LCJqdGkiOiI0ZWU2YjJkZDJkNDI0YjViYTdhY2U4ZTRiZDM1ZjU0YiIsInVzZXJfaWQiOjV9.uNSRG9SEGH40ZsqWMrp8JQw-J1Ggi1CRroWqaWlYfmQ','2024-08-26 18:25:24.265555','2024-09-05 18:25:24.000000',5,'4ee6b2dd2d424b5ba7ace8e4bd35f54b'),(20,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU2MDc3MCwiaWF0IjoxNzI0Njk2NzcwLCJqdGkiOiIxYTU1MTRhZGI5ZjE0MmJkODAyY2YyZWM0NWYxOTVmYiIsInVzZXJfaWQiOjV9.eMJuvsMHDRt4Jv0JYGgaUXxV3UmKlq4LMtljh0dH_f4','2024-08-26 18:26:10.408124','2024-09-05 18:26:10.000000',5,'1a5514adb9f142bd802cf2ec45f195fb'),(21,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU2MTIzNywiaWF0IjoxNzI0Njk3MjM3LCJqdGkiOiI1NmZkY2E2ZTAwMDI0ZWY5YTAwNTExMjk2ZjU3M2ZmOSIsInVzZXJfaWQiOjV9.xaJHN2dXWAw0ahey6e98J-AhKg4VGlaW82cupLNUGHM','2024-08-26 18:33:57.097080','2024-09-05 18:33:57.000000',5,'56fdca6e00024ef9a00511296f573ff9'),(22,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU2MTU3NSwiaWF0IjoxNzI0Njk3NTc1LCJqdGkiOiI4NmJhNmVmODAxMzQ0ZTE1OTVlOTRiMDhlNTc2NDlmZSIsInVzZXJfaWQiOjV9.4TeY84wFzQfZ3xZNxb5bn6fWyhRIFx56oNdvZSv62Z8','2024-08-26 18:39:35.626907','2024-09-05 18:39:35.000000',5,'86ba6ef801344e1595e94b08e57649fe'),(23,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU2MTcxNSwiaWF0IjoxNzI0Njk3NzE1LCJqdGkiOiI2NmM2NzdlOWQxMmQ0ZGQxYmEwZjk2NTNmOWFkZTNlMCIsInVzZXJfaWQiOjV9.bclijNb8FEeZb75ttVZZ2Vp5mU9Vrbq29llTOSQ_G_w','2024-08-26 18:41:55.659265','2024-09-05 18:41:55.000000',5,'66c677e9d12d4dd1ba0f9653f9ade3e0'),(24,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU4NzkxNSwiaWF0IjoxNzI0NzIzOTE1LCJqdGkiOiJhZDI4N2RhMzQzNWE0OTI1YjFhZmU5ZGEzZGY2MWZkOSIsInVzZXJfaWQiOjV9.em_RoxCqkmx2ncM1G7Kht3_nGtW6vbERBbKR1D7XW4I','2024-08-27 01:58:35.039802','2024-09-06 01:58:35.000000',5,'ad287da3435a4925b1afe9da3df61fd9'),(25,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU4ODAwOCwiaWF0IjoxNzI0NzI0MDA4LCJqdGkiOiI2ZmJhYzM1M2EwZmU0OGIzYmMyZjI2ZjJiNGQ3YmFiOCIsInVzZXJfaWQiOjV9.qoM9X4eFvInvmB0oLHpLxJjFFMxfMJNYXIZYwWG539k','2024-08-27 02:00:08.221798','2024-09-06 02:00:08.000000',5,'6fbac353a0fe48b3bc2f26f2b4d7bab8'),(26,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU4ODEzNiwiaWF0IjoxNzI0NzI0MTM2LCJqdGkiOiI3NzA5YTJlNDljNjg0YWMxODI3OTc2YWIzMDliMWEwZCIsInVzZXJfaWQiOjV9.bn6b--y1Dx30Il0quopBfYrC-RzU7TrKZBXuqTjtKQ4','2024-08-27 02:02:16.925608','2024-09-06 02:02:16.000000',5,'7709a2e49c684ac1827976ab309b1a0d'),(27,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU4ODE1MywiaWF0IjoxNzI0NzI0MTUzLCJqdGkiOiJiOTMyN2ZjNjhhZDQ0YTJhODg1ZGU5YjM5Y2MzZDA3MCIsInVzZXJfaWQiOjV9.rPgvqlSmupbb529ksXrVwC-CRZEEoYHhskUFTraoBA8','2024-08-27 02:02:33.587236','2024-09-06 02:02:33.000000',5,'b9327fc68ad44a2a885de9b39cc3d070'),(28,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU4OTA5NiwiaWF0IjoxNzI0NzI1MDk2LCJqdGkiOiI1YjBhNjM0NzBiZTI0NmE4YjBmN2VkOTVlM2RhMThkMyIsInVzZXJfaWQiOjV9.ztX0SniQ3QgVv5Ww7b1kpK_LQM14xm0aX4maALYM5k4','2024-08-27 02:18:16.738462','2024-09-06 02:18:16.000000',5,'5b0a63470be246a8b0f7ed95e3da18d3'),(29,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU5NTU5OSwiaWF0IjoxNzI0NzMxNTk5LCJqdGkiOiI2ODkyOTg1ZTUxMTU0MmQyYjgzNzUxNGM1ZjE1ODc3ZSIsInVzZXJfaWQiOjV9.End0ve3lN91SxyamxMkEgsA0Qq7P5gNdTC3-S-gm71I','2024-08-27 04:06:39.920510','2024-09-06 04:06:39.000000',5,'6892985e511542d2b837514c5f15877e'),(30,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU5ODQ4OCwiaWF0IjoxNzI0NzM0NDg4LCJqdGkiOiIyNjVjZGY0Zjg4YWU0ZDk3ODI4ZGIwYzI1M2RiMWI3YSIsInVzZXJfaWQiOjV9.aO2Ng4zm4uYLCzK8R9lSz0-BISKd_s-L_z08_UzPqPs','2024-08-27 04:54:48.160434','2024-09-06 04:54:48.000000',5,'265cdf4f88ae4d97828db0c253db1b7a'),(31,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTU5ODczMSwiaWF0IjoxNzI0NzM0NzMxLCJqdGkiOiIzMjcxYzUwNzY3NTE0YjhiYjNjYjgzNDAxNmVhM2UzYiIsInVzZXJfaWQiOjV9.d4G6UESFHc5zquIq5xy0IaANE8KKnmnYvsVfqhis6Ak','2024-08-27 04:58:51.553179','2024-09-06 04:58:51.000000',5,'3271c50767514b8bb3cb834016ea3e3b'),(32,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTY0MzU3OCwiaWF0IjoxNzI0Nzc5NTc4LCJqdGkiOiJhMTBmNGI3MDY2MzE0NGFkYjRmMGMxODA5ZmQzNDgxOSIsInVzZXJfaWQiOjV9.rkaex5j7TttF9Grvz0z1EF3bbSklgHhmQ0EtQJkYbJU','2024-08-27 17:26:18.995560','2024-09-06 17:26:18.000000',5,'a10f4b70663144adb4f0c1809fd34819'),(33,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTY1NzUyNiwiaWF0IjoxNzI0NzkzNTI2LCJqdGkiOiI0NDY0NTVlMzVjOTM0ODkzYjg1YjZkODY4ZGE1ZDJkYiIsInVzZXJfaWQiOjJ9.sJ-pBkDAJ_pFOlahNJLNT18Pdef9Pz9GEEUUpmGyQ7U','2024-08-27 21:18:46.190847','2024-09-06 21:18:46.000000',2,'446455e35c934893b85b6d868da5d2db'),(34,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTY1NzYxMCwiaWF0IjoxNzI0NzkzNjEwLCJqdGkiOiI3MDVkMDkxMWZkODM0NWUxODQ3ZGEzZThlZWFmMzc0YiIsInVzZXJfaWQiOjJ9.t5zpSM-GIn-QpSTKJQxUqWB2nkGXiCBaih1ES_8kBK0','2024-08-27 21:20:10.044174','2024-09-06 21:20:10.000000',2,'705d0911fd8345e1847da3e8eeaf374b'),(35,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTY1NzYzMSwiaWF0IjoxNzI0NzkzNjMxLCJqdGkiOiJmNmNmNjUwODNjYzI0NmY4YmM1YTljZjQ0ODhjZGVjYyIsInVzZXJfaWQiOjJ9.oB6YD7woBdLKbyiyJ9tcgBG--CugbJ0VZWZcmxA2rmE','2024-08-27 21:20:31.639334','2024-09-06 21:20:31.000000',2,'f6cf65083cc246f8bc5a9cf4488cdecc'),(36,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTc2MzYwNywiaWF0IjoxNzI0ODk5NjA3LCJqdGkiOiI4MDA2NzFmODU5NDE0YzQwOWU5Mjk4YTQ4MTVhODQ1ZiIsInVzZXJfaWQiOjJ9.MdqUbGH8IoRdMzsZCf989m3t11LL1lxRMT07AVgGoVc','2024-08-29 02:46:47.861686','2024-09-08 02:46:47.000000',2,'800671f859414c409e9298a4815a845f'),(37,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTg0ODkzMiwiaWF0IjoxNzI0OTg0OTMyLCJqdGkiOiI1OTBiNDE2YzZiNDk0MmQwYWJjNGJlM2FlZTk0MGMyNyIsInVzZXJfaWQiOjJ9.UrCQdDo6mcqV-At_fB4zt_-n1tTsevTbcvXzVaRqyxk','2024-08-30 02:28:52.321125','2024-09-09 02:28:52.000000',2,'590b416c6b4942d0abc4be3aee940c27'),(38,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTg3MjA5NCwiaWF0IjoxNzI1MDA4MDk0LCJqdGkiOiI1OWYwZjczOTk0NjQ0ZjIxYmRmZTZmNDhhYzYyM2FlNCIsInVzZXJfaWQiOjJ9.yX0OVnvt-SxIY12k-a_GnO21vgtkuUEUZOuUjkoo5Ao','2024-08-30 08:54:54.372005','2024-09-09 08:54:54.000000',2,'59f0f73994644f21bdfe6f48ac623ae4'),(39,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjMxNjc2MCwiaWF0IjoxNzI1NDUyNzYwLCJqdGkiOiI1YjcwMjcwNTdhYmQ0OWU2OGM0MjRmYjc3ODlkNjFiNiIsInVzZXJfaWQiOjJ9.2b2QH-AH8NjV5WNTghBR_rsiGCrHgMbsoAhTZNDDshg','2024-09-04 12:26:00.196361','2024-09-14 12:26:00.000000',2,'5b7027057abd49e68c424fb7789d61b6'),(40,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjYzMzMyOSwiaWF0IjoxNzI1NzY5MzI5LCJqdGkiOiI2NWM3OTRlZGIzMTA0MWY3OWI5ZmYzNzE3MTczMmJjNyIsInVzZXJfaWQiOjJ9.O0a6NOpZ9oJroLPXejof683GpLz2pbnc0tZsGpcmoz8','2024-09-08 04:22:09.527086','2024-09-18 04:22:09.000000',2,'65c794edb31041f79b9ff37171732bc7'),(41,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNjc4MjI5MywiaWF0IjoxNzI1OTE4MjkzLCJqdGkiOiJiODRmODBlNzFhODk0ZGZkOWY3MTFlZThlNjhmNzA3YiIsInVzZXJfaWQiOjJ9.7GobLItWHSF9PRCcxNRSDJhjl1fK7QhB8WbC3dP9z1Y','2024-09-09 21:44:53.647119','2024-09-19 21:44:53.000000',2,'b84f80e71a894dfd9f711ee8e68f707b'),(42,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzE5OTc3OCwiaWF0IjoxNzI2MzM1Nzc4LCJqdGkiOiIyY2QwNjc1NDM1ZjI0N2I0YmIxODdlZmM5MTRmMGJlOCIsInVzZXJfaWQiOjJ9.M5Y7X0l_wuMO8yVUgKIYXHbGVATeI8tDGX1L_qX3ndc','2024-09-14 17:42:58.837836','2024-09-24 17:42:58.000000',2,'2cd0675435f247b4bb187efc914f0be8'),(43,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzIxNTM1MiwiaWF0IjoxNzI2MzUxMzUyLCJqdGkiOiIxYzFiZjBmYTI3NjE0ODRmOTMwMTQyNWJlODIzNzg4MSIsInVzZXJfaWQiOjJ9.e-AgWNwhEzo7oghi3wdouDQWajTRdQtv-eZE-2Qdoek','2024-09-14 22:02:32.458268','2024-09-24 22:02:32.000000',2,'1c1bf0fa2761484f9301425be8237881'),(44,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzI4NTQ1MSwiaWF0IjoxNzI2NDIxNDUxLCJqdGkiOiI4NjExMmYxZTg2MWU0NTgwOTEyMThkZDBmMzU2ZjcyNiIsInVzZXJfaWQiOjJ9.CzhBg8aW_GHdu5PzGNlMHcCOPLpxznoXALzLtR4URCI','2024-09-15 17:30:51.920756','2024-09-25 17:30:51.000000',2,'86112f1e861e458091218dd0f356f726'),(45,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzM5MjA5MSwiaWF0IjoxNzI2NTI4MDkxLCJqdGkiOiI2MGRiNzA2MzcwZWE0ZjgzOWRiODcwODM1NjA4OTdiNiIsInVzZXJfaWQiOjJ9.8uAovdx1X6KyC7Kf1wpyY5DxR8l2M9NbZIA8uplUGBg','2024-09-16 23:08:11.656920','2024-09-26 23:08:11.000000',2,'60db706370ea4f839db87083560897b6'),(46,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzcyMTM5MywiaWF0IjoxNzI2ODU3MzkzLCJqdGkiOiJjMDYzNjgzYzFhYjE0ODNhODQ3MjYwNGZhNmY4NzdhNyIsInVzZXJfaWQiOjJ9.X_PgO3mLd6Gm15x2LlsVqR_b_U24oXCQ0tBwSaGcEv8','2024-09-20 18:36:33.033093','2024-09-30 18:36:33.000000',2,'c063683c1ab1483a8472604fa6f877a7'),(47,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzgyNjQ3OCwiaWF0IjoxNzI2OTYyNDc4LCJqdGkiOiI5MDdiYTRiMDA4NDQ0NDcwYjBmMGQ4YzRiOGQyOGUwMyIsInVzZXJfaWQiOjJ9.MN0E2sFmMBUG-C9brU4uk6TToUAQnt6mAOOjXj8Kfsk','2024-09-21 23:47:58.421945','2024-10-01 23:47:58.000000',2,'907ba4b008444470b0f0d8c4b8d28e03'),(48,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNzgzNzk5MiwiaWF0IjoxNzI2OTczOTkyLCJqdGkiOiJhZTFjYzc2ZDI1YTM0MjViYTEwZGZlOGVkYzQ3ZDFlYyIsInVzZXJfaWQiOjJ9.eGjd2nLwxiQfeVwtNJPF-xB2nnNyLd_pjEPnPZzdf2Q','2024-09-22 02:59:52.995625','2024-10-02 02:59:52.000000',2,'ae1cc76d25a3425ba10dfe8edc47d1ec'),(49,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyODI2OTU3OCwiaWF0IjoxNzI3NDA1NTc4LCJqdGkiOiIxMWYwOTdhN2VkNGE0M2Y5YWNjYzg5MTFkMWVkOWFjMyIsInVzZXJfaWQiOjJ9.dAlksqJRKRmFujz3BQ8EWdhI1yIp7WwizexEUU2FlkY','2024-09-27 02:52:58.210416','2024-10-07 02:52:58.000000',2,'11f097a7ed4a43f9accc8911d1ed9ac3'),(50,'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyODI3NTE2MCwiaWF0IjoxNzI3NDExMTYwLCJqdGkiOiIxODM3MGJhOTNlOTA0ZmVhOTU3NGFiMGJjM2MzZDgwMiIsInVzZXJfaWQiOjJ9.GUNiOXJMgKGIVNc7n5tcersC0e_MVQbSBxU7pSx2R3M','2024-09-27 04:26:00.201870','2024-10-07 04:26:00.000000',2,'18370ba93e904fea9574ab0bc3c3d802');
/*!40000 ALTER TABLE `token_blacklist_outstandingtoken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_profile`
--

DROP TABLE IF EXISTS `users_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_profile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `full_name` varchar(100) DEFAULT NULL,
  `bio` varchar(1000) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `verified` tinyint(1) NOT NULL,
  `user_id` bigint NOT NULL,
  `birthday` date DEFAULT NULL,
  `fb` varchar(100) DEFAULT NULL,
  `image_ProfileLarge` varchar(100) DEFAULT NULL,
  `image_ProfileSmall` varchar(100) DEFAULT NULL,
  `instagram` varchar(100) DEFAULT NULL,
  `otherOnline` varchar(100) DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  `tiktok` varchar(100) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `twiter` varchar(100) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `users_profile_user_id_2112e78d_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_profile`
--

LOCK TABLES `users_profile` WRITE;
/*!40000 ALTER TABLE `users_profile` DISABLE KEYS */;
INSERT INTO `users_profile` VALUES (1,'YABASH INTERNATINOAL LLC',' An integrated Company  ','default.jpg',1,1,NULL,NULL,'','','@yabash',NULL,NULL,'@yabash','Company','@yabash',NULL),(2,'Kingsley Ugochukwu','Ordinary people making super EXTRA_ordinary impacts.','images/design_1.jpg',1,2,'1985-10-21','@kings','images/design_2.png','images/logo.png','@kings','@kings',7136890771,'@kings','CEO','@kings','kings.com'),(3,NULL,NULL,'',1,3,NULL,NULL,'','',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(4,NULL,NULL,'',1,4,NULL,NULL,'','',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'Emmanuel Ugochukwu','The main man','images/asus_FODp67s.jpg',1,5,'2024-08-01','@emma','images/asus.jpg','images/asus_5VmMrin.jpg','@emma','@emma',4444444444,'@emma','President','@emma','emma.com'),(6,NULL,NULL,'',1,6,NULL,NULL,'','',NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `users_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user`
--

DROP TABLE IF EXISTS `users_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `username` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `paidMember` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user`
--

LOCK TABLES `users_user` WRITE;
/*!40000 ALTER TABLE `users_user` DISABLE KEYS */;
INSERT INTO `users_user` VALUES (1,'pbkdf2_sha256$720000$I0iQ0UdzR2SYVs3nsnsyQU$R9Br0JRuN3DmYXTJ+bvPIuwsWIM/yhCdcErRSrrYiu8=','2024-08-17 22:43:41.716830',1,'','',1,1,'2024-08-12 12:52:56.425586','Yabash','yabashllc@gmail.com',0),(2,'pbkdf2_sha256$720000$dmZ2qHj1DbsVIHirtBtKef$yTaBTf0BQ+58hPUSY6MRUGx/kQenCtdnJECshC4ZdvI=',NULL,0,'','',0,1,'2024-08-17 19:46:25.702127','yabash','kings@gmail.com',0),(3,'pbkdf2_sha256$720000$RT9QghJnBzx0IFTfw8aXxK$lSATBiXPDTELPYjB+/vHFacaotHEqPHwJQ5DM8jZ18c=','2024-08-20 02:37:53.995770',1,'','',1,1,'2024-08-20 02:37:18.555195','uprikings','uprikings@gmail.com',0),(4,'pbkdf2_sha256$720000$93BnjtVoEIVxA1qYrCoimV$1q9+W2+w0D0B8alUKPaUyeovh4PFH5PaEDCrjIBr7aM=','2024-08-21 00:23:37.970855',1,'','',1,1,'2024-08-21 00:23:16.462443','kingsley','k@gmail.com',0),(5,'pbkdf2_sha256$720000$1xnroxgS03ST9hNQiEiHWr$i6U5pi2EHoxLYVUOHRVC0+Bcq5Xj/Uv8aebfu4PL1AU=',NULL,0,'','',0,1,'2024-08-21 00:24:40.632772','Emma','emma@gmail.com',0),(6,'pbkdf2_sha256$720000$yzmZbjkOOcvTFJBMi3l336$nD54r5/weY+8XKl0Ivr2BpTDZmL0Wxr8D2+cuPUAMKk=','2024-09-19 08:01:33.806580',1,'','',1,1,'2024-08-27 02:25:36.269221','timo','timo@gmail.com',0);
/*!40000 ALTER TABLE `users_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_groups`
--

DROP TABLE IF EXISTS `users_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_groups`
--

LOCK TABLES `users_user_groups` WRITE;
/*!40000 ALTER TABLE `users_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_user_user_permissions`
--

DROP TABLE IF EXISTS `users_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_user_user_permissions`
--

LOCK TABLES `users_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `users_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-02  1:54:47

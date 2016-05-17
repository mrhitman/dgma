/*
Navicat SQLite Data Transfer

Source Server         : lllll
Source Server Version : 30714
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30714
File Encoding         : 65001

Date: 2016-05-17 21:08:50
*/

PRAGMA foreign_keys = OFF;

-- ----------------------------
-- Table structure for cathedra
-- ----------------------------
DROP TABLE IF EXISTS "main"."cathedra";
CREATE TABLE cathedra (
	id INTEGER NOT NULL, 
	name VARCHAR(50), 
	short_name VARCHAR(15), 
	image VARCHAR(100), 
	facility_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(facility_id) REFERENCES facility (id)
);

-- ----------------------------
-- Records of cathedra
-- ----------------------------
INSERT INTO "main"."cathedra" VALUES (1, null, 'АПП', null, 1);
INSERT INTO "main"."cathedra" VALUES (2, null, 'ИСПР', null, 1);
INSERT INTO "main"."cathedra" VALUES (3, null, 'ЭСА', null, 1);
INSERT INTO "main"."cathedra" VALUES (4, null, 'КИТ', null, 1);
INSERT INTO "main"."cathedra" VALUES (5, null, 'ИиИг', null, 1);
INSERT INTO "main"."cathedra" VALUES (6, null, 'ТМ', null, 1);
INSERT INTO "main"."cathedra" VALUES (7, null, 'АММО', null, 2);
INSERT INTO "main"."cathedra" VALUES (8, null, 'ПТМ', null, 2);
INSERT INTO "main"."cathedra" VALUES (9, null, 'КМСИиТ', null, 2);
INSERT INTO "main"."cathedra" VALUES (10, null, 'ВМ', null, 2);
INSERT INTO "main"."cathedra" VALUES (11, null, 'ИКГ', null, 2);
INSERT INTO "main"."cathedra" VALUES (12, null, 'КФ', null, 2);
INSERT INTO "main"."cathedra" VALUES (13, null, 'ТМ', null, 3);
INSERT INTO "main"."cathedra" VALUES (14, null, 'ОиТПС', null, 3);
INSERT INTO "main"."cathedra" VALUES (15, null, 'ОМД', null, 3);
INSERT INTO "main"."cathedra" VALUES (16, null, 'ТОЛП', null, 3);
INSERT INTO "main"."cathedra" VALUES (17, null, 'ХиОТ', null, 3);
INSERT INTO "main"."cathedra" VALUES (18, null, 'ОПМ', null, 3);
INSERT INTO "main"."cathedra" VALUES (19, null, 'Финансы', null, 4);
INSERT INTO "main"."cathedra" VALUES (20, null, 'УиА', null, 4);
INSERT INTO "main"."cathedra" VALUES (21, null, 'Менеджмент', null, 4);
INSERT INTO "main"."cathedra" VALUES (22, null, 'Эп', null, 4);
INSERT INTO "main"."cathedra" VALUES (23, null, 'МПФ', null, 4);
INSERT INTO "main"."cathedra" VALUES (24, null, 'ФВ', null, 4);
INSERT INTO "main"."cathedra" VALUES (25, null, 'ЭТ', null, null);

-- ----------------------------
-- Table structure for facility
-- ----------------------------
DROP TABLE IF EXISTS "main"."facility";
CREATE TABLE "facility" (
"id"  INTEGER NOT NULL,
"name"  VARCHAR(50),
"short_name"  VARCHAR(15),
"image"  VARCHAR(100),
PRIMARY KEY ("id" ASC)
);

-- ----------------------------
-- Records of facility
-- ----------------------------
INSERT INTO "main"."facility" VALUES (1, 'ФАКУЛЬТЕТ АВТОМАТИЗАЦИИ МАШИНОСТРОЕНИЯ И ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ ', 'ФАМИТ', null);
INSERT INTO "main"."facility" VALUES (2, 'ФАКУЛЬТЕТ МАШИНОСТРОЕНИЯ ', 'ФМ', null);
INSERT INTO "main"."facility" VALUES (3, 'ФАКУЛЬТЕТ ИНТЕГРИРОВАННЫХ ТЕХНОЛОГИЙ И ОБОРУДОВАНИЯ', 'ФИТО', null);
INSERT INTO "main"."facility" VALUES (4, 'ФАКУЛЬТЕТ ЭКОНОМИКИ И МЕНЕДЖМЕНТА', 'ФЭМ', null);

-- ----------------------------
-- Table structure for professor
-- ----------------------------
DROP TABLE IF EXISTS "main"."professor";
CREATE TABLE professor (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	cathedra_id INTEGER, 
	post VARCHAR(50), 
	academic_degree VARCHAR(50), 
	rank VARCHAR(50), 
	photo VARCHAR(100), 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	FOREIGN KEY(cathedra_id) REFERENCES cathedra (id)
);

-- ----------------------------
-- Records of professor
-- ----------------------------
INSERT INTO "main"."professor" VALUES (1, 1, 2, 'Преподаватель', 1, 'Старший преподаватель', null);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "main"."user";
CREATE TABLE user (
	id INTEGER NOT NULL, 
	name VARCHAR(50), 
	second_name VARCHAR(50), 
	middle_name VARCHAR(50), 
	password VARCHAR(50), 
	email VARCHAR(50), 
	birthday DATETIME, 
	PRIMARY KEY (id)
);

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO "main"."user" VALUES (1, 'Виктор', 'Вареник', 'Владимирович', 1, 'kabalx47@gmail.com', '1988-12-25 00:00:00.000000');

-- ----------------------------
-- Indexes structure for table user
-- ----------------------------
CREATE UNIQUE INDEX "main"."ix_user_email"
ON "user" ("email" ASC);

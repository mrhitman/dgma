/*
Navicat SQLite Data Transfer

Source Server         : data
Source Server Version : 30714
Source Host           : :0

Target Server Type    : SQLite
Target Server Version : 30714
File Encoding         : 65001

Date: 2016-05-18 11:04:35
*/

PRAGMA foreign_keys = OFF;

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
INSERT INTO "main"."facility" VALUES (1, 'ФАКУЛЬТЕТ АВТОМАТИЗАЦИИ МАШИНОСТРОЕНИЯ И ИНФОРМАЦИОННЫХ ТЕХНОЛОГИЙ ', 'ФАМИТ', 'facility/famit.jpg');
INSERT INTO "main"."facility" VALUES (2, 'ФАКУЛЬТЕТ МАШИНОСТРОЕНИЯ ', 'ФМ', 'facility/finansi.jpg');
INSERT INTO "main"."facility" VALUES (3, 'ФАКУЛЬТЕТ ИНТЕГРИРОВАННЫХ ТЕХНОЛОГИЙ И ОБОРУДОВАНИЯ', 'ФИТО', 'facility/fito.jpg');
INSERT INTO "main"."facility" VALUES (4, 'ФАКУЛЬТЕТ ЭКОНОМИКИ И МЕНЕДЖМЕНТА', 'ФЭМ', 'facility/fm.jpg');

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
INSERT INTO "main"."cathedra" VALUES (1, null, 'АПП', 'cathedra/app.jpg', 1);
INSERT INTO "main"."cathedra" VALUES (2, null, 'ИСПР', 'cathedra/ispr.jpg', 1);
INSERT INTO "main"."cathedra" VALUES (3, null, 'ЭСА', 'cathedra/esa.jpg', 1);
INSERT INTO "main"."cathedra" VALUES (4, null, 'КИТ', 'cathedra/it.jpg', 1);
INSERT INTO "main"."cathedra" VALUES (5, null, 'ИиИг', 'cathedra/iiig.jpg', 1);
INSERT INTO "main"."cathedra" VALUES (6, null, 'ТМ', 'cathedra/tm.jpg', 1);
INSERT INTO "main"."cathedra" VALUES (7, null, 'АММО', 'cathedra/ammio.jpg', 2);
INSERT INTO "main"."cathedra" VALUES (8, null, 'ПТМ', 'cathedra/ptm.jpg', 2);
INSERT INTO "main"."cathedra" VALUES (9, null, 'КМСИиТ', 'cathedra/msi.jpg', 2);
INSERT INTO "main"."cathedra" VALUES (10, null, 'ВМ', 'cathedra/vm.jpg', 2);
INSERT INTO "main"."cathedra" VALUES (11, null, 'ИГ', 'cathedra/graf.jpg', 2);
INSERT INTO "main"."cathedra" VALUES (12, null, 'КФ', 'cathedra/fiz.jpg', 2);
INSERT INTO "main"."cathedra" VALUES (13, null, 'ТМ', 'cathedra/tm_1.jpg', 3);
INSERT INTO "main"."cathedra" VALUES (14, null, 'ОиТПС', 'cathedra/sp.jpg', 3);
INSERT INTO "main"."cathedra" VALUES (15, null, 'ОМД', 'cathedra/omd.jpg', 3);
INSERT INTO "main"."cathedra" VALUES (16, null, 'ТОЛП', 'cathedra/lp.jpg', 3);
INSERT INTO "main"."cathedra" VALUES (17, null, 'ХиОТ', 'cathedra/hiop.jpg', 3);
INSERT INTO "main"."cathedra" VALUES (18, null, 'ОПМ', 'cathedra/opm.jpg', 3);
INSERT INTO "main"."cathedra" VALUES (19, null, 'Финансы', 'cathedra/f.jpg', 4);
INSERT INTO "main"."cathedra" VALUES (20, null, 'УиА', 'cathedra/yia.jpg', 4);
INSERT INTO "main"."cathedra" VALUES (21, null, 'Менеджмент', 'cathedra/logo_kaf.png', 4);
INSERT INTO "main"."cathedra" VALUES (22, null, 'Эп', 'cathedra/ep.jpg', 4);
INSERT INTO "main"."cathedra" VALUES (23, null, 'МПФ', 'cathedra/eng.jpg', 4);
INSERT INTO "main"."cathedra" VALUES (24, null, 'ФВ', 'cathedra/fv.jpg', 4);
INSERT INTO "main"."cathedra" VALUES (25, null, 'ЭТ', 'cathedra/et.jpg', 4);
INSERT INTO "main"."cathedra" VALUES (26, null, 'Философия', 'cathedra/fil.jpg', 4);

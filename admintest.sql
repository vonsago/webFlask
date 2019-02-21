/*
 Navicat Premium Data Transfer

 Source Server         : admintest
 Source Server Type    : MySQL
 Source Server Version : 50719
 Source Host           : localhost:3306
 Source Schema         : admintest

 Target Server Type    : MySQL
 Target Server Version : 50719
 File Encoding         : 65001

 Date: 21/02/2019 15:55:32
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for message
-- ----------------------------
DROP TABLE IF EXISTS `message`;
CREATE TABLE `message` (
  `s_num` varchar(20) NOT NULL,
  `title` varchar(40) NOT NULL,
  `message` text,
  PRIMARY KEY (`s_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of message
-- ----------------------------
BEGIN;
INSERT INTO `message` VALUES ('123', 'new essay', 'fengyufei');
COMMIT;

-- ----------------------------
-- Table structure for shop
-- ----------------------------
DROP TABLE IF EXISTS `shop`;
CREATE TABLE `shop` (
  `name` varchar(20) NOT NULL,
  `message` text,
  `key1` text,
  `key2` text,
  `classname` varchar(40) DEFAULT NULL,
  `picture` text,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of shop
-- ----------------------------
BEGIN;
INSERT INTO `shop` VALUES ('1', '1', '1', '1', '英语', 'timg.jpeg');
INSERT INTO `shop` VALUES ('2', '2', '2', '2', '机械', 'timg.jpeg');
INSERT INTO `shop` VALUES ('3', '3', '3', '3', '计算机', 'timg.jpeg');
INSERT INTO `shop` VALUES ('4', '4', '4', '4', '体育', 'timg.jpeg');
INSERT INTO `shop` VALUES ('5', '5', '5', '5', '艺术', 'timg.jpeg');
COMMIT;

-- ----------------------------
-- Table structure for student_detail
-- ----------------------------
DROP TABLE IF EXISTS `student_detail`;
CREATE TABLE `student_detail` (
  `name` varchar(20) NOT NULL,
  `num` varchar(20) NOT NULL,
  `message` text,
  `key1` text,
  `key2` text,
  `classname` varchar(40) DEFAULT NULL,
  `picture` text,
  PRIMARY KEY (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student_detail
-- ----------------------------
BEGIN;
INSERT INTO `student_detail` VALUES ('feng', '1234', 'fengyufei', '123', '123', '英语', 'timg.jpeg');
INSERT INTO `student_detail` VALUES ('xie', '12345', 'xiiii', '123', '123', '计算机', 'test2.png');
INSERT INTO `student_detail` VALUES ('yu', '444', 'yyy', '4', '44', '艺术', 'test1.png');
COMMIT;

-- ----------------------------
-- Table structure for student_info
-- ----------------------------
DROP TABLE IF EXISTS `student_info`;
CREATE TABLE `student_info` (
  `num` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `s_num` varchar(20) NOT NULL,
  `s_name` varchar(40) NOT NULL,
  `s_score` varchar(20) DEFAULT NULL,
  `s_image` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student_info
-- ----------------------------
BEGIN;
INSERT INTO `student_info` VALUES (42, '2', '1', '3', 'timg.jpeg');
INSERT INTO `student_info` VALUES (44, '009', 'yu', '60', 'timg.jpeg');
INSERT INTO `student_info` VALUES (45, '625', 'fei', '91', 'test2.png');
INSERT INTO `student_info` VALUES (46, '2', '1', '3', 'timg.jpeg');
INSERT INTO `student_info` VALUES (48, '009', 'yu', '60', 'timg.jpeg');
INSERT INTO `student_info` VALUES (49, '625', 'fei', '91', 'test2.png');
INSERT INTO `student_info` VALUES (51, '12', 'feng', '100', 'test1.png');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, 'admin', 'admin');
INSERT INTO `user` VALUES (2, 'test', 'test');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;

-- phpMyAdmin SQL Dump
-- version 4.5.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: 2017-06-22 15:16:32
-- 服务器版本： 5.7.11
-- PHP Version: 5.6.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `xss`
--

-- --------------------------------------------------------

--
-- 表的结构 `message`
--

CREATE TABLE `message` (
  `id` int(11) NOT NULL,
  `content` text NOT NULL,
  `createtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `flag` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `message`
--

INSERT INTO `message` (`id`, `content`, `createtime`, `flag`) VALUES
(1, 'å‘  å‘å‘ddddddddddddddddddfaå‘µå‘µå‘µå‘µå‘µ', '2017-06-18 06:50:02', 1),
(2, 'dfadffda', '2017-06-18 06:50:19', 1),
(3, 'dfadffda<>scriptfafds>fadsfsc', '2017-06-18 06:50:28', 1),
(4, '', '2017-06-19 13:20:08', 1),
(5, 'å‘æ”¾æ¾æ”¾æ¾', '2017-06-19 13:30:24', 1),
(6, 'å‘å‘å‘†æ—¶', '2017-06-19 13:31:19', 1),
(7, 'fdfaå‘å‘æµ‹è¯•äºšéº»ç±½åŠéž¥ï¼Œå•ŠéªŒè¯ç ', '2017-06-19 13:37:33', 0),
(8, 'æµ‹è¯•æµ‹è¯•', '2017-06-20 12:54:38', 0),
(9, 'dddddd<script>', '2017-06-20 13:01:57', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `message`
--
ALTER TABLE `message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2024-06-16 18:00:17
-- 伺服器版本： 10.4.21-MariaDB
-- PHP 版本： 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `socams3`
--

-- --------------------------------------------------------

--
-- 資料表結構 `account`
--

CREATE TABLE `account` (
  `ID` varchar(15) NOT NULL,
  `Password` varchar(15) NOT NULL,
  `UserType` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `account`
--

INSERT INTO `account` (`ID`, `Password`, `UserType`) VALUES
('a1103306', '12345', 1),
('a1105501', '12345', 2),
('a1105502', '12345', 2),
('a1105503', '12345', 2),
('a1105510', '12345', 2),
('a1105656', '12345', 2),
('a1105678', '12345', 2),
('Long', '12345', 2),
('t0001', '12345', 3),
('t002', '12345', 3),
('t003', '12345', 3);

-- --------------------------------------------------------

--
-- 資料表結構 `administrator`
--

CREATE TABLE `administrator` (
  `AID` varchar(15) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `advertisement`
--

CREATE TABLE `advertisement` (
  `ADID` varchar(15) NOT NULL,
  `LID` varchar(15) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `HouseAge` varchar(5) NOT NULL,
  `HouseType` int(1) NOT NULL,
  `RoomType` int(1) NOT NULL,
  `Address` varchar(30) NOT NULL,
  `RentLimit` text DEFAULT NULL,
  `Price` int(10) NOT NULL,
  `ContactName` varchar(15) NOT NULL,
  `ContactTel` varchar(15) NOT NULL,
  `Start` date NOT NULL,
  `End` date DEFAULT NULL,
  `AD_Des` text NOT NULL,
  `AD_File` varchar(100) DEFAULT NULL,
  `Validated` int(1) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `class`
--

CREATE TABLE `class` (
  `CID` varchar(15) NOT NULL,
  `Department` varchar(15) NOT NULL,
  `Section` varchar(5) DEFAULT NULL,
  `Grade` varchar(15) NOT NULL,
  `TID` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `class`
--

INSERT INTO `class` (`CID`, `Department`, `Section`, `Grade`, `TID`) VALUES
('c001', '資工', 'A', '3', 't0001'),
('c002', '外交', 'A', '1', 't002'),
('c003', '文化', 'A', '2', 't003');

-- --------------------------------------------------------

--
-- 資料表結構 `comment`
--

CREATE TABLE `comment` (
  `CMID` varchar(15) NOT NULL,
  `PID` varchar(15) NOT NULL,
  `ID` varchar(15) NOT NULL,
  `Content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `landlord`
--

CREATE TABLE `landlord` (
  `LID` varchar(15) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Tel` varchar(15) NOT NULL,
  `Email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `landlord`
--

INSERT INTO `landlord` (`LID`, `Name`, `Tel`, `Email`) VALUES
('Long', '林佳龍', '09898989898', 'long@mail.com');

-- --------------------------------------------------------

--
-- 資料表結構 `post`
--

CREATE TABLE `post` (
  `PID` varchar(15) NOT NULL,
  `ID` varchar(15) NOT NULL,
  `Name` varchar(20) NOT NULL,
  `Content` text NOT NULL,
  `Post_File` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `review`
--

CREATE TABLE `review` (
  `RID` varchar(15) NOT NULL,
  `ADID` varchar(15) NOT NULL,
  `ID` varchar(15) NOT NULL,
  `Content` text NOT NULL,
  `Rate` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `student`
--

CREATE TABLE `student` (
  `SID` varchar(15) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Grade` int(2) NOT NULL,
  `Gender` int(1) NOT NULL,
  `CLASS` varchar(15) DEFAULT NULL,
  `Tel` varchar(15) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Address` varchar(30) NOT NULL,
  `HomeTel` varchar(15) NOT NULL,
  `ContactName` varchar(15) NOT NULL,
  `ConTel` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `student`
--

INSERT INTO `student` (`SID`, `Name`, `Grade`, `Gender`, `CLASS`, `Tel`, `Email`, `Address`, `HomeTel`, `ContactName`, `ConTel`) VALUES
('a1105501', 'aaa', 3, 1, 'c001', '090909090', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa'),
('a1105502', 'bbb', 3, 1, 'c001', 'bbb', 'bbb', 'bbb', 'bbb', 'bbb', 'bbb'),
('a1105503', 'asdf', 1, 1, 'c001', '123', '123', '123', '123', '123', '123'),
('a1105510', 'Tony', 1, 1, 'c001', '123', '123', '123', '123', '123', '123'),
('a1105656', '老李', 3, 1, 'c003', '1234', '1234', '1234', '1234', '1234', '1234'),
('a1105678', '小陳', 3, 1, 'c003', '1234', '1234', '1234', '1234', '1234', '1234');

-- --------------------------------------------------------

--
-- 資料表結構 `teacher`
--

CREATE TABLE `teacher` (
  `TID` varchar(15) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Rank` int(1) NOT NULL,
  `Tel` varchar(15) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `OfficeAddr` varchar(30) NOT NULL,
  `OfficeTel` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `teacher`
--

INSERT INTO `teacher` (`TID`, `Name`, `Rank`, `Tel`, `Email`, `OfficeAddr`, `OfficeTel`) VALUES
('t0001', '林文揚', 2, '0988888888', 'WanYan@gmail.com', '12345', '1234'),
('t002', '林佳龍', 2, '134123', '12341234', '1234', '1234'),
('t003', '李遠', 1, '1234', '1234', '1234', '1234');

-- --------------------------------------------------------

--
-- 資料表結構 `visit_form`
--

CREATE TABLE `visit_form` (
  `VFID` int(15) NOT NULL,
  `SID` varchar(15) NOT NULL,
  `S_Name` varchar(15) NOT NULL,
  `DG` varchar(10) NOT NULL,
  `S_Tel` varchar(15) NOT NULL,
  `T_Name` varchar(15) NOT NULL,
  `State` int(1) NOT NULL DEFAULT 0,
  `V_Time` datetime DEFAULT NULL,
  `L_Name` varchar(15) DEFAULT NULL,
  `L_Tel` varchar(15) DEFAULT NULL,
  `R_Addr` varchar(30) DEFAULT NULL,
  `RentType` int(1) DEFAULT NULL,
  `RoomType` int(1) DEFAULT NULL,
  `Price` int(10) DEFAULT NULL,
  `RoommateN` varchar(15) NOT NULL,
  `RoommateP` varchar(15) NOT NULL,
  `RA` int(2) NOT NULL,
  `Deposit` int(10) DEFAULT NULL,
  `Recommend` int(1) DEFAULT NULL,
  `SA_01` int(1) DEFAULT NULL,
  `SA_02` int(1) DEFAULT NULL,
  `SA_03` int(1) DEFAULT NULL,
  `SA_04` int(1) DEFAULT NULL,
  `SA_05` int(1) DEFAULT NULL,
  `SA_06` int(1) DEFAULT NULL,
  `SA_07` int(1) DEFAULT NULL,
  `SA_08` int(1) DEFAULT NULL,
  `SA_09` int(1) DEFAULT NULL,
  `SA_10` int(1) DEFAULT NULL,
  `SA_11` int(1) DEFAULT NULL,
  `SA_12` int(1) DEFAULT NULL,
  `SA_13` int(1) DEFAULT NULL,
  `EN_01` int(1) DEFAULT NULL,
  `EN_02` int(1) DEFAULT NULL,
  `EN_03` int(1) DEFAULT NULL,
  `EN_04` int(1) DEFAULT NULL,
  `VI_01` int(1) DEFAULT NULL,
  `VI_02` int(1) DEFAULT NULL,
  `Result` int(1) DEFAULT NULL,
  `DI_01` int(1) DEFAULT NULL,
  `DI_02` int(1) DEFAULT NULL,
  `DI_03` int(1) DEFAULT NULL,
  `DI_04` int(1) DEFAULT NULL,
  `DI_05` int(1) DEFAULT NULL,
  `EN_03_Des` varchar(50) DEFAULT NULL,
  `EN_04_Des` varchar(50) DEFAULT NULL,
  `VI_01_Des` varchar(50) DEFAULT NULL,
  `RE_Des` varchar(50) DEFAULT NULL,
  `RE_Memo` varchar(50) DEFAULT NULL,
  `DI_05_Des` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `visit_form`
--
ALTER TABLE `visit_form`
  ADD PRIMARY KEY (`VFID`),
  ADD KEY `SID` (`SID`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `visit_form`
--
ALTER TABLE `visit_form`
  MODIFY `VFID` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 2024 年 06 月 16 日 19:15
-- 伺服器版本： 10.4.28-MariaDB
-- PHP 版本： 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `SO2`
--

-- --------------------------------------------------------

--
-- 資料表結構 `account`
--

CREATE TABLE `account` (
  `ID` varchar(15) NOT NULL,
  `Password` varchar(15) NOT NULL,
  `UserType` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 傾印資料表的資料 `account`
--

INSERT INTO `account` (`ID`, `Password`, `UserType`) VALUES
('a1103306', '12345', 1),
('a1105501', '12345', 2),
('a1105502', '12345', 2),
('a1105503', '12345', 2),
('a1105510', '12345', 2),
('a1105530', '12345', 3),
('a1105656', '12345', 2),
('a1105678', '12345', 2),
('Long', '12345', 2),
('t0001', '12345', 3),
('t0004', '12345', 4),
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 傾印資料表的資料 `administrator`
--

INSERT INTO `administrator` (`AID`, `Name`, `Email`) VALUES
('a1103306', 'L', 'asdfaf');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 傾印資料表的資料 `class`
--

INSERT INTO `class` (`CID`, `Department`, `Section`, `Grade`, `TID`) VALUES
('c001', '資工', '3', 'A', 't0001'),
('c002', '外交', '1', 'A', 't002'),
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `landlord`
--

CREATE TABLE `landlord` (
  `LID` varchar(15) NOT NULL,
  `Name` varchar(15) NOT NULL,
  `Tel` varchar(15) NOT NULL,
  `Email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 傾印資料表的資料 `student`
--

INSERT INTO `student` (`SID`, `Name`, `Grade`, `Gender`, `CLASS`, `Tel`, `Email`, `Address`, `HomeTel`, `ContactName`, `ConTel`) VALUES
('a1105501', 'aaa', 3, 1, 'c001', '090909090', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa'),
('a1105502', 'bbb', 3, 1, 'c001', 'bbb', 'bbb', 'bbb', 'bbb', 'bbb', 'bbb'),
('a1105503', 'asdf', 1, 1, 'c002', '123', '123', '123', '123', '123', '123'),
('a1105510', 'Tony', 1, 1, 'c002', '123', '123', '123', '123', '123', '123'),
('a1105530', 'asdf', 3, 1, NULL, '1234', 'asdf', 'asdf', 'asdf', 'adsf', 'asdf'),
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 傾印資料表的資料 `teacher`
--

INSERT INTO `teacher` (`TID`, `Name`, `Rank`, `Tel`, `Email`, `OfficeAddr`, `OfficeTel`) VALUES
('t0001', '林文揚', 2, '0988888888', 'WanYan@gmail.com', '12345', '1234'),
('t0004', 'teacher', 1, '12342134', 'adfad', 'adsfa', 'adsf'),
('t002', '林佳龍', 2, '134123', '12341234', '1234', '1234'),
('t003', '李遠', 1, '1234', '1234', '1234', '1234');

-- --------------------------------------------------------

--
-- 資料表結構 `visit_form`
--

CREATE TABLE `visit_form` (
  `VFID` int(11) NOT NULL,
  `SID` varchar(15) NOT NULL,
  `S_Name` varchar(15) NOT NULL,
  `DG` varchar(10) NOT NULL,
  `S_Tel` varchar(15) NOT NULL,
  `T_Name` varchar(15) NOT NULL,
  `State` int(11) DEFAULT 0,
  `V_Time` datetime DEFAULT NULL,
  `L_Name` varchar(15) DEFAULT NULL,
  `L_Tel` varchar(15) DEFAULT NULL,
  `R_Addr` varchar(30) DEFAULT NULL,
  `RentType` int(11) DEFAULT NULL,
  `RoomType` int(11) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL,
  `RoommateN` varchar(15) DEFAULT NULL,
  `RoommateP` varchar(15) DEFAULT NULL,
  `RA` int(11) NOT NULL,
  `Deposit` int(11) DEFAULT NULL,
  `Recommend` int(11) DEFAULT NULL,
  `SA_01` int(11) DEFAULT NULL,
  `SA_02` int(11) DEFAULT NULL,
  `SA_03` int(11) DEFAULT NULL,
  `SA_04` int(11) DEFAULT NULL,
  `SA_05` int(11) DEFAULT NULL,
  `SA_06` int(11) DEFAULT NULL,
  `SA_07` int(11) DEFAULT NULL,
  `SA_08` int(11) DEFAULT NULL,
  `SA_09` int(11) DEFAULT NULL,
  `SA_10` int(11) DEFAULT NULL,
  `SA_11` int(11) DEFAULT NULL,
  `SA_12` int(11) DEFAULT NULL,
  `SA_13` int(11) DEFAULT NULL,
  `EN_01` int(11) DEFAULT NULL,
  `EN_02` int(11) DEFAULT NULL,
  `EN_03` int(11) DEFAULT NULL,
  `EN_04` int(11) DEFAULT NULL,
  `VI_01` int(11) DEFAULT NULL,
  `VI_02` int(11) DEFAULT NULL,
  `Result` int(11) DEFAULT NULL,
  `DI_01` int(11) DEFAULT NULL,
  `DI_02` int(11) DEFAULT NULL,
  `DI_03` int(11) DEFAULT NULL,
  `DI_04` int(11) DEFAULT NULL,
  `DI_05` int(11) DEFAULT NULL,
  `EN_03_Des` varchar(50) DEFAULT NULL,
  `EN_04_Des` varchar(50) DEFAULT NULL,
  `VI_01_Des` varchar(50) DEFAULT NULL,
  `RE_Des` varchar(50) DEFAULT NULL,
  `RE_Memo` varchar(50) DEFAULT NULL,
  `DI_05_Des` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- 傾印資料表的資料 `visit_form`
--

INSERT INTO `visit_form` (`VFID`, `SID`, `S_Name`, `DG`, `S_Tel`, `T_Name`, `State`, `V_Time`, `L_Name`, `L_Tel`, `R_Addr`, `RentType`, `RoomType`, `Price`, `RoommateN`, `RoommateP`, `RA`, `Deposit`, `Recommend`, `SA_01`, `SA_02`, `SA_03`, `SA_04`, `SA_05`, `SA_06`, `SA_07`, `SA_08`, `SA_09`, `SA_10`, `SA_11`, `SA_12`, `SA_13`, `EN_01`, `EN_02`, `EN_03`, `EN_04`, `VI_01`, `VI_02`, `Result`, `DI_01`, `DI_02`, `DI_03`, `DI_04`, `DI_05`, `EN_03_Des`, `EN_04_Des`, `VI_01_Des`, `RE_Des`, `RE_Memo`, `DI_05_Des`) VALUES
(1, 'A1105530', '資工114', 'L', '12342134', '林文揚', 1, '0111-01-01 09:00:00', 'F', '1234123', 'adsfas', 1, 0, 3434, 'afsdfa', '123412', 34, 1212, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, NULL, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'asdfa', NULL);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`ID`);

--
-- 資料表索引 `administrator`
--
ALTER TABLE `administrator`
  ADD PRIMARY KEY (`AID`);

--
-- 資料表索引 `advertisement`
--
ALTER TABLE `advertisement`
  ADD PRIMARY KEY (`ADID`),
  ADD KEY `LID` (`LID`);

--
-- 資料表索引 `class`
--
ALTER TABLE `class`
  ADD PRIMARY KEY (`CID`),
  ADD KEY `TID` (`TID`);

--
-- 資料表索引 `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`CMID`),
  ADD KEY `PID` (`PID`,`ID`),
  ADD KEY `ID` (`ID`);

--
-- 資料表索引 `landlord`
--
ALTER TABLE `landlord`
  ADD PRIMARY KEY (`LID`);

--
-- 資料表索引 `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`PID`),
  ADD KEY `ID` (`ID`);

--
-- 資料表索引 `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`RID`),
  ADD KEY `ADID` (`ADID`,`ID`),
  ADD KEY `ID` (`ID`);

--
-- 資料表索引 `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`SID`),
  ADD KEY `TEACHER` (`CLASS`),
  ADD KEY `CLASS` (`CLASS`);

--
-- 資料表索引 `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`TID`);

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
  MODIFY `VFID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `administrator`
--
ALTER TABLE `administrator`
  ADD CONSTRAINT `administrator_ibfk_1` FOREIGN KEY (`AID`) REFERENCES `account` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `advertisement`
--
ALTER TABLE `advertisement`
  ADD CONSTRAINT `advertisement_ibfk_1` FOREIGN KEY (`LID`) REFERENCES `landlord` (`LID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `class`
--
ALTER TABLE `class`
  ADD CONSTRAINT `class_ibfk_1` FOREIGN KEY (`TID`) REFERENCES `teacher` (`TID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `account` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`PID`) REFERENCES `post` (`PID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `landlord`
--
ALTER TABLE `landlord`
  ADD CONSTRAINT `landlord_ibfk_1` FOREIGN KEY (`LID`) REFERENCES `account` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `post_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `account` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `review`
--
ALTER TABLE `review`
  ADD CONSTRAINT `review_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `account` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `review_ibfk_2` FOREIGN KEY (`ADID`) REFERENCES `advertisement` (`ADID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `account` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `student_ibfk_2` FOREIGN KEY (`CLASS`) REFERENCES `class` (`CID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`TID`) REFERENCES `account` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- 資料表的限制式 `visit_form`
--
ALTER TABLE `visit_form`
  ADD CONSTRAINT `visit_form_ibfk_1` FOREIGN KEY (`SID`) REFERENCES `student` (`SID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

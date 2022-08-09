DROP DATABASE IF EXISTS AjeetASS;
CREATE DATABASE AjeetASS;
USE AjeetASS;
CREATE TABLE SalesPeople
(
Snum INT PRIMARY KEY,
Sname VARCHAR(100) UNIQUE,
City VARCHAR(100),
Comm int
);
INSERT INTO salespeople(snum,sname,city,comm)
values
(1001,"Peel","London",12),
(1002,"Serres","Sanjose",13),
(1004,"Motika","London",11),
(1007,"Rifkin","Barcelona",15),
(1003,"Axelrod","Newyork",10);

CREATE TABLE Customers
(
	Cnum INT PRIMARY KEY,
	Cname VARCHAR(100),
	City VARCHAR(100) NOT NULL,
	Snum int,
FOREIGN KEY(Snum) REFERENCES salespeople(Snum)
);
INSERT INTO Customers(cnum,cname,city,snum)
VALUES
(2001,"Hoffman","London",1001),
(2002,"Giovanni","Rome",1003),
(2003,"Liu","Sanjose",1002),
(2004,"Grass","Berlin",1002),
(2006,"Clemens","London",1001),
(2008,"Cisneros","Sanjose",1007),
(2007,"Pereira","Rome",1004);

CREATE TABLE Orders
(
Onum INT PRIMARY KEY,
Amt DECIMAL(8,2),
Odate DATE,
Cnum INT,
Snum INT,
FOREIGN KEY(Cnum) REFERENCES Customers(Cnum),
FOREIGN KEY(Snum) REFERENCES SalesPeople(Snum)
);
INSERT INTO Orders(Onum,Amt,Odate,Cnum,Snum)
VALUES
(3001,18.69,STR_TO_DATE("3-10-1990","%d-%m-%Y"),2008,1007),
(3003,767.19,STR_TO_DATE("3-10-1990","%d-%m-%Y"),2001,1001),
(3002,1900.10,STR_TO_DATE("3-10-1990","%d-%m-%Y"),2007,1004),
(3005,5160.45,STR_TO_DATE("3-10-1990","%d-%m-%Y"),2003,1002),
(3006,1098.16,STR_TO_DATE("3-10-1990","%d-%m-%Y"),2008,1007),
(3009,1713.23,STR_TO_DATE("4-10-1990","%d-%m-%Y"),2002,1003),
(3007,75.75,STR_TO_DATE("4-10-1990","%d-%m-%Y"),2004,1002),
(3008,4273.00,STR_TO_DATE("5-10-1990","%d-%m-%Y"),2006,1001),
(3010,1309.95,STR_TO_DATE("6-10-1990","%d-%m-%Y"),2004,1002),
(3011,9891.88,STR_TO_DATE("6-10-1990","%d-%m-%Y"),2006,1001);

#Question 1
SELECT COUNT(Sname) AS 'Count of salespeople name starting with a/A'
 FROM salespeople 
 WHERE sname LIKE 'a%';
 
#question 2
SELECT sname AS 'Salesperson name'
FROM salespeople 
JOIN orders ON salespeople.snum=orders.snum 
GROUP BY orders.snum HAVING sum(amt)>2000;
#question 3
SELECT COUNT(Sname) AS 'count from newyork'
 FROM salespeople
 WHERE City LIKE 'newyork';
#question 4
SELECT COUNT(Sname)  AS 'count from london' FROM salespeople WHERE City='london' AND City='paris'; 
-- SELECT COUNT(sname) AS 'count from paris' FROM salespeople WHERE city LIKE 'paris';
#question 5
SELECT sname AS 'name',Odate AS 'order date',COUNT(orders.snum) AS 'number of orders'
FROM orders 
RIGHT JOIN salespeople ON salespeople.snum=orders.snum 
GROUP BY orders.odate,orders.snum 
ORDER BY salespeople.sname;

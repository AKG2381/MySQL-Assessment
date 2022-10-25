-- 2- Write a SQL statement to create the duplicate of the countries table named country_new with all structure and data.
-- Here in the following is the structure of the table countries.

-- +--------------+---------------+------+-----+---------+-------+
-- | Field | Type | Null | Key | Default | Extra |
-- +--------------+---------------+------+-----+---------+-------+
-- | COUNTRY_ID | varchar(2) | YES | | NULL | |
-- | COUNTRY_NAME | varchar(40) | YES | | NULL | |
-- | REGION_ID | decimal(10,0) | YES | | NULL | |
-- +--------------+---------------+------+-----+---------+-------+


use ajeet;
DROP TABLE IF EXISTS  countries;
CREATE TABLE countries(
COUNTRY_ID VARCHAR(2),
COUNTRY_NAME VARCHAR(40),
REGION_ID DECIMAL(10,0)
);
desc countries;

DROP TABLE IF EXISTS country_new;
CREATE TABLE  country_new 
AS SELECT * FROM countries;

desc country_new;
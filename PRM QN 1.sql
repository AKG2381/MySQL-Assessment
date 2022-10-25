-- 1. Write a SQL statement to create a table named countries including columns  
-- country_id, country_name and region_id and make sure that no countries except Italy, 
-- India and China will be entered in the table.
USE ajeet;
DROP TABLE IF EXISTS countries;
CREATE TABLE countries(
country_id VARCHAR(100),
country_name VARCHAR(100)
CHECK(country_name IN('Italy','India','China')) ,
region_id decimal(10,0)
);
desc countries;
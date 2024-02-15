-- Creates the database hbtn_0d_usa
-- Query to perform operation
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
       id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
       state_id INT NOT NULL PRIMARY KEY,
       name VARCHAR(256) NOT NULL
       PRIMARY KEY (id),
       CONSTRAINT cities_ibfk_1 FOREIGN KEY (state_id)
       REFERENCES states(id)
);

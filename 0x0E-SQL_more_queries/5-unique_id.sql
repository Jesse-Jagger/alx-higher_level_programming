-- a script that will create the table unique_id on your MySQL server.

CREATE TABLE unique_id (id INT DEFAULT 1, name VARCHAR(256), UNIQUE(id));


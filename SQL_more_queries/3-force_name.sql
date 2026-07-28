-- Creates the table force_name
-- id INT, name VARCHAR(256) NOT NULL
-- Does not fail if the table already exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

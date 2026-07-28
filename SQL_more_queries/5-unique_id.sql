-- Creates the table unique_id
-- id INT with default value 1 and must be unique
-- name VARCHAR(256)
-- Does not fail if the table already exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);

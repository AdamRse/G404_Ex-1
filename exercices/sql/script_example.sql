-- script.sql
CREATE DATABASE IF NOT EXISTS boutique;

\c boutique

CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO clients (nom, email) VALUES
('Alice Dupont', 'alice@example.com'),
('Bob Martin', 'bob@example.com');

SELECT * FROM clients;

-- CREATE DATABASE space_traders;

\c space_traders

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(20),
    password BYTEA
);

CREATE SCHEMA world_bank_api

CREATE TABLE country (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    iso3_code VARCHAR(50)
);

CREATE TABLE gdp (
    country_id INTEGER REFERENCES country (id),
    year INTEGER,
    value VARCHAR(50)
);

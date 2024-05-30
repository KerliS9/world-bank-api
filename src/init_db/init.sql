
-- CREATE SCHEMA world_bank_api

CREATE TABLE rw_economic_data (
    indicator_id VARCHAR(50),
    indicator_value VARCHAR(255),
    country_id VARCHAR(5),
    country_value VARCHAR(100),
    countryiso3code VARCHAR(5),
    date VARCHAR(10),
    value NUMERIC,
    unit VARCHAR(50),
    obs_status VARCHAR(50),
    decimal INTEGER
);

CREATE TABLE country (
    id VARCHAR PRIMARY KEY,
    name VARCHAR(50),
    iso3_code VARCHAR(50)
);

CREATE TABLE gdp (
    id VARCHAR PRIMARY KEY,
    country_id VARCHAR(50),
    year INTEGER,
    value VARCHAR(50)
);

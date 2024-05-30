# world-bank-api

## Introduction

This repository aims to show a data search project in an API, treating the data in columnar format and storing it into tables.

* API: `https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page=1&per_page=50`

## Requirements to run this project
- git
- python
- docker-compose

## How to start this project

Clone this repoh $ `git clone git@github.com:KerliS9/world-bank-api.git`

Set your file .env file, like this:
```
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  POSTGRES_DB=world_bank_api
  POSTGRES_HOST=db
  POSTGRES_PORT=5432
```
Project structure:

```
world-bank-api/
├── src/
│   ├── flask_routes.py
│   ├── get_api.py
│   ├── insert_data.py
│   ├── queries.py
│   └── utils.py
│   │
│   ├── init_db/
│   │   └── init.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .env

```
Run $ `docker-compose up --build -d` - wait the building to finished

Then open the browser with `http://localhost:5000/insert`

Wait the message bellow will appear:

```
{
  "message": "Dados inseridos com sucesso!"
}
```
Great! Now you can see the data in the routes below.

### Routes to see the data

- `http://localhost:5000/tables` - show tables in database
- `http://localhost:5000/rw_economic_data` - show all data from API
- `http://localhost:5000/rw_economic_data/count` - show number of lines in table rw_economic_data
- `http://localhost:5000/country` - show data from table country
- `http://localhost:5000/gdp` - show data from table gdp
- `http://localhost:5000/pivoted` - show pivoted data, like bellow

```
{
    "2019": "1873288205186.45",
    "2020": "1476107231194.11",
    "2021": "1649622821885.14",
    "2022": "1920095779022.73",
    "2023": null,
    "id": "BR",
    "iso3_code": "BRA",
    "name": "Brazil"
},
```

### Challenge Description

The objective of this test is to develop a data ingestion pipeline using Python, which will:

* **Extract** data on the Gross Domestic Product (GDP) of South American countries using the World Bank API:
  * Endpoint: `https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page=1&per_page=50`

* **Load** this data into a SQL database of your choice (such as PostgreSQL, SQLite, DuckDB, Trino, etc.):
  * Create `country` (id, name, iso3_code) and `gdp` (country_id, year, value) tables.
  * Additional structures or control columns may be implemented as needed.

* **Query** the loaded data to produce a pivoted report of the last 5 years for each country, presented in Billions:
  * Expected query structure:

    | id | name     | iso3_code | 2019 | 2020 | 2021 | 2022 | 2023 |
    |----|----------|-----------|------|------|------|------|------|

### Technical Requirements

* Implement the solution in a Docker environment, using Docker Compose to orchestrate the necessary services.
* Use only pure Python or SQL for data manipulation, without frameworks or libraries based on dataframes (such as Pandas, Polars, etc.). Utility and database access libraries are allowed.
* The use of Apache Airflow for process automation is optional, but will be considered a differential.

### Submission

* Submit the code in a Git repository (e.g., GitHub, GitLab).
* Include a `README.md` file with detailed instructions on how to execute the project.
* Document assumptions and design decisions made during development.

### Evaluation Criteria

* Reliability and efficiency of the script.
* Clarity and organization of the code.
* Strict adherence to the provided instructions and requirements.

We hope you find this challenge stimulating and informative. Should you have any questions or need further information, please do not hesitate to contact us.

### Decisions

I decided to use Flask to present the data inside de tables, because it's easy to load and manage.

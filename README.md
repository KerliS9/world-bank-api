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

Set your file `.env` file, like this:
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
│   └── init_db/
│      └── init.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── .env

```
Run $ `docker-compose up --build -d`. Wait the building to finished.

Then open the browser with `http://localhost:5000/insert`

Wait until the message bellow appear:

```
{
  "message": "Successfully inserted data!"
}
```
Great! Now you can see the data in the routes below.

### Data routes:

- `http://localhost:5000/tables` - shows all the tables in the database
- `http://localhost:5000/rw_economic_data` - shows all the data from the API
- `http://localhost:5000/rw_economic_data/count` - shows the amount of lines in the rw_economic_data table
- `http://localhost:5000/country` - shows the data from the country table
- `http://localhost:5000/gdp` - shows the data from the gdp table
- `http://localhost:5000/pivoted` - shows pivoted data, like below

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

### Decisions made

At first I tried to configure Postgres with PgAdmin, but the workload was too heavy for my notebook to run. So I changed the way to present the data inside the tables to Flask, because it's lightweight, easier to load and manage.

For the data extraction, I chose to bring all the data from the API into a raw table, and locally manage the data. Because this way the code connects to the API only one time, and not everytime a new table is created.

# Used technologies:

- Git
- Docker-compose
- Python
- PostgreSQL
- Python framework - Flask

def change_table_schema(table_name, old_schema, new_schema):
    query = f"ALTER TABLE {old_schema}.{table_name} SET SCHEMA {new_schema};"

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                print(f"Table '{table_name}' moved from schema '{old_schema}' to '{new_schema}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

#change_table_schema('rw_economic_data', 'world_bank_api', 'public')

create_rw_economic_data = """
    CREATE TABLE IF NOT EXISTS rw_economic_data (
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
"""

create_country = """
    CREATE TABLE country (
        id VARCHAR PRIMARY KEY,
        name VARCHAR(50),
        iso3_code VARCHAR(50)
    );
"""

create_gdp = """
    CREATE TABLE gdp (
        id VARCHAR PRIMARY KEY,
        country_id VARCHAR(50),
        year INTEGER,
        value VARCHAR(50)
    );
"""

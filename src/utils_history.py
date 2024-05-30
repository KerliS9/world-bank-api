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


def create_table():
    create_table_query = """
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
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(create_table_query)
    cur.close()
    conn.close()
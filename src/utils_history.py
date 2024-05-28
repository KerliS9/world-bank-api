def change_table_schema(table_name, old_schema, new_schema):
    query = f"ALTER TABLE {old_schema}.{table_name} SET SCHEMA {new_schema};"

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                print(f"Table '{table_name}' moved from schema '{old_schema}' to '{new_schema}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

change_table_schema('rw_economic_data', 'world_bank_api', 'public')
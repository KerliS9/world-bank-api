from utils import get_db_connection, cur_fetchall, delete_data_from_table


def insert_raw_data(response_data):
    table_name = 'rw_economic_data'
    delete_data_from_table(table_name)
    insert_query = """
    INSERT INTO rw_economic_data (indicator_id, indicator_value, country_id, country_value, countryiso3code, date, value, unit, obs_status, decimal)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                for data in response_data:
                    indicator_id = data['indicator']['id']
                    indicator_value = data['indicator']['value']
                    country_id = data['country']['id']
                    country_value = data['country']['value']
                    countryiso3code = data['countryiso3code']
                    date = data['date']
                    value = data['value']
                    unit = data['unit']
                    obs_status = data['obs_status']
                    decimal = data['decimal']

                    cur.execute(insert_query, (indicator_id, indicator_value, country_id, country_value, countryiso3code, date, value, unit, obs_status, decimal))
            conn.commit()
            print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def insert_country_data():
    table_name = 'country'
    delete_data_from_table(table_name)
    select_query = "SELECT country_id, country_value, countryiso3code FROM rw_economic_data;"
    response_data = cur_fetchall(select_query)
    insert_query = """
        INSERT INTO country (id, name, iso3_code)
        VALUES (%s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
    """

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                for data in response_data:
                    country_id = data['country_id']
                    name = data['country_value']
                    iso3_code = data['countryiso3code']

                    cur.execute(insert_query, (country_id, name, iso3_code))
            conn.commit()
            print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def insert_gdp_data():
    table_name = 'gdp'
    delete_data_from_table(table_name)
    select_query = "SELECT country_id, date, value FROM rw_economic_data;"
    response_data = cur_fetchall(select_query)
    insert_query = """
        INSERT INTO gdp (id, country_id, year, value)
        VALUES (%s, %s, %s, %s);
    """

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                for data in response_data:
                    country_id = data['country_id']
                    year = data['date']
                    id_ = f"{country_id}-{year}"
                    value = data['value']
                    cur.execute(insert_query, (id_, country_id, year, value))
            conn.commit()
            print("Data inserted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
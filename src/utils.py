import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from flask import jsonify
import os
from dotenv import load_dotenv


load_dotenv()


def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return conn


def database_exists(conn, db_name):
    query = "SELECT 1 FROM pg_database WHERE datname=%s;"
    with conn.cursor() as cur:
        cur.execute(query, (db_name,))
        return cur.fetchone() is not None


def create_database(db_name):
    try:
        with get_db_connection() as conn:
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 
            if database_exists(conn, db_name):
                print(f"Database '{db_name}' already exists.")
            else:
                query = f"CREATE DATABASE {db_name};"
                with conn.cursor() as cur:
                    cur.execute(query)
                    print(f"Database '{db_name}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

create_database(os.getenv('POSTGRES_DB'))


def cur_fetchone(query):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(db_version)


def cur_fetchall(select_query):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(select_query)
            tables = cur.fetchall()
    return tables


def cur_fetchall_data(select_query):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(select_query)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            results = [dict(zip(columns, row)) for row in rows]
    return results


def insert_into(insert_query, data_to_insert):
      with get_db_connection() as conn:
          with conn.cursor() as cur:
              cur.execute(insert_query, data_to_insert)
              conn.commit()
      # return jsonify({'message': 'Dados inseridos com sucesso!'}), 201


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
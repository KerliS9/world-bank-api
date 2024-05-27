from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv
from get_api import get_data

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(db_version)

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


@app.route('/insert', methods=['POST'])
def insert_data():
    data = get_data()
    print(data[0])
    for item in data:
        insert_query = """
        INSERT INTO rw_economic_data (indicator_id, indicator_value, country_id, country_value, countryiso3code, date, value, unit, obs_status, decimal)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data_to_insert = (
            item['indicator']['id'],
            item['indicator']['value'],
            item['country']['id'],
            item['country']['value'],
            item['countryiso3code'],
            item['date'],
            item['value'],
            item['unit'],
            item['obs_status'],
            item['decimal']
        )

        try:
            #with psycopg2.connect(**conn_params) as conn:
            #    with conn.cursor() as cur:
            #        cur.execute(insert_query, data_to_insert)
            #        conn.commit()
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute(insert_query, data_to_insert)
            cur.close()
            conn.close()
            return jsonify({'message': 'Dados inseridos com sucesso!'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

insert_data()

@app.route('/tables', methods=['GET'])
def get_tables():
    select_query = """
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE' AND table_schema NOT IN ('pg_catalog', 'information_schema')
        ORDER BY table_schema, table_name;
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(select_query)
                tables = cur.fetchall()
        return jsonify(tables), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/data', methods=['GET'])
def get_data():
    select_query = "SELECT * FROM rw_economic_data"
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(select_query)
                rows = cur.fetchall()
                columns = [desc[0] for desc in cur.description]
                results = [dict(zip(columns, row)) for row in rows]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    #create_table()
    app.run(host='0.0.0.0', port=5000, debug=True)
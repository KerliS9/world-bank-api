from flask import Flask, jsonify
import psycopg2
from get_api import get_data
from utils import get_db_connection, cur_fetchone, cur_fetchall, delete_data_from_table


app = Flask(__name__)


@app.route('/')
def index():
    query = 'SELECT version();'
    return cur_fetchone(query)


@app.route('/databases', methods=['GET'])
def show_databases():
    select_query = "SELECT datname FROM pg_database WHERE datistemplate = false;"
    try:
        databases = cur_fetchall(select_query)
        return jsonify(databases), 200
    except Exception as e:
        print(f"An error occurred: {e}")


@app.route('/tables', methods=['GET'])
def get_tables():
    select_query = """
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE' AND table_schema NOT IN ('pg_catalog', 'information_schema')
        ORDER BY table_schema, table_name;
    """
    try:
        tables = cur_fetchall(select_query)
        return jsonify(tables), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/insert', methods=['POST'])
def insert_data():
    with app.app_context():
        response_data = get_data()
        #print("response_data[0]:", response_data[0])
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
                return jsonify({'message': 'Dados inseridos com sucesso!'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/rw_economic_data', methods=['GET'])
def get_data():
    select_query = "SELECT * FROM rw_economic_data;"
    try:
        data = cur_fetchall(select_query)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    table_name = 'rw_economic_data'
    delete_data_from_table(table_name)
    app.run(debug=True)
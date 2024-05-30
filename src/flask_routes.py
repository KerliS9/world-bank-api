from flask import Flask, jsonify
import psycopg2
from get_api import get_data
from utils import get_db_connection, cur_fetchone, cur_fetchall, delete_data_from_table
from insert_data import insert_raw_data, insert_country_data, insert_gdp_data


app = Flask(__name__)


@app.route('/')
def index():
    query = 'SELECT version();'
    try:
        databases = cur_fetchone(query)
        return jsonify(databases), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/databases', methods=['GET'])
def show_databases():
    select_query = "SELECT datname FROM pg_database WHERE datistemplate = false;"
    try:
        databases = cur_fetchall(select_query)
        return jsonify(databases), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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


@app.route('/insert', methods=['GET'])
def insert_data():
    with app.app_context():
        try:
            response_data = get_data()
            insert_raw_data(response_data)
            insert_country_data()
            insert_gdp_data()
            return jsonify({'message': 'Dados inseridos com sucesso!'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/rw_economic_data', methods=['GET'])
def get_raw_data():
    select_query = "SELECT * FROM rw_economic_data;"
    try:
        data = cur_fetchall(select_query)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/rw_economic_data/count', methods=['GET'])
def count_data():
    select_query = "SELECT count(*) FROM rw_economic_data;"
    try:
        data = cur_fetchall(select_query)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/country', methods=['GET'])
def get_country_data():
    select_query = "SELECT * FROM country;"
    try:
        data = cur_fetchall(select_query)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/gdp', methods=['GET'])
def get_gdp_data():
    select_query = "SELECT * FROM gdp;"
    try:
        data = cur_fetchall(select_query)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/pivoted', methods=['GET'])
def get_pivoted_data():
    select_query = "SELECT C.*, RW.date, RW.value FROM country C LEFT JOIN rw_economic_data AS RW ON C.id = RW.country_id WHERE date >= '2019';"
    try:
        data = cur_fetchall(select_query)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

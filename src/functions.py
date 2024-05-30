def insert_data():
    table_name = 'rw_economic_data'
    delete_data_from_table(table_name)
    with app.app_context():
        response_data = get_data()
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


@app.route('/insertCountry', methods=['GET'])
def insert_country_data():
    select_query = "SELECT country_id, country_value, countryiso3code, date FROM rw_economic_data;"
    with app.app_context():
        response_data = cur_fetchall(select_query)
        try:
            return jsonify({'message': 'Dados inseridos com sucesso!'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
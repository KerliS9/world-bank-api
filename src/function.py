def insert_data():
    response_data = get_data()
    print("response_data[0]:", response_data[0])
    for item in response_data:
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


def insert_data():
    response_data = get_data()
    print("response_data[0]:", response_data[0])
    data = {
        'indicator': {'id': 'NY.GDP.MKTP.CD', 'value': 'GDP (current US$)'},
        'country': {'id': 'AR', 'value': 'Argentina'},
        'countryiso3code': 'ARG',
        'date': '1989',
        'value': 76629657863.6557,
        'unit': '',
        'obs_status': '',
        'decimal': 0
    }

    insert_query = """
    INSERT INTO rw_economic_data (indicator_id, indicator_value, country_id, country_value, countryiso3code, date, value, unit, obs_status, decimal)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    data_to_insert = (
        data['indicator']['id'],
        data['indicator']['value'],
        data['country']['id'],
        data['country']['value'],
        data['countryiso3code'],
        data['date'],
        data['value'],
        data['unit'],
        data['obs_status'],
        data['decimal']
    )
    
    try:
        insert_into(insert_query, data_to_insert)
        return jsonify({'message': 'Dados inseridos com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
        print(indicator_id, indicator_value, country_id, country_value, countryiso3code, date, value, unit, obs_status, decimal)

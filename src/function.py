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

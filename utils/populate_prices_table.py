from mysql.connector import connect

CRIDENTIALS = {
    'host': 'localhost', 'user': 'root',
    'password': 'password', 'database': 'trading'
}

def populate_prices_table(ticker, data):
    connection = connect(**CRIDENTIALS)
    query = f'''INSERT INTO {ticker} (
        time, open, high, low, close, tick_volume, spread, volume
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    with connection.cursor() as cursor:
        cursor.executemany(query, data)
        connection.commit()

if __name__ == '__main__':
    test_data = [(1, 2, 3, 4, 5, 6, 7), (1, 2, 3, 4, 5, 6, 7)]
    create_prices_table('SBER', test_data)

from load_pickle_object import load_pickle_object
from mysql.connector import connect

CRIDENTIALS = {
    'host': 'localhost', 'user': 'root',
    'password': 'password', 'database': 'trading'
}
ALL_TICKERS = load_pickle_object('data/tickers/all_tickers.pickle')

def create_prices_table(ticker):
    connection = connect(**CRIDENTIALS)
    query = f'''CREATE TABLE IF NOT EXISTS {ticker} (
        time INT, open FLOAT, high FLOAT, low FLOAT,
        close FLOAT, tick_volume INT, spread INT, volume INT
    )'''
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

if __name__ == '__main__':
    for ticker in ALL_TICKERS:
        create_prices_table(ticker)

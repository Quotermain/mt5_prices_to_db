from load_pickle_object import load_pickle_object
from mysql.connector import connect

CRIDENTIALS = {
    'host': 'localhost', 'user': 'root',
    'password': 'password', 'database': 'trading'
}
ALL_TICKERS = load_pickle_object('data/tickers/all_tickers.pickle')

def clean_prices_table(ticker):
    connection = connect(**CRIDENTIALS)
    query = f'TRUNCATE {ticker}'
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()

if __name__ == '__main__':
    for ticker in ALL_TICKERS:
        clean_prices_table(ticker)

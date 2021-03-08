from utils.get_candles import get_candles
from utils.load_pickle_object import load_pickle_object
from utils.populate_prices_table import populate_prices_table

from time import sleep

ALL_TICKERS = load_pickle_object('data/tickers/all_tickers.pickle')

def run(ticker):
    print(ticker)
    prices = get_candles(ticker, 'mt5.TIMEFRAME_M1', 500).tolist()
    print(prices)
    populate_prices_table(ticker, prices)

if __name__ == '__main__':
    while True:
        for ticker in ALL_TICKERS:
            run(ticker)

from utils.get_candles import get_candles
from utils.load_pickle_object import load_pickle_object
from multiprocessing import Pool
import pickle

ALL_TICKERS = load_pickle_object('data/tickers/all_tickers.pickle')

def run(ticker):
    print(ticker)
    prices = get_candles(ticker, 'mt5.TIMEFRAME_M1', 100000)
    with open(f'data/prices/{ticker}.pickle', 'wb') as file:
        pickle.dump(prices, file)

if __name__ == '__main__':
    while True:
        try:
            with Pool(4) as p:
                p.map(run, ALL_TICKERS)
        except KeyboardInterrupt:
            print('Aborting')
        except Exception:
            continue

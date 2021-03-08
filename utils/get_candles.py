import MetaTrader5 as mt5
from sys import argv

def get_candles(ticker, timeframe, n_candles):
    """
    Establishes connection with the terminal, parses prices,
    as is, shuts down the connection
    """
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()
    rates = mt5.copy_rates_from_pos(ticker, eval(timeframe), 0, n_candles)
    mt5.shutdown()
    return rates

if __name__ == '__main__':
    ticker = argv[1]
    timeframe = argv[2]
    n_candles = int(argv[3])
    print(get_candles(ticker, timeframe, n_candles))

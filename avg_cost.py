import datetime


class Trade:
    def __init__(self, ticker, side, datetime, shares, share_price):
        self.ticker = ticker
        self.side = side
        self.datetime = datetime
        self.shares = shares
        self.share_price = share_price


# define datetimes that will be assigned to Trade objects
datetime1 = datetime.datetime(2020, 1, 1, 9, 30)
datetime2 = datetime.datetime(2020, 1, 2, 9, 30)
datetime3 = datetime.datetime(2020, 1, 3, 9, 30)
datetime4 = datetime.datetime(2020, 1, 4, 9, 30)

# define Trade objects to test on
trade1 = Trade('KO', 'BUY', datetime1, 5, 50.00)
trade2 = Trade('KO', 'BUY', datetime2, 5, 55.00)
trade3 = Trade('KO', 'SELL', datetime3, 8, 58.00)
trade4 = Trade('KO', 'BUY', datetime4, 5, 52.00)

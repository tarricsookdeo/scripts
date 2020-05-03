class Trade:
    def __init__(self, ticker, side, datetime, shares, share_price):
        self.ticker = ticker
        self.side = side
        self.datetime = datetime
        self.shares = shares
        self.share_price = share_price
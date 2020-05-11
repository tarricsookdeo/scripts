import datetime


class Trade:
    def __init__(self, ticker, side, datetime, shares, share_price):
        self.ticker = ticker
        self.side = side
        self.datetime = datetime
        self.shares = shares
        self.share_price = share_price


# define datetimes that will be assigned to Trade objects

# KO datetimes
datetime1 = datetime.datetime(2020, 1, 1, 9, 30)
datetime2 = datetime.datetime(2020, 1, 2, 9, 30)
datetime3 = datetime.datetime(2020, 1, 3, 9, 30)
datetime4 = datetime.datetime(2020, 1, 4, 9, 30)
datetime5 = datetime.datetime(2020, 1, 5, 9, 30)

# MSFT datetimes
datetime6 = datetime.datetime(2020, 1, 6, 9, 30)
datetime7 = datetime.datetime(2020, 1, 7, 9, 30)
datetime8 = datetime.datetime(2020, 1, 8, 9, 30)
datetime9 = datetime.datetime(2020, 1, 9, 9, 30)
datetime10 = datetime.datetime(2020, 1, 10, 9, 30)

# AAPL datetimes
datetime11 = datetime.datetime(2020, 1, 11, 9, 30)
datetime12 = datetime.datetime(2020, 1, 12, 9, 30)
datetime13 = datetime.datetime(2020, 1, 13, 9, 30)
datetime14 = datetime.datetime(2020, 1, 14, 9, 30)
datetime15 = datetime.datetime(2020, 1, 15, 9, 30)

# define KO Trade objects to test on
trade1 = Trade('KO', 'BUY', datetime1, 5, 50.00)   # [50.00, 5]
trade2 = Trade('KO', 'BUY', datetime2, 5, 55.00)   # [52.50, 10]
trade3 = Trade('KO', 'SELL', datetime3, 8, 58.00)  # [52.50, 2]
trade4 = Trade('KO', 'BUY', datetime4, 5, 52.00)   # [52.14, 7]
trade5 = Trade('KO', 'SELL', datetime5, 2, 52.00)  # [52.00, 5]

# define MSFT Trade objects to test on
trade6 = Trade('MSFT', 'BUY', datetime6, 5, 50.00)   # [50.00, 5]
trade7 = Trade('MSFT', 'BUY', datetime7, 5, 55.00)   # [52.50, 10]
trade8 = Trade('MSFT', 'SELL', datetime8, 8, 58.00)  # [52.50, 2]
trade9 = Trade('MSFT', 'BUY', datetime9, 5, 52.00)   # [52.14, 7]
trade10 = Trade('MSFT', 'SELL', datetime10, 2, 52.00)  # [52.00, 5]

# define MSFT Trade objects to test on
trade11 = Trade('AAPL', 'BUY', datetime11, 5, 50.00)   # [50.00, 5]
trade12 = Trade('AAPL', 'BUY', datetime12, 5, 55.00)   # [52.50, 10]
trade13 = Trade('AAPL', 'SELL', datetime13, 8, 58.00)  # [52.50, 2]
trade14 = Trade('AAPL', 'BUY', datetime14, 5, 52.00)   # [52.14, 7]
trade15 = Trade('AAPL', 'SELL', datetime15, 2, 52.00)  # [52.00, 5]

trades = [trade9, trade2, trade15, trade8, trade11, trade5, trade6, trade13,
          trade4, trade1, trade10, trade12, trade7, trade14, trade3]

# OBJECTIVE: RETURN A LIST CONTAINING LISTS OF THE CURRENT POSITIONS IN
# [ticker, avg_price_per_share, shares] FORMAT
# [
#   ['KO', 52.00, 5],
#   ['MSFT', 52.00, 5],
#   ['AAPL', 52.00, 5]
# ]


def calculate_positions(trades):
    # return all unique tickers into a set using list compression
    tickers = {trade.ticker for trade in trades}

    # create a list which will contain lists of trades seperated for each unique ticker
    trades_seperated = []
    for ticker in tickers:
        trades_seperated.append([x for x in trades if x.ticker == ticker])

    # create a list of lists of trades that are expensed from sell orders
    expensed_trades = []
    for trades in trades_seperated:
        shares_to_sell = 0
        buy_trades = [x for x in trades if x.side == 'BUY']
        buy_trades = sorted(buy_trades, key=lambda trade: trade.datetime)
        for trade in trades:
            if trade.side == 'SELL':
                shares_to_sell += trade.shares
            while shares_to_sell > 0:
                for trade in buy_trades:
                    if trade.shares - shares_to_sell >= 0:
                        trade.shares -= shares_to_sell
                        shares_to_sell = 0
                    else:
                        shares_to_sell -= trade.shares
                        trade.shares = 0
        filtered_buy_trades = [x for x in buy_trades if x.shares != 0]
        expensed_trades.append(filtered_buy_trades)

    # calculate positions based on expensed_trades
    positions = []
    for trades in expensed_trades:
        total_shares = 0.0
        avg_price_per_share = 0.0
        for trade in trades:
            if total_shares == 0.0 and avg_price_per_share == 0.0:
                total_shares = trade.shares
                avg_price_per_share = trade.share_price
            else:
                total_shares += trade.shares
                avg_price_per_share = (trade.share_price * (trade.shares / total_shares)) + (
                    avg_price_per_share * ((total_shares - trade.shares) / total_shares))
        positions.append([trade.ticker, avg_price_per_share, total_shares])

    return positions


positions = calculate_positions(trades)

for position in positions:
    print(position[0], position[1], position[2])

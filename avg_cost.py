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
datetime5 = datetime.datetime(2020, 1, 5, 9, 30)

# define Trade objects to test on
trade1 = Trade('KO', 'BUY', datetime1, 5, 50.00)   # [50.00, 5]
trade2 = Trade('KO', 'BUY', datetime2, 5, 55.00)   # [52.50, 10]
trade3 = Trade('KO', 'SELL', datetime3, 8, 58.00)  # [55.00, 2]
trade4 = Trade('KO', 'BUY', datetime4, 5, 52.00)   # [52.86, 7]
trade5 = Trade('KO', 'SELL', datetime5, 2, 52.00)  # [52.00, 5]

trades = [trade1, trade2, trade3, trade4]


def sort_trades_by_datetime(trades_list):
    """Returns a list of trades sorted by their datetime in assending order."""
    return sorted(trades_list, key=lambda trade: trade.datetime)


def expense_shares_from_sell_orders(trades_list):
    """Returns a list of trades where the BUY orders are expensed from the SELL
       orders using the FIFO pricipal. Any Trade objects with 0 shares after
       being expensed, will be filtered out of the returned list. The returned
       list will be a list of BUY orders only.
    """
    shares_to_sell = 0
    for trade in trades_list:
        if trade.side == 'SELL':
            shares_to_sell += trade.shares

    buy_trades = [x for x in trades_list if x.side == 'BUY']
    sorted_buy_trades = sort_trades_by_datetime(buy_trades)

    index = 0
    while shares_to_sell != 0:
        if sorted_buy_trades[index].shares - shares_to_sell >= 0:
            sorted_buy_trades[index].shares -= shares_to_sell
            shares_to_sell = 0
        else:
            shares_to_sell -= sorted_buy_trades[index].shares
            sorted_buy_trades[index].shares = 0
            index += 1

    filtered_and_sorted_buy_trades = [
        x for x in sorted_buy_trades if x.shares != 0]

    return filtered_and_sorted_buy_trades


def calculate_avg_cost_per_share(trades_list):
    """Returns the average cost per share of a specific ticker symbol by using
       a list of all trades for that ticker symbol.
    """
    total_shares = 0
    avg_price_per_share = 0.00

    sorted_and_expensed_buy_orders = expense_shares_from_sell_orders(
        trades_list)

    for trade in sorted_and_expensed_buy_orders:
        if total_shares == 0 and avg_price_per_share == 0.00:
            total_shares = trade.shares
            avg_price_per_share = trade.share_price
        else:
            total_shares += trade.shares
            avg_price_per_share = (trade.share_price * (trade.shares / total_shares)) + (
                avg_price_per_share * ((total_shares - trade.shares) / total_shares))

    return [avg_price_per_share, total_shares]


print(calculate_avg_cost_per_share(trades))

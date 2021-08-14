from collections import namedtuple

StockData = namedtuple(
    "StockData",
    "ticker price_text name price dividends",
)

StockTarget = namedtuple("StockTarget", "ticker type min max")

DividendData = namedtuple("DividendData", "type date_in date_cash value")

from .scrapper import StockData
from src.models import StockTarget


class StockAnalyzer:
    def __init__(self, stock: StockData, target: StockTarget):
        self.stock = stock
        self.target = target

    def analyze(self) -> str:
        if self.__is_maximum_target_level():
            return self.__proceed_maximal_based_report()
        elif self.__is_minimum_target_level():
            return self.__proceed_minimal_based_report()
        else:
            return self.__proceed_neutral_report()

    def last_dividend(self) -> str:
        if len(self.stock.dividends) > 0:
            return self.stock.dividends[0].value
        return None

    def __is_maximum_target_level(self) -> bool:
        return self.stock.price >= self.target.max

    def __is_minimum_target_level(self) -> bool:
        return self.stock.price <= self.target.min

    def __proceed_maximal_based_report(self) -> str:
        return "{} ({}) atigiu sua máxima configurada em R${}".format(
            self.stock.name, self.stock.ticker, self.stock.price_text
        )

    def __proceed_minimal_based_report(self) -> str:
        return "{} ({}) atigiu sua mínima configurada em R${}".format(
            self.stock.name, self.stock.ticker, self.stock.price_text
        )

    def __proceed_neutral_report(self) -> str:
        return "{} ({}) ainda está {} entre o gap {}<->{}".format(
            self.stock.name,
            self.stock.ticker,
            self.stock.price,
            self.target.min,
            self.target.max,
        )

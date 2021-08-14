from src.services import StatusInvestScrapper
from src.services import StockAnalyzer
from src.models import StockTarget
from concurrent.futures import ThreadPoolExecutor, wait
from typing import List


class Application:
    def __init__(self, pool_executor: ThreadPoolExecutor):
        self.pool_executor = pool_executor

    def __get_wallet(self) -> List[StockTarget]:
        return [
            StockTarget(ticker="bbse3", min=21.5, max=27.5, type="STOCK"),
            StockTarget(ticker="vvar3", min=10.5, max=17.5, type="STOCK"),
            StockTarget(ticker="mglu3", min=18.5, max=25.5, type="STOCK"),
            StockTarget(ticker="igta3", min=36.5, max=48.5, type="STOCK"),
            StockTarget(ticker="brdt3", min=24.5, max=31.5, type="STOCK"),
            StockTarget(ticker="petr4", min=24.5, max=32.5, type="STOCK"),
            StockTarget(ticker="recr11", min=24.5, max=32.5, type="FII"),
        ]

    def __fetch_item(self, stock_target: StockTarget) -> None:
        try:
            scrapper = StatusInvestScrapper()
            stock = scrapper.scrap(stock_target.ticker, stock_target.type)
            analyzer = StockAnalyzer(stock, stock_target)
            analyzer.analyze()
            print(analyzer.last_dividend())
        except Exception as e:
            print(e)

    def run(self):
        wait(
            [
                self.pool_executor.submit(self.__fetch_item, stock)
                for stock in self.__get_wallet()
            ]
        )

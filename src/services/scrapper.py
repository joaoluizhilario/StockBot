import requests
import lxml.html as lh
from abc import abstractclassmethod
from typing import List
from src.models import StockData, DividendData


class Scrapper:
    def __init__(self):
        self.price_xpath = None
        self.name_xpath = None
        self.ticker_xpath = None
        self.dividends_table_xpath = None
        self.url = None

    @abstractclassmethod
    def _build_url_to_scrap(self, ticker: str, type: str) -> str:
        raise Exception("Must implement url builder")

    def scrap(self, ticker: str, type: str) -> StockData:
        try:
            document = self.__fetch_document_data(ticker, type)
            return self.__extract_stock_data_from_document(document)
        except Exception as e:
            print(e)
        return None

    def __fetch_document_data(self, ticker: str, type: str):
        req = requests.get(self._build_url_to_scrap(ticker, type))
        return lh.fromstring(req.content)

    def __extract_stock_data_from_document(self, document) -> StockData:
        return StockData(
            ticker=self.__extract_ticker_code(document),
            name=self.__extract_stock_name(document),
            price_text=self.__extract_price_as_text(document),
            price=self.__extact_price_as_number(document),
            dividends=self.__extract_stock_dividends(document),
        )

    def __extract_price_as_text(self, document) -> str:
        return document.xpath(self.price_xpath)[0].text_content()

    def __extact_price_as_number(self, document) -> float:
        return float(self.__extract_price_as_text(document).replace(",", "."))

    def __extract_stock_name(self, document) -> str:
        return document.xpath(self.name_xpath)[0].text_content()

    def __extract_ticker_code(self, document) -> str:
        return document.xpath(self.ticker_xpath)[0].text_content()

    def __extract_stock_dividends(self, document) -> List[DividendData]:
        data = []
        for tr in document.xpath(self.dividends_table_xpath):
            tds = tr.xpath("td")
            data.append(
                DividendData(
                    type=tds[0].text_content(),
                    date_in=tds[1].text_content(),
                    date_cash=tds[2].text_content(),
                    value=tds[3].text_content(),
                )
            )
        return data

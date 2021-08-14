from .scrapper import Scrapper


class StatusInvestScrapper(Scrapper):
    def __init__(self):
        self.price_xpath = (
            '//*[@id="main-2"]/div[2]/div/div[1]/div/div[1]/div/div[1]/strong'
        )
        self.name_xpath = '//*[@id="main-header"]/div/div/div[1]/h1/small'
        self.ticker_xpath = '//*[@id="main-2"]/div[1]/div/div/ul/li[1]/a'
        self.dividends_table_xpath = (
            '//*[@id="earning-section"]/div[6]/div/div[2]/table/tbody/tr'
        )
        self.base_url = "https://statusinvest.com.br/"

    def _build_url_to_scrap(self, ticker: str, type: str) -> str:
        area = "acoes" if type == "STOCK" else "fundos-imobiliarios"
        return self.base_url + area + "/" + ticker

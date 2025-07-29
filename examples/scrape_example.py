from webscraper.fetcher import Fetcher
from webscraper.parser import Parser
from webscraper.exporter import Exporter
from webscraper.scraper import ScraperEngine

urls = [
    "https://quotes.toscrape.com/page/1/",
    "https://quotes.toscrape.com/page/2/"
]

rules = {
    "quote": ".quote span.text",
    "author": ".quote small.author"
}

fetcher = Fetcher(delay=2)
parser = Parser(rules)
exporter = Exporter("quotes.csv")

engine = ScraperEngine(fetcher, parser, exporter)
engine.scrape(urls)
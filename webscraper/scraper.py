class ScraperEngine:
    def __init__(self, fetcher, parser, exporter):
        self.fetcher = fetcher
        self.parser = parser
        self.exporter = exporter

    def scrape(self, urls):
        for url in urls:
            print(f"Scraping {url}...")
            html = self.fetcher.fetch(url)
            if html:
                data = self.parser.parse(html)
                self.exporter.save(data)
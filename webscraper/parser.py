from bs4 import BeautifulSoup

class Parser:
    def __init__(self, rules):
        self.rules = rules  # dict of field: css_selector

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        data = {}
        for key, selector in self.rules.items():
            element = soup.select_one(selector)
            data[key] = element.get_text(strip=True) if element else None
        return data
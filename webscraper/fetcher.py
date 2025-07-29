import requests
import time

class Fetcher:
    def __init__(self, headers=None, delay=1):
        self.headers = headers or {"User-Agent": "Mozilla/5.0"}
        self.delay = delay

    def fetch(self, url):
        time.sleep(self.delay)
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
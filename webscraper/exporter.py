import csv

class Exporter:
    def __init__(self, filename="output.csv"):
        self.filename = filename
        self.file = open(filename, "w", newline="", encoding="utf-8")
        self.writer = None

    def save(self, data):
        if not data:
            return
        if self.writer is None:
            self.writer = csv.DictWriter(self.file, fieldnames=data.keys())
            self.writer.writeheader()
        self.writer.writerow(data)

    def __del__(self):
        self.file.close()
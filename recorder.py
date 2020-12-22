"""Record data."""

import csv
import os


class Recorder:
    def __init__(self):
        pass

    def record_data_in_csv_file(self, data):
        with open(
            data["category"] + ".csv", "a", encoding="utf8", newline=""
        ) as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys(), delimiter=";")
            if os.stat(data["category"] + ".csv").st_size == 0:
                writer.writeheader()
            writer.writerow(data)

    def record_data_from_list_in_csv(self, data_list):
        for book in data_list:
            self.record_data_in_csv_file(book)
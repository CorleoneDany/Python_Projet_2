"""Record data."""

import csv
import os
import requests


class Recorder:
    def __init__(self):
        pass

    def record_data_in_csv_file(self, data):
        """Record data from cleaner in a CSV."""
        path_csv = "./CSV/"
        path_image = "./IMG/"
        os.makedirs(path_csv, exist_ok=True)
        os.makedirs(path_image, exist_ok=True)

        filepath_CSV = f"{path_csv}{data['category']}.csv"
        filepath_IMG = f"{path_image}{data['title']}.png"

        with open(filepath_CSV, "a", encoding="utf8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys(), delimiter=";")
            if os.stat(filepath_CSV).st_size == 0:
                writer.writeheader()
            writer.writerow(data)

        image = requests.get(
            "https://books.toscrape.com/media/cache/" + data["image_url"]
        )
        file = open(filepath_IMG, "wb")
        file.write(image.content)
        file.close()

    def record_data_from_list_in_csv(self, data_list):
        """Record data from a list from cleaner."""
        for book in data_list:
            self.record_data_in_csv_file(book)

import csv

class Recorder:
    def __init__(self):
        pass

    def record(self, collector):
        csv_columns = collector.data.keys()
        with open(collector.data["Category"] + ".csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=';')
            writer.writeheader()
            writer.writerow(collector.data)
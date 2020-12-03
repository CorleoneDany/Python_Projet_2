import csv

class Recorder:
    def __init__(self):
        pass

    def record(self, data):
            csv_columns = data.keys()
            with open(data["category"] + ".csv", 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=';')
                writer.writeheader()
                writer.writerow(data)
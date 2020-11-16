import re

class Cleaner:
    def __init__(self):
        pass

    def clean(self, collector):
        collector.donnees["Link"] = collector.donnees["Link"].strip("https://books.toscrape.com/catalogue/")
        collector.donnees["Availability"] = collector.donnees["Availability"].strip("In stock (").strip(" available)")
        collector.donnees["Price_b_tax"] = collector.donnees["Price_b_tax"].strip("Â£")
        collector.donnees["Price_a_tax"] = collector.donnees["Price_a_tax"].strip("Â£")
        collector.donnees["Tax"] = collector.donnees["Tax"].strip("Â£")
        collector.donnees["Image_URL"] = collector.donnees["Image_URL"].strip("../")
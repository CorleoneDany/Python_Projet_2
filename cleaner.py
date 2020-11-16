class Cleaner:
    def __init__(self):
        pass

    def clean(self, collector):
        collector.data["Link"] = collector.data["Link"].strip("https://books.toscrape.com/catalogue/")
        collector.data["Category"] = collector.data["Category"].strip("\n")
        collector.data["Availability"] = collector.data["Availability"].strip("In stock (").strip(" available)")
        collector.data["Price_b_tax"] = collector.data["Price_b_tax"].strip("Â£")
        collector.data["Price_a_tax"] = collector.data["Price_a_tax"].strip("Â£")
        collector.data["Tax"] = collector.data["Tax"].strip("Â£")
        collector.data["Image_URL"] = collector.data["Image_URL"].strip("../")
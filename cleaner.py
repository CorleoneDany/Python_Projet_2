class Cleaner:
    def __init__(self):
        pass

    def clean(self, data):
        data["Link"] = data["Link"].replace("https://books.toscrape.com/catalogue/", "")
        data["Category"] = data["Category"].strip("\n")
        data["Availability"] = data["Availability"].strip("In stock (").strip(" available)")
        data["Price_b_tax"] = data["Price_b_tax"].strip("£")
        data["Price_a_tax"] = data["Price_a_tax"].strip("£")
        data["Tax"] = data["Tax"].strip("£")
        data["Image_URL"] = data["Image_URL"].replace("../../media/cache/", "")
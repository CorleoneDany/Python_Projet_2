"""Clean data from other classes."""


class Cleaner:
    def __init__(self):
        pass

    def clean_data_from_book(self, data):
        data["link"] = data["link"].replace("https://books.toscrape.com/catalogue/", "")
        data["category"] = data["category"].strip("\n")
        data["availability"] = (
            data["availability"].strip("In stock (").strip(" available)")
        )
        data["price_before_tax"] = data["price_before_tax"].strip("£")
        data["price_after_tax"] = data["price_after_tax"].strip("£")
        data["tax"] = data["tax"].strip("£")
        data["image_url"] = data["image_url"].replace("../../media/cache/", "")

        return data

    def clean_data_from_list_of_books(self, data_list):
        for data in range(len(data_list)):
            data_list[data] = self.clean_data_from_book(data_list[data])

    def clean_url_list(self, url_list):
        path = "https://books.toscrape.com/catalogue"
        for urls in range(len(url_list)):
            url_list[urls] = url_list[urls].replace("../../..", path)
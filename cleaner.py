class Cleaner:
    def __init__(self):
        pass

    def clean_data_from_book(self, data):
        data["link"] = data["link"].replace("https://books.toscrape.com/catalogue/", "")
        data["category"] = data["category"].strip("\n")
        data["availability"] = data["availability"].strip("In stock (").strip(" available)")
        data["price_before_tax"] = data["price_before_tax"].strip("£")
        data["price_after_tax"] = data["price_after_tax"].strip("£")
        data["tax"] = data["tax"].strip("£")
        data["image_url"] = data["image_url"].replace("../../media/cache/", "")

    def clean_data_from_list_of_books(self):
        pass

    def clean_url_list(self, url_list):
        path = "https://books.toscrape.com/catalogue"
        i = 0
        for urls in url_list:
            url_list[i] = url_list[i].replace("../../..", path)
            i+=1
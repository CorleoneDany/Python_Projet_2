from collector import Collector
from cleaner import Cleaner
from website import Website
from recorder import Recorder
import pprint as pp

class Application:
    def __init__(self):
        self.website = Website()
        self.collector = Collector()
        self.cleaner = Cleaner()
        self.recorder = Recorder()

    def get_book(self):
        self.website.request_book_html("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
        self.collector.collect_book_data(self.website.url, self.website.content)
        self.cleaner.clean_data_from_book(self.collector.data)
        self.recorder.record(self.collector.data)

    def get_category(self):
        self.website.request_category_urls("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
        self.cleaner.clean_url_list(self.website.url_list)
        self.website.request_category_html(self.website.content_list)

        pp.pprint(self.website.content_list)



if __name__ == "__main__":

    application = Application()

    #application.get_book()
    application.get_category()
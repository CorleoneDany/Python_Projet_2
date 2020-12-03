import subprocess
import sys
from bs4 import BeautifulSoup

class Collector:
    def __init__(self):
        self.data = {
            "link" : "",
            "title" : "",
            "note" : 0,
            "upc" : "",
            "type" : "",
            "price_before_tax" : "",
            "price_after_tax" : "",
            "tax" : "",
            "availability" : 0,
            "review_count" : 0,
            "image_url" : "",
            "category" : "",
            "description" :"" 
        }

    def collect_book_data(self, url, content): 
        information_table = content.find("table", {"class":"table table-striped"})
        description = content.find("article", {"class":"product_page"}).find("p", recursive=False).text
        category = content.find("ul", {"class":"breadcrumb"}).findAll("li")[2].text
        image_link = content.find("img")["src"]
        star_numbers = content.find("p", {"class":"star-rating"})["class"][1]
        td_list = information_table.findAll("td")

        self.data["title"] = content.find("h1").text
        self.data["link"] = url
        self.data["upc"] = td_list[0].text
        self.data["type"] = td_list[1].text
        self.data["price_before_tax"] = td_list[2].text
        self.data["price_after_tax"] = td_list[3].text
        self.data["tax"] = td_list[4].text
        self.data["availability"] = td_list[5].text
        self.data["review_Count"] = td_list[6].content
        self.data["description"] = description
        self.data["category"] = category
        self.data["note"] = star_numbers
        self.data["image_url"] = image_link

    def collect_data_from_list_of_books(self, content_list):
        # Collecte les données des livres d'une liste de contenu html
        pass
import subprocess
import sys
from bs4 import BeautifulSoup

class Collector:
    def __init__(self):
        self.data = {
            "Link" : "",
            "Title" : "",
            "Note" : 0,
            "UPC" : "",
            "Type" : "",
            "Price_b_tax" : "",
            "Price_a_tax" : "",
            "Tax" : "",
            "Availability" : 0,
            "Review_count" : 0,
            "Image_URL" : "",
            "Category" : "",
            "Description" :"" 
        }

    def collect(self, website):
        soup = BeautifulSoup(website.content, features="html.parser")
        information_table = soup.find("table", {"class":"table table-striped"})
        description = soup.find("article", {"class":"product_page"}).find("p", recursive=False).text
        category = soup.find("ul", {"class":"breadcrumb"}).findAll("li")[2].text
        image = soup.find("img")
        star_numbers = soup.find("p", {"class":"star-rating"})["class"][1]
        td_list = information_table.findAll("td")

        self.data["Title"] = soup.find("h1").text
        self.data["Link"] = website.url
        self.data["UPC"] = td_list[0].text
        self.data["Type"] = td_list[1].text
        self.data["Price_b_tax"] = td_list[2].text
        self.data["Price_a_tax"] = td_list[3].text
        self.data["Tax"] = td_list[4].text
        self.data["Availability"] = td_list[5].text
        self.data["Review_Count"] = td_list[6].content
        self.data["Description"] = description
        self.data["Category"] = category
        self.data["Note"] = star_numbers
        self.data["Image_URL"] = image["src"]
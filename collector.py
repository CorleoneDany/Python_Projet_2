import subprocess
import sys
from bs4 import BeautifulSoup

class Collector:
    def __init__(self):
        self.donnees = {
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
            "Category" : ""
        }

    def Collect(self, website):
        # i = 0
        # n = 4
        soup = BeautifulSoup(website.content, features="html.parser")
        information_table = soup.find("table", {"class":"table table-striped"})
        image = soup.find("img")
        star_numbers = soup.findAll("i", {"class":"icon-star"}, {"color" : "#E6CE31"}) #faux, à corriger
        for stars in star_numbers:
            self.donnees["Note"] +=1
        td_list = information_table.findAll("td")
        # for td in td_list:
        #     self.donnees.values()[n] = td_list[i].text
        #     i = i+1
        #     n = x+1

        self.donnees["Title"] = soup.find("h1").text
        self.donnees["Link"] = website.url
        self.donnees["UPC"] = td_list[0].text
        self.donnees["Type"] = td_list[1].text
        self.donnees["Price_b_tax"] = td_list[2].text
        self.donnees["Price_a_tax"] = td_list[3].text
        self.donnees["Tax"] = td_list[4].text
        self.donnees["Availability"] = td_list[5].text
        self.donnees["Review_Count"] = td_list[6].content
        self.donnees["Image_URL"] = image["src"] #chemin relatif, ok ? a voir pour la fonction d'enregistrement d'image plus tard 

        # print(self.donnees)
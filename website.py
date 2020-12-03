import subprocess
import sys
import requests
from bs4 import BeautifulSoup

class Website:
    def __init__(self):
        self.url = ""
        self.content = ""
        self.url_list = []
        self.content_list = []

    def request_book_html(self, url):
        self.url = url
        # Renvoie le contenu html d'un livre à partir d'une url
        print("Tentative de connection à l'url books.toscrape.com")
        response = requests.get(self.url)
        if response.ok:
            print("Connection ok")
            print("La requête à retourné des informations : ")
            response.encoding = "utf-8"
            self.content = BeautifulSoup(response.text, features="html.parser")
            return(self.content)
        else:
            print("La requête à retourné une erreur : ")
            print(requests.status_codes)

    def request_category_urls(self, url):
        # Renvoie une liste d'url composé de toutes les urls des livres d'une catégorie
        self.url = url
        print("Tentative de connection à l'url books.toscrape.com")
        response = requests.get(self.url)
        if response.ok:
            print("Connection ok")
            print("La requête à retourné des informations : ")
            response.encoding = "utf-8"
            self.content = BeautifulSoup(response.text, features="html.parser")
            self.url_list = self.content.findAll("div", {"class" : "image_container"})
            i = 0
            for div in self.url_list:
                self.url_list[i] = self.url_list[i].find("a")["href"]
                i+=1

        else:
            print("La requête à retourné une erreur : ")
            print(requests.status_codes)

    def request_category_html(self, url_list):
        # Renvoie le html de tous les livres d'une catégorie
        i = 0
        for urls in self.url_list:
            self.content_list.append(self.request_book_html(self.url_list[i]))
            i+=1

    def request_all_books(self):
        pass
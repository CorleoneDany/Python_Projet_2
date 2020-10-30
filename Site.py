import subprocess
import sys
import requests

class Site:
    def __init__(self):
        self.page_number = "1"
        self.url = "http://books.toscrape.com/catalogue/category/books_" + self.page_number + "/index.html"    

    def requestWebsite(self):
        print("Tentative de connection à l'url books.toscrape.com")
        response = requests.get(self.url)
        if response.ok:
            print("La requête à retourné des informations : ")
            print(response.text)
        else:
            print("La requête à retourné une erreur : ")
            print(requests.status_codes)
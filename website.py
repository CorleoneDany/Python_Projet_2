import subprocess
import sys
import requests

class Website:
    def __init__(self):
        page_number = "1"
        self.url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"  
        self.content = ""

    def request_Website(self):
        print("Tentative de connection à l'url books.toscrape.com")
        response = requests.get(self.url)
        if response.ok:
            print("Connection ok")
            print("La requête à retourné des informations : ")
            response.encoding = "utf-8"
            self.content = response.text
        else:
            print("La requête à retourné une erreur : ")
            print(requests.status_codes)
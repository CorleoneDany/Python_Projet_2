"""Collect urls and html."""

import requests
from bs4 import BeautifulSoup


class Website:
    def __init__(self):
        self.url = ""
        self.content = ""
        self.url_list = []
        self.content_list = []

    def request_book_html(self, url):
        """Renvoie le contenu html d'un livre à partir d'une url."""
        self.url = url
        print("Tentative de connection à l'url books.toscrape.com")
        response = requests.get(self.url)
        if response.ok:
            print("Connection ok")
            print("La requête à retourné des informations : ")
            response.encoding = "utf-8"
            self.content = BeautifulSoup(response.text, features="html.parser")

            return self.content
        else:
            print("La requête à retourné une erreur : ")
            print(requests.status_codes)

    def request_category_urls(self, url):
        """Renvoie une liste d'url composé de toutes les urls d'une catégorie."""
        self.url = url
        response = requests.get(self.url)
        if response.ok:
            response.encoding = "utf-8"
            self.content = BeautifulSoup(response.text, features="html.parser")
            self.retrieve_urls_from_content(self.content)
            try:
                next_page_html = requests.get(self.load_next_page_url(self.content))
                next_page_html.encoding = "utf-8"
                next_page_content = BeautifulSoup(
                next_page_html.text, features="html.parser"
            )
                self.retrieve_urls_from_content(next_page_content)

                while self.has_next_page(next_page_content):
                    self.retrieve_urls_from_content(next_page_content)
                    next_page_html = requests.get(
                    self.load_next_page_url(next_page_content)
                )
                    next_page_content.encoding = "utf-8"
                    next_page_content = BeautifulSoup(
                    next_page_html.text, features="html.parser"
                )

            except AttributeError:
                pass
                
        else:
            print("La requête à retourné une erreur : ")
            print(requests.status_codes)

    def retrieve_urls_from_content(self, content):
        """Extrait les urls d'une page."""
        current_page_url_list = content.findAll("div", {"class": "image_container"})
        for urls in range(len(current_page_url_list)):
            current_page_url_list[urls] = current_page_url_list[urls].find("a")["href"]
        self.url_list.extend(current_page_url_list)

    def load_next_page_url(self, content):
        """Charge l'url de la page suivante s'il y en a une."""
        if self.has_next_page(content):
            next_page_number = content.find("li", {"class": "next"}).find("a")["href"]
            next_page_url = self.url.replace("index.html", next_page_number)
            return next_page_url

    def has_next_page(self, content):
        """Vérifie s'il existe une page suivante."""
        try:
            content.find("li", {"class": "next"}).find("a")["href"]
            return True
        except AttributeError:
            return False

    def request_category_html(self, url_list):
        """Renvoie le html de tous les livres d'une catégorie."""
        for urls in self.url_list:
            self.content_list.append(self.request_book_html(urls))

    def request_all_books_url(self):
        domain = "https://books.toscrape.com/"
        main_page_html = requests.get("https://books.toscrape.com/index.html")
        main_page_html.encoding = "utf-8"
        soup = BeautifulSoup(main_page_html.text, features="html.parser")
        url_category_list = soup.find("ul", {"class" : "nav nav-list"}).find("ul").findAll("li")
        for category in range(len(url_category_list)):
            url_category_list[category] = url_category_list[category].find("a")["href"]
            url_category_list[category] = domain + url_category_list[category]
            self.request_category_urls(url_category_list[category])
            self.request_category_html(url_category_list[category])
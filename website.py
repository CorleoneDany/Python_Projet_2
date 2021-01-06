"""Collect urls and html."""

import requests
from requests.exceptions import MissingSchema
from bs4 import BeautifulSoup


class Website:
    """Collect urls and html."""

    def __init__(self):
        """Init class with attributes."""
        self.url = ""
        self.content = ""
        self.url_list = []
        self.content_list = []

    def request_book_content(self, url):
        """Return content of a page from an url."""
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

            # Lors d'un input / output toujours faire un try except

    def request_category_urls(self, url):
        """Return all the books's urls from a category."""
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

            except MissingSchema:
                pass

        else:
            print("La requête à retourné une erreur : ")
            print(requests.status_codes)

    def retrieve_urls_from_content(self, content):
        """Extract urls from a list of content."""
        current_page_url_list = content.findAll("div", {"class": "image_container"})
        for urls in range(len(current_page_url_list)):
            current_page_url_list[urls] = current_page_url_list[urls].find("a")["href"]
        self.url_list.extend(current_page_url_list)

    def load_next_page_url(self, content):
        """Extract url from next page if there is one"""
        if self.has_next_page(content):
            next_page_number = content.find("li", {"class": "next"}).find("a")["href"]
            next_page_url = self.url.replace("index.html", next_page_number)
            return next_page_url

    def has_next_page(self, content):
        """Verify if the page has a next one."""
        try:
            content.find("li", {"class": "next"}).find("a")["href"]
            return True
        except AttributeError:
            return False

    def request_category_content(self, url_list):
        """Return content of all books in a category."""
        for urls in self.url_list:
            self.content_list.append(self.request_book_content(urls))

    def request_all_categories_url(self):
        """Return the urls of all categories from the index."""
        domain = "https://books.toscrape.com/"
        main_page_html = requests.get("https://books.toscrape.com/index.html")
        main_page_html.encoding = "utf-8"
        soup = BeautifulSoup(main_page_html.text, features="html.parser")
        url_category_list = (
            soup.find("ul", {"class": "nav nav-list"}).find("ul").findAll("li")
        )
        for category in range(len(url_category_list)):
            url_category_list[category] = url_category_list[category].find("a")["href"]
            url_category_list[category] = domain + url_category_list[category]
        return url_category_list

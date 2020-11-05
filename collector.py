import subprocess
import sys
from bs4 import BeautifulSoup

class Collector:
    def __init__(self):
        self.titre = ""
        self.information = ""
        self.information_table = ""

    def Collect(self, website):
        i = 0
        soup = BeautifulSoup(website.content, features="html.parser")
        self.titre = soup.find("h1").text
        print(self.titre)
        self.information_table = soup.find("table", {"class":"table table-striped"})
        self.td_list = self.information_table.findAll("td")
        for td in self.td_list:
            self.information = self.td_list[i].text
            print(self.information)
            i = i+1
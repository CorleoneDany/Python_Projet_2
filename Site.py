import subprocess
import sys
try:
    import requests
    print("Python imported requests successfully")
except ImportError:
    print("Python could'nt import requests successfully, it is gonna be installed")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    print("Requests was installed successfully")
    import requests
    print("Python imported requests successfully")

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
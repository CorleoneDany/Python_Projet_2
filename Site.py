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

url ="http://books.toscrape.com/catalogue/category/books_1/index.html"
print("Tentative de connection à l'url books.toscrape.com")
response = requests.get(url)

if response.ok:
    print("La requête à retourné des informations : ")
    print(response.headers)
else:
    print("La requête à retourné une erreur")
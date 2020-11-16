from collector import Collector
from cleaner import Cleaner
from website import Website
from recorder import Recorder
import pprint as pp

#def main(): 
#initialiser classes et utiliser methodes dans un bloc chacun
website = Website()

website.request_Website()

collector = Collector()

collector.collect(website) #prendre que le website.content et website.url seulement

cleaner = Cleaner()

cleaner.clean(collector) #prendre le collector.data seulement

pp.pprint(collector.donnees)

#renommer la classe en main.py if __name__ == "__main__":
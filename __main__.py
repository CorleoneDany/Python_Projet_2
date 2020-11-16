from collector import Collector
from cleaner import Cleaner
from website import Website
from recorder import Recorder
import pprint as pp

class Application:
    def main(self):
        if __name__ == "__main__":
            website = Website()
            collector = Collector()
            cleaner = Cleaner()

            website.request_Website()
            collector.collect(website) #prendre que le website.content et website.url seulement
            cleaner.clean(collector) #prendre le collector.data seulement

            pp.pprint(collector.data)

application = Application()

application.main()
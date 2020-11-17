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
            recorder = Recorder()

            website.request_Website()
            collector.collect(website.url, website.content) 
            cleaner.clean(collector.data) 
            recorder.record(collector.data) 

            pp.pprint(collector.data)

application = Application()

application.main()
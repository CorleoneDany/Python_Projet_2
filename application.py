from collector import Collector
from cleaner import Cleaner
from website import Website
from recorder import Recorder
import pprint as pp

website = Website()

website.requestWebsite()

collector = Collector()

collector.Collect(website)

cleaner = Cleaner()

cleaner.clean(collector)

pp.pprint(collector.donnees)
from collector import Collector
from cleaner import Cleaner
from website import Website
from recorder import Recorder

website = Website()

website.requestWebsite()

collector = Collector()

collector.Collect(website)
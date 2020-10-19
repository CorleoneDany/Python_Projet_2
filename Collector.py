import subprocess
import sys
try:
    from bs4 import BeautifulSoup
except ImportError:
    subprocess.check_call([sys.executable, "pip", "install", "bs4"])
    from bs4 import BeautifulSoup


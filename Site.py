import subprocess
import sys
try:
    import requests
    print("Python imported requests successfully")
except ImportError:
    print("Python could'nt import requests successfully, it is gonna be installed")
    subprocess.check_call([sys.executable, "pip", "install", "requests"])
    print("Requests was installed successfully")
    import requests
    print("Python imported requests successfully")

url =""
response = requests.get(url)

if response.ok:
    print(response)
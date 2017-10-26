import googlemaps
import requests
import json
from bs4 import BeautifulSoup
from bin import Bin

url1 = "http://www.diabetes.ca/dropBoxes/phpsqlsearch_genxml.php?&lat=49.2057&lng=-122.9110&radius=50"
r1 = requests.get(url1)

soup1  = BeautifulSoup(r1.content,"lxml")

filtered = soup1.find_all("marker",{"type":"Drop Box"})

for item in filtered:
    print(item['address'])

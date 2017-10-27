import googlemaps
import requests
import json
from bs4 import BeautifulSoup
from bin import Bin

#url1 = "http://www.diabetes.ca/dropBoxes/phpsqlsearch_genxml.php?&lat=49.2057&lng=-122.9110&radius=50"
#r1 = requests.get(url1)

#soup1  = BeautifulSoup(r1.content,"lxml")

#filtered = soup1.find_all("marker",{"type":"Drop Box"})

#for item in filtered:
#    print(item['address'])

#Big Brothers
url2 = "https://www.bigbrothersvancouver.com/clothing-donation/donation-bins/"
r2 = requests.get(url2)

soup2  = BeautifulSoup(r2.content,"lxml")

filtered2 = soup2.find_all("span")

print(filtered2)

#for item in filtered2:
#   print(item['address'])

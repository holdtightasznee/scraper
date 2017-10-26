#this file contains all the functions concerned with scraping
#html table sites
#google map sites
#get data
#misc scraper

import googlemaps
import requests
import json
from bs4 import BeautifulSoup
from bin import Bin


googleApiKey = "AIzaSyCr90UZMD3fl6SLE7cHIDvWF4yofQdWIgk"
gmaps = googlemaps.Client(key=googleApiKey)


#Salvation Army Thrift Store
url1 = "https://www.thriftstore.ca/british-columbia/drop-bin-locations"
r1 = requests.get(url1)

soup1 = BeautifulSoup(r1.content,"lxml")
filtered1 = soup1.find_all("tr")

list = []

for td in filtered1:
	inter = td.find_all("span")
	count = 0
	addBin = Bin("", "", "", "", "", "")
	while (count <= 3):
		value = inter[count].text.strip()
		if(count == 0):
			addBin.name = value
		elif (count == 1):
			addBin.company = value
		elif (count == 2):
			addBin.address = value
		else:
			addBin.city = value
		count += 1
	list.append(addBin)



#Inclusion BC & CPABC Clothing
url2 = "http://www.google.com/maps/d/kml?mid=1kqVfqYiPtnqrO8L5zC_yVkAiwB0&forcekml=1"
url3 = "https://www.google.com/maps/d/kml?mid=1ekVOoKgoAW2vIjiDh3DmP4OU04g&forcekml=1"
r2 = requests.get(url2)
r3 = requests.get(url3)

soup2 = BeautifulSoup(r2.content,"lxml")
soup3 = BeautifulSoup(r3.content,"lxml")

filtered2 = soup2.find_all("placemark")
filtered3 = soup3.find_all("placemark")

for item in filtered2:
	addBin = Bin("", "", "", "", "", "")
	addBin.address = item.find_all("name")[0].text.strip()
	addBin.coordinate = item.find_all("coordinates")[0].text.strip()
	list.append(addBin)

for item in filtered2:
	addBin = Bin("", "", "", "", "", "")
	addBin.address = item.find_all("name")[0].text.strip()
	addBin.coordinate = item.find_all("coordinates")[0].text.strip()
	list.append(addBin)


for item in list:
	if item.address:
		list.remove(item)



#Diabetes Canada
url1 = "http://www.diabetes.ca/dropBoxes/phpsqlsearch_genxml.php?&lat=49.2057&lng=-122.9110&radius=50"
r1 = requests.get(url1)

soup1  = BeautifulSoup(r1.content,"lxml")

filtered = soup1.find_all("marker",{"type":"Drop Box"})

for item in filtered:
    print(item['address'])



#geoencoding
for item in list:
	if item.getCoordinate():
		coordinateRaw = item.getCoordinate()
		print(coordinateRaw)
		coordinate = coordinateRaw.split(",")
		reverse_geocode_result = gmaps.reverse_geocode((coordinate[1],coordinate[0]))
		print(reverse_geocode_result[0]['formatted_address'])


	elif item.getAddress():
		address = item.getAddress()
		geocode_result = gmaps.geocode(address)
		item.coordinate = reverse_geocode_result[0]['geometry']['location']
		print(geocode_result[0]['formatted_address'])


#print all bin objects
for item in list:
	print("-----------------------")
	print(item)
	print("-----------------------")

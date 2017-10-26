import requests
import json
from bs4 import BeautifulSoup

url1 = "https://www.thriftstore.ca/british-columbia/drop-bin-locations"
r1 = requests.get(url1)

soup1 = BeautifulSoup(r1.content,"lxml")
soup1.prettify();

filtered1 = soup1.find_all("tr")


'''prints out all the addresses stored
in the table on URL1'''

for sub1 in filtered1:
    inter = sub1.find_all("span")
    for sub2 in inter:
        if(len(sub2.text)>2):
            print(sub2.text)
    print("------------")

class Bin:
    __company = ""
    __address = ""
    __city = ""
    __postalCode = ""
    __longitude = ""
    __latitude = ""
    __name =""
        __type = ""

    def __init__(self, company, address, city, postalCode, longitude, latitude, name):
        self.company = company
        self.address = address
        self.city = city
        self.postalCode = postalCode
        self.longitude = longitude
        self.name = name
        def getCompany()
            return self.company

        def getAddress()
            return self.address

        def getCity()
            return self.city

        def getPostalCode()
            return self.postalcode

        def getLongitude()
            return self.longitude

        def getLatitude()
            return self.latitude

        def getName()
            return self.name

        def getType()
            return self.type

        def toString()
            return self.company + "is at" + self.address + ", " + self.city
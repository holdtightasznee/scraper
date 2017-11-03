import googlemaps
import requests
import json
from bs4 import BeautifulSoup
from bin import Bin
from bs4 import UnicodeDammit
from contextlib import closing
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time


#Big Brothers
'''
url = "https://www.bigbrothersvancouver.com/clothing-donation/donation-bins/"
browser = webdriver.PhantomJS()
browser.get(url)
time.sleep(1)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
filtered1 = soup.find_all("span", {"class":"slp_result_address"})
for item in filtered1:
	print(item)
browser.close()'''


url = "http://www.develop.bc.ca/donate/"
browser = webdriver.PhantomJS()
browser.get(url)
time.sleep(1)
html = browser.page_source
#r = urllib2.urlopen("http://www.bcchauxiliary.com/our-businesses/clothing-donation-bin-program/")
#html = r.read()

gmaps = googlemaps.Client(key="AIzaSyDqGPoS9GUio0FZndRTdnvNDFIatMHGeus")

soup = BeautifulSoup(html, "lxml")
individual_results = soup.find_all("div", {"class":"results_wrapper"})

for result in individual_results:
   address = ""
   address_components = result.find_all("span", {"class":"slp_result_address"})
   for address_component in address_components:
       address += address_component.get_text()
       if('slp_result_citystatezip' in address_component.get("class")):
           address += ", "
   print(address)

browser.close()
#!/usr/bin/env python3

import requests
import os
import sys 
from bs4 import BeautifulSoup


BASE_URL = 'http://www.zi-han.net/theme/hplus/'

BASE_PATH = BASE_URL.replace("http://", "")

CURRENT_PATH_LIST = BASE_PATH.split("/")

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

CURRENT_PATH_LEVEL = "{}/{}".format(CURRENT_PATH, "/".join(CURRENT_PATH_LIST))

dirs = ''
dir_split = ''
for dir in CURRENT_PATH_LEVEL.split('/')
	dirs += dir_split + dir
	if not os.path.isdir(dirs):
		os.makedir(dirs)
	dir_split = '/'
	
	
	
if not os.path.isdir(CURRENT_PATH_LEVEL):
	os.makedirs(CURRENT_PATH + '/' + '')

response = requests.get(BASE_URL)
response.encoding = 'UTF-8'  
soup = BeautifulSoup(response.text, "lxml")

aTags = soup.find_all(class_="J_menuItem")

for atag in aTags:
	if ".html" in atag['href']:
		print(atag['href'])
		
		
		
		
if __name__ == '__main__':
	main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:20:34 2018

@author: sarfraz
"""

import requests

#Set Headers for request to the website 
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

#URL from where the tables will be scraped
url='https://electionpakistan.com/constituency-profile/?assembly=5&election=2&constituency=1&assemblyName=National%20Assembly&electionType=General%20Election%202008&constituencyName=NA-1%20Peshawar-I'

#Fetch the page at the url using "requests" module
r = requests.get(url, headers=header)

#Print the response's text
print(r.text);
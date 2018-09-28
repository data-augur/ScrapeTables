#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:20:34 2018

@author: sarfraz
"""

import requests
import pandas as pd

#Set Headers for request to the website 
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

#URL from where the tables will be scraped
url='https://www.ecp.gov.pk/ResultDetails.aspx?EleId=10070&Election=General%20Election%2025%20Jul%202018'

#Fetch the page at the url using "requests" module
r = requests.get(url, headers=header)

#Read all tables in the response into a list of dataframes
dataframes=pd.read_html(r.text, header=0)

#Iterate through the data frames to access each table
for dataframe in dataframes:
    print(dataframe)
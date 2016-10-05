# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:01:04 2016

@author: jayson
"""

import urllib.request
import csv
			
url='https://raw.githubusercontent.com/opower/implementation-engineering-hw/master/src/main/resources/aSkDddKs.csv'
page=urllib.request.urlopen(url)
csv=csv.reader(page.read().decode('ISO-8859-1').splitlines())
row_count=sum(1 for row in csv)
print (row_count)

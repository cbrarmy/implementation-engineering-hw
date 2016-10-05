# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:03:31 2016

@author: jayson
"""

import urllib.request

testfile=urllib.request.urlretrieve('http://www.google-analytics.com/ga.js','ga_local.js')

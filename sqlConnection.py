# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:34:31 2016

@author: jayson
"""

import pypyodbc

connection = pypyodbc.connect('Driver={SQL Server};''server=localhost;''database=mytestdb;''uid=****;pwd=****')
cursor = connection.cursor() 
SQLCommand = ("")

cursor.execute(SQLCommand)
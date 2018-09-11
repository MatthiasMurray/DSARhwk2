#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 14:01:26 2018

@author: Matthias
"""
#this imports the csv package so that csv-related commands may be used
import csv

#the variable name csvout is assigned to the open, writable file instantiated here as 'out'
csvout = open('out', 'w')
#the variable name recordwriter is assigned to a copy of csvout that can be written to in python. 
recordwriter = csv.writer(csvout, dialect='unix', quoting=csv.QUOTE_MINIMAL)

#'1 LAYOUT B CSV.csv' is opened and assigned to the local variable name csvfile
with open('1 LAYOUT B CSV.csv') as csvfile:
    recordreader = csv.reader(csvfile, dialect='unix')
    row = []
    for line in recordreader:
        #print(line)
        row.extend(line)
        if line[0][:12]=='RELEASE DATE':
            #print(line)
            recordwriter.writerow(row)
            row = []

print(list(recordreader))
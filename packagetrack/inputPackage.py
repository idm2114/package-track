#!/usr/bin/env python

import pandas as pd
import numpy as np
import csv
import os 
import re

trackinglist = []
path = "/Users/ian/.package-track/bin/"
files = os.listdir(path)
for file in files:
    if file.endswith(".txt"):
        filename = file.split(".")[0]
        regex = ["^(94)[0-9]{20}$", "^(92)[0-9]{20}$", "^[0-9]{20}$", "^(1Z)[0-9A-Z]{16}$", 
            "^[0-9]{9}$", "^[0-9]{26}$", "^[0-9]{15}$", "^[0-9]{12}$", "^[0-9]{22}$",
            "^(EC)[0-9]{9}(US)$", "^[0-9]{10}$"]
        for expr in regex:     
            if re.match(expr, filename):
                trackinglist.append(filename)

''' checking existing tracking numbers ''' 

if (trackinglist):
    print("Here are the current packages that you have on the way: ")
    for file in trackinglist:
        print(file)

if not trackinglist:
    print("You have no current packages that are on the way.")

''' checking tracking numbers found from parsing emails ''' 

emailtrackinglist = []
try: 
    with open("/Users/ian/.package-track/bin/tracking_from_email.txt", "r") as fileHandle:
        for line in fileHandle:  
            current = line[:-1]  
            emailtrackinglist.append(current)
    if (emailtrackinglist):
        print("We found the following tracking numbers from your email: ")
        for number in emailtrackinglist:
            print(number)
        include = input("Would you like to add any of these tracking numbers to PackageTracker? [y / n] ")
        if (include == "y"):
            for number in emailtrackinglist:
                print(number)
                add = input("Add this tracking number? [y / n] ")
                if (add == "y"):
                    trackinglist.append(number)
except:
    """do nothing"""
    pass



more = False

new = input("Would you like to enter a tracking number? [y / n] ")
if (new == "y"):
    more = True

while (more):
    trackingNumber = input("Please input the tracking number of a package you want to track: ")
    trackinglist.append(trackingNumber)
    next = input("Would you like to enter another tracking number? [y / n] ")
    if (next == "n"):
       more = False

#writing list to txt file
with open ('/Users/ian/.package-track/bin/trackingnumbers.txt', 'w') as filehandle:
    for item in trackinglist:
        filehandle.write('%s\n' % item)


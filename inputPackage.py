import pandas as pd
import numpy as np
import csv
import os 


trackinglist = []
files = os.listdir(".")
for file in files:
    if file.endswith(".txt"):
        if file.startswith("trackingnumbers"):
            continue
        trackinglist.append(file)

if (trackinglist):
    print("Here are the current packages that you have on the way: ")
    for file in trackinglist:
        print(file)

if not trackinglist:
    print("You have no current packages that are on the way.")

more = True

while (more): 
    trackingNumber = input("Please input the tracking number of a package you want to track: ")
    trackinglist.append(trackingNumber)
    next = input("Would you like to enter another tracking number? [y / n] ")
    if (next == "n"):
       more = False

#writing list to txt file
with open ('trackingnumbers.txt', 'w') as filehandle:
    for item in trackinglist:
        filehandle.write('%s\n' % item)


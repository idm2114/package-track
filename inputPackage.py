import pandas as pd
import numpy as np
import csv

more = True

trackinglist = []
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


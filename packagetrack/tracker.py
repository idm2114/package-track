#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import os

trackinglist = []
finaltrackinglist = []
with open("~/.package-track/bin/trackingnumbers.txt", "r") as fileHandle:
    for line in fileHandle:
        current = line[:-1]
        trackinglist.append(current)

for number in trackinglist: 
    # creating boolean flag to track if package was delivered
    delivered = False
    
    #printing tracking number
    print(number)

    #selenium
    #runs in background 
    driver=webdriver
    try:
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        driver = webdriver.Firefox(firefox_options=fireFoxOptions)
    except:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get("https://www.packagetrackr.com")
    #print(driver.title)
    #importing tracking list from csv

    search = driver.find_element_by_name("n")
    search.send_keys(number)
    search.send_keys(Keys.ENTER)

    time.sleep(5)
    #waiting for new page to load
    results = driver.find_elements_by_class_name("media-body")
    for result in results:
    # trying to remove listed number if item was delivered
        if ("Delivered" in result.text):
            delivered = True
    # writing contents to new temp file
    with open ('~/.package-track/bin/tempfile.txt', 'w') as filehandle:
        for result in results:
            if ("WE KNOW WHERE YOUR STUFF IS." in result.text):
                continue
            filehandle.write('%s\n' % result.text)

    # comparing the results of old and new files if old file exists
    # returning difference to provide most accurate (recent) tracking info
    try: 
        oldfile = open((number)+'.txt', "r+")
        tempfile = open("~/.package-track/bin/tempfile.txt", "r+")
        old_dict = oldfile.readlines()
        new_dict = tempfile.readlines()
        oldfile.close()
        tempfile.close()
        #finding the difference between the two files
        diff = [ x for x in new_dict if x not in old_dict ]
        if diff: 
            print(diff[0].rstrip())
            old_dict = new_dict
            with open ("~/.package-track/bin/"+(number)+'.txt', "w") as filehandle:
                for line in old_dict:
                    filehandle.write('%s\n' % line.rstrip())
    # if older version of the file isn't found, create it based on temp file
    except:
        with open("~/.package-track/bin/"+(number)+'.txt', "w") as filehandle:
            for result in results: 
                if ("WE KNOW WHERE YOUR STUFF IS." in result.text):
                    continue
                filehandle.write('%s\n' % result.text)
                print(result)
    if (delivered):
        print("package " + number + " was delivered, tracking number removed from list")
        try:
            os.remove((number)+'.txt')
        except:
            pass

    finaltrackinglist.append(number)

#updating tracking list txt file
with open ('~/.package-track/bin/trackingnumbers.txt', 'w') as filehandle:
    for item in finaltrackinglist:
        filehandle.write('%s\n' % item)

#removing tempfile 
try: 
    os.remove("~/.package-track/bin/tempfile.txt")
    os.remove("~/.package-track/bin/tracking_from_email.txt")
except: 
    pass 
#print("program complete!")




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import os

trackinglist = []

with open("trackingnumbers.txt", "r") as fileHandle:
    for line in fileHandle:
        current = line[:-1]
        trackinglist.append(current)

for number in trackinglist: 
    # creating boolean flag to track if package was delivered
    delivered = False
    
    #printing tracking number
    print(number)

    #selenium
    with webdriver.Firefox() as driver:
        driver.get("https://www.packagetrackr.com")
        print(driver.title)
        #importing tracking list from csv

        search = driver.find_element_by_name("n")
        search.send_keys(number)
        search.send_keys(Keys.ENTER)

        time.sleep(5)
        #waiting for new page to load
        results = driver.find_elements_by_class_name("media-body")
        for result in results:
            # print(result.text)
       
        # trying to remove listed number if item was delivered
            if (result.text == "Delivered"):
                trackinglist.remove(number)
                delivered = True

        # writing contents to new temp file
        with open ('tempfile.txt', 'w') as filehandle:
            for result in results:
                filehandle.write('%s\n' % result.text)

        # comparing the results of old and new files if old file exists
        # returning difference to provide most accurate (recent) tracking info
        try: 
            oldfile = open((number)+'.txt', "r+")
            tempfile = open("tempfile.txt", "r+")
            old_dict = oldfile.readlines()
            new_dict = tempfile.readlines()
            oldfile.close()
            tempfile.close()
            #finding the difference between the two files
            diff = [ x for x in new_dict if x not in old_dict ]
            if diff: 
                print(diff[0].rstrip())
                old_dict = new_dict
                with open ((number)+'.txt', "w") as filehandle:
                    for line in old_dict:
                        filehandle.write('%s\n' % line.rstrip())
        # if older version of the file isn't found, create it based on temp file
        except:
            with open((number)+'.txt', "w") as filehandle:
                for result in results: 
                    filehandle.write('%s\n' % result.text)

    if (delivered):
        print(" ")
        print("package " + number + " was delivered, tracking number removed from list")
        # cleaning out old textfiles for delivered packages
        os.remove((number)+'.txt')
#updating tracking list txt file
with open ('trackingnumbers.txt', 'w') as filehandle:
    for item in trackinglist:
        filehandle.write('%s\n' % item)

#removing tempfile 
os.remove("tempfile.txt")

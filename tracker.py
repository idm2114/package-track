from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

trackinglist = []

with open("trackingnumbers.txt", "r") as fileHandle:
    for line in fileHandle:
        current = line[:-1]
        trackinglist.append(current)

delivered = True
for number in trackinglist: 
    print(number)
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
            print(result.text)
        
        # trying to remove listed number if item was delivered 
            if (result.text == "Delivered"):
                trackinglist.remove(number)
                delivered = True

    if (delivered):
        print(" ")
        print("package " + number + " was delivered, tracking number removed from list")

#updating tracking list txt file
with open ('trackingnumbers.txt', 'w') as filehandle:
    for item in trackinglist:
        filehandle.write('%s\n' % item)



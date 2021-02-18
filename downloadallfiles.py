# Python program to download files recursively
# Author - Ranjan Goyal

# importing os module 
import os 
import requests

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Directory 
directory = "wow i did it"

# Parent Directory path 
parent_dir = ""  #Insert Directory Here

driver = webdriver.Chrome()
driver.get('')   # Insert Main Link Here
time.sleep(10)

not_included = []

def find_downloadables(current_dir):
    names = []
    items_name = driver.find_elements_by_xpath('') #Insert XPATH For NAMES
    for item_name in items_name:
        names.append(item_name.get_attribute('title'))
        print(item_name.get_attribute('title'))
        
    link_array = []
    links = driver.find_elements_by_xpath(''). #Insert XPATH FOR LINKS
    for link in links:
        print(link.get_attribute('href'))
        link_array.append(link.get_attribute('href'))

    print("Going into loop")
    for i in range(len(link_array)):
        url = link_array[i]
        if(url[-7:]=="?a=view"):
            print("Downloading Content")
            print("Directory is : " + current_dir)
            url = url[:-7]
            print("Downloading: " + names[i])
            if(names[i].rfind("%3F")>=0):
                print("%3F Found")
                url = url.replace("%3F", "%253F")
            if(names[i].rfind("?")>=0):
                print("? Found")
                url = url.replace("?", "%3F")
            # print(url)
            r = requests.get(url)
            # download started  
            with open(current_dir+names[i], 'wb') as f:  
                for chunk in r.iter_content(chunk_size = 1024*1024):  
                    if chunk:  
                        f.write(chunk)  
        elif(url[-1]=="/"):
            flag = 0
            for a in not_included:
                if(a == url):
                    print("Dont Include")
                    flag = 1
            if(flag == 0):
                # print(i)
                path = os.path.join(current_dir, names[i]) 
                try:
                    os.mkdir(path) 
                    print("Directory '% s' created" % names[i]) 
                except:
                    print("exists")
                driver.get(url)
                time.sleep(10)
                current_dir = current_dir + names[i] + "/"
                find_downloadables(current_dir)
                x = current_dir.rfind(names[i])
                current_dir = current_dir[0:x]
        else:
            print("Downloading Content")
            print("Directory is : " + current_dir)
            # url = url[:-7]
            print("Downloading: " + names[i])
            if(names[i].rfind("%3F")>=0):
                print("%3F Found")
                url = url.replace("%3F", "%253F")
            if(names[i].rfind("?")>=0):
                print("? Found")
                url = url.replace("?", "%3F")
            # print(url)
            r = requests.get(url)
            # download started  
            with open(current_dir+names[i], 'wb') as f:  
                for chunk in r.iter_content(chunk_size = 1024*1024):  
                    if chunk:  
                        f.write(chunk) 

find_downloadables(parent_dir)
print("Finished Downloading.")
time.sleep(5)
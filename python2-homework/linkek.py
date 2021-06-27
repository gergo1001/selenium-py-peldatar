from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:9999")

linkek = driver.find_elements_by_xpath('//a')
with open('linkek.txt', 'w') as f2:
    for elem in linkek:
        f2.write(elem.get_attribute("href") + "\n")
print(len(linkek))

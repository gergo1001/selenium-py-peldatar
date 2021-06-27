import time

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://localhost:9999/general.html")

linkek=driver.find_elements_by_xpath('//a')

for link in linkek:

    try:
        url=link.get_attribute("href")
        link.click()
        time.sleep(1.0)
        assert (url, driver.current_url)
        driver.back()

    except:
        print("ez uj ablakban nyilna meg:, ilyenről végképp nem volt szó ;)" ,link.id,"!!!!")


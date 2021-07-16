from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import shutil
import urllib.request
import csv
from selenium.webdriver.common.keys import Keys

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/loadmore.html')

gomb = driver.find_element_by_class_name("load-more-button")
kepek = []
while True:
    kepek = driver.find_elements_by_class_name("image")
    if len(kepek) >= 20:
        break
    if gomb.is_enabled():
        gomb.click()
    else:
        break
    time.sleep(3)

for _ in range(20):
    if _ < len(kepek):
        image_url = kepek[_].find_element_by_tag_name('img').get_attribute("src")
        filename = str(_ + 1) + '_' + kepek[_].find_element_by_tag_name('p').text.replace('Cat id: ', '')

        download_file = f'cats/{filename}'
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            with open(download_file, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
        print('Image sucessfully Downloaded: ', filename)

driver.close()

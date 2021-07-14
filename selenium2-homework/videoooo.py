from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/videos.html')

html5video = driver.find_element_by_id("html5video")
html5video.send_keys(Keys.SPACE)
time.sleep(10)
html5video.send_keys(Keys.SPACE)


button = driver.find_element_by_xpath("//button[text()='Play/Pause']")
button.click()
time.sleep(10)
button.click()


youtube = driver.find_element_by_id("youtubeframe")
youtube.click()
time.sleep(10)
youtube.click()

time.sleep(5)
driver.close()

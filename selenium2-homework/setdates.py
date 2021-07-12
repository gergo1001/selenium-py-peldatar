from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/forms.html')

testdate = datetime(2021, 6, 5)
# driver.find_element_by_id("example-input-date").send_keys(testdate.strftime('00%Y%mm%dd'))
driver.find_element_by_id("example-input-date").send_keys(testdate.strftime('00%Y%%%M%%%D'))

testdate = datetime(2012, 5, 5, 5, 5, 5, 555)
seged = testdate.strftime('%Y.%m.%d %H:%M:%S:%f')
driver.find_element_by_id("example-input-date-time").send_keys(seged)
# itt a 19 karakter után a felvezető nullákat le kell cserélni. nem találtam rá jó beépített függvényt

testdate = datetime(2000, 12, 5, 12, 1)
driver.find_element_by_id("example-input-date-time-local").send_keys(testdate.strftime('00%Y.%m.%dT%I:%M %p\t'))

testdate = datetime(1995, 12, 1)
driver.find_element_by_id("example-input-month").send_keys(testdate.strftime('%Y\t%b'))

testdate = datetime(2015, 12, 31)
driver.find_element_by_id("example-input-week").send_keys(testdate.strftime('%W%Y'))

testdate = datetime(2021, 1, 1, 12, 25)
driver.find_element_by_id("example-input-time").send_keys(testdate.strftime('%H:%M'))

driver.close()

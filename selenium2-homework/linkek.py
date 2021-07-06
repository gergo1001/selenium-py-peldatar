from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999')

linkek = driver.find_elements_by_xpath("//a")
linkek2 = []
for link in linkek:
    linkek2 += link.get_attribute('href') + '\n'
fajl = open('linkek.txt', 'w')
fajl.writelines(linkek)
fajl.close()
print(f"linkek száma: {len(linkek)}")
driver.close()

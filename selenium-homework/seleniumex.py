from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://index.hu")
try:
    q = driver.find_elements("nem létező")
except:
    print("hiba történt az elem keresése közben")
    driver.close()

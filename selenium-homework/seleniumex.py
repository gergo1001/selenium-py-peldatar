from selenium import webdriver


def find_elements_ex(driver):
    try:
        q = driver.find_elements("nem létező")
    except:
        print("hiba történt az elem keresése közben")
        driver.close()


driver = webdriver.Chrome()
find_elements_ex(driver)

# driver.get("https://index.hu")
# try:
#    q = driver.find_elements("nem létező")
# except:
#    print("hiba történt az elem keresése közben")
#    driver.close()

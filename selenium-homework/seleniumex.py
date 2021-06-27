from selenium import webdriver


def find_elements_ex(driver, elem):
    try:
        q = driver.find_elements(elem)
    except:
        print(f"hiba történt a(z) <{elem}> keresése közben")
        driver.close()


driver = webdriver.Chrome()
find_elements_ex(driver, "nem létező")

# driver.get("https://index.hu")
# try:
#    q = driver.find_elements("nem létező")
# except:
#    print("hiba történt az elem keresése közben")
#    driver.close()

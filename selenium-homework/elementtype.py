from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/trickyelements.html")

elemek = driver.find_elements_by_xpath(".//*")
# miután már megcsináltam ezt a feladatot olvastam az XPATH wordben, hogy ne használjunk * karaktert, de miért ne? most már ezt a feladatot itt hagyom,
# de egy konzultáción majd megkérdezem

for elem in elemek:
    # print (elem.get_attribute("type"))
    if elem.get_attribute("type") == "submit":
        # print("gomb:", elem.id)
        result = driver.find_element_by_id("result")
        elem.click()
        webelement_id = elem.get_attribute("id")
        # print(elem.get_attribute("id"))
        assert (result.text == f"{webelement_id} was clicked")
        break

    # else:
    #    print("nem gomb:", elem.get_attribute("type"),elem.tag_name)

driver.close()

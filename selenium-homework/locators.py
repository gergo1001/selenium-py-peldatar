from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/kitchensink.html")


def attrubutomok(elem):
    print("value (attr): ", elem.get_attribute("value"))
    print("checked (prop): ", elem.get_property("checked"))
    print("name: (prop)", elem.get_property("name"))  # nem tudom, hogy mire szolgál a cars, csak tipp
    print("text: ", elem.text)
    print("--------")


# radiobutton
bmw = driver.find_element_by_id("bmwradio")
attrubutomok(bmw)

combobox = driver.find_element_by_xpath("/html/body/div[2]/div[2]/fieldset/select")
attrubutomok(combobox)

multiselect = driver.find_element_by_name("multiple-select-example");
attrubutomok(multiselect)

bmwcheck = driver.find_element_by_id("bmwcheck")
attrubutomok(bmw)


# driver.close();

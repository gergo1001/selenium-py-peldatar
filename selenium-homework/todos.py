from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/todo.html")

elemek = driver.find_elements_by_xpath('//ul/li[not(@checked)]')

for elem in elemek:
    print(elem.text)

driver.close()

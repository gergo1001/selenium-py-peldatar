from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from selenium.webdriver.common.keys import Keys

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/pagination.html')

gomb = driver.find_element_by_id("next")
data_in_memory = []


def read_from_table():
    time.sleep(3)
    table_rows = driver.find_elements_by_xpath("//table/tbody/tr")
    for row in table_rows:
        cells = row.find_elements_by_tag_name("td")
        if len(cells[1].text) > 0:
            if cells[1].text[0] == 'A':
                men = {}
                men["id"] = cells[0].text
                men["first_name"] = cells[1].text
                men["second_name"] = cells[2].text
                men["surname"] = cells[3].text
                men["second_surname"] = cells[4].text
                men["birth_date"] = cells[5].text
                data_in_memory.append(men)


read_from_table()
while True:
    time.sleep(2)
    if gomb.is_enabled():
        gomb.click()
        read_from_table()
    if not gomb.is_enabled():
        break
csv_columns = ['id', 'first_name', 'second_name', 'surname', 'second_surname', 'birth_date']
csv_file = "pagination.csv"
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in data_in_memory:
        writer.writerow(data)
driver.close()

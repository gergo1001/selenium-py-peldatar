import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/editable-table.html')

add_button = driver.find_element_by_xpath("//button[text()='Add']")

search_input = driver.find_element_by_xpath("//input")


# Adj hozzá még két teljsen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.

def fill_cell(cell, value):
    assert (cell.get_property("value") == None) # ez nem jó, mindig none..nem tudom miért nem jó
    # azt azért megnézem, hogy value ne legyen az új értéknél
    cell.find_element_by_tag_name("input").clear()
    cell.find_element_by_tag_name("input").send_keys(value)


def add_row(name, price, quantity, category):
    act_row_count = len(driver.find_elements_by_xpath("//table/tbody/tr"))
    add_button.click()
    table_rows = driver.find_elements_by_xpath("//table/tbody/tr")
    assert (act_row_count + 1 == len(table_rows))
    # az értékre nem ellenőrzök, mivel azokat én töltöm, ott talán nincs értelme ellenőrizni (mondjuk ebben nem vagyok biztos)
    cells = table_rows[len(table_rows) - 1].find_elements_by_tag_name("td")

    fill_cell(cells[0], name)
    fill_cell(cells[1], price)
    fill_cell(cells[2], quantity)
    fill_cell(cells[3], category)


# a) Addj hozzá még két teljsen kitöltött sort. Ellenőrizd, hogy tényleg hozzáadódtak-e a sorok.
add_row('tePt', 12, 36, 'elem')
add_row('masik termek', 16, 46, 'elem')


# b) Ellenőrizd a kereső funkciót.
def check_search(serch_text):
    voltrossz = False
    good_row = 0
    table_rows = driver.find_elements_by_xpath("//table/tbody/tr")
    for row in table_rows:
        ertek = row.find_element_by_name('name').get_attribute('value')
        # a program igy kiakad, mert neki más a Ipod vagy az ipod, de szerintem ez igy rossz, ezért ellenőrzök így

        if search_text.lower() in ertek.lower():
            good_row += 1
        else:
            voltrossz = True
    return good_row


voltrossz = False
search_text = "Pt"
good_row = check_search(search_text)
voltrossz = False
search_input.send_keys(search_text)
time.sleep(2)
act_row = len(driver.find_elements_by_xpath("//table/tbody/tr"))
assert (good_row == act_row)  # pont annyi sor van, ahanynak kellene lenni
assert (voltrossz == False)  # csak jó sor van

#c) írd át a táblázat egyes celláit és ellenőrizd, hogy megfelelően frissült-e a DOM struktúra.
#nem frissül, gondolom ennek köze van, hogy miért nem megy a másik fajta elérés, ha arra kapok választ, akkor vizsgálom ezt
#driver.close()

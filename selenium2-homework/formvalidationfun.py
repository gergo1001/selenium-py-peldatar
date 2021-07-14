from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/simplevalidation.html')

# textmezok=driver.find_elements_by_xpath("//div[@class='validate-input']")
# textmezok=driver.find_elements_by_class_name('validate-input')
# for csoport in textmezok:
#     csoport.find_element_by_tag_name("input").send_keys("teszt")
#     time.sleep(5)
#     hibauzenetek = csoport.find_elements_by_xpath("//*[@class='validate-field-error-message']")
#     for hibauzenet in hibauzenetek:
#         if hibauzenet.parent == csoport:
#             print(hibauzenet.text)
#     #out = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="{}"]'.format(attr)))).text


# print(out)


ids = ["test-email", "test-password", "test-confirm-password", "test-customer-number",
       "test-dealer-number", "test-random-field", "test-date-field", "test-url-field",
       "test-random-textarea", "test-card-type", "test-card-number", "test-card-cvv",
       "test-card-month", "test-card-year", "test-single-checkbox", "test-save-email-yes",
       "test-terms-service", "test-terms-service-more"]  # ez mar nem kell ide

errs = [("Please enter an e-mail", 'Please check your E-Mail format', 'Login does not exist'),
        ("This field can't be empty", 'Should be between 6 and 20 characters'),
        ('Please complete Desired Password', 'Does not match Desired Password'),
        ("This field can't be empty", 'Should be a number'),
        ("This field can't be empty", 'Should be a 4 character number'),
        ('Should contain "twelve"',), ("This field can't be empty", 'Must match pattern YYYY-MM-DD'),
        ('Please enter a valid URL (starts with "http" or "https")',), ("This field can't be empty",),
        ('Please select a card type',),
        ('Please enter a credit card number (no spaces)', 'Please check your credit card nubmer'),
        ("This field can't be empty", 'Should be a number between 3 and 4 characters'),
        ('Select a month',), ('Select a year',), ("This field can't be empty",),
        ('Please select one',), ('Please agree to both to continue',)]

Dictonary1 = {"test-email": ("Please enter an e-mail", 'Please check your E-Mail format', 'Login does not exist'),
              "test-password": ("This field can't be empty", 'Should be between 6 and 20 characters')
              }


def get_element_error_msg(element, inp):
    tmp = driver.find_element_by_id(element)
    tmp.send_keys(inp)
    attr = tmp.get_attribute("data-jsv-message-target")
    time.sleep(5)
    try:
        out = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
            (By.XPATH, '//div[@id="{}"]'.format(attr)))).text
    except TimeoutException:
        out = None
    return out

    # Tesztelés üres mezőkkel


# for count,i in enumerate(ids):
#     e = get_element_error_msg(i, '\t')
#     if e is not None:
#
#         # assert e in x
#         if e in errs[count]:
#             print(f'id={i} mező tesztelve, a(z) >>{e}<< üzenet megjelent! ')
#         else:
#             print(e)
#     else:
#         print(f'id={i} mező tesztelve, nincs hibaüzenet!')

for elem in Dictonary1:
    e = get_element_error_msg(elem, '\t')
    if e is not None:

        # assert e in x
        if e in Dictonary1[elem]:
            print(f'id={elem} mező tesztelve, a(z) >>{e}<< üzenet megjelent! ')
        else:
            print(e)
    else:
        print(f'id={elem} mező tesztelve, nincs hibaüzenet!')

driver.quit()

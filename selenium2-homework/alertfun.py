import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# In order for ChromeDriverManager to work you must pip install it in your own environment.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://localhost:9999/alert_playground.html')

button = driver.find_element_by_name('alert')
button.click()
alert = driver.switch_to.alert
time.sleep(3)
alert.accept()

button = driver.find_element_by_name("confirmation")
button.click()
alert = driver.switch_to.alert
time.sleep(3)
alert.accept()

button.click()
time.sleep(3)
alert.dismiss()

button = driver.find_element_by_id("double-click")
action = ActionChains(driver)
action.double_click(button).perform()
alert = driver.switch_to.alert
alert.accept()

text_now = driver.find_element_by_id("demo").text
button = driver.find_element_by_name("prompt")
button.click()
alert = driver.switch_to.alert
send_text = "123456"
alert.send_keys(send_text)
time.sleep(10)
alert.dismiss()
time.sleep(3)
assert (driver.find_element_by_id("demo").text, text_now)
button.click()
alert = driver.switch_to.alert
send_text = "123456"
alert.send_keys(send_text)
alert.accept()
assert (driver.find_element_by_id("demo").text, f"You entered: {send_text}")
time.sleep(3)
driver.close()
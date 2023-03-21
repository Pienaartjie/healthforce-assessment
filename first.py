
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:6464")

#identify input
query = driver.find_element("id", "number")
#send an 'x' in the input field
query.send_keys("x")
#select the calculate button
driver.find_element(By.XPATH, '//button[@type="submit"]').click()

#Console message
console_message = driver.find_element("id", "resultDiv").text

#1.Write a locator (CSS selector/XPath) for the red form validation styling
red_form_locator = driver.find_element("id", "number")
print("Style: " + red_form_locator.value_of_css_property('border'))

print(console_message)

#query = driver.find_element("id", "number")
query.clear()
query.send_keys("7")
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
console_message = driver.find_element("id", "resultDiv").text
if console_message == 'The factorial of 7 is: 5040':
    print('Correct. The factorial of 7 is: 5040')
else:
    print('Incorrect the factorial of 7 is not 5040')






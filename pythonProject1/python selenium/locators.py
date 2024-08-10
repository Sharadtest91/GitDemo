import time
from select import select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Hello@123")
driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
driver.find_element(By.CSS_SELECTOR, "input[name ='name']").send_keys("sharad")
driver.find_element(By.CSS_SELECTOR, "input[id='inlineRadio1'").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()


dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)


assert "Success" in message


print(message)

driver.maximize_window()
time.sleep(5)


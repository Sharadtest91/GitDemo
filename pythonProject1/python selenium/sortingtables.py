import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait
browsersortedveggies = []
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

veggiwebelements = driver.find_elements(By.XPATH, "//tr/td[1]")

for ele in veggiwebelements:
    browsersortedveggies.append(ele.text)

originalsortedbrowserlist = browsersortedveggies.copy()

browsersortedveggies.sort()


assert browsersortedveggies == originalsortedbrowserlist
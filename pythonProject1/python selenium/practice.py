import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input[type='search']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("onion")
driver.find_element(By.LINK_TEXT, "+").click()


driver.find_element(By.LINK_TEXT,"ADD TO CART").click()









time.sleep(5)

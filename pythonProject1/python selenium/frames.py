import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M17.3 8.2L')]").click()
driver.switch_to.default_content()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I will get job soon")


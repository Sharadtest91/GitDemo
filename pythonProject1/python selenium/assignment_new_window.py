import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])
message = driver.find_element(By.XPATH, "//p[@class='im-para red']").text
details = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(windowsopened[0])
driver.find_element(By.ID, "username").send_keys(details)
driver.find_element(By.ID, "password").send_keys(details)
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger.col-md-12")))

print(driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.col-md-12").text)




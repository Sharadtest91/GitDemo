from selenium import webdriver

chromeoptions =webdriver.ChromeOptions()
chromeoptions.add_argument("--start--maximize")
chromeoptions.add_argument("headless")
chromeoptions.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chromeoptions)

driver.get("https://rahulshettyacademy.com/angularpractice/")


print(driver.title)
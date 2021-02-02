from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://www.google.co.in/")
elementSearch = driver.find_element(By.NAME, "q")
elementSearch.click()
elementSearch.send_keys("learn python")
elementSearch.send_keys(Keys.ENTER)
print(driver.title)
print("execution completed")
driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
url = "http://localhost:81/orangehrm/symfony/web/index.php/auth/login"

driver.get(url)
driver.find_element_by_id("txtUsername").send_keys("user")
driver.find_element_by_name("txtPassword").send_keys("password123")
driver.find_element(By.NAME, "Submit").click()

checkLoginSuccessful = driver.find_element(By.ID, "welcome").is_displayed()
if checkLoginSuccessful:
    print("user logged in successfully")
    driver.find_element(By.ID, "welcome").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()
    checkLogoutSuccessful = driver.find_element(By.ID, "txtUsername").is_displayed()
    if checkLogoutSuccessful:
        print("user logged out successfully")
    else:
        print("user failed to log out")
else:
    print("user failed to log in")




from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
try:
    path = r"https://www.facebook.com/"

    driver = webdriver.Chrome(service=ChromeService (ChromeDriverManager().install()))

#navigate to the login page
    driver.get(path)
    driver.maximize_window()

    email_input = driver.find_element(By.ID, "email")
    pass_input = driver.find_element(By.ID, "pass")
    login_button = driver.find_element(By.ID, "u_0_5_2+")

    email_input.send_keys("seleniumtesting@gmail.com")
    pass_input.send_keys("selenium123")

    time.sleep(2)

    search_box.send_keys(Keys.ENTER)

except Exception as e:

    print("Error in opening chrome")
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.description_url)
    driver.quit()
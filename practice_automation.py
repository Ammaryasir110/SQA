from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
data=["Ammar", "Yasir", "Dahar", "Artificial Intelligence", "Evening", "Female",]
try:
    path = r"file:///C:/Users/Lenovo/Desktop/SQA%20TASKS/Selenium/form.html"

    driver = webdriver.Chrome(service=ChromeService (ChromeDriverManager().install()))

#navigate to the login page
    driver.get(path)
    driver.maximize_window()

    time.sleep(2)
    name=driver.find_element(By.ID, "name")
    name.send_keys(data[0])

    father_name=driver.find_element(By.ID, "F/name")
    father_name.send_keys(data[1])

    caste=driver.find_element(By.ID,"Cast")
    caste.send_keys(data[2])
    
    
    course=driver.find_element(By.ID,"Course")
    if data[3]=="Cloud Architecture":
        cc=driver.find_element(By.ID,"cloud")
        cc.click()
    elif data[3]=="SQA":
        sqa=driver.find_element(By.ID,"sqa")
        sqa.click()
    elif data[3]=="Artificial Intelligence":
        ai=driver.find_element(By.ID,"AI")
        ai.click()    
    if data[4]=="Morning":
        morning=driver.find_element(By.ID,"Morning")
        morning.click()
    elif data[4]=="Evening":
        evening=driver.find_element(By.ID, "Evening")
        evening.click()
    
    if data[5]=="Male":
        male=driver.find_element(By.ID,"Male")
        male.click()
    elif data[5]=="Female":
        female=driver.find_element(By.ID,"Female")
        female.click()
    button=driver.find_element(By.ID,"Submit")
    button.click()
    
except Exception as e:

    print("Error in opening chrome")
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.description_url)
    driver.quit()
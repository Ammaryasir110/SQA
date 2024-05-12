from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

data= ["Ammar", "Yasir", "dahar", "Cloud Architecture", "Evening", "Female"]
try:
    path = r"file:///C:/Users/Lenovo/Desktop/SQA%20TASKS/Selenium/form.html"

    driver = webdriver.Chrome(service=ChromeService (ChromeDriverManager().install()))

#navigate to the login page
    driver.get(path)
    driver.maximize_window()

    time.sleep(2)
    #name
    name=driver.find_element(By.ID, "name")
    name.send_keys(data[0])
    #father_name
    f_name=driver.find_element(By.ID, "F/name")
    f_name.send_keys(data[1])
    #cast
    cast=driver.find_element(By.ID, "Cast")
    cast.send_keys(data[2])
    #course
    course=driver.find_element(By.ID, "Course")
    if data[3]=="Cloud Architecture":
        cc=driver.find_element(By.ID,"cloud")
        cc.click()
    elif data[3]=="Artificial Intelligence":
        AI=driver.find_element(By.ID,"AI")
        AI.click()
    elif data[3]=="SQA":
        sqa=driver.find_element(By.ID,"sqa")
        sqa.click()
    #shift
    if data[4]=="Morning":
        morning=driver.find_element(By.ID,"Morning")
        time.sleep(2)
        morning.click()
    elif data[4]=="Evening":
        evening=driver.find_element(By.ID, "Evening")
        evening.click() 
    #gender
    if data[5]=="Male":
        male=driver.find_element(By.ID, "Male")
        time.sleep(2)
        male.click()
    elif data[5]=="Female":
        female=driver.find_element(By.ID, "Female")
        female.click()
    submit=driver.find_element(By.ID, "Submit")
    submit.click()
    # course.click()
    # course.send_keys("Cloud Architecture")
    # time.sleep(2)
    # course.click()
    # course.send_keys("Cloud Architecture")
    print(len(data))

except Exception as e:

    print("Error in opening chrome")
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.current_url)
    driver.quit()
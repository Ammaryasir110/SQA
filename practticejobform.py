from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
data=["Ammar", "Yasir","dahar","04/04/2003","qasimabad","ay720240@gmail.com","12345","male","sukkur","graduate","","Cricket","AYD"]
try:
    path = r"file:///C:/Users/Lenovo/Desktop/SQA%20TASKS/Selenium/HTML/jobapplication_form.html"

    driver = webdriver.Chrome(service=ChromeService (ChromeDriverManager().install()))

#navigate to the login page
    driver.get(path)
    driver.maximize_window()

    time.sleep(2)
    name=driver.find_element(By.ID,"name")
    name.send_keys(data[0])
    F_name=driver.find_element(By.ID,"f_name")
    F_name.send_keys(data[1])
    caste=driver.find_element(By.ID,"caste")
    caste.send_keys(data[2])
    dob=driver.find_element(By.ID,"dob")
    dob.click()
    address=driver.find_element(By.ID,"add")
    address.send_keys(data[4])
    email=driver.find_element(By.ID,"email")
    email.send_keys(data[5])
    passe=driver.find_element(By.ID,"pass")
    passe.send_keys(data[6])
    if data[7]=="male":
        male=driver.find_element(By.ID,"male")
        male.click()
    elif data[7]=="female":
        female=driver.find_element(By.ID,"female")
        female.click()
    city=driver.find_element(By.ID,"city")
    city.click()
    if data[8]=="sukkur":
        suk=driver.find_element(By.ID,"Sukkur")
        suk.click()
    elif data[8]=="hyderabad":
        hyd=driver.find_element(By.ID,"Hyderabad")
        hyd.click()
    elif data[8]=="karachi":
        khi=driver.find_element(By.ID,"Karachi")
        khi.click()
    city.click()

    qualification=driver.find_element(By.ID,"qualify")
    qualification.click()
    if data[9]=="graduate":
        grad=driver.find_element(By.ID,"graduate")
        grad.click()
    elif data[9]=="matric":
        X=driver.find_element(By.ID,"matric")
        X.click()
    elif data[9]=="intermediate":
        XII=driver.find_element(By.ID,"intermediate")
        XII.click()
    qualification.click()

    if data[11]=="Cricket":
        cricket=driver.find_element(By.ID,"cricket")
        cricket.click()
    elif data[11]=="Football":
        foot=driver.find_element(By.ID,"football")
        foot.click()
    elif data[11]=="BAdminton":
        bad=driver.find_element(By.ID,"badminton")
        bad.click()
    elif data[11]=="Basketball":
        basket=driver.find_element(By.ID,"basketball")
        basket.click()
    comment=driver.find_element(By.ID,"comment")
    comment.send_keys("Testing is working successfully")

    submit=driver.find_element(By.ID,"submit")
    submit.click()

    reset=driver.find_element(By.ID,"reset")
    reset.click()
except Exception as e:

    print("Error in opening chrome")
finally:
    time.sleep(20)
    print(driver.title)
    print(driver.current_url)
    driver.quit()
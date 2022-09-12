from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
#mention your email and password
email = '-------------------------'
password = '###############'

companyName = "Groww"
job_link = "https://groww.skillate.com/jobs/44512"

s = Service('C:/Users/gsuni/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get('https://www.linkedin.com')
time.sleep(2)


#********** Message  *************

describe = "I'm Sunil, Can you please refer me for the below mention Job role at "+companyName+"\nJob link: "

resume_link = "\nResume Link: https://drive.google.com/file/d/1M4QVN76gcNl55qnNUaGVOw38wA69AYqA/view "

message_format = describe+job_link+resume_link

#***************** totalConnections ************
totalConnections = 25

#********** LOGIN ********************
username = driver.find_element("xpath","//input[@name='session_key']")
authentication = driver.find_element("xpath","//input[@name='session_password']")

username.send_keys(email)
authentication.send_keys(password)
time.sleep(2)

submit = driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(2)

#**************** Company specific search **********************

textBox = driver.find_element("xpath","//input[@placeholder='Search']")
textBox.send_keys(companyName)
textBox.send_keys(Keys.ENTER)
time.sleep(5)
people_button = driver.find_element("xpath","//button[normalize-space()='People']").click()
time.sleep(2)


#*********************** Sending Connection request *******************
while totalConnections>0:
    all_buttons = driver.find_elements("tag name","button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
    time.sleep(2)
    if connect_buttons:
        for btn in connect_buttons:
            driver.execute_script("arguments[0].click();", btn)
            person_name =driver.find_element( "xpath","//span[@class='flex-1']//strong").text
            time.sleep(2)
            add_note = driver.find_element("xpath","//button[@aria-label='Add a note']")
            driver.execute_script("arguments[0].click();", add_note)
            time.sleep(2)
            textArea = driver.find_element("xpath","//textarea[@id='custom-message']")
            final_message = "Hi "+person_name+" \n"+message_format
            textArea.send_keys(final_message)
            send = driver.find_element("xpath","//button[@aria-label='Send now']")
            driver.execute_script("arguments[0].click();", send)
            time.sleep(1)
            close = driver.find_element("xpath","//button[@aria-label='Dismiss']")
            driver.execute_script("arguments[0].click();", close)
            time.sleep(2)
            totalConnections=totalConnections-1
    else:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        next = driver.find_element("xpath","//button[@aria-label='Next']")
        driver.execute_script("arguments[0].click();", next)
        time.sleep(2)
        
    

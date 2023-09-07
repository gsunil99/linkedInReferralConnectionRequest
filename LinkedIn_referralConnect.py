from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import secrets
# mention your email and password
email = secrets.EMAIL
password = secrets.LINKEDIN_PASSWORD

companyName = "RamSoft"

s = Service('/Users/sunilg/Desktop/linkedconnect/chromedriver')
driver = webdriver.Chrome(service=s)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get('https://www.linkedin.com')
time.sleep(2)


# ********** Message  *************

describe = "I'm sunil currently working as a fullstack software developer at climate connect Digital. I have worked on technology such as java, spring, python, Django, aws-chalice, mongodb."
job_desc = "\nCan you please refer me for this job: https://tinyurl.com/khb6phs6"
resume_link = "\nResume Link: https://tinyurl.com/ycynkw2z "

message_format = describe+job_desc+resume_link
print(message_format)
# ***************** totalConnections ************
totalConnections = 20

# ********** LOGIN ********************
username = driver.find_element("xpath", "//input[@name='session_key']")
authentication = driver.find_element(
    "xpath", "//input[@name='session_password']")

username.send_keys(email)
authentication.send_keys(password)
time.sleep(2)

submit = driver.find_element("xpath", "//button[@type='submit']").click()
time.sleep(2)

# **************** Company specific search **********************

textBox = driver.find_element("xpath", "//input[@placeholder='Search']")
textBox.send_keys(companyName)
textBox.send_keys(Keys.ENTER)
time.sleep(5)
people_button = driver.find_element(
    "xpath", "//button[normalize-space()='People']").click()
time.sleep(2)


# *********************** Sending Connection request *******************
while totalConnections > 0:
    # print('inside')
    # all_buttons = driver.find_elements("tag name", "button")
    # connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
    connect_buttons = driver.find_elements(
        "xpath", "//button[.//li-icon[@type='connect']]")
    time.sleep(2)
    if connect_buttons:
        for btn in connect_buttons:
            driver.execute_script("arguments[0].click();", btn)
            try:
                if driver.find_element("xpath", "//button[@aria-label='Work Colleagues']") > 0:
                    work_colleagues = driver.find_element(
                        "xpath", "//button[@aria-label='Work Colleagues']")
                    driver.execute_script(
                        "arguments[0].click();", work_colleagues)
                    time.sleep(2)
                    connect = driver.find_element(
                        "xpath", "//button[@aria-label='Connect']")
                    driver.execute_script("arguments[0].click();", connect)
                    time.sleep(2)
            except:
                print("No work colleagues")
            person_name = driver.find_element(
                "xpath", "//span[@class='flex-1']//strong").text
            time.sleep(2)
            add_note = driver.find_element(
                "xpath", "//button[@aria-label='Add a note']")
            driver.execute_script("arguments[0].click();", add_note)
            time.sleep(2)
            textArea = driver.find_element(
                "xpath", "//textarea[@id='custom-message']")
            final_message = "Hi "+person_name+" \n"+message_format
            textArea.send_keys(final_message)
            send = driver.find_element(
                "xpath", "//button[@aria-label='Send now']")
            driver.execute_script("arguments[0].click();", send)
            time.sleep(1)
            close = driver.find_element(
                "xpath", "//button[@aria-label='Dismiss']")
            driver.execute_script("arguments[0].click();", close)
            time.sleep(2)
            totalConnections = totalConnections-1
    else:
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        next = driver.find_element("xpath", "//button[@aria-label='Next']")
        driver.execute_script("arguments[0].click();", next)
        time.sleep(4)

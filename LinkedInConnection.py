'send connections based on company name'
import secrets
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


# ***************** company detail ************
COMPANY_NAME = "Appviewx"

# ***************** totalConnections ************
totalConnections = 30


# ************** mention your EMAIL and PASSWORD *******
EMAIL = secrets.EMAIL
PASSWORD = secrets.LINKEDIN_PASSWORD


# **************** service started ************
s = Service(
    '/Users/sunilg/Desktop/linkedInReferralConnectionRequest/chromedriver')
driver = webdriver.Chrome(service=s)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get('https://www.linkedin.com')


# ********** LOGIN ********************
wait = WebDriverWait(driver, 20)  # Adjust the timeout as needed

username = wait.until(EC.presence_of_element_located((By.NAME, 'session_key')))
authentication = wait.until(
    EC.presence_of_element_located((By.NAME, 'session_password')))

username.send_keys(EMAIL)
authentication.send_keys(PASSWORD)

submit = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[@type='submit']")))
submit.click()

# **************** Company specific search **********************

textBox = wait.until(EC.presence_of_element_located(
    (By.XPATH, "//input[@placeholder='Search']")))
textBox.send_keys(COMPANY_NAME)
textBox.send_keys(Keys.ENTER)
wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
people_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[normalize-space()='People']")))
people_button.click()

# *********************** Sending Connection request *******************
while totalConnections > 0:
    connect_buttons = ''
    try:
        wait.until(EC.presence_of_element_located((By.XPATH, "//body")))
        connect_buttons = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//button[contains(@aria-label, 'connect')]")))
        if connect_buttons:
            for btn in connect_buttons:
                try:
                    driver.execute_script("arguments[0].click();", btn)
                    send = wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "//button[@aria-label='Send now']")))
                    send.click()
                    totalConnections -= 1
                except StaleElementReferenceException as stale_ex:
                    print("StaleElementReferenceException occurred. Retrying...")
                    print(str(stale_ex))
                    continue

    except (TimeoutException, NoSuchElementException) as e:
        print('Timeoutexception, No such element exception')
        print(str(e))
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        next_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Next']")))
        next_button.click()
        continue
    except Exception as e:
        print(' outer exception')
        print(str(e))
        break

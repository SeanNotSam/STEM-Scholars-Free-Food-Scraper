#sean Broderick

import json
import re
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CHROME_WINDOW_SIZE = "1920,1080"
DOWNLOAD_DIR = r"/Users/seanbrod16/Downloads/data"
ELEMENT_LOAD_WAIT_SEC = 30
DELAY_SEC = 2
DELAY_SEC1 = 6
MAIL_BOX = "broderick.81@buckeyemail.osu.edu"
FULL_DATE_PATTERN = r'(\d{4})-(\d{1,2})-(\d{1,2})'
STOP_DATE = "2024-2-14"

def preprocess_element_class(x: str):
    return x.replace(" ", ".")

if __name__ == "__main__":
    with open('authen.json') as json_file:
        authen = json.load(json_file)

    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={CHROME_WINDOW_SIZE}")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver_wait = WebDriverWait(driver, ELEMENT_LOAD_WAIT_SEC)

    # Navigate to outlook.office.com/mail
    driver.get("https://outlook.office.com/mail/")

    # Input my email address
    login_box = (By.NAME, "loginfmt")
    login_box = driver_wait.until(EC.presence_of_element_located(login_box))
    login_box.send_keys(authen["username"])
    login_box.send_keys(Keys.RETURN)

    time.sleep(DELAY_SEC)

    # Input my password
    password_box = (By.NAME, "passwd")
    password_box = driver_wait.until(EC.presence_of_element_located(password_box))
    password_box.send_keys(authen["password"])
    password_box.send_keys(Keys.ENTER)

    time.sleep(DELAY_SEC1)

    # Select the targeted email
    mail = (By.CLASS_NAME, preprocess_element_class("hcptT gDC9O"))
    mail = driver_wait.until(EC.presence_of_element_located(mail))

with open('email_subjects.txt', 'a') as file:

    while True:
        time.sleep(DELAY_SEC)

        # Check stop condition (email date)
        mail.click()
        email_date = (By.CLASS_NAME, preprocess_element_class("AL_OM l8Tnu I1wdR"))
        email_date = driver_wait.until(EC.presence_of_element_located(email_date))
        email_date = re.search(FULL_DATE_PATTERN, email_date.text, re.MULTILINE).group(0)
        if email_date == STOP_DATE:
            break

        time.sleep(DELAY_SEC)

        # Instead of downloading, use cmd+p or ctrl+p to open the print dialog
        # For macOS, use Keys.COMMAND. For Windows/Linux, use Keys.CONTROL
        #webdriver.ActionChains(driver).key_down(Keys.COMMAND).send_keys('p').key_up(Keys.COMMAND).perform()
        #time.sleep(DELAY_SEC-1)
        #webdriver.ActionChains(driver).key_down(Keys.COMMAND).send_keys('p').key_up(Keys.COMMAND).perform()
        #time.sleep(DELAY_SEC-1)

        # Use PyAutoGUI to press Enter
        #pyautogui.press('enter')
        #time.sleep(DELAY_SEC-1)
        #pyautogui.press('enter')

        aria_label = mail.get_attribute('aria-label')
        if aria_label is not None:
            file.write(aria_label)
            file.write('\n')
        
        time.sleep(DELAY_SEC)

        # Return to the email list
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        time.sleep(DELAY_SEC)

        # Move on to the next email
        mail.click()
        webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()
        mail = driver.switch_to.active_element

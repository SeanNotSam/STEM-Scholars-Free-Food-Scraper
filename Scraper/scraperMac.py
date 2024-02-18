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
DOWNLOAD_DIR = r"ARB"
ELEMENT_LOAD_WAIT_SEC = 30
DELAY_SEC = 1
DELAY_SEC1 = 6
MAIL_BOX = "ARB"
FULL_DATE_PATTERN = r'(\d{4})-(\d{1,2})-(\d{1,2})'
STOP_DATE = "2024-2-14"

def preprocess_element_class(x: str):
    return x.replace(" ", ".")

if __name__ == "__main__":
    with open('Scraper/authen.json') as json_file:
        authen = json.load(json_file)

    chrome_options = Options()
    chrome_options.add_argument(f"--window-size={CHROME_WINDOW_SIZE}")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
        "download.prompt_for_download": False,
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver_wait = WebDriverWait(driver, ELEMENT_LOAD_WAIT_SEC)

    driver.get("https://outlook.office.com/mail/")

    login_box = (By.NAME, "loginfmt")
    login_box = driver_wait.until(EC.presence_of_element_located(login_box))
    login_box.send_keys(authen["username"])
    login_box.send_keys(Keys.RETURN)

    time.sleep(DELAY_SEC)

    password_box = (By.NAME, "passwd")
    password_box = driver_wait.until(EC.presence_of_element_located(password_box))
    password_box.send_keys(authen["password"])
    password_box.send_keys(Keys.ENTER)

    time.sleep(DELAY_SEC1)

    # select email
    mail = (By.CLASS_NAME, preprocess_element_class("hcptT gDC9O"))
    mail = driver_wait.until(EC.presence_of_element_located(mail))

with open('email_subjects.txt', 'a') as file:

    while True:
        time.sleep(DELAY_SEC)

        # Stop condition by email date
        mail.click()
        email_date = (By.CLASS_NAME, preprocess_element_class("AL_OM l8Tnu I1wdR"))
        email_date = driver_wait.until(EC.presence_of_element_located(email_date))
        email_date = re.search(FULL_DATE_PATTERN, email_date.text, re.MULTILINE).group(0)
        if email_date == STOP_DATE:
            break

        time.sleep(DELAY_SEC)

        aria_label = mail.get_attribute('aria-label')
        if aria_label is not None:
            file.write(aria_label)
            file.write('\n')
        
        time.sleep(DELAY_SEC)

        #return 
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        time.sleep(DELAY_SEC)

        #move to next email
        mail.click()
        webdriver.ActionChains(driver).send_keys(Keys.DOWN).perform()
        mail = driver.switch_to.active_element

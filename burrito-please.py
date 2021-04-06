from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
bOptions = Options()
bOptions.headless = True

print("Sending request")



browser = webdriver.Firefox(options = bOptions)
browser.get("https://www.chipotle.com/contact-us")

try:
    suggestion_box = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/section/div/div/div/div[2]/div/div[3]'))
    )
    print("Clicking box")
    suggestion_box.click()
    print("Box Clicked")




    suggestion_input = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div[4]/section/div/div/div/div[5]/section/div[2]/div/div/div/div[4]/div/div[2]/form/div/input[1]'))
    )
    
    suggestion_input.click()
    print("Entering 59901")
    suggestion_input.send_keys("59901")
    suggestion_input.send_keys(Keys.ENTER)

    print("Entry complete")
finally:
    browser.close()
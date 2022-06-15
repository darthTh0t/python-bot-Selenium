from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = Service(r"C:\Users\coola\OneDrive\Desktop\Projects\python-bot-Selenium\chromedriver.exe")     # path for webdriver
driver = webdriver.Chrome(service=PATH)

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

driver.get(r"https://www.youtube.com/watch?v=wH3BIDBAFGY")

wait.until(visible((By.CLASS_NAME, "ytp-play-button")))
driver.find_element(By.CLASS_NAME, "ytp-play-button").click()
driver.find_element(By.CLASS_NAME, "ytp-mute-button").click()

while True:
    time.sleep(60)  #seconds
    driver.refresh()

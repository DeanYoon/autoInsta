import threading
from selenium import webdriver
import time

def example_thread():
    chromedriver_path = "./chromedriver"
    driver = webdriver.Chrome(chromedriver_path)
    time.sleep(3)
    driver.get("https://www.instagram.com/")
    time.sleep(30)
    driver.quit()

def example():
    t = threading.Thread(target=example_thread)
    t.start()

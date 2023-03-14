from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import base64
import json

def read_data():
    f = open("seed_urls.json")
    data = json.load(f)
    return data
read_data()


def crawler():
    driver = webdriver.Chrome()
    total_data = {}
    for index,link in enumerate(read_data()):
        driver.get(link)
        content = driver.page_source
        content = content.replace('\n', '')
        screenshot = driver.get_screenshot_as_base64()
        screenshot = screenshot.replace('\n','')
        seed_url = f"seed_url{index}"
        current_url = f"current_url{index}"
        html = f"html{index}"
        base64_image = f"html{index}"
        total_data[seed_url] = link
        total_data[current_url] = link
        total_data[html] = content
        total_data[base64_image] = screenshot
    with open('output.json', 'a') as f:
        json.dump(total_data, f)

crawler()

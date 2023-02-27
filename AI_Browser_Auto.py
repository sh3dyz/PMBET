from selenium import webdriver
from selenium.webdriver.common.by import By

# ID = "id"
# NAME = "name"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

links = [
    "https://pmbet.co.tz/",
    "https://pmbet.co.tz/"
]

d_xpath = {
    "tangazo":"/html/body/app-root/royal-win-popup-v2/div/main/div/div/div",
    "#":"#"
}

def CreateBrowser():
    # REMINDER: make it headless
    driver = webdriver.Firefox()
    return driver

browser = CreateBrowser()

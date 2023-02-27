from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ID = "id"
# NAME = "name"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

links = {
    "home":"https://pmbet.co.tz/",
    "login":"https://pmbet.co.tz/en/auth/signin",
    "casino":"https://pmbet.co.tz/en/livecasino_ms/h-roulette-autoroulette-evolution2"
}

welcm_xpath = {
    "Tangazo":"/html/body/app-root/royal-win-popup-v2/div/main/div/div/div",
    "CloseAds":"/html/body/app-root/royal-win-popup-v2/div/main/div/div/div/button[1]/img"
}

login_xpath = {
    "submit":"/html/body/app-root/app-sign-in/desktopsignincomponent/div/div/main/div/div/form/div/div[5]/button",
    "Error":"/html/body/app-root/app-sign-in/desktopsignincomponent/div/div/main/div/div/form/div/div[3]/div/label/span/p"
}

cas_h = {
    "play":"/html/body/app-root/app-ucasino-game/desktopucasinogamemscomponent/div/div/div/div[2]/button[1]",
    "lobyFrame":"/html/body/app-root/app-ucasino-game/desktopucasinogamemscomponent/div/div/iframe",
    "playCasino":"/html/body/div[4]/div/div[2]/div/div/div/main/section/div[2]/ul/li[13]/div/article/div[1]/div[3]"
}

def CreateBrowser():
    # REMINDER: make it headless
    driver = webdriver.Firefox()
    return driver

browser = CreateBrowser()

def Delay(seconds):
    time.sleep(seconds)

def OpenHome(browser):
    browser.get(links["home"])
    try:
        ads = browser.find_element(By.XPATH, welcm_xpath["Tangazo"])
        cls = browser.find_element(By.XPATH, welcm_xpath["CloseAds"])
    except:
        return "Error find Ad"
    cls.click()
    return True

def Login(browser, username, password):
    browser.get(links["login"])
    Delay(2)
    username = browser.find_element(By.ID, "login-username")
    username.clear() # remove nonsense
    username.send_keys(username)
    password = browser.find_element(By.ID, "login-password")
    password.clear() # remove nonsense
    password.send_keys(password)
    Delay(2)
    login = browser.find_element(By.XPATH, login_xpath["submit"])
    login.click()
    Delay(2)
    try:
        error = browser.find_element(By.XPATH, login_xpath["Error"])
    except:
        return True
    return error.text

def OpenCasino(browser):
    browser.get(links["casino"])
    play = browser.find_element(cas_h["play"])
    play.click()
    Delay(2)
    
    # dive into casino dashboard iframe
    
    loby_frame = browser.find_element(By.XPATH, cas_h["lobyFrame"])
    browser.switch_to.frame(loby_frame)
    # wait it to load then click play
    wait = WebDriverWait(browser, 10)
    play_casino = wait.until(EC.presence_of_element_located((By.XPATH, cas_h["playCasino"])))
    play_casino.click()
    

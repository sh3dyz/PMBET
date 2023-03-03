# Coded By sh3dyz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

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
    "playCasino":"/html/body/div[4]/div/div[2]/div/div/div/main/section/div[2]/ul/li[13]/div/article/div[1]/div[3]",
    "viewMod":"/html/body/div[4]/div[2]/div/div[2]/div[9]/div[2]/div/div/div[1]/div[2]/div[2]/div/button/span/span/svg"
}

def CreateBrowser():
    # REMINDER: make it headless
    driver = webdriver.Firefox()
    return driver

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

def Login(browser, uname, pword):
    browser.get(links["login"])
    Delay(2)
    username = browser.find_element(By.ID, "login-username")
    username.clear() # remove nonsense
    username.send_keys(uname)
    password = browser.find_element(By.ID, "login-password")
    password.clear() # remove nonsense
    password.send_keys(pword)
    Delay(2)
    login = browser.find_element(By.XPATH, login_xpath["submit"])
    login.click()
    Delay(2)
    try:
        error = browser.find_element(By.XPATH, login_xpath["Error"])
    except:
        return True
    return error.text

def waitGetElement(browser, xpath, seconds):
    subiri = WebDriverWait(browser, int(seconds))
    element = subiri.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return element

def OpenCasino(browser):
    browser.get(links["casino"])
    play = browser.find_element(cas_h["play"])
    play.click()
    Delay(2)
    
    # dive into casino dashboard iframe
    
    loby_frame = browser.find_element(By.XPATH, cas_h["lobyFrame"])
    browser.switch_to.frame(loby_frame)
    # wait it to load then click play
    play_casino = waitGetElement(browser, cas_h["playCasino"], "5")
    play_casino.click()
    # REMINDER: we are in the game, but we dont dive out of a frame
    # we gonna proceed with next stuffs
    return True

def openNewTab(browser, tab=None):
    if tab == None:
        browser.execute_script("window.open('', '_blank');")
        return True
    else:
        n_t = len(browser.window_handles)
        if tab - 1 > n_t:
            return "Tab Not Found"
        else:
            browser.switch_to.window(browser.window_handles[int(tab)])
            return True
    
def main():
    # create browser
    browser = CreateBrowser()
    home = OpenHome(browser)
    if home == True:
        # success pass home Ads
        print("Home Ads passed")
    else:
        # failed shit
        print(home)
    # Now lets Login
    openNewTab(browser) # open new tab [1]
    openNewTab(browser, tab=1)
    while True:
        phonenumber = str(input("Enter Phone: "))
        password = str(input("Enter password: "))
        login = Login(browser, phonenumber, password)
        if login == True:
            # Success
            print("Login Success : Lets Bet")
            print("Now Opening Casino...")
            break
        else:
            # imezingua ku login
            print(login)
            continue
    openNewTab(browser) # open new tab [2]
    openNewTab(browser, tab=2) # shift to new tab
    ka_no = OpenCasino(browser)
    if ka_no:
        # opened casino
        print()
        # REMINDER: casino is open!,
        # ?we now need to find game history elements
        # ?Solve logic behind view mod and elements arrangment!
        # ?Solve logic behind network error loading element
        # ?Check Balance, know ho much to bet
        # ?know how much you win
        # ?know how much you loose
        # ?Detect if game round is completed

if __name__ == "__main__":
    main()
# Coded By sh3dyz
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from sklearn .linear_model import LogisticRegression
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

def PredictNumber(history):
    #convert that history to a numpy array
    X = np.array(history[:-1]).reshape(-1, 1)

    #create array for the label - next number according to our history
    Y = np.array(history[1:])

    #lets create logistic regression model and fit it to the data
    md = LogisticRegression()
    md.fit(X, Y)

    #lets use the above model to predict next number
    nx_num = md.predict(np.array([history[-1]]).reshape(-1, 1))[0]

    # #show history
    # print("HISTORY: ", history)
    # #lets print next number
    # print("Possible Next Number: ", nx_num)
    return nx_num

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
    "PvipCasino":"/html/body/div[4]/div/div[2]/div/div/div/main/section/div[2]/ul/li[10]/div/article/div[1]/div[2]",
    "viewMod":"/html/body/div[4]/div[2]/div/div[2]/div[9]/div[2]/div/div/div[1]/div[2]/div[2]/div/button/span/span/svg"
}

cas_game = {
    "Low-Bal-Pop":"/html/body/div[4]/div[2]/div/div[2]/div[6]/div/div",
    "low-Bal-But":"/html/body/div[4]/div[2]/div/div[2]/div[6]/div/div/div/div[3]/div/div/button",
    "Game-Hist":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div/div/div/div[2]/div/div[{}]/div/span",
    "Red-Btn":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/svg/g/rect[45]",
    "Black-Btn":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/svg/g/rect[46]",
    "View-Btn":"/html/body/div[4]/div[2]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[2]/div[2]/div/button/span/span/svg",
    "Balance":"/html/body/div[4]/div[2]/div/div[2]/div[4]/div[3]/div/div/div[1]/div/span[2]/span[2]",
    "Last-Win-Balance":"/html/body/div[4]/div[2]/div/div[2]/div[4]/div[3]/div/div/div[2]/div[2]/span[2]/span[2]",
    "Price-Btn":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[6]/div[3]/div/div/div[2]/div/div[{}]/div[2]/svg/text",
    "Refresh-Btn":"/html/body/div[4]/div[2]/div/div[2]/div[11]/div/div/div/div[2]/div/div[2]/button",
    "result-bod":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[6]/div[1]/div/div/div[2]",
    "Net-Err":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[7]/div[2]/div/div[3]",
    "BetOn":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/div/svg/g/circle[2]",
    "RetOn":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/div/svg/g/circle[2]"
}

auto_vip = {
    "view-classic":"/html/body/div[4]/div[2]/div/div[2]/div[8]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/span/div/div[2]",
    "open-vip":"/html/body/div[4]/div/div[2]/div/div/div/main/section/div[2]/ul/li[10]/div/article/div[1]/div[2]",
    "red-btn":"/html/body/div[4]/div[2]/div/div[2]/div[2]/div/div[6]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/svg/g/rect[45]"
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

def waitGetElement(browser, xpath, seconds, disp=None):
    subiri = WebDriverWait(browser, int(seconds))
    if disp:
        subiri.until(EC.invisibility_of_element_located((By.XPATH, xpath)))
        return True
    else:    
        element = subiri.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element

def OpenCasino(browser):
    browser.get(links["casino"])
    Delay(2)
    play = browser.find_element(By.XPATH, cas_h["play"])
    play.click()
    Delay(2)
    
    # dive into casino dashboard iframe
    
    loby_frame = browser.find_element(By.XPATH, cas_h["lobyFrame"])
    browser.switch_to.frame(loby_frame)
    # wait it to load then click play
    Delay(5)
    play_casino = waitGetElement(browser, cas_h["PvipCasino"], "60") # timeout to 60, play VIP auto 
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
    openNewTab(browser, tab=2) # move to new tab
    ka_no = OpenCasino(browser)
    if ka_no:
        # opened casino
        print()
        # REMINDER: casino is open!,
        # [+]we now need to find game history elements
        # [+]Solve logic behind view mod and elements arrangment!
        # [+]Solve logic behind network error loading element
        # [+]Check Balance, know how much to bet
        # [+]know how much you win
        # ?know how much you loose
        # [+]Detect if game round is completed
        
        global BALANCE # we will update it on every game
        PLAYED_GAMES = [] # kila game tuliyocheza tunaiweka hapa
        global CURRENT_BET_AMOUNT # Amount Handler
        CURRENT_BET = 0 # red or black
        WIN_GAME = 0 # Win Game count
        LOST_GAME = 0 # Lost Game count
        WIN_PERCNT = 0 # Win Percent
        LOST_PERCNT = 0 # Lost percent
        FULL_HIST = list()
        global LAST_WIN_B
        GAMEHIST = []
        while True:
            FULL_HIST = FULL_HIST + GAMEHIST
            def check_balance(browser):
                # return balance as int
                try:
                    balance = browser.find_element(By.XPATH, cas_game["Balance"])
                    return int(balance.text)
                except Exception as Error:
                    return Error
                
            def check_pop(browser):
                try:
                    pop = browser.find_element(By.XPATH, cas_game["Low-Bal-Pop"])
                    close_pop = browser.find_element(By.XPATH, cas_game["low-Bal-But"])
                    close_pop.click()
                    return True # Kama ipo 
                except Exception as Error:
                    return Error # Kama haipo
                
            def GameHist(browser):
                red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
                histlist = list() # store game hist as list
                colorlist = list()
                try:
                    for i in range(12):
                        hist = browser.find_element(By.XPATH, cas_game["Game-Hist"].format(i+1))
                        histlist.append(hist.text)
                    for i in histlist:
                        if i in red:
                            colorlist.append(1)
                        elif i == 0:
                            colorlist.append(0)
                        else:
                            colorlist.append(2)
                    colorlist.reverse() # same listing as casino history
                    return colorlist
                except Exception as Error:
                    return Error # Error maybe there is other frame on top of this
            
            def changeAmount(browser, bei):
                # Bei : 1 = 100, 2 = 100, 3 = 1000
                # Auto VIP roulate, Bet price start with 200
                # So we use 1 = 200, 2 = 400 etc...
                try:
                    amount = browser.find_element(By.XPATH, cas_game["Price-Btn"].format(str(bei)))
                    amount.click()
                    return True # amount changed
                except Exception as Error:
                    return Error
            
            def NetError(browser):
                try:
                    net = browser.find_element(By.XPATH, cas_game["Net-Err"])
                    return True
                except Exception as Error:
                    return Error
                
            def LastWinBalance(browser):
                try:
                    balance = browser.find_element(By.XPATH, cas_game["Last-Win-Balance"])
                    return int(balance.text)
                except Exception as Error:
                    return Error
            
            def RoundDone(browser):
                try:
                    resbar = browser.find_element(By.XPATH, cas_game["result-bod"])
                    # if not exist basi game inaendelea
                    # lets return whole method, tutakagua mbele kama ni games result au ni lighting au ni countdown
                    return resbar
                except Exception as Error:
                    return "False: {}".format(Error) 
            
            def BetColor(browser, prediction):
                # we bet on red and black
                # means 1 = red and 2 = black
                if int(prediction) == 1: # means we bet on red
                    try:
                        bet_red = browser.find_element(By.XPATH, cas_game["Red-Btn"])
                        bet_red.click()
                        return True
                    except Exception as Error:
                        return Error
                elif int(prediction) == 2: # means we bet on black
                    try:
                        bet_black = browser.find_element(By.XPATH, cas_game["Black-Btn"])
                        bet_black.click()
                        return True
                    except Exception as Error:
                        return Error
                else:
                    return False
            
            def ChangeView(browser):
                # no need for view type, we deal with classic only
                try:
                    classic = browser.find_element(By.XPATH, auto_vip["view-classic"])
                    classic.click()
                    return True
                except Exception as Error:
                    return Error
            
            # Change View to Classic First
            view = ChangeView(browser)
            if view != True:
                print("Failed To Change View Mod To Classic!\nError: {}".format(view))
                sys.exit(1) # we quit it for debugging
            else:
                Delay(3)
                pass
            
            global isStarted
            
            def GameProg(browser, skip=None):
                while True: # detect game progress
                    # check and remove low price btn
                    pO = check_pop(browser)
                    if pO:
                        # low balance, ask user to add funds
                        print("Low Balance Please add min amount for Bet, 200 Tsh")
                        pass
                    else:
                        pass
                    # check if have current bet
                    try:
                        rb = browser.find_element(By.XPATH, cas_game["BetOn"]) # Find other fucking xpath
                        # we need to wait till that shit money disapper
                        waitGetElement(browser, cas_game["BetOn"], 60, disp=True)
                    except:
                        pass
                    if skip:
                        waitGetElement(browser, cas_game["result-bod"], 60, disp=True)
                    skip = None
                    rnd = RoundDone(browser)
                    if rnd.startswith("False:"):
                        print("Error Generated on Checking Round:\nError: {}".format(rnd))
                        continue
                    else:
                        rst = rnd.text
                        if "PLACE YOUR BETS".lower() == rst.lower():
                            # Bet Time
                            isStarted = True
                            break # stop and lets Go!
                        elif "WAIT FOR NEXT GAME".lower() == rst.lower():
                            # lets wait
                            continue
                        else:
                            # result
                            continue
            GameProg()
            
            gmh = GameHist(browser)
            if str(type(wb))[8:][:-2] != "list":
                print("Failed to get History\nError: {}".format(gmh))
                sys.exit(1)
            else:
                GAMEHIST = gmh
            
            # update last win balance
            wb = LastWinBalance(browser)
            if str(type(wb))[8:][:-2] != "int":
                print("Failed to get last win balance\nError: {}".format(wb))
                sys.exit(1)
            else:
                LAST_WIN_B = wb
            
            # lets check if we win or we lost
            if CURRENT_BET in [1, 2]:
                if gmh[0] == CURRENT_BET:
                    # Win
                    WIN_GAME += 1
                    WIN_PERCNT = (WIN_GAME / len(PLAYED_GAMES)) * 100
                    print("You Win : {} Tsh".format(str(wb)))
                    print("Win Percent : {}%".format(str(WIN_PERCNT)))
                    CURRENT_BET = 0
                else:
                    # Lost
                    LOST_GAME += 1
                    LOST_PERCNT = (LOST_GAME / len(PLAYED_GAMES)) * 100
                    print("You Lost : {} Tsh".format(str(CURRENT_BET_AMOUNT)))
                    print("Lost Percent : {}%".format(str(LOST_PERCNT)))
                    CURRENT_BET = 0
            else:
                pass
            
            # set bet amount 
            betamount = changeAmount(browser, 1) # REMEINDER: 1 = 200, 2 = 400 etc...
            if betamount != True:
                print("Failed To change Bet Amount\nError: {}".format(betamount))
                sys.exit(1)
            else:
                CURRENT_BET_AMOUNT = 200
            
            # update balance
            bl = check_balance(browser)
            if str(type(bl))[8:][:-2] != "int":
                print("Failed To Get Balance\nError: {}".format(bl))
                sys.exit(1)
            else:
                BALANCE = bl
                
            # INABIDI TUMPE AI wetu mchongo ajifunze hii history!
            next_number = PredictNumber(GAMEHIST)
            if next_number == 1:
                CURRENT_BET = 1
                if False:
                    Bet_Red = BetColor(browser, 1)
                    if Bet_Red != True:
                        # we got damn Error
                        print("There is Error in Placing Red color Bet\nError: {}".format(Bet_Red))
                        pass
                    else:
                        # Bet accepted
                        print("Bet is accepted")
                        PLAYED_GAMES.append(1)
                        Delay(18) # inachukua sec 20 hadi round kuwa closed
            elif next_number == 2:
                CURRENT_BET = 2
                if False:
                    Bet_Black = BetColor(browser, 2)
                    if Bet_Black != True:
                        # we got damn Error
                        print("There is Error in Placing Red color Bet\nError: {}".format(Bet_Black))
                        pass
                    else:
                        # Bet accepted
                        print("Bet is accepted")
                        PLAYED_GAMES.append(2)
                        Delay(18) # inachukua sec 20 hadi round kuwa closed
                else:
                    # dont bet on zero
                    GameProg(browser, skip=True)
                    

if __name__ == "__main__":
    main()
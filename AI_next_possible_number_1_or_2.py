# Coded By sh3dyz
import numpy as np
from sklearn .linear_model import LogisticRegression
import random

# behind the game there is red and black color, so we will use 1 = red and 2 = black
# and our AI will use atleast 20 past result to learn and guess next number if
# its 1 or 2, (red or black)

# below is our history from game
history = [] #minmum of one sample
for i in range(20):
    history.append(random.randint(1,2)) # we add some samples
history_bk = history
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

win = 0 # total win
los = 0 # total loss
totg = int(input("Enter number of games: ")) # total game
winp = 0 # win %
losp = 0 # loss %

for i in range(totg):
    pn = PredictNumber(history)
    rn = int(random.randint(1, 2))
    history.append(rn)
    history_bk.append(rn)
    del(history[0]) # we need to learn from few history
    
    # lets verify if AI win or Not
    if pn == rn:
        win += 1
    else:
        los += 1

# calculate percantage
winp = (win / totg) * 100 
losp = (los / totg) * 100
print("AI Win : {}\nAI Loss : {}\nTotal Games : {}".format(win, los, totg))
print("Win Percentage: {}%\nLoss percantage: {}%".format(int(winp), int(losp)))
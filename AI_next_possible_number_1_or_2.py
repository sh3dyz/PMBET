import numpy as np
from sklearn .linear_model import LogisticRegression
import random

# below is our history from game
history = [] #minmum of one sample
for i in range(10):
    history.append(random.randint(1,2)) # we add some samples
    
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

win = 0
los = 0
totg = int(input("Enter number of games: "))
winp = 0
losp = 0

for i in range(totg):
    pn = PredictNumber(history)
    rn = int(random.randint(1, 2))
    history.append(rn)
    
    # lets verify if AI win or Not
    if pn == rn:
        win += 1
    else:
        los += 1
winp = (win / totg) * 100
losp = (los / totg) * 100
print("AI Win : {}\nAI Loss : {}\nTotal Games : {}".format(win, los, totg))
print("Win Percentage: {}%\nLoss percantage: {}%".format(int(winp), int(losp)))
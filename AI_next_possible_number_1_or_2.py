import numpy as np
from sklearn .linear_model import LogisticRegression
# below is our history from game
history = [1, 2, 2, 1, 2, 1, 2, 1, 1, 2]

#convert that history to a numpy array
X = np.array(history[:-1]).reshape(-1, 1)

#create array for the label - next number according to our history
Y = np.array(history[1:])

#lets create logistic regression model and fit it to the data
md = LogisticRegression()
md.fit(X, Y)

#lets use the above model to predict next number
nx_num = md.predict(np.array([history[-1]]).reshape(-1, 1))[0]

#show history
print("HISTORY: ", history)
#lets print next number
print("Possible Next Number: ", nx_num)
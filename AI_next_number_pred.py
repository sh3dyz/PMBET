import numpy as np
from sklearn.linear_model import LinearRegression

# Define past numbers as input data
xtrain = [[1], [2], [3], [4]]
print(f"X Trained Data : {train}")
X_train = np.array(train)

# Define next numbers as output data
ytrain = [6, 7, 8, 9]
print(f"Y Trained Data: {ytrain}")
y_train = np.array(ytrain)

# Create linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X_train, y_train)

# Predict the next number based on the past numbers
X_test = np.array([[int(input("Enter Number To predect: "))]])
y_pred = model.predict(X_test)

print(int(y_pred))

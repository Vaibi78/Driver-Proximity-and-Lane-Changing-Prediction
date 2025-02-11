import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle #To save the models

# 1. Load the data
data = pd.read_csv('data/traffic_data.csv')

# 2. Prepare the data
X = data[['Distance_Main_Next_Lane', 'Relative_Speed']]
y = data['Lane_Change']

# 3. Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model (Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# 6. Save the model (optional)
filename = 'models/lane_change_model.pkl'
pickle.dump(model, open(filename, 'wb')) #Use dump to write the model to a file

print(f"Model dumped into {filename}")

import pickle
import argparse

#Load model function
def load_model(filename):
    try:
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        print(f"Error: Model file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

#Prediction function
def predict_lane_change(model, proximity, speed):
    try:
        prediction = model.predict([[proximity, speed]])[0]
        return prediction
    except Exception as e:
        print(f"Error during prediction: {e}")
        return None
# 1. Load the trained model
filename = 'models/lane_change_model.pkl'
loaded_model = load_model(filename)

# 2. Get new data from the command line
parser = argparse.ArgumentParser(description='Predict lane change based on proximity and speed.')
parser.add_argument('--proximity', type=float, required=True, help='Distance to the next lane vehicle')
parser.add_argument('--speed', type=float, required=True, help='Relative speed to the next lane vehicle')

args = parser.parse_args()
proximity = args.proximity
speed = args.speed

# 3. Make a prediction
if loaded_model:
    prediction = predict_lane_change(loaded_model, proximity, speed)

    if prediction is not None:
        if prediction == 1:
            print("Predicted: Lane change is likely.")
        else:
            print("Predicted: Lane change is unlikely.")
else:
    print("Error: Model not loaded. Please ensure the model is correctly trained and saved.")

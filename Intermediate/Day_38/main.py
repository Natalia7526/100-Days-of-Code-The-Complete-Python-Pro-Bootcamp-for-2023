import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_API_KEY = os.environ["NUTRITIONIX_API_KEY"]
SHEETY_API_KEY = os.environ["SHEETY_API_KEY"]
SHEETY_SPREADSHEET_ID = os.environ["SHEETY_SPREADSHEET_ID"]

# Constants
GENDER = "Female"
WEIGHT_KG = 64
HEIGHT_CM = 170
AGE = 27

# API credentials and endpoints
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_WORKOUTS_ENDPOINT = f"https://api.sheety.co/{SHEETY_SPREADSHEET_ID}/myWorkouts/workouts"


def get_nutritionix_exercises(query):
    """
    Fetches exercise data from Nutritionix API based on given query.
    """
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_API_KEY,
    }
    parameters = {
        "query": query,
    }
    response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, json=parameters)
    return response.json()


def add_workouts():
    """
    Adds workouts fetched from Nutritionix API to the Sheety spreadsheet.
    """
    exercises = get_nutritionix_exercises(input("Tell me which exercises you did: "))
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    headers = {"Authorization": f"Bearer {SHEETY_API_KEY}"}

    for exercise in exercises.get("exercises", []):
        workout_data = {
            "workout": {
                "Date": current_time.split()[0],
                "Time": current_time.split()[1],
                "Exercise": exercise["name"].title(),
                "Duration": exercise["duration_min"],
                "Calories": exercise["nf_calories"]
            }
        }
        response = requests.post(SHEETY_WORKOUTS_ENDPOINT, json=workout_data, headers=headers)
        if response.status_code != 200:
            print(f"Failed to add workout for exercise: {exercise['name']}")


# Main function call
add_workouts()

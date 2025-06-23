import datetime
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# print("App ID:", os.getenv("app_id"))
# print("App Key:", os.getenv("app_key"))

GENDER = "female"
WEIGHT = 58
HEIGHT = 155
AGE = 21

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did? ")

headers = {
    "x-app-id": os.getenv("app_id"),
    "x-app-key": os.getenv("app_key"),
    "Content-Type": "application/json"
}
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=params, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Start of Step 4

today_date = datetime.datetime.now().strftime("%d%m%Y")
now_time = datetime.datetime.now().strftime("%X")

sheet_endpoint = os.environ["sheety_endpoint"]
for exercise in result["exercises"]:
    workout_data = {
        "folha1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


    # Sheety Authentication Option 1: No Auth
    sheet_response = requests.post(sheet_endpoint, json=workout_data)
    # print(sheet_response.json())

    #  Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=workout_data,
        auth=(os.getenv("sheety_username"), os.getenv("sheety_password"))
    )
    print(f"Sheety Response: \n {sheet_response.text}")

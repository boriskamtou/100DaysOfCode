import requests


API_KEY = "3b8020d579ee0036bda3c0ada8c76ec7"
APP_ID = "4c9394ce"

GENDER = "male"
AGE = 25
WEIGHT = 86

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": str(APP_ID),
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

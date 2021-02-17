import json
import requests
def client():
    response=requests.post(
        "http://127.0.0.1:8000/teachers",
        {
            "id":3,
            "surname_of_teacher":"Anna",
            "years_old":22

        }
    )
    print(response.text)
    #response=json.loads(response.text)
    #print(response["can_be_cached"])
client()
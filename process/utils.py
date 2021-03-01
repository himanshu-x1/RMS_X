import requests
import json

def sendTextMessage(message,contactno):
    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {
        "authorization": "UV6Fl6CIKIhRzrUWa05bOK6ZtYsALx0ggjd7ycmQC6v4Q1z5xLGJ4JLBOveQ",
        "sender_id": "CHKSMS",
        "message": message,
        "Language": "english",
        "variables_values": "12345",
        "route": "s",
        "numbers": contactno}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data =response.text
    d1 = json.loads(json_data)

    return d1['return']



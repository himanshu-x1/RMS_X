
import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {"authorization":"UV6Fl6CIKIhRzrUWa05bOK6ZtYsALx0ggjd7ycmQC6v4Q1z5xLGJ4JLBOveQ",
               "sender_id":"CHKSMS",
               "message":"2",
               #"variables_values":"12345|asdaswdx",
               "route":"s",
               "numbers":"9422443358"}

headers = {
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
# In US/Canada
# $3/50 texts
# $5/200 texts

import requests
import time
from datetime import date, datetime

def send_sms(phone_number, message):
    url = "https://textbelt.com/text"
    payload = {
        "phone": phone_number,
        "message": message,
        "key": "698c67cf236deb82c5d696e5b05142dc10f696e6flTuF0pX2j8LcR0bH4FVGOiuM", 
    }
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("SMS sent successfully!")
        else:
            print(f"Failed to send SMS. Error: {response.text}")
    except requests.RequestException as e:
        print(f"Error sending SMS: {e}")
        
# Example usage:
send_sms("+18326897908", "SortOptions: VALE, PBR, BP")
time.sleep(3)
send_sms("+17635875117", "SortOptions: VALE, PBR, BP")   #Dave
time.sleep(3)
send_sms("+18327823690", "SortOptions: VALE, PBR, BP")   #Xing
time.sleep(3)
send_sms("+12818182512", "SortOptions: VALE, PBR, BP")   #Wang

now = datetime.now()
currentDatetime = now.strftime("%m%d%Y-%H%M%S")
print(f"Current date time is " + currentDatetime)
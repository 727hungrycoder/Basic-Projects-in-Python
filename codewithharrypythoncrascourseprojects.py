
"""
email validation in python

import re
pattern  = re.compile(r"(^[\w\d]+[\. _]?[\d\w])@([\w])+\.([a-z]+)")
user_email= input("Enter your mail")

if re.search(pattern,user_email):
    print("right email")
else:
    print("Wrong email")

"""

# Robo speaker in Python.

# os. system() is the state code that is returned after the execution result is executed in the Shell, with 0 indicating a successful execution.
"""


While using mac command  use say. Only for mac
x = input("What do you want to speak")
command=f"say{x}"
os.system(command)

"""
"""



weather api app

The requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

"""

"""import requests
import json
while True:

            city = input("Enter the name of the city\n")

            url = f"https://api.weatherapi.com/v1/current.json?key=82d3ce35736a48c9810102240231110&q={city}&aqi=no"
            r = requests.get(url)
            wdic = json.loads(r.text)
            w=wdic["current"]["temp_c"]
            print(f"the current weather in {city} is {w}")
            if city == "Ranchi":
                break


 """

# image resizer

#  waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed.

 # import cv2 install module opencv-python for cv2 library













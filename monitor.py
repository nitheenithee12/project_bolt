from boltiot import Bolt, Sms #Import Sms and Bolt class from boltiot library
import json, time
import urllib.request
import requests
import threading
import json

water_depth_storage = 30 # the distance between device and  garbage in dustbin in cm

API_KEY = "0afa*b9c-689a-4ff3*9513-34*d0dfa8*28" #use your credentials.
DEVICE_ID  = "BOLT*7*8*52"


mybolt = Bolt(API_KEY, DEVICE_ID) #Create object to fetch data

response = mybolt.serialRead(10)
print(response)

while True:
    response = mybolt.serialRead('10')  #Fetching the value from Arduiprint (data) = json.loads
    print(response)

while True:
    response = mybolt.serialRead('10')  #Fetching the value from Arduino
    data = json.loads(response)
    water_level = data['value'].rstrip()
    print("water level is", water_level)
    URl='https://api.thingspeak.com/update?api_key=X3*3W7NH2*MVS*25'  #pushing data to the thingspeak, to visualize the data
    # and to track the water usage...
    HEADER='&field1={}'.format(water_level)
    NEW_URL = URl+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)

    if int(water_level) > water_depth_storage:
        print("warning:: water level got decreased......")
    time.sleep(200)

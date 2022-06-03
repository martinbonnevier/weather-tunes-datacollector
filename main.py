from sense_hat import SenseHat
import time
import pymongo
from pymongo import MongoClient
import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()


cluster = join(MongoClient("mongodb+srv://iot:", os.environ.get("PASSWORD"), "@iotcluster.pfotz.mongodb.net/iot?retryWrites=true&w=majority"))
db = cluster["UserData"]
collection = db["python"]

starttime = time.time()
counter = 0
while True:
    counter = counter + 1
    print("tick: ")
    print(counter)
    sense = SenseHat()
    sense.clear()

    pressure = sense.get_pressure()
    print(pressure)
    temp = sense.get_temperature()
    print(temp)
    humidity = sense.get_humidity()
    print(humidity)
    collection.insert_one({"time":time.time(), "temperature":temp, "humidity": humidity, "pressure": pressure})
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))

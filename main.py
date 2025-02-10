import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time
import os 

DEVICE_NUMBER = int(os.getenv("DEVICE_NUMBER",3))
client = mqtt.Client()
print("[INFO] Device Number:",DEVICE_NUMBER)
# 設定連線資訊(IP, Port, 連線時間)
try:
    client.connect(
        os.getenv("MQTT_SERVER_IP","127.0.0.1"), 
        int(os.getenv("MQTT_SERVER_PORT",1883)),
        60
    )
except Exception as e:
    client.connect(
        "127.0.0.1", 
        1883,
        60
    )
while True:
    t = datetime.datetime.now().isoformat(timespec='seconds')
    for i in range(1,DEVICE_NUMBER+1):
        payload = random.randint(0,30)
        clientID = f"PythonTest0{i}"
        print (f"[{clientID}]:現在溫度：",payload)
        client.publish(f"home/{clientID}", payload)
    time.sleep(2)
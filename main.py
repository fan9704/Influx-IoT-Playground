import paho.mqtt.client as mqtt
import random
import json  
import datetime 
import time
import os 

clientID = "PythonTest01"

# 連線設定
# 初始化地端程式
client = mqtt.Client()

# 設定連線資訊(IP, Port, 連線時間)
client.connect(
    os.getenv("MQTT_SERVER_IP","127.0.0.1"), 
    int(os.getenv("MQTT_SERVER_PORT",1883)),
    60
)

while True:
    t0 = random.randint(0,30)
    t1 = random.randint(0,30)
    t = datetime.datetime.now().isoformat(timespec='seconds')
    # Temperature and Humidity
    # payload = {
    #     'Temperature' : t0 ,
    #     "Humidity":t1,
    #     'Time' : t
    # }
    payload = t0
    # payload = json.dumps(payload, separators=(',', ':'))
    print (payload)
    client.publish(f"home/{clientID}", payload)
    time.sleep(2)
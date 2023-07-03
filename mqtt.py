print("MQTT with Adafruit IO")
import sys
import time
import random
import requests
from Adafruit_IO import MQTTClient

AIO_FEED_ID=""
AIO_USERNAME = "minh_nhu"
AIO_KEY = "aio_ySuj88kSvTNLpHE5xvw5i3JNxKzH"

def connected(client):
    print("Connecting to the server ...")
    client.subscribe(AIO_FEED_ID)
    client.subscribe("button1")
    client.subscribe("button2")

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe successfully ...")

def disconnected(client):
    print("Disconnecting ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Input data: " + payload)

client = MQTTClient(AIO_USERNAME , AIO_KEY)

client.on_connect = connected  # function pointer
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()


print("Test Eval")
equation = 'x1 + 2 * x2 + x3'
def modify_value(x1, x2, x3):
 result = eval(equation)
 print(result)
 return result
modify_value(1,2,3)

def connected(client):
    print("Server connected ...")
    client.subscribe("button1")
    client.subscribe("button2")
    client.subscribe("equation")
global_equation = ""
def message(client , feed_id , payload):
    print("Received: " + payload)
    if(feed_id == "equation"):
        global_equation = payload
    print(global_equation)

def init_global_equation():
    headers = {}
    aio_url = "https://io.adafruit.com/api/v2/minh_nhu/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]
    print("Get lastest value:", global_equation)




while True:
    time.sleep(5)
    value1 = random.randint(20, 70)
    value2 = random.randint(0, 100)
    value3 = random.randint(0, 1000)
    value4 = modify_value (value1, value2,value3)
    print("Updating ...")
    client.publish("sensor1", value1)
    client.publish("sensor2", value2)
    client.publish("sensor3", value3)
    client.publish("sensorequation",value4)
    pass


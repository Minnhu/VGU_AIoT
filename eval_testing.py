print("Test Eval")
equation = 'x1 + 2 * x2 + x3'
def modify_value(x1, x2, x3):
 result = eval(equation)
 print(result)
 return result

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

modify_value(1,2,3)
init_global_equation()




import paho.mqtt.client as mqtt
import json
import configparser

#config = configparser.ConfigParser()

#config.read('settings.ini')

mqtt_ip = "localhost"
mqtt_topic = "sensors/pico1"
logfile = "sensor_data.txt"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        client.subscribe(mqtt_topic)
    else:
        print("Connection failed")
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(client)
        print(userdata)
        print(data)
        with open(logfile, "a") as f:
            f.write(str(data) + "\n")
    except Exception as e:
        print(e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_ip, 1883, 60)
client.loop_forever()







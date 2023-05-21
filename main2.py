import paho.mqtt.client as mqttclient
from main import Application
from threading import Thread

broker_address = "broker.emqx.io"
port = 1883
user = "maksym_kashuba"
password = "1234566"

app = Application()

def mqtt_loop():
    def on_connect(client, userdata, flags, rc):
        print("Connecting to broker...")
        if rc == 0:
            print("Connected to broker")
            client.subscribe("THEBESTMessage")
        else:
            print(f"Connection failed with error code {rc}")

    def on_message(client, userdata, message):
        print("Get message:", message.payload.decode())
        payload = message.payload.decode()
        parts = payload.split(':')
        if len(parts) == 2:
            try:
                value = int(parts[1].strip())
                if(value <= 62):
                    app.setCounter(value)
            except ValueError:
                print("Invalid numerical value:", payload)
        else:
            print("Invalid payload format:", payload)

    def on_publish(client, userdata, mid):
        print("Message published with ID:", mid)

    client = mqttclient.Client("new1")
    client.username_pw_set(user, password=password)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.connect(broker_address, port, 60)

    client.loop_forever()

mqtt_thread = Thread(target=mqtt_loop)
mqtt_thread.start()

app.run()
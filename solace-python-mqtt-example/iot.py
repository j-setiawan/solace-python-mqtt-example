import certifi
import paho.mqtt.client as mqtt
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="Your Solace IoT endpoint")
parser.add_argument("-u", "--username", action="store", required=True, dest="username", help="Your Solace IoT username")
parser.add_argument("-p", "--password", action="store", required=True, dest="password", help="Your Solace IoT password")

args = parser.parse_args()
host = args.host
username = args.username
password = args.password

# Callback on connection
def on_connect(client, userdata, flags, rc):
    print(f'Connected (Result: {rc})')
    client.subscribe(f'iot/{username}/messages')


# Callback when message is received
def on_message(client, userdata, msg):
    print(f'Message received on topic: {msg.topic}. Message: {msg.payload}')

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.tls_set(ca_certs=certifi.where())
client.username_pw_set(username, password)
client.connect(host, port=8883)

client.loop_start()

while True:
    client.publish(f'iot/{username}/heartbeat', payload='ping')

    time.sleep(1.0)

# solace-python-mqtt-example
Get started with MQTT on Python with Solace and [Paho MQTT](https://pypi.org/project/paho-mqtt/).

After creating a service on [Solace Cloud](https://console.solace.cloud), check under the "Connect" tab for the MQTT connection details:
![Solace Cloud MQTT Connection Details](https://raw.githubusercontent.com/j-setiawan/solace-python-mqtt-example/master/sc_mqtt.png)

Edit `mqtt.py` with your username, password, and URL (omit the protocol, like `wss://` and the port, which is a separate argument). There are some differences depending on which protocol you choose
* MQTT Host (`tcp://`)
  * Remove SSL: ~~client.tls_set(ca_certs=certifi.where())~~
* WebSocket MQTT Host (`ws://`)
  * Remove SSL: ~~client.tls_set(ca_certs=certifi.where())~~
  * Add Websocket transport to client: `client = mqtt.Client(transport='websockets')`
* Secured MQTT Host (`ssl://`)
  * Use SSL: `client.tls_set(ca_certs=certifi.where())`
* WebSocket Secured MQTT Host (`wss://`)
  * Use SSL: `client.tls_set(ca_certs=certifi.where())`
  * Add Websocket transport to client: `client = mqtt.Client(transport='websockets')`

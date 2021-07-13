import paho.mqtt.publish as publish
 

def send(Nachricht):
    MQTT_SERVER = "localhost"
    MQTT_PATH = "test_c"
    print(Nachricht)
    publish.single(MQTT_PATH, Nachricht, hostname=MQTT_SERVER)
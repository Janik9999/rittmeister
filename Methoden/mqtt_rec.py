import paho.mqtt.client as mqtt
from Methoden import Wert
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test_c")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    Message=str(msg.payload)
    print(Message)
    Message=Message.replace("'b", "")
    Message=Message.replace("b'", "")
    Message=Message.replace("'", "")
    Messagesplit=Message.split("_",1)
    Wert.Fach.append(Messagesplit[0])
    
    #Hier muss eine DB Anfrage statt finden
    
    # more callbacks, etc
 
#client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message
#client.connect("localhost", 1883, 60)
#client.loop_forever()
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

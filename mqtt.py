import paho.mqtt.client as mqtt
import os, urlparse

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)
def main():
    mqttc = mqtt.Client()
    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # Uncomment to enable debug messages
    #mqttc.on_log = on_log
    # Parse CLOUDMQTT_URL (or fallback to localhost)
    url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://pi:raspberry@m10.cloudmqtt.com:14396')
    url = urlparse.urlparse(url_str)
    topic = url.path[1:] or 'pi'
    print ('URL')
    print(url)
    # Connect
    mqttc.username_pw_set(url.username, url.password)
    mqttc.connect(url.hostname, url.port)
    # Start subscribe, with QoS level 0
    mqttc.subscribe(topic, 0)
    # Publish a message
    mqttc.publish(topic, "my message")
    # Continue the network loop, exit when an error occurs
    rc = 0
    while rc == 0:
        rc = mqttc.loop()
    print("rc: " + str(rc))
def connect():
    mqttc = mqtt.Client()
    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://pi:raspberry@m10.cloudmqtt.com:14396')
    url = urlparse.urlparse(url_str)
    topic = url.path[1:] or 'pi'
    mqttc.username_pw_set(url.username, url.password)
    mqttc.connect(url.hostname, url.port)
    return mqttc
def publish(mqttc,message):
    mqttc.publish(topic, message)

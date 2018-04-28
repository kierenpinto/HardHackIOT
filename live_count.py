from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import paho.mqtt.client as mqtt
import os, urlparse

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))
    #print("mqqtSEND: "+ str(len(obj)))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
#mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://pi:raspberry@m10.cloudmqtt.com:14396')
url = urlparse.urlparse(url_str)
topic = url.path[1:] or 'pi'
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    ratio = image.shape[1] / float(image.shape[0])
    grayImage = cv2.resize(image, (int(ratio * 450), 450))
    faces = face_cascade.detectMultiScale(grayImage)
    if len(faces) == 0:
        print "No faces found"
    else:
        print faces
        print faces.shape
        print "Number of faces detected: " + str(faces.shape[0])
    mqttc.publish(topic, str(len(faces)))
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # key = cv2.waitKey(1) & 0xFF
    # # if the `q` key was pressed, break from the loop
    # if key == ord("q"):
    # 	break

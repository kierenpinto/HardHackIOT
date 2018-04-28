from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
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
    # show the frame
    cv2.imshow("Frame", grayImage)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
    	break

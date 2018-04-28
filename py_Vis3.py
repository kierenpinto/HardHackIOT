import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    ret, image = cap.read()

    #ratio = image.shape[1] / float(image.shape[0])
    #grayImage = cv2.resize(image, (int(ratio * 450), 450))
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',image)
    cv2.waitKey()
    ratio = gray.shape[1]
    grayImage = cv2.resize(gray,(50, 450))
    faces = face_cascade.detectMultiScale(grayImage)

    # print type(faces)
    # cv2.imshow('frame',grayImage)
    # cv2.waitKey()
    # if len(faces) == 0:
    #     print "No faces found"

    # else:
    #     print faces
    #     print faces.shape
    #     print "Number of faces detected: " + str(faces.shape[0])

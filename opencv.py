import cv2
import numpy as np
img = cv2.imread('cambridge1.jpg')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml)
gray= cv2.cvtColor(img,cv2,COLOR_BGR2GRAY)
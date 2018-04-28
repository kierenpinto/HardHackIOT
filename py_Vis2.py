import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv2.imread('test.jpg', 0)
ratio = image.shape[1] / float(image.shape[0])
grayImage = cv2.resize(image, (int(ratio * 450), 450))

#cv2.imshow('test', grayImage)
#cv2.waitKey()


faces = face_cascade.detectMultiScale(grayImage)

print type(faces)

if len(faces) == 0:
    print "No faces found"

else:
    print faces
    print faces.shape
    print "Number of faces detected: " + str(faces.shape[0])

    for (x,y,w,h) in faces:
        cv2.rectangle(grayImage,(x,y),(x+w,y+h),(0,255,0),1)

    cv2.rectangle(grayImage, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
    cv2.putText(grayImage, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

    cv2.imshow('Image with faces',grayImage)
    cv2.waitKey()
    cv2.destroyAllWindows()

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import copy

PHOTOS = "./opencv-course-master/Resources/Photos"
VIDEOS = "./opencv-course-master/Resources/Videos"

img_number = 0

def cvdir(string):
    d = dir(cv)
    d = filter(lambda s: string in s.lower(), d)
    for item in d:
        print(item)
        
def display(image):
    global img_number
    cv.imshow(str(img_number), image)
    img_number += 1
    

#img = cv.imread(f'{PHOTOS}/lady.jpg')
#img = cv.imread(f'{PHOTOS}/group 2.jpg')
img = cv.imread(f'{PHOTOS}/group 1.jpg')


# FACE DETECTION WITH HAARCASCADES (just yes or no not recoginizing whose face)
# open cv comes with pretrained classifiers for this (yay)

# convert to grayscale because face detection uses edges not color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
display(gray)

# load harrcascade file
FILE = "classifiers/harr_face.xml"
haar_cascade = cv.CascadeClassifier(FILE)

# adjusting scale factor and minimum neighbors can be used to adjust the sensitivity of the detector
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1) # number of neighbors a rect should have to be a face
# returns the rect coords of the face

print(len(faces_rect))
print(faces_rect)

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 200, 0), thickness = 2)
display(img)
    









cv.waitKey(10000)
cv.destroyAllWindows()
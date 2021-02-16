import cv2 as cv
import numpy as np

PHOTOS = "./opencv-course-master/Resources/Photos"
VIDEOS = "./opencv-course-master/Resources/Videos"

img = cv.imread(f"{PHOTOS}/cat.jpg")

# GRAYSCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

# Edge cascade (edge detection)
canny = cv.Canny(img, 125, 175)
blurred = cv.Canny(blur, 125, 175) # reduce edges found by blurring image first

# Dilate an Image using canny edges
dilated = cv.dilate(canny, (7, 7), iterations=3) # can up the iterations

# undo the dilations
eroded = cv.erode(dilated, (7, 7), iterations = 3)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # CUBIC IS HIGHER QUALITY THAN LINEAR

# cropping
cropped = img[-400:-50, -300:]


#cv.imshow("Cat", img)
#cv.imshow("Cat", canny)
#cv.imshow("Cat2", blurred)
#cv.imshow("dil", dilated)
#cv.imshow('er', eroded)
#cv.imshow('res', resized)
cv.imshow('crop', cropped)

cv.waitKey(7000)
cv.destroyAllWindows()
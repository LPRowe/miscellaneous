import cv2 as cv
import numpy as np

PHOTOS = "./opencv-course-master/Resources/Photos"
VIDEOS = "./opencv-course-master/Resources/Videos"

img = cv.imread(f"{PHOTOS}/cats.jpg")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)


blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(gray, 125, 175)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # looks at an image and tries to binarize it < 125 is black white for >125

# RETR_TREE (all hierarchical contours)
# RETR_EXTERNAL (for only the external contours)
# RETR_LIST (for all controus in the image)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) #chain approx simple compresses points to the two end points fo a line 
contours, hierarchies = cv.findContours(blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) 
print(len(contours))

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) # (B, G, R) draws contours on the blank image


#cv.imshow("GRAY", gray)
#cv.imshow("canny", canny)
#cv.imshow('blur', blur)
#cv.imshow('thresh', thresh)
cv.imshow('blank', blank)

cv.waitKey(5000)
cv.destroyAllWindows()
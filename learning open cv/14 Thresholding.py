import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

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


img = cv.imread(f"{PHOTOS}/cats.jpg")
img = cv.imread(f"{PHOTOS}/cats 2.jpg")
#display(img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
display(gray)

# SIMPLE THRESHOLDING
threshold, thresh = cv.threshold(gray, 130, 255, cv.THRESH_BINARY) # sets all pixesl > 150 to 255 otherwise is 0
# thresh is the image threshold is the value
#display(thresh)

threshold, thresh_inv = cv.threshold(gray, 130, 255, cv.THRESH_BINARY_INV) # sets all pixesl > 150 to 255 otherwise is 0
#display(thresh_inv)
#display(~thresh_inv)


# ADAPTIVE THRESHOLDING
# let comp find optimal threshold itself and apply it sub windows as opposed to entire window
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 3)
display(adaptive_thresh)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 3)
display(adaptive_thresh)







cv.waitKey(0)
cv.destroyAllWindows()
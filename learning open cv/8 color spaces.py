import cv2 as cv
import numpy as np
import itertools 

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
display(img)

# convert from BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
display(gray)

# BGR to hue saturation value (HSV)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
display(hsv)

# BGR to LAB (L * a * b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
display(lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
display(rgb)


# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
display(hsv_bgr)


cv.waitKey(0)
cv.destroyAllWindows()
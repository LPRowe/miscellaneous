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


#img = cv.imread(f"{PHOTOS}/cat.jpg")
#img = cv.imread(f"{PHOTOS}/cats 2.jpg")
img = cv.imread(f"{PHOTOS}/park.jpg")
#display(img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#display(gray)

# LAPLACIAN EDGE DETECTION (computes gradients of grayscale image)
lap = cv.Laplacian(gray, cv.CV_64F) # works on gray or color
lap = np.uint8(np.absolute(lap)) # convert all pixels to abs value first
#display(lap)

# SOBEL EDGE DETECTION
# converts gradients in x and y direction separately
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) # 1 x dir and 0 y dir
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) # 0 x dir and 1 y dir
#display(sobelx)
#display(sobely)
combined_sobel = cv.bitwise_or(sobelx, sobely)
display(combined_sobel)


cv.waitKey(0)
cv.destroyAllWindows()
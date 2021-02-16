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

k = 3

# blurring by averaging # averages all pixesl in the kernel window and replaces pixel value)
ave = cv.blur(img, (k, k)) # kernel size
display(ave)

# gaussian blur (same as averaging, but adds a weight to neighboring pixels)
gauss = cv.GaussianBlur(img, (k, k), 0) # kernel size, standard deviation
display(gauss)

# median blur (finds mdeian of surrounding pixels) better at reducing noise than gauss and ave
med = cv.medianBlur(img, k) # kernel assumed to be square
display(med)

# bilateral blurring (most effective) applies blurring while retaining edges in the image
# larger sigma space means color values farther from pixel color will affect the blurring
bilat = cv.bilateralFilter(img, 2*k, 15, 15) # not kernal size (diameter), sigma is how many colors that will be considered when calculating blur
display(bilat)


cv.waitKey(0)
cv.destroyAllWindows()
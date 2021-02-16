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

b, g, r = cv.split(img) # split image into color components
display(b)
display(g)
display(r)

merge = cv.merge([b, g, r])
display(merge)

# display color component in color
blank = np.zeros(b.shape, dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
display(blue)
display(green)
display(red)







cv.waitKey(10000)
cv.destroyAllWindows()
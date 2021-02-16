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
img = cv.imread(f"{PHOTOS}/cats 2.jpg")
display(img)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

display(mask)

masked = cv.bitwise_and(img, img, mask=mask)
display(masked)

#display(np.where(mask, img[:,:,0], mask))








cv.waitKey(10000)
cv.destroyAllWindows()

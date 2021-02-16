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


#img = cv.imread(f"{PHOTOS}/cats.jpg")
#display(img)

blank = np.zeros((400, 400), dtype='uint8')


rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1) # filled recangle on blank
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
dim_circle = cv.circle(blank.copy(), (200, 200), 200, 125, -1)
#display(rectangle)
#display(~rectangle)
#display(circle)
#display(rectangle^circle)

# bitwise and
#display(rectangle & cirlce)
#display(rectangle | circle)
#display(rectangle ^ circle)
#display(~(~rectangle & ~circle))
#display(rectangle | circle ^ dim_circle)




cv.waitKey(30000)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np

PHOTOS = "./opencv-course-master/Resources/Photos"
VIDEOS = "./opencv-course-master/Resources/Videos"

img = cv.imread(f"{PHOTOS}/cat.jpg")


# Translation (shift an image along x and y axis)
def translate(img, dx, dy):
    transMat = np.float32([[1, 0, dx], [0, 1, dy]])
    dimensions = (img.shape[1], img.shape[0]) # (widht, height)
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, 100)

# Rotation (about any location on the image)
def rotate(img, angle, rotPoint=None):
    height, width = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = width//2, height//2
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = width, height
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
rotated2 = rotate(rotated, -45) # gets cropped

# resize the image
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)

# FLIP AN IMAGE
flip = cv.flip(img, 0) # 0 vertical, 1 horizontal, -1 both vert and horiz

# CROPPING
cropped = img[200:400, 300:400]



#cv.imshow('cat', img)
#cv.imshow("translate", translated)
#cv.imshow("rot", rotated)
#cv.imshow("rot2", rotated2)
#cv.imshow('Resized', resized)
cv.imshow('flip', flip)
#cv.imshow('c', cropped)
cv.waitKey(7000)
cv.destroyAllWindows()
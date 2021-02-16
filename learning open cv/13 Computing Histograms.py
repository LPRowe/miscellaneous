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
#display(gray)

gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256]) # list of images, list of channels, 

plt.close('all')
plt.figure()
plt.title('grayscale hit')
plt.xlabel('bins')
plt.ylabel('num of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])


# compute histogram over a specific area using a mask
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
#display(cv.bitwise_and(img, img, mask=mask))

gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256]) # list of images, list of channels, mask

plt.close('all')
plt.figure()
plt.title('grayscale hit')
plt.xlabel('bins')
plt.ylabel('num of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])


# colored image histogram
plt.close('all')
plt.figure()
plt.title('grayscale hit')
plt.xlabel('bins')
plt.ylabel('num of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim(0, 256)
    



cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv
import numpy as np

PHOTOS = "./opencv-course-master/Resources/Photos"
VIDEOS = "./opencv-course-master/Resources/Videos"

blank = np.zeros((500, 500, 3), dtype='uint8')

#img = cv.imread(f"{PHOTOS}/cat.jpg")
#cv.imshow("Cat", img)

blank[150:250, 150:250] = 0, 255, 255

# RECTANGLE FILLED AND LINE
cv.rectangle(blank, (0, 0), (100, 200), (255, 0, 0), thickness = 2)
cv.rectangle(blank, (100, 150), (200, 250), (255, 255, 0), thickness = -1)


# DRAW A CIRCLE
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness = 5)


# DRAW A LINE
cv.line(blank, (50, 50), (300, 170), (100, 100, 200), thickness = 3)


# WRITE TEXT
cv.putText(blank, "Hello", (225, 325), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)



cv.imshow("pallet", blank)
cv.waitKey(0)


cv.destroyAllWindows()
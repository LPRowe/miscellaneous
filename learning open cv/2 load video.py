import cv2 as cv

PHOTOS = "./opencv-course-master/Resources/Photos"
VIDEOS = "./opencv-course-master/Resources/Videos"

# reading images
img = cv.imread(f"{PHOTOS}/cat.jpg")
cv.imshow("Cat", img)
cv.waitKey(100)
cv.destroyAllWindows()

# reading videos
capture = cv.VideoCapture(f"{VIDEOS}/dog.mp4") # use 0, 1, 2, 3 integer if using a camera/webcam connected to computer  (webcam = 0) usually
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
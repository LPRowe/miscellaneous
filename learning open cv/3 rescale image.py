import cv2 as cv

PHOTOS = "./opencv-course-master/Resources/Photos"
VIDEOS = "./opencv-course-master/Resources/Videos"

# reading images
img = cv.imread(f"{PHOTOS}/cat.jpg")
cv.imshow("Cat", img)

def rescaleFrame(frame, scale=0.25):
    # resize existing video or image
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # resizing that only works for live video
    capture.set(3, width)
    capture.set(4, height) # 4 references height
    
    

capture = cv.VideoCapture(f"{VIDEOS}/dog.mp4") # use 0, 1, 2, 3 integer if using a camera/webcam connected to computer  (webcam = 0) usually
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow("Video", frame)
    cv.imshow('video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
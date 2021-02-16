import numpy as np
import cv2 as cv
import random
import glob

def display(image):
    global img_number
    cv.imshow(str(img_number), image)
    img_number += 1

FACES = "./opencv-course-master/Resources/Faces"


FILE = "classifiers/harr_face.xml"
haar_cascade = cv.CascadeClassifier(FILE)

#features = np.load('features.npy', allow_pickle = True) # allow pickle bc features are dtype 'object'
#labels = np.laod('labels.npy', allow_pickle = True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

people = [name.split('/')[-1].split('\\')[-1] for name in glob.glob(f"{FACES}/val/*")]

PERSON = random.choice(people)
images = glob.glob(f"{FACES}/val/{PERSON}")
img = cv.imread(random.choice(glob.glob(f"{FACES}/val/{PERSON}/*")))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
display(gray)

# Detect face in image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for x, y, w, h in faces_rect:
    faces_region_of_interest = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_region_of_interest)
    print(f"Confidence: {int(confidence)}")
    print(f"Predict {people[label]}")
    print(f"Actually: {PERSON}\n")
    
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness = 2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness = 2)

display(img)



cv.waitKey(2500)
cv.destroyAllWindows()
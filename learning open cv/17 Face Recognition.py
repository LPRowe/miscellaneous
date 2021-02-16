import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import copy
import os
import glob

PHOTOS = "./opencv-course-master/Resources/Photos"
VIDEOS = "./opencv-course-master/Resources/Videos"
FACES = "./opencv-course-master/Resources/Faces"

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
    
img = cv.imread(f"{PHOTOS}/cat.jpg")
#display(img)

# haarcascade calassifier
FILE = "classifiers/harr_face.xml"
haar_cascade = cv.CascadeClassifier(FILE)

# Train open cv face recognizer on 5 celebrities
people = [name.split('/')[-1].split('\\')[-1] for name in glob.glob(f"{FACES}/train/*")]
print(people)

DIR = os.path.join(FACES, 'train')
features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)
            
            for x, y, w, h in faces_rect:
                faces_region_of_interest = gray[y:y+h, x:x+w]
                features.append(faces_region_of_interest)
                labels.append(label)

create_train()
#print(labels)
#print(features)
features = np.array(features)
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train recognizer on the features list and the labels list
face_recognizer.train(features, labels)
    
face_recognizer.save('face_trained.yml')
    
np.save('features.npy', features)
np.save('labels.npy', labels)
    
    
    
    

    
    
    
    
    
    
cv.waitKey(50)
cv.destroyAllWindows()
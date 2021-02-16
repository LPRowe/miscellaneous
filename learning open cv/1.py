import cv2

MODE = 1 # -1, 0, 1
img = cv2.imread('python-logo.png', MODE)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) # change by scale (400, 400) for to pixel size
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

#cv2.imwrite('new_img.jpg', img)
# loads blue, green, red (not RGB)
# -1 reads img in color
# 0 reads gray scale
# 1 read image unchanged

cv2.imshow('Image', img) # Image is window name
cv2.waitKey(250) # waits infinite time for a key input before closing time in milliseconds

# edit a horizontal space within the image array
for i in range(50, 100):
    for j in range(img.shape[1]):
        img[i][j] = img[i][j][::-1]
        
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# copy and paste a part of the image
tag = img[100: 200, 200:300]
img[100:200, 100:200] = tag
cv2.imshow("Image", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()
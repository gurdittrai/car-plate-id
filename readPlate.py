# Reading Car Plate Numbers
import cv2
import numpy as np

# get image
fp = "car-plate-sample-1.jpg"
rawimg = cv2.imread(fp)

# crop
h = np.size(rawimg, 0)
w = np.size(rawimg, 1)

x = (int)(w * 0.05)
y = (int)(h * 0.25)
w = (int)(w - x)
h = (int)(h - y)
cropimg = rawimg[y:h, x:w]

# save offset
rawoffset = (x,y)

# convert grayscale
grayimg = cv2.cvtColor(cropimg, cv2.COLOR_RGB2GRAY)
if grayimg is None:
    print("error opening file\n")

# seperate background
thresh = 100
maxval = 255
th, dst = cv2.threshold(grayimg, thresh, maxval, cv2.THRESH_BINARY)
cv2.imshow('raw', rawimg)
cv2.imshow("binary", dst)

# get contour
_, contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    [x, y, w, h] = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    if area > 500 :
        cv2.rectangle(cropimg, (x, y), (x + w, y + h), (255, 0, 255), 2)

    if area > 200 :
        contour_list.append(contour)

cv2.drawContours(rawimg, contour_list,  -1, (0,180,255), 2, offset=rawoffset)
cv2.imshow('Objects Detected Contour', rawimg)
cv2.imshow('Objects Detected Box', cropimg)

# wait for user to exit
cv2.waitKey(0) 
cv2.destroyAllWindows()

# Reading Car Plate Numbers
import cv2

# Get Image and convert grayscale
fp = "car-plate-sample-1.jpg"
grayimg = cv2.imread(fp, cv2.IMREAD_GRAYSCALE)
if grayimg is None:
    print("error opening file\n")

# seperate background
thresh = 35
maxval = 255
th, dst = cv2.threshold(grayimg, thresh, maxval, cv2.THRESH_BINARY)

# create window and show the gray image
cv2.namedWindow("binary", cv2.WINDOW_AUTOSIZE)
cv2.imshow("binary", dst)

cv2.imwrite("result.jpg", dst) 

# wait for user to exit
cv2.waitKey(0) 
cv2.destroyAllWindows()

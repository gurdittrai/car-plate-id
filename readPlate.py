# Reading Car Plate Numbers
import cv2

# Get Image and convert grayscale
fp = "car-plate-sample-1.jpg"
plateimg = cv2.imread(fp, cv2.IMREAD_GRAYSCALE)
if plateimg is None:
    print("error opening file\n")


# create window and show the gray image
cv2.namedWindow("plateimg", cv2.WINDOW_AUTOSIZE)
cv2.imshow("plateimg", plateimg)
cv2.imwrite("result.jpg", plateimg) 

# wait for user to exit
cv2.waitKey(0) 
cv2.destroyAllWindows()



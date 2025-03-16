# this file contains histogram equalization code using opencv package with equalizeHist() function
import cv2 
import numpy as np

rgb_image = cv2.imread("self-study/basics/histogram_equalization/horse.jpg")
grey_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(grey_image)

cv2.imshow("Unequal intensity Image",grey_image)
cv2.imshow("Equalized Image",equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# saving the high contrast image
cv2.imwrite("self-study/basics/histogram_equalization/simple_eq.jpg",equalized)
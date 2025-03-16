# histogram equalization using CLAHE method
import cv2

image = cv2.imread("self-study/basics/histogram_equalization/horse.jpg")
grey_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE()

equalized =clahe.apply(grey_image)

cv2.imshow("Unequal intensity Image",grey_image)
cv2.imshow("Equalized intensity Image",equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save the image
cv2.imwrite("self-study/basics/histogram_equalization/clahe_image.jpg",equalized)
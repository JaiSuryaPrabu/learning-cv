# custom filtering
import cv2
import numpy as np

# gaussian blurring / smoothing
gaussian_blur_kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) * 1 / 16

def gauss_blur(file: str):
    image = cv2.imread(file)
    gauss_blurred_image = cv2.filter2D(
        src=image, ddepth=-1, kernel=gaussian_blur_kernel
    )
    cv2.imshow("Gaussian Blurred Image", gauss_blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("self-study/basics/filtering/gauss_blur.jpg", gauss_blurred_image)


# sharpening
sharpening_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

def sharpen(file: str):
    image = cv2.imread(file)
    # ddepth = -1 means same depth from the input image
    sharpened_image = cv2.filter2D(src=image, ddepth=-1, kernel=sharpening_kernel)
    cv2.imshow("Sharpened Image", sharpened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("basics/filtering/sharp.jpg", sharpened_image)


if __name__ == "__main__":
    image = "basics/filtering/dog.jpg"
    gauss_blur(image)
    sharpen(image)

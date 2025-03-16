# Merging photos
In this directory, I have implemented a basic computer vision application that takes the foreground image that contains a text and background image that contains any and they are merged. For example :
![Process](images/Logo_Manipulation.png)

## Code Explanation :
### 1️⃣ Importing the Libraries : 
```py
import cv2
import numpy as np
```
* cv2 - OpenCV for image manipulation and merging the photos
* numpy - for handling mathematical operations
### 2️⃣ Reading the Image
```py
foreground_image_bgr = cv2.imread('self-study/applications/merging-photos/images/coca-cola-logo.png',cv2.IMREAD_COLOR)
foreground_image_rgb = cv2.cvtColor(foreground_image_bgr,cv2.COLOR_BGR2RGB)

foreground_image_w = foreground_image_rgb.shape[0] 
foreground_image_h = foreground_image_rgb.shape[1]

background_image_bgr = cv2.imread('self-study/applications/merging-photos/images/checkerboard_color.png',cv2.IMREAD_COLOR)
background_image_rgb = cv2.cvtColor(background_image_bgr,cv2.COLOR_BGR2RGB)

background_image_w = background_image_rgb.shape[0]
background_image_h = background_image_rgb.shape[1]
```
* Reading the image using `imread()` function
### 3️⃣ Resizing the background image
```py
aspect_ratio = foreground_image_w / background_image_h
dim = (foreground_image_w,int(background_image_h * aspect_ratio))
background_image_rgb = cv2.resize(background_image_rgb,dim,interpolation = cv2.INTER_AREA)
```
* Resizing the background image using `resize()` image
### 4️⃣ Masking the foreground image
```py
foreground_image_gray = cv2.cvtColor(foreground_image_rgb,cv2.COLOR_RGB2GRAY)
ret_val,foreground_image_mask = cv2.threshold(foreground_image_gray,127,255,cv2.THRESH_BINARY)
```
* Masking can be done by `threshold()` function and it accepts grayscale image and produces single channel binary image
### 5️⃣ Inverting the masking image
```py
foreground_image_inv_mask = cv2.bitwise_not(foreground_image_mask)
```
* Inverting an image can be done by `bitwise_not()` function
### 6️⃣ Adding the foreground mask to background image
```py
background_image = cv2.bitwise_and(background_image_rgb,background_image_rgb,mask=foreground_image_mask)
```
* `bitwise_and()` is used to add two images with the `mask`
### 7️⃣ Removing the text in the foreground image with inverse mask
```py
foreground_image = cv2.bitwise_and(foreground_image_rgb,foreground_image_rgb,mask=foreground_image_inv_mask)
```
### 8️⃣ Add the forground and background image
```py
final_image = cv2.add(background_image,foreground_image)
```
* Finally, the two images are added by `add()` function
### 9️⃣ Save the image
```py
cv2.imwrite("self-study/applications/merging-photos/images/final.png",final_image[...,::-1])
```
* To save the image, we use `imwrite()` function
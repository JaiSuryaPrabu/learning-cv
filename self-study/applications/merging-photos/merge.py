import cv2
import numpy as np

# 1. Get the image
print("[INFO] 1. Starting the process ...")
foreground_image_bgr = cv2.imread('self-study/applications/merging-photos/images/coca-cola-logo.png',cv2.IMREAD_COLOR)
print("[INFO] Got foreground image ...")
foreground_image_rgb = cv2.cvtColor(foreground_image_bgr,cv2.COLOR_BGR2RGB)
print("[INFO] Converted foreground image to RGB ...")
foreground_image_w = foreground_image_rgb.shape[0] 
foreground_image_h = foreground_image_rgb.shape[1]
print(f"[INFO] The shape of the foreground image = {(foreground_image_w,foreground_image_h)}")
background_image_bgr = cv2.imread('self-study/applications/merging-photos/images/checkerboard_color.png',cv2.IMREAD_COLOR)
print("[INFO] Got background image ...")
background_image_rgb = cv2.cvtColor(background_image_bgr,cv2.COLOR_BGR2RGB)
print("[INFO] Converted background image to RGB ...")
background_image_w = background_image_rgb.shape[0]
background_image_h = background_image_rgb.shape[1]
print(f"[INFO] The shape of the background image = {(background_image_w,background_image_h)}")

# 2. Resize the background image
print("[INFO] 2. Starting the resizing process for the background image ...")
aspect_ratio = foreground_image_w / background_image_h
print(f"[INFO] The aspect ratio = {aspect_ratio}")
dim = (foreground_image_w,int(background_image_h * aspect_ratio))
print(f"[INFO] The calculated dimension of the background = {dim}")
background_image_rgb = cv2.resize(background_image_rgb,dim,interpolation = cv2.INTER_AREA)
print("[INFO] The background image is resized ...")

# 3. Masking the foreground image
print("[INFO] 3. Process of masking is started ...")
foreground_image_gray = cv2.cvtColor(foreground_image_rgb,cv2.COLOR_RGB2GRAY)
print("[INFO] The foreground image is converted into gray image")
ret_val,foreground_image_mask = cv2.threshold(foreground_image_gray,127,255,cv2.THRESH_BINARY)
print("[INFO] The foreground image is converted into mask")

# 4. Inverting the threshold image
print("[INFO] 4. Inverting the threshold image started ...")
foreground_image_inv_mask = cv2.bitwise_not(foreground_image_mask)
print("[INFO] The foreground image is inverted ...")

# 5. Adding the mask and background image
print("[INFO] 5. Adding the foreground image to the background image ...")
background_image = cv2.bitwise_and(background_image_rgb,background_image_rgb,mask=foreground_image_mask)
print("[INFO} Background image is ready ...")

# 6. Remove the text in the foreground image
print("[INFO] 6. Removing the text in the foreground image ...")
foreground_image = cv2.bitwise_and(foreground_image_rgb,foreground_image_rgb,mask=foreground_image_inv_mask)
print("[INFO] Foreground image is ready ...")

# 7. Add the background and foreground image
final_image = cv2.add(background_image,foreground_image)
print("[INFO] 7. Saving the final image ...")
cv2.imwrite("self-study/applications/merging-photos/images/final.png",final_image[...,::-1])
cv2.imshow("Merged Photo",final_image[...,::-1])
cv2.waitKey(0)
cv2.destroyAllWindows()
print("[INFO] Two photos have been merged sucessfully ... ")
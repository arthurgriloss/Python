import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/itl.cat_nature-wallpaper-for-whatsapp_796150.png")
resized_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
blank = np.zeros(resized_img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (resized_img.shape[1]//2, resized_img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(resized_img, resized_img, mask=mask)

cv.imshow("Image", masked)
cv.waitKey(0)
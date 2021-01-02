import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/itl.cat_nature-wallpaper-for-whatsapp_796150.png")
resized_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
img_gray = cv.cvtColor(resized_img, cv.COLOR_RGB2GRAY)

# Laplacian
lap = cv.Laplacian(img_gray, cv.CV_64F)
lap =  np.uint8(np.absolute(lap))

# Sabel
sabelx = cv.Sobel(img_gray, cv.CV_64F, 1, 0)
sabely = cv.Sobel(img_gray, cv.CV_64F, 0, 1)
combined_sabel = cv.bitwise_or(sabelx, sabely)

# Canny
canny = cv.Canny(img_gray, 150, 175)

cv.imshow("Image", canny)
cv.imshow("Imag2", lap)
cv.imshow("Imag3", combined_sabel)
cv.waitKey(0)
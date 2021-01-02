import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/4k-ultra-hd-background-toronto-canada-long-exposure-photogra.jpg")
resized_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
blur_img = cv.blur(resized_img, (2, 2), cv.BORDER_DEFAULT)
grey_img = cv.cvtColor(blur_img, cv.COLOR_RGB2GRAY)
blank = np.zeros(resized_img.shape, dtype='uint8')

canny_img = cv.Canny(grey_img, 125, 175)

ret, thresh = cv.threshold(grey_img, 125, 255, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours(s) found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)

cv.imshow("Image", blank)
cv.waitKey(0)
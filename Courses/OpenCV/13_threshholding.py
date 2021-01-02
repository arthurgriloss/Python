import cv2 as cv

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/itl.cat_nature-wallpaper-for-whatsapp_796150.png")
resized_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
img_gray = cv.cvtColor(resized_img, cv.COLOR_RGB2GRAY)

# Simple Thresholding
threshold, thresh = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY)
threshold, thresh_inv = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY_INV)

# Adaptative Thresholding
adaptative_thresh = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)



cv.imshow("Image", thresh)
cv.imshow("Image", adaptative_thresh)
cv.waitKey(0)
import cv2 as cv

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/itl.cat_nature-wallpaper-for-whatsapp_796150.png")
resized_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))

# Average Blur
average = cv.blur(resized_img, (7, 7))

# Gaussian Blur
gauss = cv.GaussianBlur(resized_img, (7, 7), 0)

# median Blur
median = cv.medianBlur(resized_img, 7)

# Bilateral
bilateral = cv.bilateralFilter(resized_img, 10, 35, 25)

cv.imshow("img", resized_img)
cv.imshow("Avg", average)
cv.imshow("Gaussian", gauss)
cv.imshow("Median", median)
cv.imshow("Bilateral", bilateral)
cv.waitKey(0)
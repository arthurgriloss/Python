import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/itl.cat_nature-wallpaper-for-whatsapp_796150.png")
resized_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
blank = np.zeros(resized_img.shape[:2], dtype='uint8')

img_gray = cv.cvtColor(resized_img, cv.COLOR_RGB2GRAY)

mask = cv.circle(blank, (resized_img.shape[1]//2, resized_img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(resized_img, resized_img, mask=mask)

# gray scale histogram
gray_hist = cv.calcHist([img_gray], [0], mask, [256], [0, 256])

# colors histogram
colors = ('b', 'g', 'r')
plt.figure()
for i, col in enumerate(colors):
    hist = cv.calcHist([resized_img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)

cv.imshow("Image", masked)
cv.waitKey(0)


# plt.plot(gray_hist)
plt.ylabel("Number of pixels")
plt.show()
import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/itl.cat_nature-wallpaper-for-whatsapp_796150.png")
resized_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))
blank = np.zeros(resized_img.shape[:2], dtype='uint8')

b, g, r = cv.split(resized_img)
merged = cv.merge([b, g, r])
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# cv.imshow("Blue", b)
# cv.imshow("Red", g)
# cv.imshow("Grenn", r)
cv.imshow("Image", merged)
cv.imshow("Blue", blue)
cv.imshow("Red", green)
cv.imshow("Grenn", red)

print(resized_img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)
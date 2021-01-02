import cv2 as cv

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/itl.cat_nature-wallpaper-for-whatsapp_796150.png")
resized_img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2))

# grey
img_gray = cv.cvtColor(resized_img, cv.COLOR_RGB2GRAY)

# hsv
img_hsv = cv.cvtColor(resized_img, cv.COLOR_BGR2HSV)

# l*a*b
img_lab = cv.cvtColor(resized_img, cv.COLOR_BGR2LAB)

# bgr to rgb
img_rgb = cv.cvtColor(resized_img, cv.COLOR_BGR2RGB)

# hsv to gray
img_gbr = cv.cvtColor(img_hsv, cv.COLOR_HSV2BGR)
img_gray = cv.cvtColor(img_gbr, cv.COLOR_BGR2GRAY)

cv.imshow("image", img_gray)
cv.waitKey(0)
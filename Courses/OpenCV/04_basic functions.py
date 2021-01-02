import cv2 as cv

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/109676.jpg")

# resized
img = cv.resize(img, dsize=(img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_AREA)

# converting to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=3)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=3)

# Cropping
cropped = img[50:200, 200:400]

# extending img
extended = cv.resize(cropped, (500, 500), interpolation=cv.INTER_CUBIC)

cv.imshow("Image", extended)
cv.waitKey(0)
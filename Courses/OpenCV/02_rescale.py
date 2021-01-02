import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    # image, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def resolution(capture, width, height, brightness):
    capture.set(3, width) # 3 stands for width
    capture.set(4, height) # 4 stands for height
    capture.set(10, brightness) # 10 stands for brightness


im = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/109676.jpg")
cv.imshow("Image", im)
im_resized = rescaleFrame(im, scale=0.5)
cv.imshow("Resized Image", im_resized)

cv.waitKey(0)
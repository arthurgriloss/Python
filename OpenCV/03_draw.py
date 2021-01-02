import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')


# paint the image certain color
red = blank.copy()
red[:] = 0, 0, 255

green_square = blank.copy()
green_square[200:300, 300:400] = 0, 255, 0

cv.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=-1)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=2)

cv.line(blank, (0, 0), (blank.shape[1], blank.shape[0]), (255, 255, 255), thickness=1)

cv.putText(blank, "Hello", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)

cv.imshow("Image", blank)
cv.waitKey(0)

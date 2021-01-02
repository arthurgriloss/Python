import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectagle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

bitwise_and = cv.bitwise_and(circle, rectagle)
bitwise_or = cv.bitwise_or(circle, rectagle)
bitwise_xor = cv.bitwise_xor(circle, rectagle)
bitwise_not = cv.bitwise_not(bitwise_xor)

cv.imshow("Rectangle", rectagle)
cv.imshow("Circle", circle)
cv.imshow("Image", bitwise_not)
cv.waitKey(0)
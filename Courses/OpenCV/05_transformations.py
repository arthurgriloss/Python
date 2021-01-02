import cv2 as cv
import numpy as np

img = cv.imread("C:/Users/arthu/Pictures/Saved Pictures/109676.jpg")
img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_AREA)

# Translation
def translation(img, x, y):
    '''
    -x  --> Left
     x  --> Right
    -y  --> Up
     y  --> Down
    '''
    trans_mat = np.float32([[1,0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)
translated = translation(img, 100, -100)

# Rotation
def rotation(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotation(img, 45)
rotated_rotated = rotation(rotated, -45)

# Flip
flip = cv.flip(img, 0)
'''0 --> Vertical flip, 1 --> Horizontal, -1 --> Both'''

cv.imshow("Image", flip)
cv.waitKey(0)
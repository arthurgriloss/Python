import cv2
import mediapipe as mp
import time
import handtracking as ht
import numpy as np


def tip_mcp (img, lm):
    for i in range(5):
        tip = tuple(lm[4*i+1][1:])
        mcp = tuple(lm[4*(i+1)][1:])
        cv2.circle(img, tip, 5, (0, 0, 255), -1)
        cv2.circle(img, mcp, 5, (0, 0, 255), -1)
        cv2.line(img, tip, mcp, color=(255, 0, 0))


def tip_dist(immg, lm, color_list):

    for i in range(1, 5):
            for j in range(1+i, 6):
                color = color_list[i]
                ft1 = tuple(lm[4*i][1:])
                ft2 = tuple(lm[4*j][1:])
                cv2.circle(img, ft1, 5, (0, 0, 255), -1)
                cv2.circle(img, ft2, 5, (0, 0, 255), -1)
                cv2.line(img, ft1, ft2, color=(int(color[0]), int(color[1]), int(color[2])))


color_list = []
for i in range(5):
    color_list.append(np.random.choice(range(256), size=3))

pre_time = 0  # start previous time = 0
cur_time = 0  # start current time = 0

cap = cv2.VideoCapture(0)   # capture video in the webcam

detector = ht.handDetector(max_hands=2) # Start hand detector (if max_hands not specified max_hands=2)

while True:
    sucess, img = cap.read()    # save image that the webcam records
    img = cv2.flip(img,1)   # mirror the img for better user interaction exp (the user see the img as in a mirror)

    img = detector.find_hands(img, False)  # find and draw Hands landmarks in the img
    lm_list = detector.find_positions(img)  # calculate the landmark positions in pixel

    if len(lm_list) != 0:
        tip_dist(img, lm_list, color_list)
        # tip_mcp(img, lm_list)

    # CALCULATE AND DISPLAY FPS
    cur_time = time.time()
    fps = 1/(cur_time-pre_time)
    pre_time = cur_time
    cv2.putText(img, "FPS: " + str(int(fps)), (500, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    # END

    cv2.imshow("Image", img) # Display img
    cv2.waitKey(1)  # keep displaying img

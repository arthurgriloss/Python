import cv2
import mediapipe as mp
import time
import handtracking as ht
import random


def point_inside(x, y, x_center, y_center, radius):
    if ((x - x_center) ** 2 + (y - y_center) ** 2) < radius ** 2:
        return True
    else:
        return False


pre_time = 0  # start previous time = 0
cur_time = 0  # start current time = 0
points = 0 # points made by the player
s_time = time.time() # starting time
random_width_start = random.randint(0, 640) # random start the circle in the latidinal direction

cap = cv2.VideoCapture(0)   # capture video in the webcam

detector = ht.handDetector(max_hands=1) # Start hand detector (if max_hands not specified max_hands=2)


while True:
    sucess, img = cap.read()    # save image that the webcam records
    img = cv2.flip(img,1)   # mirror the img for better user interaction exp (the user see the img as in a mirror)
    h, w, c = img.shape     # read heigh, widht and channels of the img displayed

    img = detector.find_hands(img, False)  # find and draw Hands landmarks in the img
    lm_list = detector.find_positions(img)  # calculate the landmark positions in pixel

    # CALCULATE AND DISPLAY FPS
    cur_time = time.time()
    fps = 1/(cur_time-pre_time)
    pre_time = cur_time
    cv2.putText(img, "FPS: " + str(int(fps)), (500, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    # END

    # MAKE CIRCLES MOVE UPWARD
    cv2.putText(img, "Points: " + str(int(points)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    r_time = cur_time - s_time    # time runnning the game

    c_speed = int(r_time * 10 * (points + 1) ** 1.5) # define how fast the circle moves
    c_radius = 25 # radius of the circle
    c_center = (random_width_start, h - c_speed) # position of the circle's center
    c_color = (0, 0, 255)   # color of the circle
    circle = cv2.circle(img, c_center, c_radius, c_color, thickness=-1) # draw a circle in the img
    # END
    
    # game ends if the ball arrive the top of the screen
    if c_speed >= h:
        cv2.putText(img, "Game Over", (200, 240), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    
    # ball becomes green and start in the bottle again
    if (len(lm_list) != 0) and (point_inside(lm_list[8][1], lm_list[8][2], random_width_start, h - c_speed, c_radius)):
        c_color = (0, 255, 0)
        circle = cv2.circle(img, c_center, c_radius, c_color, thickness=-1)
        s_time = cur_time
        random_width_start = random.randint(0, w)
        points += 1

    cv2.imshow("Image", img) # Display img
    cv2.waitKey(1)  # keep displaying img
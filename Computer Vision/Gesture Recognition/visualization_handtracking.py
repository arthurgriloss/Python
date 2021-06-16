import cv2
import mediapipe as mp
import time
import handtracking as ht

pre_time = 0  # start previous time = 0
cur_time = 0  # start current time = 0

cap = cv2.VideoCapture(0)   # capture video in the webcam

detector = ht.handDetector(max_hands=2) # Start hand detector (if max_hands not specified max_hands=2)

while True:
    sucess, img = cap.read()    # save image that the webcam records
    img = cv2.flip(img,1)   # mirror the img for better user interaction exp (the user see the img as in a mirror)

    img = detector.find_hands(img)  # find and draw Hands landmarks in the img
    lm_list = detector.find_positions(img)  # calculate the landmark positions in pixel

    if len(lm_list) != 0:
        print([lm_list[4]])   # show pixel distance from index finger tip
                                                                                # to index finger mcp

    # CALCULATE AND DISPLAY FPS
    cur_time = time.time()
    fps = 1/(cur_time-pre_time)
    pre_time = cur_time
    cv2.putText(img, "FPS: " + str(int(fps)), (500, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)
    # END

    cv2.imshow("Image", img) # Display img
    cv2.waitKey(1)  # keep displaying img

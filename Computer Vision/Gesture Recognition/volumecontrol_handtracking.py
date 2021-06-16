import cv2
import mediapipe as mp
import time
import handtracking as ht
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def dist_points(x1, x2, y1, y2):
    # Find the distance between two points
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)


def set_volume(dist):
    # Set the volume based on the input dist
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if dist <= 20:
        volume.SetMasterVolumeLevel(-65.25, None)
    elif 20 < dist <= 100:
        volume.SetMasterVolumeLevel(- 65.25 + 65.25 / 80 * (dist - 20), None)
    else:
        volume.SetMasterVolumeLevel(0, None)


p_time = 0  # start previous time = 0
c_time = 0  # start current time = 0

cap = cv2.VideoCapture(0)   # capture video in the webcam

detector = ht.handDetector(detection_confidence= 0.7, max_hands=1) # Start hand detector (if max_hands not specified max_hands=2)

while True:
    sucess, img = cap.read()    # save image that the webcam records
    img = cv2.flip(img,1)   # mirror the img for better user interaction exp (the user see the img as in a mirror)

    img = detector.find_hands(img, False)  # find and draw Hands landmarks in the img
    lm_list = detector.find_positions(img)  # calculate the landmark positions in pixel

    # CALCULATE AND DISPLAY FPS
    c_time = time.time()
    fps = 1/(c_time-p_time)
    p_time = c_time
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    # END

    # CHECK DISTANCE BETWEEN FINGERS AND SET VOLUME BASED ON THE DISTANCE
    if len(lm_list) != 0:
        set_volume(dist_points(lm_list[4][1], lm_list[8][1], lm_list[4][2], lm_list[8][2]))
    # END

    cv2.imshow("Image", img) # Display img
    cv2.waitKey(1)  # keep displaying img

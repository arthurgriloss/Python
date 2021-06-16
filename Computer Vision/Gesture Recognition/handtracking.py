import cv2
import mediapipe as mp
import time

# This code to transform mediapipe command mediapipe.solutions.hands.Hands() into a class
# with the intention to create a model that can be called easily in other codes

class handDetector():
    def __init__(self, mode=False, max_hands=2, detection_confidence=0.5, track_confidence=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_confidance = detection_confidence
        self.track_confidence = track_confidence

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.detection_confidance, self.track_confidence)
        self.mp_draw = mp.solutions.drawing_utils


    def find_hands(self, img, draw=True):    
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)

        return img


    def find_positions(self, img, hand_no=0):
        
        lm_list = []
        
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]

            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y *h)

                lm_list.append([id, cx, cy])

        return lm_list
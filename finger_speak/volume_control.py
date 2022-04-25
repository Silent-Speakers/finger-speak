import cv2
import time
import numpy as np
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class HandDetector:
    """
    A class used to detect the hand landmarks of the hands
    Translates the landmarks to a specific feature
    """
    def __init__(self, mode=False, max_hands=2, detection_con=int(0.5), track_con=int(0.5)):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(self.mode, self.max_hands, self.detection_con, self.track_con)
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 28]

    def find_hands(self, img, draw=True):
        """
        A method that is used to detect the hands
            Arguments: img, draw
            Returns: img
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        # print(self.results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_lms, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_no=0, draw=True):
        """
        A method that is used to detect position of all the landmarks in the hand
            Arguments: img, hand_no=0, draw
            Returns: landmarks_list
        """
        self.lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, lm in enumerate(my_hand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                self.lm_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return self.lm_list

    def fingers_up(self):
        """
        A method that is used to detect the position of the fingers
            Arguments: None
            Returns: fingers 
        """
        fingers = []
        # Thumb
        if self.lm_list[self.tip_ids[0]][1] < self.lm_list[self.tip_ids[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
#         4 fingers
        for id in range(1, 5):
            if self.lm_list[self.tip_ids[id]][2] < self.lm_list[self.tip_ids[id] - 2][2]:
                fingers.append(1)
            else:
                fingers(0)
        return fingers


def main():
    p_time = 0
    c_time = 0
    # Open cam
    cap = cv2.VideoCapture(0)
    # cap.set(3, 640)
    # cap.set(4, 480)
    # cap.set(10, 100)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lm_list = detector.find_position(img)
        if len(lm_list) != 0:
            print(lm_list[4])

        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, (255, 0, 255), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
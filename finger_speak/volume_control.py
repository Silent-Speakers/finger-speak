import cv2
import time
import numpy as np
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class HandDetector:
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
	    pass
    
    def find_position(self, img, hand_no=0, draw=True):
	    pass

    def fingers_up(self):
	    pass
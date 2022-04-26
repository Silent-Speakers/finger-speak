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




def gestures_volume():
    """
    A function used to contol the volume of the sound
        Arguments: None
        Returns: Increases or Decreases the sound
    """
    wCam, hCam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    p_time = 0
    detector = HandDetector()

    # pycow
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # volume.GetMasterVolumeLevel()
    vol_range = volume.GetVolumeRange()
    min_vol = vol_range[0]
    max_vol = vol_range[1]
    vol = 0
    vol_bar = 400
    vol_per = 0
    while True:
        success, img = cap.read()
        img = detector.find_hands(img)
        lm_list = detector.find_position(img, draw=False)
        if len(lm_list) != 0:
            # print(x1, y1)
            x1, y1 = lm_list[4][1], lm_list[4][2]
            x2, y2 = lm_list[8][1], lm_list[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
            cv2.circle(img, (x2,y2), 15, (255,0,255), cv2.FILLED)
            cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
            cv2.line(img, (x1,y1), (x2,y2), (255,0,255),3)

            length = math.hypot(x2 - x1, y2 - y1)
            # print(length)

            # hand range 50 - 300
            # volume range -65 - 0
            vol = np.interp(length,[50,300], [min_vol, max_vol])
            vol_bar = np.interp(length,[50,300], [400, 150])
            vol_per =  np.interp(length,[50,300], [0, 100])
            print(length, vol)
            volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)

        cv2.rectangle(img, (50,150), (85, 400), (0,255,0), 3)
        cv2.rectangle(img, (50,int(vol_bar)), (85, 400), (255,0,255), cv2.FILLED)

        # print(lmlist)
        c_time = time.time()
        fps = 1/(c_time - p_time)
        p_time = c_time

        cv2.putText(img, f'Volume%: {int(vol_per)}%', (40,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255),3)
        cv2.imshow("Img", img)
        cv2.waitKey(1)

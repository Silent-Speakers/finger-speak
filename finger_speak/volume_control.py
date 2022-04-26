import cv2
import time
import numpy as np
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class HandSignDetector:
    """
    A class used to detect the hand landmarks of the hands
    Translates the landmarks to a specific feature
    """

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

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
                    self.mp_draw.draw_landmarks(
                        img, hand_lms, self.mp_hands.HAND_CONNECTIONS
                    )
        return img

    def find_position(self, img, hand_no=0, draw=True):
        """
        A method that is used to detect position of all the landmarks in the hand
            Arguments: img, hand_no=0, draw
            Returns: landmarks_list
        """
        self.landmarks_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            for id, landmark in enumerate(my_hand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                # print(id, cx, cy)
                self.landmarks_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return self.landmarks_list


def gestures_volume():
    """
    A function used to contol the volume of the sound
        Arguments: None
        Returns: Increases or Decreases the sound
    """
    w_cam, h_cam = 640, 480
    cap = cv2.VideoCapture(0)
    cap.set(3, w_cam)
    cap.set(4, h_cam)
    detector = HandSignDetector()

    # pycow
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    # volume.GetMasterVolumeLevel()
    vol_range = volume.GetVolumeRange()
    min_vol = vol_range[0]
    max_vol = vol_range[1]
    vol = 0
    vol_bar = 400
    vol_per = 0
    while True:
        success, image = cap.read()
        img = detector.find_hands(image)
        landmarks_list = detector.find_position(img, draw=False)
        if len(landmarks_list) != 0:
            x1, y1 = landmarks_list[4][1], landmarks_list[4][2]
            x2, y2 = landmarks_list[8][1], landmarks_list[8][2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(img, (x1, y1), 15, (255,182,193), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255,182,193), cv2.FILLED)
            cv2.circle(img, (cx, cy), 15, (255,255,0), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (176,224,230), 3)

            length = math.hypot(x2 - x1, y2 - y1)
            # hand range 50 - 300
            # volume range -65 - 0
            vol = np.interp(length, [50, 300], [min_vol, max_vol])
            vol_bar = np.interp(length, [50, 300], [400, 150])
            vol_per = np.interp(length, [50, 300], [0, 100])
            print(length, vol)
            volume.SetMasterVolumeLevel(vol, None)

            if length < 50:
                cv2.circle(img, (cx, cy), 15, (128,0,128), cv2.FILLED)

        cv2.rectangle(img, (50, 150), (85, 400), (255,182,193), 4)
        cv2.rectangle(img, (50, int(vol_bar)), (85, 400), (128,0,128), cv2.FILLED)

        cv2.putText(
            img,
            f"Speakers: {int(vol_per)}%",
            (40, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (128,0,128),
            2,
        )
        cv2.imshow("Volume Control Detection", img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            cv2.destroyAllWindows()
            break

# gestures_volume()
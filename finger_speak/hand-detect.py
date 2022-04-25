import cv2
import mediapipe as mp


class SignDetection:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(3)

    def hand_detection(self, cap):
        while True:

            ret, img = cap.read()
            if img is None:
                break
            img = cv2.flip(img, 1)
            h, w, c = img.shape
            landmarks_xyz = self.hands.process(img)

            if landmarks_xyz.multi_hand_landmarks:
                for hand_landmark in landmarks_xyz.multi_hand_landmarks:
                    lm_list = []
                    for id, lm in enumerate(hand_landmark.landmark):
                        lm_list.append(lm)

                    self.mp_draw.draw_landmarks(
                        img,
                        hand_landmark,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                        self.mp_draw.DrawingSpec((0, 255, 0), 4, 2),
                    )

            cv2.imshow("Hand Sign Detection", img)
            c = cv2.waitKey(1)
            if c == 27:
                break


SignDetection().hand_detection(SignDetection().cap)

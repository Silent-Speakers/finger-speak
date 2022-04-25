import cv2
import mediapipe as mp


class SignDetection:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(3)
        

    def hand_detection(self, cap):
        # Initialize the finger status with None
            index_tip_status_fh = None
            index_tip_status_fv = None
            index_tip_status_v = None
            index_tip_status_h = None
            middle_tip_status_fh = None
            middle_tip_status_fv = None
            middle_tip_status_v = None
            middle_tip_status_h = None
            little_tip_status_fh = None
            little_tip_status_fv = None
            little_tip_status_v = None
            little_tip_status_h = None
            ring_tip_status_fh = None
            ring_tip_status_fv = None
            ring_tip_status_v = None
            ring_tip_status_h = None
            thumb_tip_status_fh = None
            thumb_tip_status_fv = None
            thumb_tip_status_v = None
            thumb_tip_status_h = None
        while True:
            finger_tips = [8, 12, 16, 20]
            thumb_tip = 4
            index_tip = 8
            middle_tip = 12
            ring_tip = 16
            little_tip = 20
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
                        finger_fold_status = []
                        for tip in finger_tips:
                            x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)

                            # index_tip
                            if lm_list[index_tip - 2].y < lm_list[index_tip - 1].y < lm_list[index_tip].y:
                                index_tip_status_v = "down"
                            if lm_list[index_tip].y < lm_list[index_tip - 1].y < lm_list[index_tip - 2].y:
                                index_tip_status_v = "up"
                            if lm_list[index_tip].x < lm_list[index_tip - 1].x < lm_list[index_tip - 2].x:
                                index_tip_status_h = "left"
                            if lm_list[index_tip - 2].x < lm_list[index_tip - 1].x < lm_list[index_tip].x:
                                index_tip_status_h = "right"
                            if lm_list[index_tip].y < lm_list[index_tip - 2].y:
                                index_tip_status_fv = "fold up"
                            if lm_list[index_tip - 2].y < lm_list[index_tip].y:
                                index_tip_status_fv = "fold down"
                            if lm_list[index_tip].x < lm_list[index_tip - 2].x:
                                index_tip_status_fh = "fold right"
                            if lm_list[index_tip - 2].x < lm_list[index_tip].x:
                                index_tip_status_fh = "fold left"

                            # middle_tip
                            if lm_list[middle_tip - 2].y < lm_list[middle_tip - 1].y < lm_list[middle_tip].y:
                                middle_tip_status_v = "down"
                            if lm_list[middle_tip].y < lm_list[middle_tip - 1].y < lm_list[middle_tip - 2].y:
                                middle_tip_status_v = "up"
                            if lm_list[middle_tip].x < lm_list[middle_tip - 1].x < lm_list[middle_tip - 2].x:
                                middle_tip_status_h = "left"
                            if lm_list[middle_tip - 2].x < lm_list[middle_tip - 1].x < lm_list[middle_tip].x:
                                middle_tip_status_h = "right"
                            if lm_list[middle_tip].y < lm_list[middle_tip - 2].y:
                                middle_tip_status_fv = "fold up"

                            if lm_list[middle_tip - 2].y < lm_list[middle_tip].y:
                                middle_tip_status_fv = "fold down"
                            if lm_list[middle_tip].x < lm_list[middle_tip - 2].x:
                                middle_tip_status_fh = "fold right"
                            if lm_list[middle_tip - 2].x < lm_list[middle_tip].x:
                                middle_tip_status_fh = "fold left"

                            # ring_tip
                            if lm_list[ring_tip - 2].y < lm_list[ring_tip - 1].y < lm_list[ring_tip].y:
                                ring_tip_status_v = "down"
                            if lm_list[ring_tip].y < lm_list[ring_tip - 1].y < lm_list[ring_tip - 2].y:
                                ring_tip_status_v = "up"
                            if lm_list[ring_tip].x < lm_list[ring_tip - 1].x < lm_list[ring_tip - 2].x:
                                ring_tip_status_h = "left"
                            if lm_list[ring_tip - 2].x < lm_list[ring_tip - 1].x < lm_list[ring_tip].x:
                                ring_tip_status_h = "right"
                            if lm_list[ring_tip].y < lm_list[ring_tip - 2].y:
                                ring_tip_status_fv = "fold up"
                            if lm_list[ring_tip - 2].y < lm_list[ring_tip].y:
                                ring_tip_status_fv = "fold down"
                            if lm_list[ring_tip].x < lm_list[ring_tip - 2].x:
                                ring_tip_status_fh = "fold right"
                            if lm_list[ring_tip - 2].x < lm_list[ring_tip].x:
                                ring_tip_status_fh = "fold left"

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

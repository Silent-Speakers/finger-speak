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
                        

                        # little_tip
                        if lm_list[little_tip - 2].y < lm_list[little_tip - 1].y < lm_list[little_tip].y:
                            little_tip_status_v = "down"
                        if lm_list[little_tip].y < lm_list[little_tip - 1].y < lm_list[little_tip - 2].y:
                            little_tip_status_v = "up"
                        if lm_list[little_tip].x < lm_list[little_tip - 1].x < lm_list[little_tip - 2].x:
                            little_tip_status_h = "left"
                        if lm_list[little_tip - 2].x < lm_list[little_tip - 1].x < lm_list[little_tip].x:
                            little_tip_status_h = "right"
                        if lm_list[little_tip].y < lm_list[little_tip - 2].y:
                            little_tip_status_fv = "fold up"
                        if lm_list[little_tip - 2].y < lm_list[little_tip].y:
                            little_tip_status_fv = "fold down"
                        if lm_list[little_tip].x < lm_list[little_tip - 2].x:
                            little_tip_status_fh = "fold right"
                        if lm_list[little_tip - 2].x < lm_list[little_tip].x:
                            little_tip_status_fh = "fold left"

                        # thump_tip
                        if lm_list[thumb_tip - 2].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip].y:
                            thumb_tip_status_v = "down"
                        if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y:
                            thumb_tip_status_v = "up"
                        if lm_list[thumb_tip].x < lm_list[thumb_tip - 1].x < lm_list[thumb_tip - 2].x:
                            thumb_tip_status_h = "left"
                        if lm_list[thumb_tip - 2].x < lm_list[thumb_tip - 1].x < lm_list[thumb_tip].x:
                            thumb_tip_status_h = "right"
                        if lm_list[thumb_tip].y < lm_list[thumb_tip - 2].y:
                            thumb_tip_status_fv = "fold up"
                        if lm_list[thumb_tip - 2].y < lm_list[thumb_tip].y:
                            thumb_tip_status_fv = "fold down"
                        if lm_list[thumb_tip].x < lm_list[thumb_tip - 2].x:
                            thumb_tip_status_fh = "fold right"
                        if lm_list[thumb_tip - 2].x < lm_list[thumb_tip].x:
                            thumb_tip_status_fh = "fold left"
                        if lm_list[tip].x < lm_list[tip - 2].x:
                            # cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                            finger_fold_status.append(True)
                        else:
                            finger_fold_status.append(False)

                    x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)

            self.mp_draw.draw_landmarks(
                img,
                hand_landmark,
                self.mp_hands.HAND_CONNECTIONS,
                self.mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                self.mp_draw.DrawingSpec((0, 255, 0), 4, 2),
            )



            if self.quit == 27:
                break

            if lm_list[4].y < lm_list[2].y and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                    lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                    lm_list[5].x:
                cv2.putText(img, "Hello", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                self.output_list.append('Hello')
                self.letter="Hello"
                hello_sign = cv2.imread("images/hello.png")
                hello_sign = cv2.resize(hello_sign, (200, 180))
                h, w, c = hello_sign.shape
                img[0:h, 0:w] = hello_sign
                continue

            # Forward
            if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                    lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                cv2.putText(img, "Forward", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                self.output_list.append("Forward")
                self.letter="Forward"
                forward_sign = cv2.imread("images/forward.jpg")
                forward_sign = cv2.resize(forward_sign, (200, 180))
                h, w, c = forward_sign.shape
                img[0:h, 0:w] = forward_sign
                continue

            # Backward
            if lm_list[3].x > lm_list[4].x and lm_list[3].y < lm_list[4].y and lm_list[8].y > lm_list[6].y and lm_list[
                12].y < lm_list[10].y and \
                    lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y:
                cv2.putText(img, "Backward", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                self.output_list.append("Backward")
                self.letter="Backward"
                backword_sign = cv2.imread("images/backword.jpg")
                forward_sign = cv2.resize(backword_sign, (200, 180))
                h, w, c = backword_sign.shape
                img[0:h, 0:w] = backword_sign
                continue

            # Left
            if lm_list[4].y < lm_list[2].y and lm_list[8].x < lm_list[6].x and lm_list[12].x > lm_list[10].x and \
                    lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x and lm_list[5].x < lm_list[0].x:
                cv2.putText(img, "Left", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                self.output_list.append("Left")
                self.letter="Left"
                left_sign = cv2.imread("images/left.jpg")
                left_sign = cv2.resize(left_sign, (200, 180))
                h, w, c = left_sign.shape
                img[0:h, 0:w] = left_sign
                continue


            cv2.imshow("Hand Sign Detection", img)
            c = cv2.waitKey(1)
            if c == 27:
                break


SignDetection().hand_detection(SignDetection().cap)

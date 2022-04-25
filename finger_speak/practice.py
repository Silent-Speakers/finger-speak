import cv2
import mediapipe as mp
import pyttsx3


class SignDetection:
    """
    A class that detects the hand landmarks.
        Translate the landmarks into a specific american sign language using the coordinates of each finger's landmark
        Translate the sign language to voice record
        Translate the sign language to an image
    """
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)
        self.output_list = []
        self.common = ''
        self.words = {'Like': False, 'Dislike': False, 'Hello': False, 'Forward': False, 'Backward': False,
                      'Right': False, 'Left': False, 'I love you': False, 'Yes': False, 'No': False, 'Victory': False,
                      'Nice': False, 'Yellow': False, 'Purple': False, 'Green': False}
        # For voice recognition
        self.letter = ""
        self.quit = 1
        self.lm_id=[]

    def hand_detection(self,cap):
        """
        A method that is used for detecting the landmarks for the fingers and translates it to sign language using the x and y coordinates
            Arguments: None
            Returns: Displays the hand landmarks, image, text and voice for each sign language
        """
        finger_tips = [8, 12, 16, 20]
        thumb_tip = 4
        index_tip = 8
        middle_tip = 12
        ring_tip = 16
        little_tip = 20
        while True:
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

            self.output_list = []
            self.common = ''
            ret, img = cap.read()
            if img is None:
                break
            img = cv2.flip(img, 1)
            h, w, c = img.shape
            landmarks_xyz = self.hands.process(img)
            # status = []

            if landmarks_xyz.multi_hand_landmarks:
                for hand_landmark in landmarks_xyz.multi_hand_landmarks:
                    lm_list = []
                    for id, lm in enumerate(hand_landmark.landmark):
                        self.lm_id.append(id)
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

                    self.mp_draw.draw_landmarks(img, hand_landmark,
                                                self.mp_hands.HAND_CONNECTIONS,
                                                self.mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                                self.mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                                )

                    # hello
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

                    # Right
                    if lm_list[4].y < lm_list[2].y and lm_list[8].x > lm_list[6].x and lm_list[12].x < lm_list[10].x and \
                            lm_list[16].x < lm_list[14].x and lm_list[20].x < lm_list[18].x:
                        cv2.putText(img, "Right", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Right")
                        self.letter="Right"
                        right_sign = cv2.imread("images/right.jpg")
                        right_sign = cv2.resize(right_sign, (200, 180))
                        h, w, c = right_sign.shape
                        img[0:h, 0:w] = right_sign
                        continue

                    if all(finger_fold_status):
                        # like
                        if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y and lm_list[0].x < \
                                lm_list[3].y:
                            self.output_list.append("Like")
                            cv2.putText(img, "Like", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                            self.letter="Like"
                            like_sign = cv2.imread("images/like.png")
                            like_sign = cv2.resize(like_sign, (200, 180))
                            h, w, c = like_sign.shape
                            img[0:h, 0:w] = like_sign
                            continue

                        # Dislike
                        if lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y and lm_list[0].x < \
                                lm_list[3].y:
                            cv2.putText(img, "Dislike", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                            self.output_list.append("Dislike")
                            self.letter="Dislike"
                            dislike_sign = cv2.imread("images/dislike.png")
                            dislike_sign = cv2.resize(dislike_sign, (200, 180))
                            h, w, c = dislike_sign.shape
                            img[0:h, 0:w] = dislike_sign
                            continue

                    if middle_tip_status_fv == "fold down" and ring_tip_status_fv == "fold down" and thumb_tip_status_v == "up" and index_tip_status_v == "up" and little_tip_status_v == "up":
                        cv2.putText(img, "I Love You", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("I Love You")
                        self.letter="I Love You"
                        loveyou_sign = cv2.imread("images/love.png")
                        loveyou_sign = cv2.resize(loveyou_sign, (200, 180))
                        h, w, c = loveyou_sign.shape
                        img[0:h, 0:w] = loveyou_sign
                        continue

                    if thumb_tip_status_v == "up" and index_tip_status_fv == "fold down" and ring_tip_status_fv == "fold down" and middle_tip_status_fv == "fold down" and little_tip_status_fv == "fold down":
                        cv2.putText(img, "Yes", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Yes")
                        self.letter="Yes"
                        yes_sign = cv2.imread("images/yes.png")
                        yes_sign = cv2.resize(yes_sign, (200, 180))
                        h, w, c = yes_sign.shape
                        img[0:h, 0:w] = yes_sign
                        continue

                    if thumb_tip_status_h == "right" and index_tip_status_h == "right" and middle_tip_status_h == "right" and ring_tip_status_h == "right" and little_tip_status_h == "right":
                        cv2.putText(img, "No", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("No")
                        self.letter="No"
                        no_sign = cv2.imread("images/no.png")
                        no_sign = cv2.resize(no_sign, (200, 180))
                        h, w, c = no_sign.shape
                        img[0:h, 0:w] = no_sign
                        continue
                    if thumb_tip_status_v == "up" and index_tip_status_v == "up" and middle_tip_status_v == "up" and little_tip_status_fv == "fold down" and ring_tip_status_fv == "fold down":
                        cv2.putText(img, "Victory", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Victory")
                        self.letter="Victory"
                        vic_sign = cv2.imread("images/victory.jpg")
                        vic_sign = cv2.resize(vic_sign, (200, 180))
                        h, w, c = vic_sign.shape
                        img[0:h, 0:w] = vic_sign
                        continue

                    if thumb_tip_status_v == "up" and index_tip_status_fh == "fold left" and middle_tip_status_v == "up" and ring_tip_status_v == "up" and little_tip_status_v == "up":
                        cv2.putText(img, "Nice", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Nice")
                        self.letter = "Nice"
                        nice_sign = cv2.imread("images/nice.png")
                        nice_sign = cv2.resize(nice_sign, (200, 180))
                        h, w, c = nice_sign.shape
                        img[0:h, 0:w] = nice_sign
                        continue

                    if middle_tip_status_fh == 'fold right' and ring_tip_status_fh == 'fold right' and little_tip_status_fh == 'fold right' and index_tip_status_h == "right" and thumb_tip_status_h == "right":
                        cv2.putText(img, "Green", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Green")
                        self.letter="Green"
                        green_sign = cv2.imread("images/green.png")
                        green_sign = cv2.resize(green_sign, (200, 180))
                        h, w, c = green_sign.shape
                        img[0:h, 0:w] = green_sign
                        continue

                    if ring_tip_status_fh == 'fold right' and little_tip_status_fh == 'fold right' and index_tip_status_h == "right" and middle_tip_status_h == "right" and thumb_tip_status_fh == "fold left":
                        cv2.putText(img, "Purple", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Purple")
                        self.letter="Purple"
                        purple_sign = cv2.imread("images/purple.png")
                        purple_sign = cv2.resize(purple_sign, (200, 180))
                        h, w, c = purple_sign.shape
                        img[0:h, 0:w] = purple_sign
                        continue

                    if middle_tip_status_fh == 'fold right' and ring_tip_status_fh == 'fold right' and index_tip_status_fh == "fold right" and little_tip_status_h == 'right' and thumb_tip_status_v == 'up':
                        cv2.putText(img, "Yellow", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Yellow")
                        self.letter="Yellow"
                        yellow_sign = cv2.imread("images/yellow.png")
                        yellow_sign = cv2.resize(yellow_sign, (200, 180))
                        h, w, c = yellow_sign.shape
                        img[0:h, 0:w] = yellow_sign
                        continue

                    if thumb_tip_status_h=="right" and index_tip_status_v=="up" and middle_tip_status_fv=="fold down" and ring_tip_status_fv=="fold down" and little_tip_status_fv=="fold down":
                        cv2.putText(img, "leave", (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.letter="leave"

            cv2.imshow("Hand Sign Detection", img)
            # cv2.waitKey(10)
            self.quit = cv2.waitKey(1)

            # most common
            self.most_frequent()

            # add to leaned
            self.add_to_learned()

            # text
            # self.text_output()
            # print(self.letter)

            # Exits the cameras when (L) sign is done by the user
            if self.letter == "leave":
                cv2.destroyAllWindows()
                break

    def quitter(self):
        """
        A method that is used to quit the camera when esc key is pressed by the user
            Arguments: None
            Returns: Quits the camera
        (for the TK)
        """
        self.quit = 27

    def most_frequent(self):
        '''
         A method to detect the most repeated sign language
         Arguments: None
         Returns: None , edit the value of the self.common
        '''
        counter = 0
        if len(self.output_list) == 0:
            return
        self.common = self.output_list[0]
        for i in self.output_list:
            curr_frequency = self.output_list.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                self.common = i

    def text_output(self):
        '''
        A method to print the text, then print the user knowledge stats for than word (if he knows it or not)
        Arguments: None
        Return: print the word and (You learned it/This word is new to you)
        '''
        if self.common == '':
            return
        print(self.common)
        if self.words[self.common] == True:
            print('You learned it \n')
        if self.words[self.common] == False:
            print('This word is new to you \n')

    def voice_output(self, word):
        """
        A method that is used to translate the text to voicerecord
            Arguments: word
            Returns: Displays or Plays the voicerecord
        """
        engine = pyttsx3.init()
        engine.say(word)
        engine.runAndWait()

    def add_to_learned(self):
        if self.common == '':
            return
        self.words[self.common] = True

if __name__=='__main__':
    SignDetection().hand_detection(SignDetection().cap)
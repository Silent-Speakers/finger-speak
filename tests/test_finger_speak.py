import cv2
from finger_speak.hand_detect import SignDetection
import pytest



def test_i_love_you():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/Iloveyou_sign.jpg")
    sign_detect.hand_detection(cap)

    actual=sign_detect.letter

    expected="I Love You"
    assert actual==expected

def test_Hello():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/hello_sign.jpg")
    sign_detect.hand_detection(cap)

    actual=sign_detect.letter

    expected="Hello"
    assert actual==expected

def test_yellow():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/yellow_sign.jpg")
    sign_detect.hand_detection(cap)

    actual=sign_detect.letter

    expected="Yellow"
    assert actual==expected

def test_nice():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/nice_sign.jpg")
    sign_detect.hand_detection(cap)

    actual=sign_detect.letter

    expected="Nice"
    assert actual==expected

def test_camera():
    sign_detect=SignDetection()
    actual=sign_detect.cap.isOpened()
    expected=True
    assert  actual==expected

def test_landmarks():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/yellow_sign.jpg")
    sign_detect.hand_detection(cap)
    actual=sign_detect.lm_id
    expected=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert  actual==expected

def test_leave():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/leave_sign.mp4")
    sign_detect.hand_detection(cap)
    while sign_detect.hand_detection(cap):
        result=True
    else:
        result=False
    actual=result
    expected=False
    assert actual==expected

def text_to_speech(word="how are you"):
    text = word
    language = "en"
    output = gTTS(text=text, lang=language, slow=True)
    output.save("output.wav")
    os.system("start output.wav")
    return "output.wav"

def speech_to_text():
    r = sr.Recognizer()
    wav_path = text_to_speech()
    # wav, samplerate = sf.read(wav_path)
    # sf.write(saved_wav_path, wav_path, fs)
    data = wavio.read(wav_path)
    # y = (np.iinfo(np.int32).max * (data / np.abs(data).max())).astype(np.int32)
    # wavio.write(data, fs, y)
    # wavio.write(wav_path, data, fs, sampwidth=2)
    with sr.WavFile(wav_path) as source:
        audio_data = r.record(source)
        # audio_data = r.listen(source)
    text = r.recognize_google(audio_data)
    return text
    
# speech_to_text()
# def test_audio():
#     text_to_speach = text_to_speech()
#     voce_recognition = speech_to_text()
#     assert voce_recognition.lower() == 'how are you'


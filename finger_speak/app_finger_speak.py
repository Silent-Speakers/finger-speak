import tkinter as tk
import tkinter.font as tkFont
from tkinter import Frame, Label
from PIL import ImageTk, Image
from hand_detect import SignDetection
from practice import SignPractice
import webbrowser
from volume_control import gestures_volume

class App:
    def __init__(self, window):
        # setting title
        window.title("Finger Spaek")
        # setting window size
        width = 787
        height = 514
        screenwidth = window.winfo_screenwidth()
        screenheight = window.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        window.geometry(alignstr)
        window.resizable(width=False, height=False)
        window.configure(bg="#2E2E2E")

        label_524 = tk.Label(window)
        label_524["bg"] = "#2E2E2E"
        ft = tkFont.Font(family="Times", size=22)
        label_524["font"] = ft
        label_524["fg"] = "#ffffff"
        label_524["justify"] = "center"
        label_524["text"] = "FingerSpeak"
        label_524.place(x=310, y=0, width=159, height=51)

        message_251 = tk.Message(window)
        message_251["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=10)
        message_251["font"] = ft
        message_251["fg"] = "#ffffff"
        message_251["justify"] = "center"
        message_251["text"] = ""
        message_251.place(x=210, y=100, width=175, height=192)

        button_123 = tk.Button(window)
        button_123["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=16)
        button_123["font"] = ft
        button_123["fg"] = "#ffffff"
        button_123["justify"] = "center"
        button_123["text"] = "Translate"
        button_123.place(x=570, y=12, width=180, height=40)
        button_123["command"] = self.translate

        button_321 = tk.Button(window)
        button_321["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=16)
        button_321["font"] = ft
        button_321["fg"] = "#ffffff"
        button_321["justify"] = "center"
        button_321["text"] = "Help"
        button_321.place(x=40, y=12, width=80, height=40)
        button_321["command"] = self.help

        button_3210 = tk.Button(window)
        button_3210["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=16)
        button_3210["font"] = ft
        button_3210["fg"] = "#ffffff"
        button_3210["justify"] = "center"
        button_3210["text"] = "Sound"
        button_3210.place(x=130, y=12, width=80, height=40)
        button_3210["command"] = self.sound

        button_67 = tk.Button(window)
        button_67["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_67["font"] = ft
        button_67["fg"] = "#ffffff"
        button_67["justify"] = "center"
        button_67["text"] = "Listen to the word"
        button_67.place(x=240, y=220, width=126, height=30)
        button_67["command"] = self.command_voice_nice

        button_116 = tk.Button(window)
        button_116["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_116["font"] = ft
        button_116["fg"] = "#ffffff"
        button_116["justify"] = "center"
        button_116["text"] = "Practice"
        button_116.place(x=270, y=255, width=70, height=25)
        button_116["command"] = self.command_practice_nice

        label_291 = tk.Label(window)
        label_291["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        label_291["font"] = ft
        label_291["fg"] = "#ffffff"
        label_291["justify"] = "center"
        label_291["text"] = "Nice"
        label_291.place(x=230, y=100, width=138, height=49)

        message_899 = tk.Message(window)
        message_899["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=10)
        message_899["font"] = ft
        message_899["fg"] = "#ffffff"
        message_899["justify"] = "center"
        message_899["text"] = ""
        message_899.place(x=410, y=100, width=175, height=192)

        button_42 = tk.Button(window)
        button_42["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_42["font"] = ft
        button_42["fg"] = "#ffffff"
        button_42["justify"] = "center"
        button_42["text"] = "Practice"
        button_42.place(x=460, y=255, width=70, height=25)
        button_42["command"] = self.command_practice_yellow

        button_771 = tk.Button(window)
        button_771["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_771["font"] = ft
        button_771["fg"] = "#ffffff"
        button_771["justify"] = "center"
        button_771["text"] = "Listen to the word"
        button_771.place(x=440, y=220, width=118, height=30)
        button_771["command"] = self.command_voice_yellow

        label_587 = tk.Label(window)
        label_587["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        label_587["font"] = ft
        label_587["fg"] = "#ffffff"
        label_587["justify"] = "center"
        label_587["text"] = "Yellow"
        label_587.place(x=430, y=100, width=138, height=49)

        message_723 = tk.Message(window)
        message_723["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=10)
        message_723["font"] = ft
        message_723["fg"] = "#ffffff"
        message_723["justify"] = "center"
        message_723["text"] = ""
        message_723.place(x=600, y=100, width=175, height=192)

        button_779 = tk.Button(window)
        button_779["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_779["font"] = ft
        button_779["fg"] = "#ffffff"
        button_779["justify"] = "center"
        button_779["text"] = "Listen to the word"
        button_779.place(x=620, y=220, width=132, height=30)
        button_779["command"] = self.command_voice_love

        button_642 = tk.Button(window)
        button_642["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_642["font"] = ft
        button_642["fg"] = "#ffffff"
        button_642["justify"] = "center"
        button_642["text"] = "Practice"
        button_642.place(x=650, y=255, width=70, height=25)
        button_642["command"] = self.command_practice_love

        babel_579 = tk.Label(window)
        babel_579["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        babel_579["font"] = ft
        babel_579["fg"] = "#ffffff"
        babel_579["justify"] = "center"
        babel_579["text"] = "I Love You"
        babel_579.place(x=614, y=100, width=156, height=49)

        label_187 = tk.Label(window)
        label_187["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        label_187["font"] = ft
        label_187["fg"] = "#ffffff"
        label_187["justify"] = "center"
        label_187["text"] = "Yes"
        label_187.place(x=30, y=300, width=138, height=58)

        message_794 = tk.Message(window)
        message_794["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=10)
        message_794["font"] = ft
        message_794["fg"] = "#ffffff"
        message_794["justify"] = "center"
        message_794["text"] = ""
        message_794.place(x=210, y=300, width=175, height=192)

        button_442 = tk.Button(window)
        button_442["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_442["font"] = ft
        button_442["fg"] = "#ffffff"
        button_442["justify"] = "center"
        button_442["text"] = "Listen to the word"
        button_442.place(x=240, y=420, width=125, height=30)
        button_442["command"] = self.command_voice_no

        button_500 = tk.Button(window)
        button_500["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_500["font"] = ft
        button_500["fg"] = "#ffffff"
        button_500["justify"] = "center"
        button_500["text"] = "Practice"
        button_500.place(x=270, y=455, width=70, height=25)
        button_500["command"] = self.command_practice_no

        label_347 = tk.Label(window)
        label_347["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        label_347["font"] = ft
        label_347["fg"] = "#ffffff"
        label_347["justify"] = "center"
        label_347["text"] = "NO"
        label_347.place(x=230, y=300, width=138, height=49)

        message_491 = tk.Message(window)
        message_491["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=10)
        message_491["font"] = ft
        message_491["fg"] = "#ffffff"
        message_491["justify"] = "center"
        message_491["text"] = ""
        message_491.place(x=410, y=300, width=175, height=192)

        button_499 = tk.Button(window)
        button_499["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_499["font"] = ft
        button_499["fg"] = "#ffffff"
        button_499["justify"] = "center"
        button_499["text"] = "Listen to the word"
        button_499.place(x=430, y=420, width=135, height=30)
        button_499["command"] = self.command_voice_green

        button_267 = tk.Button(window)
        button_267["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_267["font"] = ft
        button_267["fg"] = "#ffffff"
        button_267["justify"] = "center"
        button_267["text"] = "Practice"
        button_267.place(x=460, y=455, width=70, height=25)
        button_267["command"] = self.command_practice_green

        label_746 = tk.Label(window)
        label_746["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        label_746["font"] = ft
        label_746["fg"] = "#ffffff"
        label_746["justify"] = "center"
        label_746["text"] = "Green"
        label_746.place(x=430, y=300, width=138, height=49)

        message_163 = tk.Message(window)
        message_163["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=10)
        message_163["font"] = ft
        message_163["fg"] = "#ffffff"
        message_163["justify"] = "center"
        message_163["text"] = ""
        message_163.place(x=20, y=100, width=175, height=192)

        label_986 = tk.Label(window)
        label_986["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=10)
        label_986["font"] = ft
        label_986["fg"] = "#ffffff"
        label_986["justify"] = "center"
        label_986["text"] = ""
        label_986.place(x=20, y=300, width=175, height=192)

        button_459 = tk.Button(window)
        button_459["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_459["font"] = ft
        button_459["fg"] = "#ffffff"
        button_459["justify"] = "center"
        button_459["text"] = "Listen to the word"
        button_459.place(x=40, y=420, width=130, height=30)
        button_459["command"] = self.command_voice_yes

        button_154 = tk.Button(window)
        button_154["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_154["font"] = ft
        button_154["fg"] = "#ffffff"
        button_154["justify"] = "center"
        button_154["text"] = "Practice"
        button_154.place(x=70, y=455, width=70, height=25)
        button_154["command"] = self.command_practice_yes

        label_483 = tk.Label(window)
        label_483["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        label_483["font"] = ft
        label_483["fg"] = "#ffffff"
        label_483["justify"] = "center"
        label_483["text"] = "Yes"
        label_483.place(x=40, y=300, width=138, height=49)

        label_250 = tk.Label(window)
        label_250["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        label_250["font"] = ft
        label_250["fg"] = "#ffffff"
        label_250["justify"] = "center"
        label_250["text"] = "Hello"
        label_250.place(x=40, y=100, width=138, height=49)

        button_282 = tk.Button(window)
        button_282["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_282["font"] = ft
        button_282["fg"] = "#ffffff"
        button_282["justify"] = "center"
        button_282["text"] = "Listen to the word"
        button_282.place(x=40, y=220, width=130, height=30)
        button_282["command"] = self.command_voice_hello

        button_754 = tk.Button(window)
        button_754["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_754["font"] = ft
        button_754["fg"] = "#ffffff"
        button_754["justify"] = "center"
        button_754["text"] = "Practice"
        button_754.place(x=70, y=255, width=70, height=25)
        button_754["command"] = self.command_practice_hello

        message_506 = tk.Message(window)
        message_506["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=10)
        message_506["font"] = ft
        message_506["fg"] = "#ffffff"
        message_506["justify"] = "center"
        message_506["text"] = ""
        message_506.place(x=600, y=300, width=175, height=192)

        button_506 = tk.Button(window)
        button_506["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_506["font"] = ft
        button_506["fg"] = "#ffffff"
        button_506["justify"] = "center"
        button_506["text"] = "Listen to the word"
        button_506.place(x=620, y=420, width=130, height=30)
        button_506["command"] = self.command_voice_purple

        button_969 = tk.Button(window)
        button_969["bg"] = "#0063B1"
        ft = tkFont.Font(family="Times", size=10)
        button_969["font"] = ft
        button_969["fg"] = "#ffffff"
        button_969["justify"] = "center"
        button_969["text"] = "Practice"
        button_969.place(x=650, y=455, width=70, height=25)
        button_969["command"] = self.command_practice_purple

        label_314 = tk.Label(window)
        label_314["bg"] = "#4D4D4D"
        ft = tkFont.Font(family="Times", size=22)
        label_314["font"] = ft
        label_314["fg"] = "#ffffff"
        label_314["justify"] = "center"
        label_314["text"] = "Purple"
        label_314.place(x=620, y=300, width=138, height=49)

        label_449 = tk.Label(window)
        label_449["bg"] = "#2E2E2E"
        ft = tkFont.Font(family="Times", size=22)
        label_449["font"] = ft
        label_449["fg"] = "#ffffff"
        label_449["justify"] = "center"
        label_449["text"] = "Start learning your words by choosing a card"
        label_449.place(x=124, y=50, width=550, height=40)

        # img, hello
        frame1 = Frame(window, width=5, height=5)
        frame1.place(anchor="center", x=105, y=175)
        img1 = Image.open("images/hello.png")
        img1 = img1.resize((50, 50), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)
        label1 = Label(frame1, image=img1)
        label1.pack()

        # img, nice
        frame2 = Frame(window, width=5, height=5)
        frame2.place(anchor="center", x=300, y=175)
        img2 = Image.open("images/nice.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        img2 = ImageTk.PhotoImage(img2)
        label2 = Label(frame2, image=img2)
        label2.pack()

        # img, yellow
        frame3 = Frame(window, width=5, height=5)
        frame3.place(anchor="center", x=500, y=175)
        img3 = Image.open("images/yellow.png")
        img3 = img3.resize((50, 50), Image.ANTIALIAS)
        img3 = ImageTk.PhotoImage(img3)
        label3 = Label(frame3, image=img3)
        label3.pack()

        # img, Ilove you
        frame4 = Frame(window, width=5, height=5)
        frame4.place(anchor="center", x=700, y=175)
        img4 = Image.open("images/Love.png")
        img4 = img4.resize((50, 50), Image.ANTIALIAS)
        img4 = ImageTk.PhotoImage(img4)
        label4 = Label(frame4, image=img4)
        label4.pack()

        # img, yes
        frame5 = Frame(window, width=5, height=5)
        frame5.place(anchor="center", x=105, y=375)
        img5 = Image.open("images/yes.png")
        img5 = img5.resize((50, 50), Image.ANTIALIAS)
        img5 = ImageTk.PhotoImage(img5)
        label5 = Label(frame5, image=img5)
        label5.pack()

        # img, No
        frame6 = Frame(window, width=5, height=5)
        frame6.place(anchor="center", x=300, y=375)
        img6 = Image.open("images/no.png")
        img6 = img6.resize((50, 50), Image.ANTIALIAS)
        img6 = ImageTk.PhotoImage(img6)
        label6 = Label(frame6, image=img6)
        label6.pack()

        # img, green
        frame7 = Frame(window, width=5, height=5)
        frame7.place(anchor="center", x=500, y=375)
        img7 = Image.open("images/green.png")
        img7 = img7.resize((50, 50), Image.ANTIALIAS)
        img7 = ImageTk.PhotoImage(img7)
        label7 = Label(frame7, image=img7)
        label7.pack()

        # img, purple
        frame = Frame(window, width=5, height=5)
        frame.place(anchor="center", x=700, y=375)
        img = Image.open("images/purple.png")
        img = img.resize((50, 50), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label = Label(frame, image=img)
        label.pack()

        window.mainloop()

    def command_voice_nice(self):
        SignDetection().voice_output("Nice")

    def command_practice_nice(self):
        SignPractice().hand_detection(SignDetection().cap, "Nice")

    def command_practice_yellow(self):
        SignPractice().hand_detection(SignDetection().cap, "Yellow")

    def command_voice_yellow(self):
        SignDetection().voice_output("Yellow")

    def command_voice_love(self):
        SignDetection().voice_output("I Love You")

    def command_practice_love(self):
        SignPractice().hand_detection(SignDetection().cap, "I Love You")

    def command_voice_no(self):
        SignDetection().voice_output("No")

    def command_practice_no(self):
        SignPractice().hand_detection(SignDetection().cap, "No")

    def command_voice_green(self):
        SignDetection().voice_output("Green")

    def command_practice_green(self):
        SignPractice().hand_detection(SignDetection().cap, "Green")

    def command_voice_yes(self):
        SignDetection().voice_output("Yes")

    def command_practice_yes(self):
        SignPractice().hand_detection(SignDetection().cap, "Yes")

    def command_voice_hello(self):
        SignDetection().voice_output("Hello")

    def command_practice_hello(self):
        SignPractice().hand_detection(SignDetection().cap, "Hello")

    def command_voice_purple(self):
        SignDetection().voice_output("Purple")

    def command_practice_purple(self):
        SignPractice().hand_detection(SignDetection().cap, "Purple")

    def translate(self):
        SignDetection().hand_detection(SignDetection().cap)

    def help(self):
        webbrowser.open("https://github.com/senas-LTUC/future-alpha/blob/main/README.md")

    def sound(self):
        gestures_volume()
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

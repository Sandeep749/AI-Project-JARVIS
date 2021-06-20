import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib  # This is used to send email
import random
import time
import sys
# Support for regular expressions (RE). Hover mouse cursor over re to learn more about it
import re
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QDate, QTime, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
# from jarvisUi import Ui_jarvisUI

# GUI FILE
from ui_main import Ui_MainWindow

# IMPORT FUNCTIONS
# from ui_main_functions import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

UI = Ui_MainWindow()


# This is a wish function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# This is a wish function, this wishes us accourding to the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Hello Sir")
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("I am Jarvis, your personal assistant. Please tell me how can I help you")

# This function is sends email for us
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sandeepkumarkarmkar49@gmail.com', 'Sandeep749@123')
    server.sendmail('sandeepkumarkarmkar49@gmail.com', to, content)
    server.close()


def setDiscussionValue(valueDiscuss):
    UI.textDisplayConversation.append(f"{valueDiscuss}")


def setDisplayValue(valueDisp):
    UI.display.setText(f"{valueDisp}")


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.taskExecution()

    # It takes microPhone input from user and returns String output
    def takeCommand(self):

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            setDisplayValue("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            setDisplayValue("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            setDiscussionValue(f"User: {query}\n")

        except Exception as e:
            print(e)

            print("Say that again please...")
            UI.display.setText("Say that again please...")
            return "None"
        return query

    def taskExecution(self):
        wishMe()
        while True:
            # if 1:
            self.query = self.takeCommand().lower()

            # logic for executing tasks on query
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                self.query = self.query.replace("search", "")
                self.query = self.query.replace("jarvis", "")
                results = wikipedia.summary(self.query, sentences=2)
                setDiscussionValue(
                    f"Jarvis: According to wikipedia {results}\n\n")
                speak("According to wikipedia")
                print(results)
                setDisplayValue("Speaking...")
                speak(results)

            elif 'who is' in self.query:
                self.query = self.query.replace("who is", "")
                self.query = self.query.replace("jarvis who is", "")
                self.query = self.query.replace("jarvis tell me who is", "")
                self.query = self.query.replace(
                    "jarvis please tell me who is", "")
                results2 = wikipedia.summary(self.query, sentences=2)
                setDiscussionValue(
                    f"Jarvis: According to google {results2}\n\n")
                speak("According to google")
                print(results2)
                setDisplayValue("Speaking...")
                speak(results2)

            elif self.query in GREETINGS:
                greet = random.choice(GREETINGS_RES)
                setDiscussionValue(f"Jarvis: {greet}")
                speak(f"{greet}")

            elif 'open youtube' in self.query:
                setDiscussionValue("Jarvis: Opening YouTube.com")
                setDisplayValue("Speaking...")
                speak("Opening youtube dot com")
                webbrowser.open("youtube.com")

            elif 'open google' in self.query:
                setDiscussionValue("Jarvis: Opening Google.com")
                setDisplayValue("Speaking...")
                speak("Opening google dot com")
                webbrowser.open("google.com")

            elif 'open stackoverflow' in self.query:
                setDiscussionValue("Jarvis: Opening stackoverflow.com")
                setDisplayValue("Speaking...")
                speak("Opening stackoverflow dot com")
                webbrowser.open("stackoverflow.com")

            elif 'play music' in self.query or 'play song' in self.query or 'play a song' in self.query:
                music_dir = 'D:\\songs\\audio'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif re.search('date', self.query):
                """
                Just return date as string
                :return: date if success, False if fail
                """
                try:
                    date = datetime.datetime.now().strftime("%b %d %Y")
                except Exception as e:
                    print(e)
                    date = False
                print(date)
                speak(f"Sir, it's {date} today")

            elif 'the time' in self.query:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strtime}")

            elif 'open vs code' in self.query:
                codepath = "C:\\Users\\Pradeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
                speak("Opening VS Code sir, please wait, it may take some time")

            elif re.search('launch', self.query):
                dict_app = {
                    'chrome': '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"',
                    'vs code': 'C:\\Users\\Pradeep\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                }

                app = self.query.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    speak('Application path not found')
                    print('Application path not found')

                else:
                    speak('Launching: ' + app + 'for you sir!')
                    try:
                        os.startfile(path)
                    except Exception as e:
                        print(e)

            elif 'email to sandeep' in self.query:
                try:
                    speak("what should I say?")
                    content = self.takeCommand()
                    to = "sandeepkarmkar49@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend Sandeep bhai, I cannot sent this email")

            elif 'quit' in self.query:
                speak("OK Sir, I am terminating myself in t minus three seconds")
                time.sleep(0.5)
                speak("three")
                time.sleep(1)
                speak("two")
                time.sleep(1)
                speak("one")
                quit()


startExecution = MainThread()


# Any setup related thing is made in this class for the gui window
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.ui = Ui_MainWindow()
        UI.setupUi(self)

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main window to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        ##########################################################
        # Apply shadow to cental widget
        UI.centralwidget.setGraphicsEffect(self.shadow)
    
        ######################################################################
        # --------------------- Set window Icon
        # -- This icon and title will not appear on our app main window
        # because we removed the title bar
        # self.setWindowIcon(QtGui.QIcon(":/icons/icons/github.svg"))
        # self.setWindowTitle("MODERN UI")

        ############################################################
        # -------- Window Size grip to resize window
        # QSizeGrip(self.ui.size_grip)


        ###############################################
        #----------------- Minimize window
        UI.Btn_MINIMISE.clicked.connect(lambda: self.showMinimized())

        #----------------- Restore/Maximize window
        UI.Btn_MAXIMISE.clicked.connect(lambda: self.restore_or_maximize_window())

        #----------------- Close window
        UI.Btn_CLOSE.clicked.connect(lambda: self.close())
        UI.Btn_EXIT.clicked.connect(lambda: self.close()) 


        # start button functionality
        UI.Btn_start.clicked.connect(self.startTask)
        # self.ui.pushButton_2.clicked.connect(self.close)

        # TOGGLE/BURGER MENU
        ######################################################
        UI.Btn_toggle.clicked.connect(lambda: self.ToggleAnimation(150, True))

        # PAGES
        ######################################################
        # PAGE HOME
        UI.Btn_HOME.clicked.connect(lambda: UI.stackedWidget.setCurrentWidget(UI.page_home))

        # PAGE ADVANCE
        UI.Btn_ADVANCE.clicked.connect(
            lambda: UI.stackedWidget.setCurrentWidget(UI.page_advance))

        # PAGE ABOUT
        UI.Btn_ABOUT.clicked.connect(
            lambda: UI.stackedWidget.setCurrentWidget(UI.page_about))

    ##################################################
    # Add mouse events  to the window
    ###############################################
    def mousePressEvent(self, event):
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the mouse window

    def ToggleAnimation(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = UI.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 40

            # SET MAX WIDTH
            if width == 40:
                widthExtended = maxExtend
                UI.Btn_HOME.setText("   HOME")
            else:
                widthExtended = standard
                UI.Btn_HOME.setText("")

            # ANIMATION
            self.animation = QPropertyAnimation(UI.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

            if width == 40:
                UI.Btn_HOME.setText("   HOME")
                UI.Btn_ADVANCE.setText("   ADVANCE")
                UI.Btn_ABOUT.setText("   ABOUT")
                UI.Btn_EXIT.setText("   EXIT")
            else:
                UI.Btn_HOME.setText("")
                UI.Btn_ADVANCE.setText("")
                UI.Btn_ABOUT.setText("")
                UI.Btn_EXIT.setText("")

    def restore_or_maximize_window(self):
            # if window is maximized
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()
    
    def startTask(self):

        UI.movie = QtGui.QMovie("gif\\45.gif")
        UI.label_4.setMovie(UI.movie)
        UI.movie.start()

        # UI.movie = QtGui.QMovie("gif\\43.gif")
        # UI.label_6.setMovie(UI.movie)
        # UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\44.gif")
        UI.label_44.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\17.gif")
        UI.globe.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\36.gif")
        UI.label_31.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\33.gif")
        UI.label_33.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\23.gif")
        UI.label_23.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\nice.gif")
        UI.label_nice.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\22.gif")
        UI.label_22.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\51.gif")
        UI.label_51.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\48.gif")
        UI.label_48.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\55.gif")
        UI.label_36.setMovie(UI.movie)
        UI.movie.start()

        # Update Time every 1000 mili.
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)

        UI.time.setText(label_time)
        UI.date.setText(label_date)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

import pyttsx3  # pip install pyttsx3
import sys
import time

from PySide2.QtWidgets import * #for QMainWindow
from PyQt5.QtCore import * #For QThread

import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QUrl, Qt, QEvent, QTimer)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


# GUI FILE
from ui_landing_page import Ui_MainWindow

UI = Ui_MainWindow()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


#This is a speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# This is the main thread
class LandingThread(QThread):
    def __init__(self):
        super(LandingThread, self).__init__()

    def run(self):
        self.introFunction()

    def introFunction(self):
        speak("Welcome to jarvish world")
        speak("I am your personal voice assistent") 
        speak("I am here to assist you to use this app easily")
        time.sleep(0.5)
        speak("if you already have an acount clicked on login button") 
        speak("or click on register button to register yourself")
        time.sleep(0.5)
        speak("to know more about me click on about button") 
        time.sleep(1)
        speak("to hear again click on the help button")
    
    def aboutFunction(self):
        speak("I am JARVIS 2.0 An advanced AI model.")
        speak("I am developed by Sandeep babu and Qamar babu") 
        time.sleep(0.5)
        speak("In this software, I will be assisting you in few tasks like")
        speak("doing google search")
        time.sleep(0.2)
        speak("opening any software")
        time.sleep(0.2)
        speak("and a lot more.")
        time.sleep(0.5)

# This is the main thread
class AboutThread(QThread):
    def __init__(self):
        super(AboutThread, self).__init__()

    def run(self):
        self.aboutFunction()

    def aboutFunction(self):
        speak("I am JARVIS 2.0 An advanced AI model.")
        speak("I am developed by Sandeep babu and Qamar babu") 
        time.sleep(0.5)
        speak("In this software, I will be assisting you in few tasks like")
        speak("doing google search")
        time.sleep(0.2)
        speak("opening any software")
        time.sleep(0.2)
        speak("and a lot more.")
        time.sleep(0.5)


LandingStartExecution = LandingThread()
AboutStartExecution = AboutThread()



# This is the main class
class Landing(QMainWindow):
    def __init__(self):
        super().__init__()
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

        LandingStartExecution.start()
        ###############################################
        #----------------- Minimize window
        UI.Btn_MINIMISE.clicked.connect(lambda: self.showMinimized())

        #----------------- Restore/Maximize window
        UI.Btn_MAXIMISE.clicked.connect(lambda: self.restore_or_maximize_window())

        #----------------- Close window
        UI.Btn_CLOSE.clicked.connect(lambda: self.close())

        # Setting GIFs
        UI.movie = QtGui.QMovie("gif\\9.gif")
        UI.gif_9.setMovie(UI.movie)
        UI.movie.start()

        UI.movie = QtGui.QMovie("gif\\3.gif")
        UI.gif_3.setMovie(UI.movie)
        UI.movie.start()

        UI.copyright.setText(u"\u00A9"+" 2021 AI Powered Personal Assistant | Designed by Sandeep and Qamar")

        UI.Btn_ABOUT.clicked.connect(self.speakIntro)
        UI.Btn_HELP.clicked.connect(self.startLandingIntro)

        UI.Btn_REGISTER.clicked.connect(self.openRegisterWindow)
        UI.Btn_LOGIN.clicked.connect(self.openLoginWindow)

    #This function is for running GUIs or GIFs
    def startLandingIntro(self):
        LandingStartExecution.start()

    def speakIntro(self):
        AboutStartExecution.start()
    
    def openRegisterWindow(self):
        LandingStartExecution.terminate()
        AboutStartExecution.terminate()
        import register

    def openLoginWindow(self):
        LandingStartExecution.terminate()
        AboutStartExecution.terminate()
        import login


       


app = QApplication(sys.argv)
landing_page = Landing()
# landing_page.setGeometry(0,0,1360,700)
landing_page.show()
exit(app.exec_())
import sys
from PySide2.QtWidgets import *
from PyQt5.QtCore import *

class LandingThread(QThread):
    def __init__(self):
        super(LandingThread, self).__init__()

LandingStartExecution = LandingThread()

class Landing(QMainWindow):
    def __init__(self):
        super().__init__()


    #This function is for running GUIs or GIFs
    def startLandingTask(self):
        LandingStartExecution.start()



app = QApplication(sys.argv)
landing_page = Landing()
landing_page.show()
exit(app.exec_())
import sys
from PySide2.QtWidgets import *

class Login(QMainWindow):
    def __init__(self):
        super().__init__()


# app = QApplication(sys.argv)
login_page = Login()
login_page.show()
# exit(app.exec_())
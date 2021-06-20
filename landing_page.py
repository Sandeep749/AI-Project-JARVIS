import sys
from PySide2.QtWidgets import *

class Landing(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)
landing_page = Landing()
landing_page.show()
exit(app.exec_())
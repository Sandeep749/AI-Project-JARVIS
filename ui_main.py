# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainSowEKm.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 731)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.main_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.main_frame)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 40))
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggle_button = QFrame(self.top_bar)
        self.toggle_button.setObjectName(u"toggle_button")
        self.toggle_button.setMaximumSize(QSize(40, 40))
        self.toggle_button.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.toggle_button.setFrameShape(QFrame.StyledPanel)
        self.toggle_button.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.toggle_button)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_toggle = QPushButton(self.toggle_button)
        self.Btn_toggle.setObjectName(u"Btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_toggle.sizePolicy().hasHeightForWidth())
        self.Btn_toggle.setSizePolicy(sizePolicy)
        self.Btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_toggle.setStyleSheet(u"\n"
"border: 0px solid;")
        icon = QIcon()
        icon.addFile(u"icons/list-button-with-3-elements-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_toggle.setIcon(icon)
        self.Btn_toggle.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.Btn_toggle)


        self.horizontalLayout.addWidget(self.toggle_button)

        self.top_frame = QFrame(self.top_bar)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 40))
        self.top_frame.setMaximumSize(QSize(16777215, 40))
        self.top_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_app_name = QFrame(self.top_frame)
        self.frame_app_name.setObjectName(u"frame_app_name")
        self.frame_app_name.setFrameShape(QFrame.StyledPanel)
        self.frame_app_name.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_app_name)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.App_name = QLabel(self.frame_app_name)
        self.App_name.setObjectName(u"App_name")
        font = QFont()
        font.setPointSize(10)
        self.App_name.setFont(font)

        self.verticalLayout_13.addWidget(self.App_name)


        self.horizontalLayout_3.addWidget(self.frame_app_name)

        self.frame_controls_2 = QFrame(self.top_frame)
        self.frame_controls_2.setObjectName(u"frame_controls_2")
        self.frame_controls_2.setFrameShape(QFrame.StyledPanel)
        self.frame_controls_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_controls_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.Btn_MINIMISE = QPushButton(self.frame_controls_2)
        self.Btn_MINIMISE.setObjectName(u"Btn_MINIMISE")
        self.Btn_MINIMISE.setMinimumSize(QSize(50, 30))
        self.Btn_MINIMISE.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_MINIMISE.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(90,90,90);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/minimize-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_MINIMISE.setIcon(icon1)
        self.Btn_MINIMISE.setFlat(True)

        self.horizontalLayout_4.addWidget(self.Btn_MINIMISE)

        self.Btn_MAXIMISE = QPushButton(self.frame_controls_2)
        self.Btn_MAXIMISE.setObjectName(u"Btn_MAXIMISE")
        self.Btn_MAXIMISE.setMinimumSize(QSize(50, 30))
        self.Btn_MAXIMISE.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_MAXIMISE.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(90, 90, 90);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/expand-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_MAXIMISE.setIcon(icon2)
        self.Btn_MAXIMISE.setFlat(True)

        self.horizontalLayout_4.addWidget(self.Btn_MAXIMISE)

        self.Btn_CLOSE = QPushButton(self.frame_controls_2)
        self.Btn_CLOSE.setObjectName(u"Btn_CLOSE")
        self.Btn_CLOSE.setMinimumSize(QSize(50, 30))
        self.Btn_CLOSE.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_CLOSE.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(170, 0, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/close-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_CLOSE.setIcon(icon3)
        self.Btn_CLOSE.setIconSize(QSize(12, 12))
        self.Btn_CLOSE.setFlat(True)

        self.horizontalLayout_4.addWidget(self.Btn_CLOSE)


        self.horizontalLayout_3.addWidget(self.frame_controls_2, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.top_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_11.addWidget(self.top_bar)

        self.content_frame = QFrame(self.main_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content_frame)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(40, 0))
        self.frame_left_menu.setMaximumSize(QSize(40, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setMinimumSize(QSize(40, 0))
        self.frame_top_menus.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_top_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_HOME = QPushButton(self.frame_top_menus)
        self.Btn_HOME.setObjectName(u"Btn_HOME")
        self.Btn_HOME.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setPointSize(11)
        self.Btn_HOME.setFont(font1)
        self.Btn_HOME.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_HOME.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/home-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_HOME.setIcon(icon4)
        self.Btn_HOME.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.Btn_HOME)

        self.Btn_ADVANCE = QPushButton(self.frame_top_menus)
        self.Btn_ADVANCE.setObjectName(u"Btn_ADVANCE")
        self.Btn_ADVANCE.setMinimumSize(QSize(0, 40))
        self.Btn_ADVANCE.setFont(font1)
        self.Btn_ADVANCE.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_ADVANCE.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"icons/circut-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_ADVANCE.setIcon(icon5)
        self.Btn_ADVANCE.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.Btn_ADVANCE)

        self.Btn_ABOUT = QPushButton(self.frame_top_menus)
        self.Btn_ABOUT.setObjectName(u"Btn_ABOUT")
        self.Btn_ABOUT.setMinimumSize(QSize(0, 40))
        self.Btn_ABOUT.setFont(font1)
        self.Btn_ABOUT.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_ABOUT.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/info-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_ABOUT.setIcon(icon6)
        self.Btn_ABOUT.setIconSize(QSize(17, 17))

        self.verticalLayout_4.addWidget(self.Btn_ABOUT)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)

        self.frame_bottom = QFrame(self.frame_left_menu)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMinimumSize(QSize(40, 0))
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Btn_EXIT = QPushButton(self.frame_bottom)
        self.Btn_EXIT.setObjectName(u"Btn_EXIT")
        self.Btn_EXIT.setMinimumSize(QSize(0, 40))
        self.Btn_EXIT.setFont(font1)
        self.Btn_EXIT.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_EXIT.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(170, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/exit-white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_EXIT.setIcon(icon7)
        self.Btn_EXIT.setIconSize(QSize(17, 17))

        self.verticalLayout_12.addWidget(self.Btn_EXIT)


        self.verticalLayout_3.addWidget(self.frame_bottom, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content_frame)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_7 = QVBoxLayout(self.page_home)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_home)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_controls = QFrame(self.frame)
        self.frame_controls.setObjectName(u"frame_controls")
        self.frame_controls.setMinimumSize(QSize(0, 50))
        self.frame_controls.setMaximumSize(QSize(16777215, 50))
        self.frame_controls.setStyleSheet(u"background-color: rgb(29, 29, 29);")
        self.frame_controls.setFrameShape(QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QFrame.Raised)
        self.Btn_start = QPushButton(self.frame_controls)
        self.Btn_start.setObjectName(u"Btn_start")
        self.Btn_start.setGeometry(QRect(10, 10, 91, 31))
        self.Btn_start.setFont(font)
        self.Btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_start.setStyleSheet(u"QPushButton {\n"
"	color: rgb(85, 170, 255);;\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid;\n"
"	border-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 0);\n"
"}")
        self.Btn_audio_mode = QPushButton(self.frame_controls)
        self.Btn_audio_mode.setObjectName(u"Btn_audio_mode")
        self.Btn_audio_mode.setGeometry(QRect(1120, 10, 91, 31))
        self.Btn_audio_mode.setFont(font)
        self.Btn_audio_mode.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_audio_mode.setStyleSheet(u"QPushButton {\n"
"	color: rgb(85, 170, 255);;\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid;\n"
"	border-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_text_mode = QPushButton(self.frame_controls)
        self.Btn_text_mode.setObjectName(u"Btn_text_mode")
        self.Btn_text_mode.setGeometry(QRect(1220, 10, 91, 31))
        self.Btn_text_mode.setFont(font)
        self.Btn_text_mode.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_text_mode.setStyleSheet(u"QPushButton {\n"
"	color: rgb(85, 170, 255);;\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 1px solid;\n"
"	border-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	border: 0px solid;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.frame_controls, 0, Qt.AlignTop)

        self.frame_main_content = QFrame(self.frame)
        self.frame_main_content.setObjectName(u"frame_main_content")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_main_content.sizePolicy().hasHeightForWidth())
        self.frame_main_content.setSizePolicy(sizePolicy1)
        self.frame_main_content.setMinimumSize(QSize(0, 100))
        self.frame_main_content.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_main_content.setFrameShape(QFrame.StyledPanel)
        self.frame_main_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_main_content)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_main_content)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_31 = QLabel(self.frame_3)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(540, 170, 91, 51))
        self.label_31.setPixmap(QPixmap(u"gif/36.gif"))
        self.label_31.setScaledContents(True)
        self.label_nice = QLabel(self.frame_3)
        self.label_nice.setObjectName(u"label_nice")
        self.label_nice.setGeometry(QRect(20, 240, 181, 141))
        self.label_nice.setPixmap(QPixmap(u"gif/nice.gif"))
        self.label_nice.setScaledContents(True)
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(470, 280, 91, 91))
        self.label_4.setPixmap(QPixmap(u"gif/45.gif"))
        self.label_4.setScaledContents(True)
        self.label_33 = QLabel(self.frame_3)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(-10, 380, 301, 171))
        self.label_33.setPixmap(QPixmap(u"gif/33.gif"))
        self.label_33.setScaledContents(True)
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(130, -30, 201, 201))
        self.label_22.setPixmap(QPixmap(u"gif/22.gif"))
        self.label_22.setScaledContents(True)
        self.label_23 = QLabel(self.frame_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(820, 260, 181, 301))
        self.label_23.setPixmap(QPixmap(u"gif/23.gif"))
        self.label_23.setScaledContents(True)
        self.label_48 = QLabel(self.frame_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(320, 140, 381, 431))
        self.label_48.setPixmap(QPixmap(u"gif/48.gif"))
        self.label_48.setScaledContents(True)
        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(200, 40, 61, 51))
        self.label_36.setPixmap(QPixmap(u"gif/55.gif"))
        self.label_36.setScaledContents(True)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 30, 401, 61))
        font2 = QFont()
        font2.setFamily(u"Algerian")
        font2.setPointSize(40)
        font2.setBold(False)
        font2.setWeight(50)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(640, 90, 201, 21))
        font3 = QFont()
        font3.setFamily(u"Arial Black")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_nice.raise_()
        self.label_33.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_48.raise_()
        self.label_31.raise_()
        self.label_4.raise_()
        self.label_36.raise_()
        self.label.raise_()
        self.label_5.raise_()

        self.horizontalLayout_6.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame_main_content)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setMaximumSize(QSize(300, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.date = QLabel(self.frame_2)
        self.date.setObjectName(u"date")
        self.date.setGeometry(QRect(130, 80, 111, 21))
        self.date.setFont(font)
        self.date.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.textDisplayConversation = QTextBrowser(self.frame_2)
        self.textDisplayConversation.setObjectName(u"textDisplayConversation")
        self.textDisplayConversation.setGeometry(QRect(0, 180, 291, 381))
        self.textDisplayConversation.setFont(font)
        self.textDisplayConversation.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"border:1px solid;\n"
"border-color: rgb(85, 170, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.time = QLabel(self.frame_2)
        self.time.setObjectName(u"time")
        self.time.setGeometry(QRect(120, 40, 171, 31))
        font4 = QFont()
        font4.setPointSize(30)
        self.time.setFont(font4)
        self.time.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_44 = QLabel(self.frame_2)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(240, 490, 41, 71))
        self.label_44.setPixmap(QPixmap(u"gif/44.gif"))
        self.label_44.setScaledContents(True)
        self.label_44.setIndent(-1)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 160, 81, 21))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.globe = QLabel(self.frame_2)
        self.globe.setObjectName(u"globe")
        self.globe.setGeometry(QRect(0, 30, 101, 101))
        self.globe.setPixmap(QPixmap(u"gif/17.gif"))
        self.globe.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_9.addWidget(self.frame_main_content)

        self.frame_footer = QFrame(self.frame)
        self.frame_footer.setObjectName(u"frame_footer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_footer.sizePolicy().hasHeightForWidth())
        self.frame_footer.setSizePolicy(sizePolicy2)
        self.frame_footer.setMinimumSize(QSize(0, 60))
        self.frame_footer.setMaximumSize(QSize(16777215, 60))
        self.frame_footer.setStyleSheet(u"border-top:1px solid;\n"
"border-top-color: rgb(85, 170, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_51 = QLabel(self.frame_footer)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"border:0px solid;")
        self.label_51.setPixmap(QPixmap(u"gif/51.gif"))

        self.horizontalLayout_5.addWidget(self.label_51)

        self.display = QLabel(self.frame_footer)
        self.display.setObjectName(u"display")
        font5 = QFont()
        font5.setPointSize(20)
        self.display.setFont(font5)
        self.display.setStyleSheet(u"color: rgb(85, 170, 255);\n"
"border:0px solid;")

        self.horizontalLayout_5.addWidget(self.display)


        self.verticalLayout_9.addWidget(self.frame_footer, 0, Qt.AlignBottom)


        self.verticalLayout_7.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_home)
        self.page_advance = QWidget()
        self.page_advance.setObjectName(u"page_advance")
        self.verticalLayout_6 = QVBoxLayout(self.page_advance)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_advance)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setPointSize(40)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_advance)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.verticalLayout_8 = QVBoxLayout(self.page_about)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.page_about)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_about)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout_11.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_toggle.setText("")
        self.App_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">AI Powered Personal Assistant</span></p></body></html>", None))
        self.Btn_MINIMISE.setText("")
        self.Btn_MAXIMISE.setText("")
        self.Btn_CLOSE.setText("")
        self.Btn_HOME.setText("")
        self.Btn_ADVANCE.setText("")
        self.Btn_ABOUT.setText("")
        self.Btn_EXIT.setText("")
        self.Btn_start.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.Btn_audio_mode.setText(QCoreApplication.translate("MainWindow", u"Audio mode", None))
        self.Btn_text_mode.setText(QCoreApplication.translate("MainWindow", u"Text Mode", None))
        self.label_31.setText("")
        self.label_nice.setText("")
        self.label_4.setText("")
        self.label_33.setText("")
        self.label_22.setText("")
        self.label_23.setText("")
        self.label_48.setText("")
        self.label_36.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"J.A.R.V.I.S. 2.0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"beyond intelligance...", None))
        self.date.setText("")
        self.time.setText("")
        self.label_44.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  Response Box", None))
        self.globe.setText("")
        self.label_51.setText("")
        self.display.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ADVANCE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
    # retranslateUi


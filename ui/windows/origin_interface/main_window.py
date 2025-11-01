# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)
from ui.resources import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.main_left_sidebar_layout = QWidget(self.centralwidget)
        self.main_left_sidebar_layout.setObjectName(u"main_left_sidebar_layout")
        self.main_left_sidebar_layout.setStyleSheet(u"/* \u00c1p d\u1ee5ng cho widget cha \u0111\u1ec3 c\u00f3 n\u1ec1n chung */\n"
"#main_left_sidebar_layout {\n"
"    background-color: #f2f2f2; /* Ho\u1eb7c m\u00e0u n\u1ec1n b\u1ea1n mu\u1ed1n */\n"
"}\n"
"\n"
"/* T\u00f9y ch\u1ec9nh cho T\u1ea4T C\u1ea2 QPushButton b\u00ean trong sidebar */\n"
"#main_left_sidebar_layout QPushButton {\n"
"    /* --- X\u00f3a b\u1ecf giao di\u1ec7n m\u1eb7c \u0111\u1ecbnh --- */\n"
"    border: none;\n"
"    background-color: transparent; /* Quan tr\u1ecdng: l\u00e0m n\u1ec1n n\u00fat trong su\u1ed1t */\n"
"\n"
"    /* --- C\u0103n ch\u1ec9nh & Kho\u1ea3ng c\u00e1ch --- */\n"
"    text-align: left; /* C\u0103n ch\u1eef sang tr\u00e1i */\n"
"    padding: 15px 10px; /* Th\u00eam kho\u1ea3ng \u0111\u1ec7m cho d\u1ec5 click */\n"
"    font-size: 16px;\n"
"\n"
"    /* --- Giao di\u1ec7n ch\u1eef --- */\n"
"    color: #333; /* M\u00e0u ch\u1eef m\u1eb7c \u0111\u1ecbnh */\n"
"}\n"
"\n"
"/* --- C\u00e1c tr\u1ea1ng th\u00e1i \u0111\u1ed9ng --- */\n"
"\n"
"/* 1. Khi di chu\u1ed9t v\u00e0o"
                        " n\u00fat */\n"
"#main_left_sidebar_layout QPushButton:hover {\n"
"   	background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* 2. Khi n\u00fat \u0111\u01b0\u1ee3c \"check\" (t\u1ee9c l\u00e0 \u0111\u01b0\u1ee3c ch\u1ecdn) */\n"
"#main_left_sidebar_layout QPushButton:checked {\n"
"    background-color: #e8e8e8; /* M\u00e0u n\u1ec1n khi \u0111\u01b0\u1ee3c ch\u1ecdn */\n"
"    color: #e60026; /* \u0110\u1ed5i m\u00e0u ch\u1eef */\n"
"    font-weight: bold;\n"
"    border-radius: 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.main_left_sidebar_layout)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.toggle_sidebar_button = QToolButton(self.main_left_sidebar_layout)
        self.toggle_sidebar_button.setObjectName(u"toggle_sidebar_button")
        self.toggle_sidebar_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggle_sidebar_button.setStyleSheet(u"QToolButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 5px; /* T\u0103ng v\u00f9ng c\u00f3 th\u1ec3 click */\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/bars-1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggle_sidebar_button.setIcon(icon)

        self.verticalLayout_3.addWidget(self.toggle_sidebar_button)

        self.dashboard_button = QPushButton(self.main_left_sidebar_layout)
        self.dashboard_button.setObjectName(u"dashboard_button")
        font = QFont()
        self.dashboard_button.setFont(font)

        self.verticalLayout_3.addWidget(self.dashboard_button)

        self.languages_button = QPushButton(self.main_left_sidebar_layout)
        self.languages_button.setObjectName(u"languages_button")
        self.languages_button.setFont(font)

        self.verticalLayout_3.addWidget(self.languages_button)

        self.databases_button = QPushButton(self.main_left_sidebar_layout)
        self.databases_button.setObjectName(u"databases_button")
        self.databases_button.setFont(font)

        self.verticalLayout_3.addWidget(self.databases_button)

        self.webserver_button = QPushButton(self.main_left_sidebar_layout)
        self.webserver_button.setObjectName(u"webserver_button")
        self.webserver_button.setFont(font)

        self.verticalLayout_3.addWidget(self.webserver_button)

        self.tools_button = QPushButton(self.main_left_sidebar_layout)
        self.tools_button.setObjectName(u"tools_button")

        self.verticalLayout_3.addWidget(self.tools_button)

        self.network_button = QPushButton(self.main_left_sidebar_layout)
        self.network_button.setObjectName(u"network_button")
        self.network_button.setFont(font)

        self.verticalLayout_3.addWidget(self.network_button)


        self.horizontalLayout_2.addWidget(self.main_left_sidebar_layout)

        self.main_content_layout = QHBoxLayout()
        self.main_content_layout.setObjectName(u"main_content_layout")
        self.main_content_area = QStackedWidget(self.centralwidget)
        self.main_content_area.setObjectName(u"main_content_area")
        self.main_content_area.setStyleSheet(u"background-color:rgb(255,255,255)")

        self.main_content_layout.addWidget(self.main_content_area)


        self.horizontalLayout_2.addLayout(self.main_content_layout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.main_content_area.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_sidebar_button.setText(QCoreApplication.translate("MainWindow", u"barsButton", None))
        self.dashboard_button.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.languages_button.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.databases_button.setText(QCoreApplication.translate("MainWindow", u"Databases", None))
        self.webserver_button.setText(QCoreApplication.translate("MainWindow", u"Webserver", None))
        self.tools_button.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.network_button.setText(QCoreApplication.translate("MainWindow", u"Network", None))
    # retranslateUi


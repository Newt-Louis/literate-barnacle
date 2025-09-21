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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)
import ui.resources.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 461)
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
        icon.addFile(u":/icons/icons/bars-1.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.main_content_area.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.webserver_page = QWidget()
        self.webserver_page.setObjectName(u"webserver_page")
        self.verticalLayout_4 = QVBoxLayout(self.webserver_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.webserver_title_layout = QHBoxLayout()
        self.webserver_title_layout.setSpacing(0)
        self.webserver_title_layout.setObjectName(u"webserver_title_layout")
        self.webserver_title_label = QLabel(self.webserver_page)
        self.webserver_title_label.setObjectName(u"webserver_title_label")
        self.webserver_title_label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webserver_title_label.sizePolicy().hasHeightForWidth())
        self.webserver_title_label.setSizePolicy(sizePolicy)

        self.webserver_title_layout.addWidget(self.webserver_title_label)


        self.verticalLayout_4.addLayout(self.webserver_title_layout)

        self.webserver_save_change_layout = QHBoxLayout()
        self.webserver_save_change_layout.setObjectName(u"webserver_save_change_layout")
        self.webserver_save_change_buttonbox = QDialogButtonBox(self.webserver_page)
        self.webserver_save_change_buttonbox.setObjectName(u"webserver_save_change_buttonbox")
        self.webserver_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.webserver_save_change_layout.addWidget(self.webserver_save_change_buttonbox)


        self.verticalLayout_4.addLayout(self.webserver_save_change_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.webserver_content_layout = QGridLayout()
        self.webserver_content_layout.setObjectName(u"webserver_content_layout")
        self.apache_checkbox = QCheckBox(self.webserver_page)
        self.apache_checkbox.setObjectName(u"apache_checkbox")

        self.webserver_content_layout.addWidget(self.apache_checkbox, 1, 0, 1, 1)

        self.nginx_checkbox = QCheckBox(self.webserver_page)
        self.nginx_checkbox.setObjectName(u"nginx_checkbox")

        self.webserver_content_layout.addWidget(self.nginx_checkbox, 2, 0, 1, 1)

        self.apache_combobox = QComboBox(self.webserver_page)
        self.apache_combobox.setObjectName(u"apache_combobox")

        self.webserver_content_layout.addWidget(self.apache_combobox, 1, 1, 1, 1)

        self.nginx_combobox = QComboBox(self.webserver_page)
        self.nginx_combobox.setObjectName(u"nginx_combobox")

        self.webserver_content_layout.addWidget(self.nginx_combobox, 2, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.webserver_content_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.verticalLayout_4.setStretch(3, 1)
        self.main_content_area.addWidget(self.webserver_page)
        self.tools_page = QWidget()
        self.tools_page.setObjectName(u"tools_page")
        self.verticalLayout_5 = QVBoxLayout(self.tools_page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tools_title_layout = QHBoxLayout()
        self.tools_title_layout.setObjectName(u"tools_title_layout")
        self.tools_title_label = QLabel(self.tools_page)
        self.tools_title_label.setObjectName(u"tools_title_label")
        sizePolicy.setHeightForWidth(self.tools_title_label.sizePolicy().hasHeightForWidth())
        self.tools_title_label.setSizePolicy(sizePolicy)

        self.tools_title_layout.addWidget(self.tools_title_label)


        self.verticalLayout_5.addLayout(self.tools_title_layout)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_11)

        self.tools_content_layout = QGridLayout()
        self.tools_content_layout.setObjectName(u"tools_content_layout")
        self.quickadd_combobox = QComboBox(self.tools_page)
        self.quickadd_combobox.setObjectName(u"quickadd_combobox")

        self.tools_content_layout.addWidget(self.quickadd_combobox, 3, 1, 1, 1)

        self.rightclickmenu_combobox = QComboBox(self.tools_page)
        self.rightclickmenu_combobox.setObjectName(u"rightclickmenu_combobox")

        self.tools_content_layout.addWidget(self.rightclickmenu_combobox, 2, 1, 1, 1)

        self.wildcarddns_combobox = QComboBox(self.tools_page)
        self.wildcarddns_combobox.setObjectName(u"wildcarddns_combobox")

        self.tools_content_layout.addWidget(self.wildcarddns_combobox, 0, 1, 1, 1)

        self.deleteproject_combobox = QComboBox(self.tools_page)
        self.deleteproject_combobox.setObjectName(u"deleteproject_combobox")

        self.tools_content_layout.addWidget(self.deleteproject_combobox, 4, 1, 1, 1)

        self.rightclickmenu_label = QLabel(self.tools_page)
        self.rightclickmenu_label.setObjectName(u"rightclickmenu_label")

        self.tools_content_layout.addWidget(self.rightclickmenu_label, 2, 0, 1, 1)

        self.deleteproject_label = QLabel(self.tools_page)
        self.deleteproject_label.setObjectName(u"deleteproject_label")

        self.tools_content_layout.addWidget(self.deleteproject_label, 4, 0, 1, 1)

        self.quickadd_label = QLabel(self.tools_page)
        self.quickadd_label.setObjectName(u"quickadd_label")

        self.tools_content_layout.addWidget(self.quickadd_label, 3, 0, 1, 1)

        self.cron_label = QLabel(self.tools_page)
        self.cron_label.setObjectName(u"cron_label")

        self.tools_content_layout.addWidget(self.cron_label, 1, 0, 1, 1)

        self.wildcarddns_label = QLabel(self.tools_page)
        self.wildcarddns_label.setObjectName(u"wildcarddns_label")

        self.tools_content_layout.addWidget(self.wildcarddns_label, 0, 0, 1, 1)

        self.cron_combobox = QComboBox(self.tools_page)
        self.cron_combobox.setObjectName(u"cron_combobox")

        self.tools_content_layout.addWidget(self.cron_combobox, 1, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.tools_content_layout)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_12)

        self.verticalLayout_5.setStretch(2, 1)
        self.main_content_area.addWidget(self.tools_page)
        self.network_page = QWidget()
        self.network_page.setObjectName(u"network_page")
        self.verticalLayout_6 = QVBoxLayout(self.network_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.network_title_layout = QHBoxLayout()
        self.network_title_layout.setObjectName(u"network_title_layout")
        self.network_title_label = QLabel(self.network_page)
        self.network_title_label.setObjectName(u"network_title_label")
        sizePolicy.setHeightForWidth(self.network_title_label.sizePolicy().hasHeightForWidth())
        self.network_title_label.setSizePolicy(sizePolicy)

        self.network_title_layout.addWidget(self.network_title_label)


        self.verticalLayout_6.addLayout(self.network_title_layout)

        self.network_save_change_layout = QHBoxLayout()
        self.network_save_change_layout.setObjectName(u"network_save_change_layout")
        self.network_save_change_buttonbox = QDialogButtonBox(self.network_page)
        self.network_save_change_buttonbox.setObjectName(u"network_save_change_buttonbox")
        self.network_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.network_save_change_layout.addWidget(self.network_save_change_buttonbox)


        self.verticalLayout_6.addLayout(self.network_save_change_layout)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_9)

        self.network_content_layout = QGridLayout()
        self.network_content_layout.setObjectName(u"network_content_layout")
        self.traceroute_checkbox = QCheckBox(self.network_page)
        self.traceroute_checkbox.setObjectName(u"traceroute_checkbox")

        self.network_content_layout.addWidget(self.traceroute_checkbox, 2, 0, 1, 1)

        self.ngrok_checkbox = QCheckBox(self.network_page)
        self.ngrok_checkbox.setObjectName(u"ngrok_checkbox")

        self.network_content_layout.addWidget(self.ngrok_checkbox, 1, 0, 1, 1)

        self.telnet_checkbox = QCheckBox(self.network_page)
        self.telnet_checkbox.setObjectName(u"telnet_checkbox")

        self.network_content_layout.addWidget(self.telnet_checkbox, 0, 0, 1, 1)

        self.telnet_combobox = QComboBox(self.network_page)
        self.telnet_combobox.setObjectName(u"telnet_combobox")

        self.network_content_layout.addWidget(self.telnet_combobox, 0, 1, 1, 1)

        self.ngrok_combobox = QComboBox(self.network_page)
        self.ngrok_combobox.setObjectName(u"ngrok_combobox")

        self.network_content_layout.addWidget(self.ngrok_combobox, 1, 1, 1, 1)

        self.traceroute_combobox = QComboBox(self.network_page)
        self.traceroute_combobox.setObjectName(u"traceroute_combobox")

        self.network_content_layout.addWidget(self.traceroute_combobox, 2, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.network_content_layout)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)

        self.network_add_new_layout = QHBoxLayout()
        self.network_add_new_layout.setObjectName(u"network_add_new_layout")
        self.network_add_new_button = QPushButton(self.network_page)
        self.network_add_new_button.setObjectName(u"network_add_new_button")

        self.network_add_new_layout.addWidget(self.network_add_new_button)


        self.verticalLayout_6.addLayout(self.network_add_new_layout)

        self.verticalLayout_6.setStretch(3, 1)
        self.main_content_area.addWidget(self.network_page)
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.verticalLayout_7 = QVBoxLayout(self.dashboard_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.dashboard_title_layout = QHBoxLayout()
        self.dashboard_title_layout.setObjectName(u"dashboard_title_layout")
        self.dashboard_title_label = QLabel(self.dashboard_page)
        self.dashboard_title_label.setObjectName(u"dashboard_title_label")

        self.dashboard_title_layout.addWidget(self.dashboard_title_label)


        self.verticalLayout_7.addLayout(self.dashboard_title_layout)

        self.dashboard_head_column_layout = QHBoxLayout()
        self.dashboard_head_column_layout.setObjectName(u"dashboard_head_column_layout")
        self.dashboard_service_label = QLabel(self.dashboard_page)
        self.dashboard_service_label.setObjectName(u"dashboard_service_label")

        self.dashboard_head_column_layout.addWidget(self.dashboard_service_label)

        self.dashboard_type_label = QLabel(self.dashboard_page)
        self.dashboard_type_label.setObjectName(u"dashboard_type_label")

        self.dashboard_head_column_layout.addWidget(self.dashboard_type_label)

        self.dashboard_version_label = QLabel(self.dashboard_page)
        self.dashboard_version_label.setObjectName(u"dashboard_version_label")

        self.dashboard_head_column_layout.addWidget(self.dashboard_version_label)


        self.verticalLayout_7.addLayout(self.dashboard_head_column_layout)

        self.dashboard_content_layout = QGridLayout()
        self.dashboard_content_layout.setObjectName(u"dashboard_content_layout")
        self.database_type_label = QLabel(self.dashboard_page)
        self.database_type_label.setObjectName(u"database_type_label")

        self.dashboard_content_layout.addWidget(self.database_type_label, 9, 1, 1, 1)

        self.network_service_label = QLabel(self.dashboard_page)
        self.network_service_label.setObjectName(u"network_service_label")

        self.dashboard_content_layout.addWidget(self.network_service_label, 15, 0, 1, 1)

        self.tools_type_3_label = QLabel(self.dashboard_page)
        self.tools_type_3_label.setObjectName(u"tools_type_3_label")

        self.dashboard_content_layout.addWidget(self.tools_type_3_label, 14, 1, 1, 1)

        self.tools_version_2_label = QLabel(self.dashboard_page)
        self.tools_version_2_label.setObjectName(u"tools_version_2_label")

        self.dashboard_content_layout.addWidget(self.tools_version_2_label, 12, 2, 1, 1)

        self.tools_version_3_label = QLabel(self.dashboard_page)
        self.tools_version_3_label.setObjectName(u"tools_version_3_label")

        self.dashboard_content_layout.addWidget(self.tools_version_3_label, 14, 2, 1, 1)

        self.language_service_label = QLabel(self.dashboard_page)
        self.language_service_label.setObjectName(u"language_service_label")

        self.dashboard_content_layout.addWidget(self.language_service_label, 8, 0, 1, 1)

        self.tools_type_1_label = QLabel(self.dashboard_page)
        self.tools_type_1_label.setObjectName(u"tools_type_1_label")

        self.dashboard_content_layout.addWidget(self.tools_type_1_label, 11, 1, 1, 1)

        self.tools_type_2_label = QLabel(self.dashboard_page)
        self.tools_type_2_label.setObjectName(u"tools_type_2_label")

        self.dashboard_content_layout.addWidget(self.tools_type_2_label, 12, 1, 1, 1)

        self.startall_button = QPushButton(self.dashboard_page)
        self.startall_button.setObjectName(u"startall_button")

        self.dashboard_content_layout.addWidget(self.startall_button, 16, 1, 1, 1)

        self.language_version_label = QLabel(self.dashboard_page)
        self.language_version_label.setObjectName(u"language_version_label")

        self.dashboard_content_layout.addWidget(self.language_version_label, 8, 2, 1, 1)

        self.tools_version_1_label = QLabel(self.dashboard_page)
        self.tools_version_1_label.setObjectName(u"tools_version_1_label")

        self.dashboard_content_layout.addWidget(self.tools_version_1_label, 11, 2, 1, 1)

        self.tools_service_label = QLabel(self.dashboard_page)
        self.tools_service_label.setObjectName(u"tools_service_label")

        self.dashboard_content_layout.addWidget(self.tools_service_label, 11, 0, 1, 1)

        self.language_type_label = QLabel(self.dashboard_page)
        self.language_type_label.setObjectName(u"language_type_label")

        self.dashboard_content_layout.addWidget(self.language_type_label, 8, 1, 1, 1)

        self.network_version_label = QLabel(self.dashboard_page)
        self.network_version_label.setObjectName(u"network_version_label")

        self.dashboard_content_layout.addWidget(self.network_version_label, 15, 2, 1, 1)

        self.database_service_label = QLabel(self.dashboard_page)
        self.database_service_label.setObjectName(u"database_service_label")

        self.dashboard_content_layout.addWidget(self.database_service_label, 9, 0, 1, 1)

        self.database_version_label = QLabel(self.dashboard_page)
        self.database_version_label.setObjectName(u"database_version_label")

        self.dashboard_content_layout.addWidget(self.database_version_label, 9, 2, 1, 1)

        self.network_type_label = QLabel(self.dashboard_page)
        self.network_type_label.setObjectName(u"network_type_label")

        self.dashboard_content_layout.addWidget(self.network_type_label, 15, 1, 1, 1)

        self.webserver_service_label = QLabel(self.dashboard_page)
        self.webserver_service_label.setObjectName(u"webserver_service_label")

        self.dashboard_content_layout.addWidget(self.webserver_service_label, 10, 0, 1, 1)

        self.webserver_type_label = QLabel(self.dashboard_page)
        self.webserver_type_label.setObjectName(u"webserver_type_label")

        self.dashboard_content_layout.addWidget(self.webserver_type_label, 10, 1, 1, 1)

        self.webserver_version_label = QLabel(self.dashboard_page)
        self.webserver_version_label.setObjectName(u"webserver_version_label")

        self.dashboard_content_layout.addWidget(self.webserver_version_label, 10, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.dashboard_content_layout)

        self.verticalLayout_7.setStretch(2, 1)
        self.main_content_area.addWidget(self.dashboard_page)
        self.languages_page = QWidget()
        self.languages_page.setObjectName(u"languages_page")
        self.verticalLayout = QVBoxLayout(self.languages_page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.language_title_layout = QHBoxLayout()
        self.language_title_layout.setObjectName(u"language_title_layout")
        self.language_title_label = QLabel(self.languages_page)
        self.language_title_label.setObjectName(u"language_title_label")
        sizePolicy.setHeightForWidth(self.language_title_label.sizePolicy().hasHeightForWidth())
        self.language_title_label.setSizePolicy(sizePolicy)

        self.language_title_layout.addWidget(self.language_title_label)


        self.verticalLayout.addLayout(self.language_title_layout)

        self.language_save_change_layout = QHBoxLayout()
        self.language_save_change_layout.setObjectName(u"language_save_change_layout")
        self.language_save_change_buttonbox = QDialogButtonBox(self.languages_page)
        self.language_save_change_buttonbox.setObjectName(u"language_save_change_buttonbox")
        self.language_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.language_save_change_layout.addWidget(self.language_save_change_buttonbox)


        self.verticalLayout.addLayout(self.language_save_change_layout)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.language_content_layout = QGridLayout()
        self.language_content_layout.setObjectName(u"language_content_layout")
        self.python_radio = QRadioButton(self.languages_page)
        self.python_radio.setObjectName(u"python_radio")

        self.language_content_layout.addWidget(self.python_radio, 1, 0, 1, 1)

        self.nodejs_radio = QRadioButton(self.languages_page)
        self.nodejs_radio.setObjectName(u"nodejs_radio")

        self.language_content_layout.addWidget(self.nodejs_radio, 3, 0, 1, 1)

        self.php_radio = QRadioButton(self.languages_page)
        self.php_radio.setObjectName(u"php_radio")

        self.language_content_layout.addWidget(self.php_radio, 0, 0, 1, 1)

        self.java_radio = QRadioButton(self.languages_page)
        self.java_radio.setObjectName(u"java_radio")

        self.language_content_layout.addWidget(self.java_radio, 2, 0, 1, 1)

        self.python_combobox = QComboBox(self.languages_page)
        self.python_combobox.setObjectName(u"python_combobox")

        self.language_content_layout.addWidget(self.python_combobox, 1, 1, 1, 1)

        self.php_combobox = QComboBox(self.languages_page)
        self.php_combobox.setObjectName(u"php_combobox")

        self.language_content_layout.addWidget(self.php_combobox, 0, 1, 1, 1)

        self.java_combobox = QComboBox(self.languages_page)
        self.java_combobox.setObjectName(u"java_combobox")

        self.language_content_layout.addWidget(self.java_combobox, 2, 1, 1, 1)

        self.nodejs_combobox = QComboBox(self.languages_page)
        self.nodejs_combobox.setObjectName(u"nodejs_combobox")

        self.language_content_layout.addWidget(self.nodejs_combobox, 3, 1, 1, 1)


        self.verticalLayout.addLayout(self.language_content_layout)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.language_add_new_layout = QHBoxLayout()
        self.language_add_new_layout.setObjectName(u"language_add_new_layout")
        self.language_add_new_button = QPushButton(self.languages_page)
        self.language_add_new_button.setObjectName(u"language_add_new_button")

        self.language_add_new_layout.addWidget(self.language_add_new_button)


        self.verticalLayout.addLayout(self.language_add_new_layout)

        self.verticalLayout.setStretch(3, 1)
        self.main_content_area.addWidget(self.languages_page)
        self.databases_page = QWidget()
        self.databases_page.setObjectName(u"databases_page")
        self.verticalLayout_2 = QVBoxLayout(self.databases_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.database_title_layout = QHBoxLayout()
        self.database_title_layout.setObjectName(u"database_title_layout")
        self.database_title_label = QLabel(self.databases_page)
        self.database_title_label.setObjectName(u"database_title_label")
        sizePolicy.setHeightForWidth(self.database_title_label.sizePolicy().hasHeightForWidth())
        self.database_title_label.setSizePolicy(sizePolicy)

        self.database_title_layout.addWidget(self.database_title_label)


        self.verticalLayout_2.addLayout(self.database_title_layout)

        self.database_save_change_layout = QHBoxLayout()
        self.database_save_change_layout.setObjectName(u"database_save_change_layout")
        self.database_save_change_buttonbox = QDialogButtonBox(self.databases_page)
        self.database_save_change_buttonbox.setObjectName(u"database_save_change_buttonbox")
        self.database_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.database_save_change_layout.addWidget(self.database_save_change_buttonbox)


        self.verticalLayout_2.addLayout(self.database_save_change_layout)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_7)

        self.database_content_layout = QGridLayout()
        self.database_content_layout.setObjectName(u"database_content_layout")
        self.mysql_radio = QRadioButton(self.databases_page)
        self.mysql_radio.setObjectName(u"mysql_radio")

        self.database_content_layout.addWidget(self.mysql_radio, 0, 0, 1, 1)

        self.mysql_combobox = QComboBox(self.databases_page)
        self.mysql_combobox.setObjectName(u"mysql_combobox")

        self.database_content_layout.addWidget(self.mysql_combobox, 0, 1, 1, 1)

        self.sqlserver_radio = QRadioButton(self.databases_page)
        self.sqlserver_radio.setObjectName(u"sqlserver_radio")

        self.database_content_layout.addWidget(self.sqlserver_radio, 1, 0, 1, 1)

        self.sqlserver_combobox = QComboBox(self.databases_page)
        self.sqlserver_combobox.setObjectName(u"sqlserver_combobox")

        self.database_content_layout.addWidget(self.sqlserver_combobox, 1, 1, 1, 1)

        self.sqlite_radio = QRadioButton(self.databases_page)
        self.sqlite_radio.setObjectName(u"sqlite_radio")

        self.database_content_layout.addWidget(self.sqlite_radio, 2, 0, 1, 1)

        self.sqlite_combobox = QComboBox(self.databases_page)
        self.sqlite_combobox.setObjectName(u"sqlite_combobox")

        self.database_content_layout.addWidget(self.sqlite_combobox, 2, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.database_content_layout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.database_add_new_layout = QHBoxLayout()
        self.database_add_new_layout.setObjectName(u"database_add_new_layout")
        self.database_add_new_button = QPushButton(self.databases_page)
        self.database_add_new_button.setObjectName(u"database_add_new_button")

        self.database_add_new_layout.addWidget(self.database_add_new_button)


        self.verticalLayout_2.addLayout(self.database_add_new_layout)

        self.verticalLayout_2.setStretch(3, 1)
        self.main_content_area.addWidget(self.databases_page)

        self.main_content_layout.addWidget(self.main_content_area)


        self.horizontalLayout_2.addLayout(self.main_content_layout)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.main_content_area.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle_sidebar_button.setText(QCoreApplication.translate("MainWindow", u"cbxcbxc", None))
        self.dashboard_button.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.languages_button.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.databases_button.setText(QCoreApplication.translate("MainWindow", u"Databases", None))
        self.webserver_button.setText(QCoreApplication.translate("MainWindow", u"Webserver", None))
        self.tools_button.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.network_button.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.webserver_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Webserver</span></p></body></html>", None))
        self.apache_checkbox.setText(QCoreApplication.translate("MainWindow", u"Apache", None))
        self.nginx_checkbox.setText(QCoreApplication.translate("MainWindow", u"Nginx", None))
        self.tools_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Tools</span></p></body></html>", None))
        self.rightclickmenu_label.setText(QCoreApplication.translate("MainWindow", u"Right Click Menu", None))
        self.deleteproject_label.setText(QCoreApplication.translate("MainWindow", u"Delete Project", None))
        self.quickadd_label.setText(QCoreApplication.translate("MainWindow", u"Quick Add", None))
        self.cron_label.setText(QCoreApplication.translate("MainWindow", u"Cron", None))
        self.wildcarddns_label.setText(QCoreApplication.translate("MainWindow", u"Wildcard DNS", None))
        self.network_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Network</span></p></body></html>", None))
        self.traceroute_checkbox.setText(QCoreApplication.translate("MainWindow", u"Traceroute", None))
        self.ngrok_checkbox.setText(QCoreApplication.translate("MainWindow", u"Ngrok", None))
        self.telnet_checkbox.setText(QCoreApplication.translate("MainWindow", u"Telnet", None))
        self.network_add_new_button.setText(QCoreApplication.translate("MainWindow", u"New Customize", None))
        self.dashboard_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Dashboard</span></p></body></html>", None))
        self.dashboard_service_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Service</span></p></body></html>", None))
        self.dashboard_type_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Type</span></p></body></html>", None))
        self.dashboard_version_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Version</span></p></body></html>", None))
        self.database_type_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.network_service_label.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.tools_type_3_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tools_version_2_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tools_version_3_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.language_service_label.setText(QCoreApplication.translate("MainWindow", u"Language", None))
        self.tools_type_1_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tools_type_2_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.startall_button.setText(QCoreApplication.translate("MainWindow", u"Start All", None))
        self.language_version_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tools_version_1_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tools_service_label.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.language_type_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.network_version_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.database_service_label.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.database_version_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.network_type_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.webserver_service_label.setText(QCoreApplication.translate("MainWindow", u"Webserver", None))
        self.webserver_type_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.webserver_version_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.language_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Languages</span></p></body></html>", None))
        self.python_radio.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.nodejs_radio.setText(QCoreApplication.translate("MainWindow", u"Nodejs", None))
        self.php_radio.setText(QCoreApplication.translate("MainWindow", u"PHP", None))
        self.java_radio.setText(QCoreApplication.translate("MainWindow", u"Java", None))
        self.language_add_new_button.setText(QCoreApplication.translate("MainWindow", u"Add New Languages", None))
        self.database_title_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Databases</span></p></body></html>", None))
        self.mysql_radio.setText(QCoreApplication.translate("MainWindow", u"MySQL", None))
        self.sqlserver_radio.setText(QCoreApplication.translate("MainWindow", u"SQL Server", None))
        self.sqlite_radio.setText(QCoreApplication.translate("MainWindow", u"SQLite", None))
        self.database_add_new_button.setText(QCoreApplication.translate("MainWindow", u"Add New Databases", None))
    # retranslateUi


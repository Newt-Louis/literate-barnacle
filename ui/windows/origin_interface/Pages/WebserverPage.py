# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WebserverPage.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_WebserverPage(object):
    def setupUi(self, WebserverPage):
        if not WebserverPage.objectName():
            WebserverPage.setObjectName(u"WebserverPage")
        WebserverPage.resize(480, 640)
        self.verticalLayout = QVBoxLayout(WebserverPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.webserver_title_layout = QHBoxLayout()
        self.webserver_title_layout.setSpacing(0)
        self.webserver_title_layout.setObjectName(u"webserver_title_layout")
        self.webserver_title_label = QLabel(WebserverPage)
        self.webserver_title_label.setObjectName(u"webserver_title_label")
        self.webserver_title_label.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webserver_title_label.sizePolicy().hasHeightForWidth())
        self.webserver_title_label.setSizePolicy(sizePolicy)

        self.webserver_title_layout.addWidget(self.webserver_title_label)


        self.verticalLayout.addLayout(self.webserver_title_layout)

        self.webserver_save_change_layout = QHBoxLayout()
        self.webserver_save_change_layout.setObjectName(u"webserver_save_change_layout")
        self.webserver_save_change_buttonbox = QDialogButtonBox(WebserverPage)
        self.webserver_save_change_buttonbox.setObjectName(u"webserver_save_change_buttonbox")
        self.webserver_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.webserver_save_change_layout.addWidget(self.webserver_save_change_buttonbox)


        self.verticalLayout.addLayout(self.webserver_save_change_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 241, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.webserver_content_layout = QGridLayout()
        self.webserver_content_layout.setObjectName(u"webserver_content_layout")
        self.apache_checkbox = QCheckBox(WebserverPage)
        self.apache_checkbox.setObjectName(u"apache_checkbox")

        self.webserver_content_layout.addWidget(self.apache_checkbox, 1, 0, 1, 1)

        self.nginx_checkbox = QCheckBox(WebserverPage)
        self.nginx_checkbox.setObjectName(u"nginx_checkbox")

        self.webserver_content_layout.addWidget(self.nginx_checkbox, 2, 0, 1, 1)

        self.apache_combobox = QComboBox(WebserverPage)
        self.apache_combobox.setObjectName(u"apache_combobox")

        self.webserver_content_layout.addWidget(self.apache_combobox, 1, 1, 1, 1)

        self.nginx_combobox = QComboBox(WebserverPage)
        self.nginx_combobox.setObjectName(u"nginx_combobox")

        self.webserver_content_layout.addWidget(self.nginx_combobox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.webserver_content_layout)

        self.verticalSpacer = QSpacerItem(20, 241, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(WebserverPage)

        QMetaObject.connectSlotsByName(WebserverPage)
    # setupUi

    def retranslateUi(self, WebserverPage):
        WebserverPage.setWindowTitle(QCoreApplication.translate("WebserverPage", u"Form", None))
        self.webserver_title_label.setText(QCoreApplication.translate("WebserverPage", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Webserver</span></p></body></html>", None))
        self.apache_checkbox.setText(QCoreApplication.translate("WebserverPage", u"Apache", None))
        self.nginx_checkbox.setText(QCoreApplication.translate("WebserverPage", u"Nginx", None))
    # retranslateUi


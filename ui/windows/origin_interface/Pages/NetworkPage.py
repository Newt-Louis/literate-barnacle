# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NetworkPage.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_NetworkPage(object):
    def setupUi(self, NetworkPage):
        if not NetworkPage.objectName():
            NetworkPage.setObjectName(u"NetworkPage")
        NetworkPage.resize(480, 640)
        self.verticalLayout = QVBoxLayout(NetworkPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.network_title_layout = QHBoxLayout()
        self.network_title_layout.setObjectName(u"network_title_layout")
        self.network_title_label = QLabel(NetworkPage)
        self.network_title_label.setObjectName(u"network_title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.network_title_label.sizePolicy().hasHeightForWidth())
        self.network_title_label.setSizePolicy(sizePolicy)

        self.network_title_layout.addWidget(self.network_title_label)


        self.verticalLayout.addLayout(self.network_title_layout)

        self.network_save_change_layout = QHBoxLayout()
        self.network_save_change_layout.setObjectName(u"network_save_change_layout")
        self.network_save_change_buttonbox = QDialogButtonBox(NetworkPage)
        self.network_save_change_buttonbox.setObjectName(u"network_save_change_buttonbox")
        self.network_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.network_save_change_layout.addWidget(self.network_save_change_buttonbox)


        self.verticalLayout.addLayout(self.network_save_change_layout)

        self.verticalSpacer_9 = QSpacerItem(20, 210, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_9)

        self.network_content_layout = QGridLayout()
        self.network_content_layout.setObjectName(u"network_content_layout")
        self.traceroute_checkbox = QCheckBox(NetworkPage)
        self.traceroute_checkbox.setObjectName(u"traceroute_checkbox")

        self.network_content_layout.addWidget(self.traceroute_checkbox, 2, 0, 1, 1)

        self.ngrok_checkbox = QCheckBox(NetworkPage)
        self.ngrok_checkbox.setObjectName(u"ngrok_checkbox")

        self.network_content_layout.addWidget(self.ngrok_checkbox, 1, 0, 1, 1)

        self.telnet_checkbox = QCheckBox(NetworkPage)
        self.telnet_checkbox.setObjectName(u"telnet_checkbox")

        self.network_content_layout.addWidget(self.telnet_checkbox, 0, 0, 1, 1)

        self.telnet_combobox = QComboBox(NetworkPage)
        self.telnet_combobox.setObjectName(u"telnet_combobox")

        self.network_content_layout.addWidget(self.telnet_combobox, 0, 1, 1, 1)

        self.ngrok_combobox = QComboBox(NetworkPage)
        self.ngrok_combobox.setObjectName(u"ngrok_combobox")

        self.network_content_layout.addWidget(self.ngrok_combobox, 1, 1, 1, 1)

        self.traceroute_combobox = QComboBox(NetworkPage)
        self.traceroute_combobox.setObjectName(u"traceroute_combobox")

        self.network_content_layout.addWidget(self.traceroute_combobox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.network_content_layout)

        self.verticalSpacer_11 = QSpacerItem(20, 210, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.network_add_new_layout = QHBoxLayout()
        self.network_add_new_layout.setObjectName(u"network_add_new_layout")
        self.network_add_new_button = QPushButton(NetworkPage)
        self.network_add_new_button.setObjectName(u"network_add_new_button")

        self.network_add_new_layout.addWidget(self.network_add_new_button)


        self.verticalLayout.addLayout(self.network_add_new_layout)


        self.retranslateUi(NetworkPage)

        QMetaObject.connectSlotsByName(NetworkPage)
    # setupUi

    def retranslateUi(self, NetworkPage):
        NetworkPage.setWindowTitle(QCoreApplication.translate("NetworkPage", u"Form", None))
        self.network_title_label.setText(QCoreApplication.translate("NetworkPage", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Network</span></p></body></html>", None))
        self.traceroute_checkbox.setText(QCoreApplication.translate("NetworkPage", u"Traceroute", None))
        self.ngrok_checkbox.setText(QCoreApplication.translate("NetworkPage", u"Ngrok", None))
        self.telnet_checkbox.setText(QCoreApplication.translate("NetworkPage", u"Telnet", None))
        self.network_add_new_button.setText(QCoreApplication.translate("NetworkPage", u"New Customize", None))
    # retranslateUi


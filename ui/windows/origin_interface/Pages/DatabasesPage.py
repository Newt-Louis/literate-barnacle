# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatabasesPage.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(480, 640)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.database_title_layout = QHBoxLayout()
        self.database_title_layout.setObjectName(u"database_title_layout")
        self.database_title_label = QLabel(Form)
        self.database_title_label.setObjectName(u"database_title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.database_title_label.sizePolicy().hasHeightForWidth())
        self.database_title_label.setSizePolicy(sizePolicy)

        self.database_title_layout.addWidget(self.database_title_label)


        self.verticalLayout.addLayout(self.database_title_layout)

        self.database_save_change_layout = QHBoxLayout()
        self.database_save_change_layout.setObjectName(u"database_save_change_layout")
        self.database_save_change_buttonbox = QDialogButtonBox(Form)
        self.database_save_change_buttonbox.setObjectName(u"database_save_change_buttonbox")
        self.database_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.database_save_change_layout.addWidget(self.database_save_change_buttonbox)


        self.verticalLayout.addLayout(self.database_save_change_layout)

        self.verticalSpacer_7 = QSpacerItem(20, 210, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.database_content_layout = QGridLayout()
        self.database_content_layout.setObjectName(u"database_content_layout")
        self.mysql_radio = QRadioButton(Form)
        self.mysql_radio.setObjectName(u"mysql_radio")

        self.database_content_layout.addWidget(self.mysql_radio, 0, 0, 1, 1)

        self.mysql_combobox = QComboBox(Form)
        self.mysql_combobox.setObjectName(u"mysql_combobox")

        self.database_content_layout.addWidget(self.mysql_combobox, 0, 1, 1, 1)

        self.sqlserver_radio = QRadioButton(Form)
        self.sqlserver_radio.setObjectName(u"sqlserver_radio")

        self.database_content_layout.addWidget(self.sqlserver_radio, 1, 0, 1, 1)

        self.sqlserver_combobox = QComboBox(Form)
        self.sqlserver_combobox.setObjectName(u"sqlserver_combobox")

        self.database_content_layout.addWidget(self.sqlserver_combobox, 1, 1, 1, 1)

        self.sqlite_radio = QRadioButton(Form)
        self.sqlite_radio.setObjectName(u"sqlite_radio")

        self.database_content_layout.addWidget(self.sqlite_radio, 2, 0, 1, 1)

        self.sqlite_combobox = QComboBox(Form)
        self.sqlite_combobox.setObjectName(u"sqlite_combobox")

        self.database_content_layout.addWidget(self.sqlite_combobox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.database_content_layout)

        self.verticalSpacer_6 = QSpacerItem(20, 210, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.database_add_new_layout = QHBoxLayout()
        self.database_add_new_layout.setObjectName(u"database_add_new_layout")
        self.database_add_new_button = QPushButton(Form)
        self.database_add_new_button.setObjectName(u"database_add_new_button")

        self.database_add_new_layout.addWidget(self.database_add_new_button)


        self.verticalLayout.addLayout(self.database_add_new_layout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.database_title_label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Databases</span></p></body></html>", None))
        self.mysql_radio.setText(QCoreApplication.translate("Form", u"MySQL", None))
        self.sqlserver_radio.setText(QCoreApplication.translate("Form", u"SQL Server", None))
        self.sqlite_radio.setText(QCoreApplication.translate("Form", u"SQLite", None))
        self.database_add_new_button.setText(QCoreApplication.translate("Form", u"Add New Databases", None))
    # retranslateUi


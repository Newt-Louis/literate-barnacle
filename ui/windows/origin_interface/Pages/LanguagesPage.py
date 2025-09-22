# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LanguagesPage.ui'
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
        self.language_title_layout = QHBoxLayout()
        self.language_title_layout.setObjectName(u"language_title_layout")
        self.language_title_label_2 = QLabel(Form)
        self.language_title_label_2.setObjectName(u"language_title_label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.language_title_label_2.sizePolicy().hasHeightForWidth())
        self.language_title_label_2.setSizePolicy(sizePolicy)

        self.language_title_layout.addWidget(self.language_title_label_2)


        self.verticalLayout.addLayout(self.language_title_layout)

        self.language_save_change_layout = QHBoxLayout()
        self.language_save_change_layout.setObjectName(u"language_save_change_layout")
        self.language_save_change_buttonbox = QDialogButtonBox(Form)
        self.language_save_change_buttonbox.setObjectName(u"language_save_change_buttonbox")
        self.language_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.language_save_change_layout.addWidget(self.language_save_change_buttonbox)


        self.verticalLayout.addLayout(self.language_save_change_layout)

        self.verticalSpacer_8 = QSpacerItem(20, 192, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.language_content_layout = QGridLayout()
        self.language_content_layout.setObjectName(u"language_content_layout")
        self.php_combobox = QComboBox(Form)
        self.php_combobox.setObjectName(u"php_combobox")

        self.language_content_layout.addWidget(self.php_combobox, 1, 1, 1, 1)

        self.java_combobox = QComboBox(Form)
        self.java_combobox.setObjectName(u"java_combobox")

        self.language_content_layout.addWidget(self.java_combobox, 3, 1, 1, 1)

        self.php_radio = QRadioButton(Form)
        self.php_radio.setObjectName(u"php_radio")

        self.language_content_layout.addWidget(self.php_radio, 1, 0, 1, 1)

        self.python_radio = QRadioButton(Form)
        self.python_radio.setObjectName(u"python_radio")

        self.language_content_layout.addWidget(self.python_radio, 2, 0, 1, 1)

        self.nodejs_radio = QRadioButton(Form)
        self.nodejs_radio.setObjectName(u"nodejs_radio")

        self.language_content_layout.addWidget(self.nodejs_radio, 4, 0, 1, 1)

        self.nodejs_combobox = QComboBox(Form)
        self.nodejs_combobox.setObjectName(u"nodejs_combobox")

        self.language_content_layout.addWidget(self.nodejs_combobox, 4, 1, 1, 1)

        self.java_radio = QRadioButton(Form)
        self.java_radio.setObjectName(u"java_radio")

        self.language_content_layout.addWidget(self.java_radio, 3, 0, 1, 1)

        self.python_combobox = QComboBox(Form)
        self.python_combobox.setObjectName(u"python_combobox")

        self.language_content_layout.addWidget(self.python_combobox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.language_content_layout)

        self.verticalSpacer_5 = QSpacerItem(20, 197, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.language_add_new_layout = QHBoxLayout()
        self.language_add_new_layout.setObjectName(u"language_add_new_layout")
        self.language_add_new_button_2 = QPushButton(Form)
        self.language_add_new_button_2.setObjectName(u"language_add_new_button_2")

        self.language_add_new_layout.addWidget(self.language_add_new_button_2)


        self.verticalLayout.addLayout(self.language_add_new_layout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.language_title_label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Languages</span></p></body></html>", None))
        self.php_radio.setText(QCoreApplication.translate("Form", u"PHP", None))
        self.python_radio.setText(QCoreApplication.translate("Form", u"Python", None))
        self.nodejs_radio.setText(QCoreApplication.translate("Form", u"Nodejs", None))
        self.java_radio.setText(QCoreApplication.translate("Form", u"Java", None))
        self.language_add_new_button_2.setText(QCoreApplication.translate("Form", u"Add New Languages", None))
    # retranslateUi


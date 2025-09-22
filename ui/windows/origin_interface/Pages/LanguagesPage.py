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

class Ui_LanguagesPage(object):
    def setupUi(self, LanguagesPage):
        if not LanguagesPage.objectName():
            LanguagesPage.setObjectName(u"LanguagesPage")
        LanguagesPage.resize(480, 640)
        self.verticalLayout = QVBoxLayout(LanguagesPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.language_title_layout = QHBoxLayout()
        self.language_title_layout.setObjectName(u"language_title_layout")
        self.language_title_label_2 = QLabel(LanguagesPage)
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
        self.language_save_change_buttonbox = QDialogButtonBox(LanguagesPage)
        self.language_save_change_buttonbox.setObjectName(u"language_save_change_buttonbox")
        self.language_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.language_save_change_layout.addWidget(self.language_save_change_buttonbox)


        self.verticalLayout.addLayout(self.language_save_change_layout)

        self.verticalSpacer_8 = QSpacerItem(20, 192, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)

        self.language_content_layout = QGridLayout()
        self.language_content_layout.setObjectName(u"language_content_layout")
        self.php_combobox = QComboBox(LanguagesPage)
        self.php_combobox.setObjectName(u"php_combobox")

        self.language_content_layout.addWidget(self.php_combobox, 1, 1, 1, 1)

        self.java_combobox = QComboBox(LanguagesPage)
        self.java_combobox.setObjectName(u"java_combobox")

        self.language_content_layout.addWidget(self.java_combobox, 3, 1, 1, 1)

        self.php_radio = QRadioButton(LanguagesPage)
        self.php_radio.setObjectName(u"php_radio")

        self.language_content_layout.addWidget(self.php_radio, 1, 0, 1, 1)

        self.python_radio = QRadioButton(LanguagesPage)
        self.python_radio.setObjectName(u"python_radio")

        self.language_content_layout.addWidget(self.python_radio, 2, 0, 1, 1)

        self.nodejs_radio = QRadioButton(LanguagesPage)
        self.nodejs_radio.setObjectName(u"nodejs_radio")

        self.language_content_layout.addWidget(self.nodejs_radio, 4, 0, 1, 1)

        self.nodejs_combobox = QComboBox(LanguagesPage)
        self.nodejs_combobox.setObjectName(u"nodejs_combobox")

        self.language_content_layout.addWidget(self.nodejs_combobox, 4, 1, 1, 1)

        self.java_radio = QRadioButton(LanguagesPage)
        self.java_radio.setObjectName(u"java_radio")

        self.language_content_layout.addWidget(self.java_radio, 3, 0, 1, 1)

        self.python_combobox = QComboBox(LanguagesPage)
        self.python_combobox.setObjectName(u"python_combobox")

        self.language_content_layout.addWidget(self.python_combobox, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.language_content_layout)

        self.verticalSpacer_5 = QSpacerItem(20, 197, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.language_add_new_layout = QHBoxLayout()
        self.language_add_new_layout.setObjectName(u"language_add_new_layout")
        self.language_add_new_button_2 = QPushButton(LanguagesPage)
        self.language_add_new_button_2.setObjectName(u"language_add_new_button_2")

        self.language_add_new_layout.addWidget(self.language_add_new_button_2)


        self.verticalLayout.addLayout(self.language_add_new_layout)


        self.retranslateUi(LanguagesPage)

        QMetaObject.connectSlotsByName(LanguagesPage)
    # setupUi

    def retranslateUi(self, LanguagesPage):
        LanguagesPage.setWindowTitle(QCoreApplication.translate("LanguagesPage", u"Form", None))
        self.language_title_label_2.setText(QCoreApplication.translate("LanguagesPage", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Languages</span></p></body></html>", None))
        self.php_radio.setText(QCoreApplication.translate("LanguagesPage", u"PHP", None))
        self.python_radio.setText(QCoreApplication.translate("LanguagesPage", u"Python", None))
        self.nodejs_radio.setText(QCoreApplication.translate("LanguagesPage", u"Nodejs", None))
        self.java_radio.setText(QCoreApplication.translate("LanguagesPage", u"Java", None))
        self.language_add_new_button_2.setText(QCoreApplication.translate("LanguagesPage", u"Add New Languages", None))
    # retranslateUi


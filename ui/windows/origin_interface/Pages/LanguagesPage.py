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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_LanguagesPage(object):
    def setupUi(self, LanguagesPage):
        if not LanguagesPage.objectName():
            LanguagesPage.setObjectName(u"LanguagesPage")
        LanguagesPage.resize(896, 640)
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
        self.language_save_change_layout.setContentsMargins(-1, -1, -1, 32)
        self.language_save_change_buttonbox = QDialogButtonBox(LanguagesPage)
        self.language_save_change_buttonbox.setObjectName(u"language_save_change_buttonbox")
        self.language_save_change_buttonbox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.language_save_change_layout.addWidget(self.language_save_change_buttonbox)


        self.verticalLayout.addLayout(self.language_save_change_layout)

        self.language_content_layout = QGridLayout()
        self.language_content_layout.setObjectName(u"language_content_layout")
        self.python_combobox = QComboBox(LanguagesPage)
        self.python_combobox.setObjectName(u"python_combobox")

        self.language_content_layout.addWidget(self.python_combobox, 2, 1, 1, 1)

        self.language_label = QLabel(LanguagesPage)
        self.language_label.setObjectName(u"language_label")

        self.language_content_layout.addWidget(self.language_label, 0, 0, 1, 1)

        self.select_language_label = QLabel(LanguagesPage)
        self.select_language_label.setObjectName(u"select_language_label")

        self.language_content_layout.addWidget(self.select_language_label, 0, 1, 1, 1)

        self.php_combobox = QComboBox(LanguagesPage)
        self.php_combobox.setObjectName(u"php_combobox")

        self.language_content_layout.addWidget(self.php_combobox, 1, 1, 1, 1)

        self.php_port_lineedit = QLineEdit(LanguagesPage)
        self.php_port_lineedit.setObjectName(u"php_port_lineedit")

        self.language_content_layout.addWidget(self.php_port_lineedit, 1, 3, 1, 1)

        self.ssl_enabled_label = QLabel(LanguagesPage)
        self.ssl_enabled_label.setObjectName(u"ssl_enabled_label")

        self.language_content_layout.addWidget(self.ssl_enabled_label, 0, 2, 1, 1)

        self.php_radio = QRadioButton(LanguagesPage)
        self.php_radio.setObjectName(u"php_radio")

        self.language_content_layout.addWidget(self.php_radio, 1, 0, 1, 1)

        self.nodejs_radio = QRadioButton(LanguagesPage)
        self.nodejs_radio.setObjectName(u"nodejs_radio")

        self.language_content_layout.addWidget(self.nodejs_radio, 4, 0, 1, 1)

        self.python_ssl_enabled_checkbox = QCheckBox(LanguagesPage)
        self.python_ssl_enabled_checkbox.setObjectName(u"python_ssl_enabled_checkbox")

        self.language_content_layout.addWidget(self.python_ssl_enabled_checkbox, 2, 2, 1, 1)

        self.python_radio = QRadioButton(LanguagesPage)
        self.python_radio.setObjectName(u"python_radio")

        self.language_content_layout.addWidget(self.python_radio, 2, 0, 1, 1)

        self.java_radio = QRadioButton(LanguagesPage)
        self.java_radio.setObjectName(u"java_radio")

        self.language_content_layout.addWidget(self.java_radio, 3, 0, 1, 1)

        self.ssl_port_label = QLabel(LanguagesPage)
        self.ssl_port_label.setObjectName(u"ssl_port_label")

        self.language_content_layout.addWidget(self.ssl_port_label, 0, 3, 1, 1)

        self.java_ssl_enabled_checkbox = QCheckBox(LanguagesPage)
        self.java_ssl_enabled_checkbox.setObjectName(u"java_ssl_enabled_checkbox")

        self.language_content_layout.addWidget(self.java_ssl_enabled_checkbox, 3, 2, 1, 1)

        self.java_combobox = QComboBox(LanguagesPage)
        self.java_combobox.setObjectName(u"java_combobox")

        self.language_content_layout.addWidget(self.java_combobox, 3, 1, 1, 1)

        self.nodejs_ssl_enabled_checkbox = QCheckBox(LanguagesPage)
        self.nodejs_ssl_enabled_checkbox.setObjectName(u"nodejs_ssl_enabled_checkbox")

        self.language_content_layout.addWidget(self.nodejs_ssl_enabled_checkbox, 4, 2, 1, 1)

        self.nodejs_combobox = QComboBox(LanguagesPage)
        self.nodejs_combobox.setObjectName(u"nodejs_combobox")

        self.language_content_layout.addWidget(self.nodejs_combobox, 4, 1, 1, 1)

        self.php_ssl_enabled_checkbox = QCheckBox(LanguagesPage)
        self.php_ssl_enabled_checkbox.setObjectName(u"php_ssl_enabled_checkbox")

        self.language_content_layout.addWidget(self.php_ssl_enabled_checkbox, 1, 2, 1, 1)

        self.root_folder_label = QLabel(LanguagesPage)
        self.root_folder_label.setObjectName(u"root_folder_label")

        self.language_content_layout.addWidget(self.root_folder_label, 0, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.php_root_folder_lineedit = QLineEdit(LanguagesPage)
        self.php_root_folder_lineedit.setObjectName(u"php_root_folder_lineedit")

        self.horizontalLayout.addWidget(self.php_root_folder_lineedit)

        self.php_browse_root_folder_pushbutton = QPushButton(LanguagesPage)
        self.php_browse_root_folder_pushbutton.setObjectName(u"php_browse_root_folder_pushbutton")

        self.horizontalLayout.addWidget(self.php_browse_root_folder_pushbutton)


        self.language_content_layout.addLayout(self.horizontalLayout, 1, 4, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.python_root_folder_lineedit = QLineEdit(LanguagesPage)
        self.python_root_folder_lineedit.setObjectName(u"python_root_folder_lineedit")

        self.horizontalLayout_2.addWidget(self.python_root_folder_lineedit)

        self.python_browse_root_folder_pushbutton = QPushButton(LanguagesPage)
        self.python_browse_root_folder_pushbutton.setObjectName(u"python_browse_root_folder_pushbutton")

        self.horizontalLayout_2.addWidget(self.python_browse_root_folder_pushbutton)


        self.language_content_layout.addLayout(self.horizontalLayout_2, 2, 4, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.java_root_folder_lineedit = QLineEdit(LanguagesPage)
        self.java_root_folder_lineedit.setObjectName(u"java_root_folder_lineedit")

        self.horizontalLayout_3.addWidget(self.java_root_folder_lineedit)

        self.java_browse_root_folder_pushbutton = QPushButton(LanguagesPage)
        self.java_browse_root_folder_pushbutton.setObjectName(u"java_browse_root_folder_pushbutton")

        self.horizontalLayout_3.addWidget(self.java_browse_root_folder_pushbutton)


        self.language_content_layout.addLayout(self.horizontalLayout_3, 3, 4, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.nodejs_root_folder_lineedit = QLineEdit(LanguagesPage)
        self.nodejs_root_folder_lineedit.setObjectName(u"nodejs_root_folder_lineedit")

        self.horizontalLayout_4.addWidget(self.nodejs_root_folder_lineedit)

        self.nodejs_browse_root_folder_pushbutton = QPushButton(LanguagesPage)
        self.nodejs_browse_root_folder_pushbutton.setObjectName(u"nodejs_browse_root_folder_pushbutton")

        self.horizontalLayout_4.addWidget(self.nodejs_browse_root_folder_pushbutton)


        self.language_content_layout.addLayout(self.horizontalLayout_4, 4, 4, 1, 1)

        self.python_port_lineedit = QLineEdit(LanguagesPage)
        self.python_port_lineedit.setObjectName(u"python_port_lineedit")

        self.language_content_layout.addWidget(self.python_port_lineedit, 2, 3, 1, 1)

        self.java_port_lineedit = QLineEdit(LanguagesPage)
        self.java_port_lineedit.setObjectName(u"java_port_lineedit")

        self.language_content_layout.addWidget(self.java_port_lineedit, 3, 3, 1, 1)

        self.nodejs_port_lineedit = QLineEdit(LanguagesPage)
        self.nodejs_port_lineedit.setObjectName(u"nodejs_port_lineedit")

        self.language_content_layout.addWidget(self.nodejs_port_lineedit, 4, 3, 1, 1)

        self.language_content_layout.setColumnStretch(1, 1)
        self.language_content_layout.setColumnStretch(4, 1)

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
        self.language_label.setText(QCoreApplication.translate("LanguagesPage", u"Language", None))
        self.select_language_label.setText(QCoreApplication.translate("LanguagesPage", u"Select version", None))
        self.ssl_enabled_label.setText(QCoreApplication.translate("LanguagesPage", u"SSL", None))
        self.php_radio.setText(QCoreApplication.translate("LanguagesPage", u"PHP", None))
        self.nodejs_radio.setText(QCoreApplication.translate("LanguagesPage", u"Nodejs", None))
        self.python_ssl_enabled_checkbox.setText(QCoreApplication.translate("LanguagesPage", u"Enabled", None))
        self.python_radio.setText(QCoreApplication.translate("LanguagesPage", u"Python", None))
        self.java_radio.setText(QCoreApplication.translate("LanguagesPage", u"Java", None))
        self.ssl_port_label.setText(QCoreApplication.translate("LanguagesPage", u"Port", None))
        self.java_ssl_enabled_checkbox.setText(QCoreApplication.translate("LanguagesPage", u"Enabled", None))
        self.nodejs_ssl_enabled_checkbox.setText(QCoreApplication.translate("LanguagesPage", u"Enabled", None))
        self.php_ssl_enabled_checkbox.setText(QCoreApplication.translate("LanguagesPage", u"Enabled", None))
        self.root_folder_label.setText(QCoreApplication.translate("LanguagesPage", u"Root Folder", None))
        self.php_browse_root_folder_pushbutton.setText(QCoreApplication.translate("LanguagesPage", u"Browse", None))
        self.python_browse_root_folder_pushbutton.setText(QCoreApplication.translate("LanguagesPage", u"Browse", None))
        self.java_browse_root_folder_pushbutton.setText(QCoreApplication.translate("LanguagesPage", u"Browse", None))
        self.nodejs_browse_root_folder_pushbutton.setText(QCoreApplication.translate("LanguagesPage", u"Browse", None))
        self.language_add_new_button_2.setText(QCoreApplication.translate("LanguagesPage", u"Add New Languages", None))
    # retranslateUi


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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialogButtonBox,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_WebserverPage(object):
    def setupUi(self, WebserverPage):
        if not WebserverPage.objectName():
            WebserverPage.setObjectName(u"WebserverPage")
        WebserverPage.resize(647, 750)
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

        self.webserver_content_layout = QGridLayout()
        self.webserver_content_layout.setObjectName(u"webserver_content_layout")
        self.apache_select_version_combobox = QComboBox(WebserverPage)
        self.apache_select_version_combobox.setObjectName(u"apache_select_version_combobox")

        self.webserver_content_layout.addWidget(self.apache_select_version_combobox, 1, 1, 1, 1)

        self.apache_elp_label = QLabel(WebserverPage)
        self.apache_elp_label.setObjectName(u"apache_elp_label")

        self.webserver_content_layout.addWidget(self.apache_elp_label, 12, 1, 1, 1)

        self.nginx_alp_label = QLabel(WebserverPage)
        self.nginx_alp_label.setObjectName(u"nginx_alp_label")

        self.webserver_content_layout.addWidget(self.nginx_alp_label, 18, 1, 1, 1)

        self.nginx_radio = QRadioButton(WebserverPage)
        self.nginx_radio.setObjectName(u"nginx_radio")

        self.webserver_content_layout.addWidget(self.nginx_radio, 14, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.nginx_sites_enabled_lineEdit = QLineEdit(WebserverPage)
        self.nginx_sites_enabled_lineEdit.setObjectName(u"nginx_sites_enabled_lineEdit")

        self.horizontalLayout_4.addWidget(self.nginx_sites_enabled_lineEdit)

        self.nginx_sites_enabled_browseButton = QPushButton(WebserverPage)
        self.nginx_sites_enabled_browseButton.setObjectName(u"nginx_sites_enabled_browseButton")

        self.horizontalLayout_4.addWidget(self.nginx_sites_enabled_browseButton)


        self.webserver_content_layout.addLayout(self.horizontalLayout_4, 15, 2, 1, 1)

        self.nginx_config_tld_lineEdit = QLineEdit(WebserverPage)
        self.nginx_config_tld_lineEdit.setObjectName(u"nginx_config_tld_lineEdit")

        self.webserver_content_layout.addWidget(self.nginx_config_tld_lineEdit, 17, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.apache_sites_enabled_lineEdit = QLineEdit(WebserverPage)
        self.apache_sites_enabled_lineEdit.setObjectName(u"apache_sites_enabled_lineEdit")

        self.horizontalLayout.addWidget(self.apache_sites_enabled_lineEdit)

        self.apache_sites_enabled_browseButton = QPushButton(WebserverPage)
        self.apache_sites_enabled_browseButton.setObjectName(u"apache_sites_enabled_browseButton")

        self.horizontalLayout.addWidget(self.apache_sites_enabled_browseButton)


        self.webserver_content_layout.addLayout(self.horizontalLayout, 2, 2, 1, 1)

        self.nginx_listen_port_label = QLabel(WebserverPage)
        self.nginx_listen_port_label.setObjectName(u"nginx_listen_port_label")

        self.webserver_content_layout.addWidget(self.nginx_listen_port_label, 16, 1, 1, 1)

        self.apache_config_tld_label = QLabel(WebserverPage)
        self.apache_config_tld_label.setObjectName(u"apache_config_tld_label")

        self.webserver_content_layout.addWidget(self.apache_config_tld_label, 8, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.nginx_alp_lineEdit = QLineEdit(WebserverPage)
        self.nginx_alp_lineEdit.setObjectName(u"nginx_alp_lineEdit")

        self.horizontalLayout_5.addWidget(self.nginx_alp_lineEdit)

        self.nginx_alp_browseButton = QPushButton(WebserverPage)
        self.nginx_alp_browseButton.setObjectName(u"nginx_alp_browseButton")

        self.horizontalLayout_5.addWidget(self.nginx_alp_browseButton)


        self.webserver_content_layout.addLayout(self.horizontalLayout_5, 18, 2, 1, 1)

        self.apache_config_tld_lineEdit = QLineEdit(WebserverPage)
        self.apache_config_tld_lineEdit.setObjectName(u"apache_config_tld_lineEdit")

        self.webserver_content_layout.addWidget(self.apache_config_tld_lineEdit, 8, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.apache_elp_lineEdit = QLineEdit(WebserverPage)
        self.apache_elp_lineEdit.setObjectName(u"apache_elp_lineEdit")

        self.horizontalLayout_3.addWidget(self.apache_elp_lineEdit)

        self.apache_elp_browseButton = QPushButton(WebserverPage)
        self.apache_elp_browseButton.setObjectName(u"apache_elp_browseButton")

        self.horizontalLayout_3.addWidget(self.apache_elp_browseButton)


        self.webserver_content_layout.addLayout(self.horizontalLayout_3, 12, 2, 1, 1)

        self.apache_radio = QRadioButton(WebserverPage)
        self.apache_radio.setObjectName(u"apache_radio")

        self.webserver_content_layout.addWidget(self.apache_radio, 1, 0, 1, 1)

        self.apache_sites_enabled_label = QLabel(WebserverPage)
        self.apache_sites_enabled_label.setObjectName(u"apache_sites_enabled_label")

        self.webserver_content_layout.addWidget(self.apache_sites_enabled_label, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.webserver_content_layout.addItem(self.verticalSpacer_2, 13, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.apache_alp_lineEdit = QLineEdit(WebserverPage)
        self.apache_alp_lineEdit.setObjectName(u"apache_alp_lineEdit")

        self.horizontalLayout_2.addWidget(self.apache_alp_lineEdit)

        self.apache_alp_browseButton = QPushButton(WebserverPage)
        self.apache_alp_browseButton.setObjectName(u"apache_alp_browseButton")

        self.horizontalLayout_2.addWidget(self.apache_alp_browseButton)


        self.webserver_content_layout.addLayout(self.horizontalLayout_2, 11, 2, 1, 1)

        self.nginx_listen_port_lineEdit = QLineEdit(WebserverPage)
        self.nginx_listen_port_lineEdit.setObjectName(u"nginx_listen_port_lineEdit")

        self.webserver_content_layout.addWidget(self.nginx_listen_port_lineEdit, 16, 2, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.apache_excutable_label = QLabel(WebserverPage)
        self.apache_excutable_label.setObjectName(u"apache_excutable_label")

        self.horizontalLayout_7.addWidget(self.apache_excutable_label)

        self.apache_excutable_lineEdit = QLineEdit(WebserverPage)
        self.apache_excutable_lineEdit.setObjectName(u"apache_excutable_lineEdit")

        self.horizontalLayout_7.addWidget(self.apache_excutable_lineEdit)

        self.apache_excutable_browseButton = QPushButton(WebserverPage)
        self.apache_excutable_browseButton.setObjectName(u"apache_excutable_browseButton")

        self.horizontalLayout_7.addWidget(self.apache_excutable_browseButton)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 4)
        self.horizontalLayout_7.setStretch(2, 1)

        self.webserver_content_layout.addLayout(self.horizontalLayout_7, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.webserver_content_layout.addItem(self.verticalSpacer_4, 13, 2, 1, 1)

        self.nginx_sites_enabled_label = QLabel(WebserverPage)
        self.nginx_sites_enabled_label.setObjectName(u"nginx_sites_enabled_label")

        self.webserver_content_layout.addWidget(self.nginx_sites_enabled_label, 15, 1, 1, 1)

        self.apache_alp_label = QLabel(WebserverPage)
        self.apache_alp_label.setObjectName(u"apache_alp_label")

        self.webserver_content_layout.addWidget(self.apache_alp_label, 11, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.webserver_content_layout.addItem(self.verticalSpacer_3, 13, 1, 1, 1)

        self.nginx_elp_label = QLabel(WebserverPage)
        self.nginx_elp_label.setObjectName(u"nginx_elp_label")

        self.webserver_content_layout.addWidget(self.nginx_elp_label, 19, 1, 1, 1)

        self.apache_listen_port_lineEdit = QLineEdit(WebserverPage)
        self.apache_listen_port_lineEdit.setObjectName(u"apache_listen_port_lineEdit")

        self.webserver_content_layout.addWidget(self.apache_listen_port_lineEdit, 3, 2, 1, 1)

        self.nginx_config_tld_label = QLabel(WebserverPage)
        self.nginx_config_tld_label.setObjectName(u"nginx_config_tld_label")

        self.webserver_content_layout.addWidget(self.nginx_config_tld_label, 17, 1, 1, 1)

        self.nginx_select_version_combobox = QComboBox(WebserverPage)
        self.nginx_select_version_combobox.setObjectName(u"nginx_select_version_combobox")

        self.webserver_content_layout.addWidget(self.nginx_select_version_combobox, 14, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.nginx_excutable_label = QLabel(WebserverPage)
        self.nginx_excutable_label.setObjectName(u"nginx_excutable_label")

        self.horizontalLayout_8.addWidget(self.nginx_excutable_label)

        self.nginx_excutable_lineEdit = QLineEdit(WebserverPage)
        self.nginx_excutable_lineEdit.setObjectName(u"nginx_excutable_lineEdit")

        self.horizontalLayout_8.addWidget(self.nginx_excutable_lineEdit)

        self.nginx_excutable_browseButton = QPushButton(WebserverPage)
        self.nginx_excutable_browseButton.setObjectName(u"nginx_excutable_browseButton")

        self.horizontalLayout_8.addWidget(self.nginx_excutable_browseButton)


        self.webserver_content_layout.addLayout(self.horizontalLayout_8, 14, 2, 1, 1)

        self.apache_listen_port_label = QLabel(WebserverPage)
        self.apache_listen_port_label.setObjectName(u"apache_listen_port_label")

        self.webserver_content_layout.addWidget(self.apache_listen_port_label, 3, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.nginx_elp_lineEdit = QLineEdit(WebserverPage)
        self.nginx_elp_lineEdit.setObjectName(u"nginx_elp_lineEdit")

        self.horizontalLayout_6.addWidget(self.nginx_elp_lineEdit)

        self.nginx_elp_browseButton = QPushButton(WebserverPage)
        self.nginx_elp_browseButton.setObjectName(u"nginx_elp_browseButton")

        self.horizontalLayout_6.addWidget(self.nginx_elp_browseButton)


        self.webserver_content_layout.addLayout(self.horizontalLayout_6, 19, 2, 1, 1)


        self.verticalLayout.addLayout(self.webserver_content_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(WebserverPage)

        QMetaObject.connectSlotsByName(WebserverPage)
    # setupUi

    def retranslateUi(self, WebserverPage):
        WebserverPage.setWindowTitle(QCoreApplication.translate("WebserverPage", u"Form", None))
        self.webserver_title_label.setText(QCoreApplication.translate("WebserverPage", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Webserver</span></p></body></html>", None))
        self.apache_elp_label.setText(QCoreApplication.translate("WebserverPage", u"Error Log Path", None))
        self.nginx_alp_label.setText(QCoreApplication.translate("WebserverPage", u"Access Log Path", None))
        self.nginx_radio.setText(QCoreApplication.translate("WebserverPage", u"Nginx Version", None))
        self.nginx_sites_enabled_browseButton.setText(QCoreApplication.translate("WebserverPage", u"Browse", None))
        self.nginx_config_tld_lineEdit.setPlaceholderText(QCoreApplication.translate("WebserverPage", u"Example: .test or .local --> my-app.test or my-app.local", None))
        self.apache_sites_enabled_browseButton.setText(QCoreApplication.translate("WebserverPage", u"Browse", None))
        self.nginx_listen_port_label.setText(QCoreApplication.translate("WebserverPage", u"Listen Port", None))
        self.apache_config_tld_label.setText(QCoreApplication.translate("WebserverPage", u"Config Top Level Domain", None))
        self.nginx_alp_browseButton.setText(QCoreApplication.translate("WebserverPage", u"Browse", None))
        self.apache_config_tld_lineEdit.setPlaceholderText(QCoreApplication.translate("WebserverPage", u"Example: .test or .local --> my-app.test or my-app.local", None))
        self.apache_elp_browseButton.setText(QCoreApplication.translate("WebserverPage", u"Browse", None))
        self.apache_radio.setText(QCoreApplication.translate("WebserverPage", u"Apache Version", None))
        self.apache_sites_enabled_label.setText(QCoreApplication.translate("WebserverPage", u"Sites-enabled Path", None))
        self.apache_alp_browseButton.setText(QCoreApplication.translate("WebserverPage", u"Browse", None))
        self.apache_excutable_label.setText(QCoreApplication.translate("WebserverPage", u"Excutable Path:", None))
        self.apache_excutable_browseButton.setText(QCoreApplication.translate("WebserverPage", u"Browse", None))
        self.nginx_sites_enabled_label.setText(QCoreApplication.translate("WebserverPage", u"Sites-enabled Path", None))
        self.apache_alp_label.setText(QCoreApplication.translate("WebserverPage", u"Access Log Path", None))
        self.nginx_elp_label.setText(QCoreApplication.translate("WebserverPage", u"Error Log Path", None))
        self.nginx_config_tld_label.setText(QCoreApplication.translate("WebserverPage", u"Config Top Level Domain", None))
        self.nginx_excutable_label.setText(QCoreApplication.translate("WebserverPage", u"Excutable Path:", None))
        self.nginx_excutable_browseButton.setText(QCoreApplication.translate("WebserverPage", u"Browse", None))
        self.apache_listen_port_label.setText(QCoreApplication.translate("WebserverPage", u"Listen Port", None))
        self.nginx_elp_browseButton.setText(QCoreApplication.translate("WebserverPage", u"Browse", None))
    # retranslateUi


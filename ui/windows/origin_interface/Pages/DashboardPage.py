# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardPage.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DashboardPage(object):
    def setupUi(self, DashboardPage):
        if not DashboardPage.objectName():
            DashboardPage.setObjectName(u"DashboardPage")
        DashboardPage.resize(480, 640)
        self.verticalLayout = QVBoxLayout(DashboardPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dashboard_title_layout = QHBoxLayout()
        self.dashboard_title_layout.setObjectName(u"dashboard_title_layout")
        self.dashboard_title_label = QLabel(DashboardPage)
        self.dashboard_title_label.setObjectName(u"dashboard_title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboard_title_label.sizePolicy().hasHeightForWidth())
        self.dashboard_title_label.setSizePolicy(sizePolicy)

        self.dashboard_title_layout.addWidget(self.dashboard_title_label)


        self.verticalLayout.addLayout(self.dashboard_title_layout)

        self.dashboard_head_column_layout = QHBoxLayout()
        self.dashboard_head_column_layout.setObjectName(u"dashboard_head_column_layout")
        self.dashboard_service_label = QLabel(DashboardPage)
        self.dashboard_service_label.setObjectName(u"dashboard_service_label")

        self.dashboard_head_column_layout.addWidget(self.dashboard_service_label)

        self.dashboard_type_label = QLabel(DashboardPage)
        self.dashboard_type_label.setObjectName(u"dashboard_type_label")

        self.dashboard_head_column_layout.addWidget(self.dashboard_type_label)

        self.dashboard_version_label = QLabel(DashboardPage)
        self.dashboard_version_label.setObjectName(u"dashboard_version_label")

        self.dashboard_head_column_layout.addWidget(self.dashboard_version_label)


        self.verticalLayout.addLayout(self.dashboard_head_column_layout)

        self.dashboard_content_layout = QGridLayout()
        self.dashboard_content_layout.setObjectName(u"dashboard_content_layout")
        self.database_type_label = QLabel(DashboardPage)
        self.database_type_label.setObjectName(u"database_type_label")

        self.dashboard_content_layout.addWidget(self.database_type_label, 9, 1, 1, 1)

        self.network_service_label = QLabel(DashboardPage)
        self.network_service_label.setObjectName(u"network_service_label")

        self.dashboard_content_layout.addWidget(self.network_service_label, 15, 0, 1, 1)

        self.tools_type_3_label = QLabel(DashboardPage)
        self.tools_type_3_label.setObjectName(u"tools_type_3_label")

        self.dashboard_content_layout.addWidget(self.tools_type_3_label, 14, 1, 1, 1)

        self.tools_version_2_label = QLabel(DashboardPage)
        self.tools_version_2_label.setObjectName(u"tools_version_2_label")

        self.dashboard_content_layout.addWidget(self.tools_version_2_label, 12, 2, 1, 1)

        self.tools_version_3_label = QLabel(DashboardPage)
        self.tools_version_3_label.setObjectName(u"tools_version_3_label")

        self.dashboard_content_layout.addWidget(self.tools_version_3_label, 14, 2, 1, 1)

        self.language_service_label = QLabel(DashboardPage)
        self.language_service_label.setObjectName(u"language_service_label")

        self.dashboard_content_layout.addWidget(self.language_service_label, 8, 0, 1, 1)

        self.tools_type_1_label = QLabel(DashboardPage)
        self.tools_type_1_label.setObjectName(u"tools_type_1_label")

        self.dashboard_content_layout.addWidget(self.tools_type_1_label, 11, 1, 1, 1)

        self.tools_type_2_label = QLabel(DashboardPage)
        self.tools_type_2_label.setObjectName(u"tools_type_2_label")

        self.dashboard_content_layout.addWidget(self.tools_type_2_label, 12, 1, 1, 1)

        self.startall_button = QPushButton(DashboardPage)
        self.startall_button.setObjectName(u"startall_button")

        self.dashboard_content_layout.addWidget(self.startall_button, 16, 1, 1, 1)

        self.language_version_label = QLabel(DashboardPage)
        self.language_version_label.setObjectName(u"language_version_label")

        self.dashboard_content_layout.addWidget(self.language_version_label, 8, 2, 1, 1)

        self.tools_version_1_label = QLabel(DashboardPage)
        self.tools_version_1_label.setObjectName(u"tools_version_1_label")

        self.dashboard_content_layout.addWidget(self.tools_version_1_label, 11, 2, 1, 1)

        self.tools_service_label = QLabel(DashboardPage)
        self.tools_service_label.setObjectName(u"tools_service_label")

        self.dashboard_content_layout.addWidget(self.tools_service_label, 11, 0, 1, 1)

        self.network_version_label = QLabel(DashboardPage)
        self.network_version_label.setObjectName(u"network_version_label")

        self.dashboard_content_layout.addWidget(self.network_version_label, 15, 2, 1, 1)

        self.database_service_label = QLabel(DashboardPage)
        self.database_service_label.setObjectName(u"database_service_label")

        self.dashboard_content_layout.addWidget(self.database_service_label, 9, 0, 1, 1)

        self.database_version_label = QLabel(DashboardPage)
        self.database_version_label.setObjectName(u"database_version_label")

        self.dashboard_content_layout.addWidget(self.database_version_label, 9, 2, 1, 1)

        self.network_type_label = QLabel(DashboardPage)
        self.network_type_label.setObjectName(u"network_type_label")

        self.dashboard_content_layout.addWidget(self.network_type_label, 15, 1, 1, 1)

        self.webserver_service_label = QLabel(DashboardPage)
        self.webserver_service_label.setObjectName(u"webserver_service_label")

        self.dashboard_content_layout.addWidget(self.webserver_service_label, 10, 0, 1, 1)

        self.webserver_type_label = QLabel(DashboardPage)
        self.webserver_type_label.setObjectName(u"webserver_type_label")

        self.dashboard_content_layout.addWidget(self.webserver_type_label, 10, 1, 1, 1)

        self.webserver_version_label = QLabel(DashboardPage)
        self.webserver_version_label.setObjectName(u"webserver_version_label")

        self.dashboard_content_layout.addWidget(self.webserver_version_label, 10, 2, 1, 1)

        self.language_type_label = QLabel(DashboardPage)
        self.language_type_label.setObjectName(u"language_type_label")

        self.dashboard_content_layout.addWidget(self.language_type_label, 8, 1, 1, 1)


        self.verticalLayout.addLayout(self.dashboard_content_layout)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(DashboardPage)

        QMetaObject.connectSlotsByName(DashboardPage)
    # setupUi

    def retranslateUi(self, DashboardPage):
        DashboardPage.setWindowTitle(QCoreApplication.translate("DashboardPage", u"Form", None))
        self.dashboard_title_label.setText(QCoreApplication.translate("DashboardPage", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Dashboard</span></p></body></html>", None))
        self.dashboard_service_label.setText(QCoreApplication.translate("DashboardPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Service</span></p></body></html>", None))
        self.dashboard_type_label.setText(QCoreApplication.translate("DashboardPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Type</span></p></body></html>", None))
        self.dashboard_version_label.setText(QCoreApplication.translate("DashboardPage", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Version</span></p></body></html>", None))
        self.database_type_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.network_service_label.setText(QCoreApplication.translate("DashboardPage", u"Network", None))
        self.tools_type_3_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.tools_version_2_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.tools_version_3_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.language_service_label.setText(QCoreApplication.translate("DashboardPage", u"Language", None))
        self.tools_type_1_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.tools_type_2_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.startall_button.setText(QCoreApplication.translate("DashboardPage", u"Start All", None))
        self.language_version_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.tools_version_1_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.tools_service_label.setText(QCoreApplication.translate("DashboardPage", u"Tools", None))
        self.network_version_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.database_service_label.setText(QCoreApplication.translate("DashboardPage", u"Database", None))
        self.database_version_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.network_type_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.webserver_service_label.setText(QCoreApplication.translate("DashboardPage", u"Webserver", None))
        self.webserver_type_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.webserver_version_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
        self.language_type_label.setText(QCoreApplication.translate("DashboardPage", u"TextLabel", None))
    # retranslateUi


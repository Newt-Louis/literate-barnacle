# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ToolsPage.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ToolsPage(object):
    def setupUi(self, ToolsPage):
        if not ToolsPage.objectName():
            ToolsPage.setObjectName(u"ToolsPage")
        ToolsPage.resize(480, 640)
        self.verticalLayout = QVBoxLayout(ToolsPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tools_title_layout = QHBoxLayout()
        self.tools_title_layout.setObjectName(u"tools_title_layout")
        self.tools_title_label = QLabel(ToolsPage)
        self.tools_title_label.setObjectName(u"tools_title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tools_title_label.sizePolicy().hasHeightForWidth())
        self.tools_title_label.setSizePolicy(sizePolicy)

        self.tools_title_layout.addWidget(self.tools_title_label)


        self.verticalLayout.addLayout(self.tools_title_layout)

        self.verticalSpacer_11 = QSpacerItem(20, 212, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_11)

        self.tools_content_layout = QGridLayout()
        self.tools_content_layout.setObjectName(u"tools_content_layout")
        self.quickadd_combobox = QComboBox(ToolsPage)
        self.quickadd_combobox.setObjectName(u"quickadd_combobox")

        self.tools_content_layout.addWidget(self.quickadd_combobox, 3, 1, 1, 1)

        self.rightclickmenu_combobox = QComboBox(ToolsPage)
        self.rightclickmenu_combobox.setObjectName(u"rightclickmenu_combobox")

        self.tools_content_layout.addWidget(self.rightclickmenu_combobox, 2, 1, 1, 1)

        self.wildcarddns_combobox = QComboBox(ToolsPage)
        self.wildcarddns_combobox.setObjectName(u"wildcarddns_combobox")

        self.tools_content_layout.addWidget(self.wildcarddns_combobox, 0, 1, 1, 1)

        self.deleteproject_combobox = QComboBox(ToolsPage)
        self.deleteproject_combobox.setObjectName(u"deleteproject_combobox")

        self.tools_content_layout.addWidget(self.deleteproject_combobox, 4, 1, 1, 1)

        self.rightclickmenu_label = QLabel(ToolsPage)
        self.rightclickmenu_label.setObjectName(u"rightclickmenu_label")

        self.tools_content_layout.addWidget(self.rightclickmenu_label, 2, 0, 1, 1)

        self.deleteproject_label = QLabel(ToolsPage)
        self.deleteproject_label.setObjectName(u"deleteproject_label")

        self.tools_content_layout.addWidget(self.deleteproject_label, 4, 0, 1, 1)

        self.quickadd_label = QLabel(ToolsPage)
        self.quickadd_label.setObjectName(u"quickadd_label")

        self.tools_content_layout.addWidget(self.quickadd_label, 3, 0, 1, 1)

        self.cron_label = QLabel(ToolsPage)
        self.cron_label.setObjectName(u"cron_label")

        self.tools_content_layout.addWidget(self.cron_label, 1, 0, 1, 1)

        self.cron_combobox = QComboBox(ToolsPage)
        self.cron_combobox.setObjectName(u"cron_combobox")

        self.tools_content_layout.addWidget(self.cron_combobox, 1, 1, 1, 1)

        self.wildcarddns_label = QLabel(ToolsPage)
        self.wildcarddns_label.setObjectName(u"wildcarddns_label")

        self.tools_content_layout.addWidget(self.wildcarddns_label, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.tools_content_layout)

        self.verticalSpacer_12 = QSpacerItem(20, 212, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_12)


        self.retranslateUi(ToolsPage)

        QMetaObject.connectSlotsByName(ToolsPage)
    # setupUi

    def retranslateUi(self, ToolsPage):
        ToolsPage.setWindowTitle(QCoreApplication.translate("ToolsPage", u"Form", None))
        self.tools_title_label.setText(QCoreApplication.translate("ToolsPage", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Tools</span></p></body></html>", None))
        self.rightclickmenu_label.setText(QCoreApplication.translate("ToolsPage", u"Right Click Menu", None))
        self.deleteproject_label.setText(QCoreApplication.translate("ToolsPage", u"Delete Project", None))
        self.quickadd_label.setText(QCoreApplication.translate("ToolsPage", u"Quick Add", None))
        self.cron_label.setText(QCoreApplication.translate("ToolsPage", u"Cron", None))
        self.wildcarddns_label.setText(QCoreApplication.translate("ToolsPage", u"Wildcard DNS", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'left_columnMdaAUt.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *
from . files_rc import *

class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(5, 34, 186, 28))
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.menu_1)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, 510, 221, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 151, 41))
        self.pushButton_2 = QPushButton(self.menu_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 370, 161, 41))
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.btn_4_widget = QWidget(self.menu_2)
        self.btn_4_widget.setObjectName(u"btn_4_widget")
        self.btn_4_widget.setMinimumSize(QSize(0, 40))
        self.btn_4_widget.setMaximumSize(QSize(16777215, 40))
        self.btn_4_layout = QVBoxLayout(self.btn_4_widget)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName(u"btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.btn_4_widget)

        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.menu_2)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(9)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"font-size: 9pt")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("LeftColumn", u"Menu 1 - Left Menu", None))
        self.pushButton.setText(QCoreApplication.translate("LeftColumn", u"example", None))
        self.pushButton_2.setText(QCoreApplication.translate("LeftColumn", u"Open Blender", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"Menu 2 - Left Menu", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u"This is just an example menu.\n"
"Add Qt Widgets or your custom widgets here.", None))
    # retranslateUi


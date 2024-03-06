# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainbkGdZw.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(747, 564)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: rgb(49, 49, 49);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.top_bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 40))
        self.frame_toggle.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(106, 106, 106);\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"	font: 700 8pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 0, 102);\n"
"border-radius: 9px;\n"
"color: rgb(255, 255, 255);\n"
"font: 700 8pt \"Segoe UI\";\n"
"}")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setMinimumSize(QSize(40, 30))
        self.Btn_Toggle.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.top_bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(106, 106, 106);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(0, 0))
        self.frame_left_menu.setMaximumSize(QSize(0, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setMinimumSize(QSize(70, 0))
        self.frame_top_menus.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_personnel = QPushButton(self.frame_top_menus)
        self.Btn_personnel.setObjectName(u"Btn_personnel")
        self.Btn_personnel.setMinimumSize(QSize(30, 40))
        self.Btn_personnel.setAutoFillBackground(False)
        self.Btn_personnel.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_personnel)

        self.Btn_projet = QPushButton(self.frame_top_menus)
        self.Btn_projet.setObjectName(u"Btn_projet")
        self.Btn_projet.setMinimumSize(QSize(0, 40))
        self.Btn_projet.setAutoFillBackground(False)
        self.Btn_projet.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_projet)

        self.Btn_depot = QPushButton(self.frame_top_menus)
        self.Btn_depot.setObjectName(u"Btn_depot")
        self.Btn_depot.setMinimumSize(QSize(0, 40))
        self.Btn_depot.setAutoFillBackground(False)
        self.Btn_depot.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border:0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.Btn_depot)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_page = QFrame(self.content)
        self.frame_page.setObjectName(u"frame_page")
        self.frame_page.setFrameShape(QFrame.StyledPanel)
        self.frame_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.SW_principal = QStackedWidget(self.frame_page)
        self.SW_principal.setObjectName(u"SW_principal")
        self.SW_principal.setFrameShadow(QFrame.Plain)
        self.pg_personnel = QWidget()
        self.pg_personnel.setObjectName(u"pg_personnel")
        self.gridLayout = QGridLayout(self.pg_personnel)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 0, 0, 0)
        self.corp_pg_personnel = QFrame(self.pg_personnel)
        self.corp_pg_personnel.setObjectName(u"corp_pg_personnel")
        self.corp_pg_personnel.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.corp_pg_personnel.setFrameShape(QFrame.StyledPanel)
        self.corp_pg_personnel.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.corp_pg_personnel)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.SW_pg_personnal = QStackedWidget(self.corp_pg_personnel)
        self.SW_pg_personnal.setObjectName(u"SW_pg_personnal")
        self.SW_pg_personnal.setStyleSheet(u"background-color: rgb(106, 106, 106);")
        self.SW_Liste_personnel = QWidget()
        self.SW_Liste_personnel.setObjectName(u"SW_Liste_personnel")
        self.gridLayout_4 = QGridLayout(self.SW_Liste_personnel)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_personnel = QTableWidget(self.SW_Liste_personnel)
        if (self.tableWidget_personnel.columnCount() < 6):
            self.tableWidget_personnel.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_personnel.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_personnel.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_personnel.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_personnel.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_personnel.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_personnel.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget_personnel.setObjectName(u"tableWidget_personnel")

        self.gridLayout_4.addWidget(self.tableWidget_personnel, 0, 0, 1, 1)

        self.frame_Boutton = QFrame(self.SW_Liste_personnel)
        self.frame_Boutton.setObjectName(u"frame_Boutton")
        self.frame_Boutton.setMinimumSize(QSize(0, 30))
        self.frame_Boutton.setFrameShape(QFrame.StyledPanel)
        self.frame_Boutton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_Boutton)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer = QSpacerItem(488, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.btn_Actualiser = QPushButton(self.frame_Boutton)
        self.btn_Actualiser.setObjectName(u"btn_Actualiser")
        self.btn_Actualiser.setMinimumSize(QSize(90, 31))
        self.btn_Actualiser.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"color: rgb(106, 106, 106);")

        self.horizontalLayout_12.addWidget(self.btn_Actualiser)


        self.gridLayout_4.addWidget(self.frame_Boutton, 1, 0, 1, 1)

        self.SW_pg_personnal.addWidget(self.SW_Liste_personnel)
        self.SW_Ajouter_personnel = QWidget()
        self.SW_Ajouter_personnel.setObjectName(u"SW_Ajouter_personnel")
        self.horizontalLayout_4 = QHBoxLayout(self.SW_Ajouter_personnel)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self.SW_Ajouter_personnel)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 459))
        self.frame.setMaximumSize(QSize(500, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.splitter_2 = QSplitter(self.frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(11, 11, 381, 256))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_ID = QLabel(self.layoutWidget)
        self.label_ID.setObjectName(u"label_ID")
        self.label_ID.setMinimumSize(QSize(71, 31))
        self.label_ID.setMaximumSize(QSize(71, 31))
        self.label_ID.setStyleSheet(u"\n"
"QLabel{\n"
"	background-color: rgb(75, 0, 56);\n"
"	border-radius:10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}")
        self.label_ID.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_ID)

        self.textEdit_ID = QTextEdit(self.layoutWidget)
        self.textEdit_ID.setObjectName(u"textEdit_ID")
        self.textEdit_ID.setMinimumSize(QSize(300, 0))
        self.textEdit_ID.setMaximumSize(QSize(300, 31))
        self.textEdit_ID.setStyleSheet(u"font: 300 9pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.textEdit_ID)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_Nom = QLabel(self.layoutWidget)
        self.label_Nom.setObjectName(u"label_Nom")
        self.label_Nom.setMinimumSize(QSize(71, 31))
        self.label_Nom.setMaximumSize(QSize(71, 31))
        self.label_Nom.setStyleSheet(u"\n"
"QLabel{\n"
"	background-color: rgb(75, 0, 56);\n"
"	border-radius:10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}")
        self.label_Nom.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_Nom)

        self.textEdit_Nom = QTextEdit(self.layoutWidget)
        self.textEdit_Nom.setObjectName(u"textEdit_Nom")
        self.textEdit_Nom.setMinimumSize(QSize(300, 0))
        self.textEdit_Nom.setMaximumSize(QSize(300, 31))
        self.textEdit_Nom.setStyleSheet(u"font: 300 9pt \"Segoe UI\";")

        self.horizontalLayout_7.addWidget(self.textEdit_Nom)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_Prenom = QLabel(self.layoutWidget)
        self.label_Prenom.setObjectName(u"label_Prenom")
        self.label_Prenom.setMinimumSize(QSize(71, 31))
        self.label_Prenom.setMaximumSize(QSize(71, 31))
        self.label_Prenom.setStyleSheet(u"\n"
"QLabel{\n"
"	background-color: rgb(75, 0, 56);\n"
"	border-radius:10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}")
        self.label_Prenom.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_Prenom)

        self.textEdit_Prenom = QTextEdit(self.layoutWidget)
        self.textEdit_Prenom.setObjectName(u"textEdit_Prenom")
        self.textEdit_Prenom.setMinimumSize(QSize(300, 0))
        self.textEdit_Prenom.setMaximumSize(QSize(300, 31))
        self.textEdit_Prenom.setStyleSheet(u"font: 300 9pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.textEdit_Prenom)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_Adresse = QLabel(self.layoutWidget)
        self.label_Adresse.setObjectName(u"label_Adresse")
        self.label_Adresse.setMinimumSize(QSize(71, 31))
        self.label_Adresse.setMaximumSize(QSize(71, 31))
        self.label_Adresse.setStyleSheet(u"\n"
"QLabel{\n"
"	background-color: rgb(75, 0, 56);\n"
"	border-radius:10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}")
        self.label_Adresse.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_Adresse)

        self.textEdit_Adresse = QTextEdit(self.layoutWidget)
        self.textEdit_Adresse.setObjectName(u"textEdit_Adresse")
        self.textEdit_Adresse.setMinimumSize(QSize(300, 0))
        self.textEdit_Adresse.setMaximumSize(QSize(300, 31))
        self.textEdit_Adresse.setStyleSheet(u"font: 300 9pt \"Segoe UI\";")

        self.horizontalLayout_9.addWidget(self.textEdit_Adresse)


        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_Email = QLabel(self.layoutWidget)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setMinimumSize(QSize(71, 31))
        self.label_Email.setMaximumSize(QSize(71, 31))
        self.label_Email.setStyleSheet(u"\n"
"QLabel{\n"
"	background-color: rgb(75, 0, 56);\n"
"	border-radius:10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}")
        self.label_Email.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_Email)

        self.textEdit_Email = QTextEdit(self.layoutWidget)
        self.textEdit_Email.setObjectName(u"textEdit_Email")
        self.textEdit_Email.setMinimumSize(QSize(300, 0))
        self.textEdit_Email.setMaximumSize(QSize(300, 31))
        self.textEdit_Email.setStyleSheet(u"font: 300 9pt \"Segoe UI\";")

        self.horizontalLayout_10.addWidget(self.textEdit_Email)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_Numero = QLabel(self.layoutWidget)
        self.label_Numero.setObjectName(u"label_Numero")
        self.label_Numero.setMinimumSize(QSize(71, 31))
        self.label_Numero.setMaximumSize(QSize(71, 31))
        self.label_Numero.setStyleSheet(u"\n"
"QLabel{\n"
"	background-color: rgb(75, 0, 56);\n"
"	border-radius:10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}")
        self.label_Numero.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_Numero)

        self.textEdit_Numero = QTextEdit(self.layoutWidget)
        self.textEdit_Numero.setObjectName(u"textEdit_Numero")
        self.textEdit_Numero.setMinimumSize(QSize(300, 0))
        self.textEdit_Numero.setMaximumSize(QSize(300, 31))
        self.textEdit_Numero.setStyleSheet(u"font: 300 9pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.textEdit_Numero)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.splitter_2.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Boutton_OK = QPushButton(self.layoutWidget1)
        self.Boutton_OK.setObjectName(u"Boutton_OK")

        self.horizontalLayout_5.addWidget(self.Boutton_OK)

        self.Button_Annuler = QPushButton(self.layoutWidget1)
        self.Button_Annuler.setObjectName(u"Button_Annuler")

        self.horizontalLayout_5.addWidget(self.Button_Annuler)

        self.splitter_2.addWidget(self.layoutWidget1)

        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.SW_Ajouter_personnel)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_2)

        self.SW_pg_personnal.addWidget(self.SW_Ajouter_personnel)
        self.SW_organiser_personnel = QWidget()
        self.SW_organiser_personnel.setObjectName(u"SW_organiser_personnel")
        self.layoutWidget2 = QWidget(self.SW_organiser_personnel)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 10, 329, 491))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lineEdit_recherche_personnel = QLineEdit(self.layoutWidget2)
        self.lineEdit_recherche_personnel.setObjectName(u"lineEdit_recherche_personnel")
        self.lineEdit_recherche_personnel.setMinimumSize(QSize(200, 30))
        self.lineEdit_recherche_personnel.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_26.addWidget(self.lineEdit_recherche_personnel)

        self.Button_recherche_personnel = QPushButton(self.layoutWidget2)
        self.Button_recherche_personnel.setObjectName(u"Button_recherche_personnel")
        self.Button_recherche_personnel.setMinimumSize(QSize(40, 30))
        self.Button_recherche_personnel.setMaximumSize(QSize(40, 30))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/search_find_tool_magnifier_glass_searching_magnifying_icon_250675.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Button_recherche_personnel.setIcon(icon1)
        self.Button_recherche_personnel.setIconSize(QSize(40, 40))

        self.horizontalLayout_26.addWidget(self.Button_recherche_personnel)


        self.verticalLayout_11.addLayout(self.horizontalLayout_26)

        self.listView_personnel = QListView(self.layoutWidget2)
        self.listView_personnel.setObjectName(u"listView_personnel")
        self.listView_personnel.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);")
        self.listView_personnel.setItemAlignment(Qt.AlignHCenter)

        self.verticalLayout_11.addWidget(self.listView_personnel)

        self.layoutWidget3 = QWidget(self.SW_organiser_personnel)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(340, 50, 77, 104))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Button_assignation_personnel = QPushButton(self.layoutWidget3)
        self.Button_assignation_personnel.setObjectName(u"Button_assignation_personnel")
        self.Button_assignation_personnel.setMinimumSize(QSize(0, 30))
        self.Button_assignation_personnel.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_12.addWidget(self.Button_assignation_personnel)

        self.Button_modifier_personnel = QPushButton(self.layoutWidget3)
        self.Button_modifier_personnel.setObjectName(u"Button_modifier_personnel")
        self.Button_modifier_personnel.setMinimumSize(QSize(0, 30))

        self.verticalLayout_12.addWidget(self.Button_modifier_personnel)

        self.Button_supprime_personnel = QPushButton(self.layoutWidget3)
        self.Button_supprime_personnel.setObjectName(u"Button_supprime_personnel")
        self.Button_supprime_personnel.setMinimumSize(QSize(0, 30))

        self.verticalLayout_12.addWidget(self.Button_supprime_personnel)

        self.SW_pg_personnal.addWidget(self.SW_organiser_personnel)
        self.GP_Supprimer = QWidget()
        self.GP_Supprimer.setObjectName(u"GP_Supprimer")
        self.SW_pg_personnal.addWidget(self.GP_Supprimer)

        self.gridLayout_2.addWidget(self.SW_pg_personnal, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.corp_pg_personnel, 1, 0, 1, 1)

        self.Menu_pg_personnel = QFrame(self.pg_personnel)
        self.Menu_pg_personnel.setObjectName(u"Menu_pg_personnel")
        self.Menu_pg_personnel.setMaximumSize(QSize(16777215, 40))
        self.Menu_pg_personnel.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	color: rgb(106, 106, 106);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 102);\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.Menu_pg_personnel.setFrameShape(QFrame.StyledPanel)
        self.Menu_pg_personnel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.Menu_pg_personnel)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Btn_liste = QPushButton(self.Menu_pg_personnel)
        self.Btn_liste.setObjectName(u"Btn_liste")
        self.Btn_liste.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.Btn_liste)

        self.Btn_ajouter = QPushButton(self.Menu_pg_personnel)
        self.Btn_ajouter.setObjectName(u"Btn_ajouter")
        self.Btn_ajouter.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.Btn_ajouter)

        self.Btn_organiser = QPushButton(self.Menu_pg_personnel)
        self.Btn_organiser.setObjectName(u"Btn_organiser")
        self.Btn_organiser.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_3.addWidget(self.Btn_organiser)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.Menu_pg_personnel, 0, 0, 1, 1)

        self.SW_principal.addWidget(self.pg_personnel)
        self.pg_depot = QWidget()
        self.pg_depot.setObjectName(u"pg_depot")
        self.SW_principal.addWidget(self.pg_depot)
        self.pg_projet = QWidget()
        self.pg_projet.setObjectName(u"pg_projet")
        self.verticalLayout_7 = QVBoxLayout(self.pg_projet)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_projet = QFrame(self.pg_projet)
        self.frame_menu_projet.setObjectName(u"frame_menu_projet")
        self.frame_menu_projet.setMinimumSize(QSize(0, 40))
        self.frame_menu_projet.setMaximumSize(QSize(16777215, 40))
        self.frame_menu_projet.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	color: rgb(106, 106, 106);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 0, 102);\n"
"	border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame_menu_projet.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_projet.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_menu_projet)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pb_listeProjet = QPushButton(self.frame_menu_projet)
        self.pb_listeProjet.setObjectName(u"pb_listeProjet")
        self.pb_listeProjet.setMinimumSize(QSize(100, 30))
        self.pb_listeProjet.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_14.addWidget(self.pb_listeProjet)

        self.pb_ajoutProjet = QPushButton(self.frame_menu_projet)
        self.pb_ajoutProjet.setObjectName(u"pb_ajoutProjet")
        self.pb_ajoutProjet.setMinimumSize(QSize(100, 30))
        self.pb_ajoutProjet.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_14.addWidget(self.pb_ajoutProjet)

        self.pb_orgniser = QPushButton(self.frame_menu_projet)
        self.pb_orgniser.setObjectName(u"pb_orgniser")
        self.pb_orgniser.setMinimumSize(QSize(100, 30))
        self.pb_orgniser.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_14.addWidget(self.pb_orgniser)

        self.pb_visualisation = QPushButton(self.frame_menu_projet)
        self.pb_visualisation.setObjectName(u"pb_visualisation")
        self.pb_visualisation.setMinimumSize(QSize(100, 30))
        self.pb_visualisation.setMaximumSize(QSize(100, 30))

        self.horizontalLayout_14.addWidget(self.pb_visualisation)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_14)


        self.verticalLayout_7.addWidget(self.frame_menu_projet)

        self.frame_contenus_projet = QFrame(self.pg_projet)
        self.frame_contenus_projet.setObjectName(u"frame_contenus_projet")
        self.frame_contenus_projet.setFrameShape(QFrame.StyledPanel)
        self.frame_contenus_projet.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_contenus_projet)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_projet = QStackedWidget(self.frame_contenus_projet)
        self.stackedWidget_projet.setObjectName(u"stackedWidget_projet")
        self.SW_Liste_projet = QWidget()
        self.SW_Liste_projet.setObjectName(u"SW_Liste_projet")
        self.verticalLayout_8 = QVBoxLayout(self.SW_Liste_projet)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tableWidget_projet = QTableWidget(self.SW_Liste_projet)
        if (self.tableWidget_projet.columnCount() < 7):
            self.tableWidget_projet.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_projet.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_projet.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_projet.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_projet.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_projet.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_projet.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_projet.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.tableWidget_projet.setObjectName(u"tableWidget_projet")

        self.verticalLayout_8.addWidget(self.tableWidget_projet)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.btn_actualiser_projet = QPushButton(self.SW_Liste_projet)
        self.btn_actualiser_projet.setObjectName(u"btn_actualiser_projet")
        self.btn_actualiser_projet.setMinimumSize(QSize(90, 30))
        self.btn_actualiser_projet.setMaximumSize(QSize(90, 30))

        self.horizontalLayout_13.addWidget(self.btn_actualiser_projet)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.stackedWidget_projet.addWidget(self.SW_Liste_projet)
        self.SW_Ajout_projet = QWidget()
        self.SW_Ajout_projet.setObjectName(u"SW_Ajout_projet")
        self.horizontalLayout_17 = QHBoxLayout(self.SW_Ajout_projet)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_4 = QFrame(self.SW_Ajout_projet)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(500, 0))
        self.frame_4.setStyleSheet(u"\n"
"QLabel{\n"
"	background-color: rgb(75, 0, 56);\n"
"	border-radius:10px;\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	font: 600 9pt \"Segoe UI\";\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.Btn_ajouter_projet = QPushButton(self.frame_4)
        self.Btn_ajouter_projet.setObjectName(u"Btn_ajouter_projet")
        self.Btn_ajouter_projet.setGeometry(QRect(160, 320, 75, 24))
        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(240, 320, 75, 24))
        self.splitter = QSplitter(self.frame_4)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(20, 11, 361, 293))
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget4 = QWidget(self.splitter)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")

        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_2 = QLabel(self.layoutWidget4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(71, 31))
        self.label_2.setMaximumSize(QSize(71, 31))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_2)

        self.textEdit_NOM_projet = QTextEdit(self.layoutWidget4)
        self.textEdit_NOM_projet.setObjectName(u"textEdit_NOM_projet")
        self.textEdit_NOM_projet.setMinimumSize(QSize(280, 30))
        self.textEdit_NOM_projet.setMaximumSize(QSize(280, 30))

        self.horizontalLayout_19.addWidget(self.textEdit_NOM_projet)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_3 = QLabel(self.layoutWidget4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(71, 31))
        self.label_3.setMaximumSize(QSize(71, 31))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_3)

        self.textEdit_societe = QTextEdit(self.layoutWidget4)
        self.textEdit_societe.setObjectName(u"textEdit_societe")
        self.textEdit_societe.setMinimumSize(QSize(280, 30))
        self.textEdit_societe.setMaximumSize(QSize(280, 30))

        self.horizontalLayout_20.addWidget(self.textEdit_societe)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(71, 31))
        self.label_4.setMaximumSize(QSize(71, 31))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_4)

        self.textEdit_Email_projet = QTextEdit(self.layoutWidget4)
        self.textEdit_Email_projet.setObjectName(u"textEdit_Email_projet")
        self.textEdit_Email_projet.setMinimumSize(QSize(280, 30))
        self.textEdit_Email_projet.setMaximumSize(QSize(280, 30))

        self.horizontalLayout_21.addWidget(self.textEdit_Email_projet)


        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_5 = QLabel(self.layoutWidget4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(71, 31))
        self.label_5.setMaximumSize(QSize(71, 31))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_5)

        self.textEdit_numero_projet = QTextEdit(self.layoutWidget4)
        self.textEdit_numero_projet.setObjectName(u"textEdit_numero_projet")
        self.textEdit_numero_projet.setMinimumSize(QSize(280, 30))
        self.textEdit_numero_projet.setMaximumSize(QSize(280, 30))

        self.horizontalLayout_22.addWidget(self.textEdit_numero_projet)


        self.verticalLayout_10.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_6 = QLabel(self.layoutWidget4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(71, 31))
        self.label_6.setMaximumSize(QSize(71, 31))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_6)

        self.textEdit_date_debut = QTextEdit(self.layoutWidget4)
        self.textEdit_date_debut.setObjectName(u"textEdit_date_debut")
        self.textEdit_date_debut.setMinimumSize(QSize(280, 30))
        self.textEdit_date_debut.setMaximumSize(QSize(280, 30))

        self.horizontalLayout_24.addWidget(self.textEdit_date_debut)


        self.verticalLayout_10.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_7 = QLabel(self.layoutWidget4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(71, 31))
        self.label_7.setMaximumSize(QSize(71, 31))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_7)

        self.textEdit_date_fin = QTextEdit(self.layoutWidget4)
        self.textEdit_date_fin.setObjectName(u"textEdit_date_fin")
        self.textEdit_date_fin.setMinimumSize(QSize(280, 30))
        self.textEdit_date_fin.setMaximumSize(QSize(280, 30))

        self.horizontalLayout_25.addWidget(self.textEdit_date_fin)


        self.verticalLayout_10.addLayout(self.horizontalLayout_25)

        self.splitter.addWidget(self.layoutWidget4)

        self.horizontalLayout_17.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.SW_Ajout_projet)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_17.addWidget(self.frame_5)

        self.stackedWidget_projet.addWidget(self.SW_Ajout_projet)
        self.SW_Organiser = QWidget()
        self.SW_Organiser.setObjectName(u"SW_Organiser")
        self.verticalLayout_9 = QVBoxLayout(self.SW_Organiser)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.stackedWidget = QStackedWidget(self.SW_Organiser)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.SW_Selection_projet = QWidget()
        self.SW_Selection_projet.setObjectName(u"SW_Selection_projet")
        self.layoutWidget5 = QWidget(self.SW_Selection_projet)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 0, 331, 33))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.textEdit_6 = QTextEdit(self.layoutWidget5)
        self.textEdit_6.setObjectName(u"textEdit_6")
        sizePolicy.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy)
        self.textEdit_6.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout_23.addWidget(self.textEdit_6)

        self.pushButton_3 = QPushButton(self.layoutWidget5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 31))
        self.pushButton_3.setMaximumSize(QSize(50, 31))

        self.horizontalLayout_23.addWidget(self.pushButton_3)

        self.comboBox = QComboBox(self.SW_Selection_projet)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(20, 50, 321, 31))
        self.pushButton_4 = QPushButton(self.SW_Selection_projet)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(260, 100, 81, 31))
        self.stackedWidget.addWidget(self.SW_Selection_projet)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_9.addWidget(self.stackedWidget)

        self.stackedWidget_projet.addWidget(self.SW_Organiser)

        self.gridLayout_3.addWidget(self.stackedWidget_projet, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_contenus_projet)

        self.SW_principal.addWidget(self.pg_projet)

        self.verticalLayout_5.addWidget(self.SW_principal)


        self.horizontalLayout_2.addWidget(self.frame_page)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.SW_principal.setCurrentIndex(2)
        self.SW_pg_personnal.setCurrentIndex(1)
        self.stackedWidget_projet.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.Btn_personnel.setText(QCoreApplication.translate("MainWindow", u"G\u00e9rer les personnels", None))
        self.Btn_projet.setText(QCoreApplication.translate("MainWindow", u"Gestion des Projets", None))
        self.Btn_depot.setText(QCoreApplication.translate("MainWindow", u"Gestion des Stoks", None))
        ___qtablewidgetitem = self.tableWidget_personnel.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_personnel.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOM", None));
        ___qtablewidgetitem2 = self.tableWidget_personnel.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PR\u00c9NOM", None));
        ___qtablewidgetitem3 = self.tableWidget_personnel.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ADRESSE", None));
        ___qtablewidgetitem4 = self.tableWidget_personnel.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem5 = self.tableWidget_personnel.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"NUM\u00c9RO", None));
        self.btn_Actualiser.setText(QCoreApplication.translate("MainWindow", u"Actualiser", None))
        self.label_ID.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_Nom.setText(QCoreApplication.translate("MainWindow", u"NOM", None))
        self.label_Prenom.setText(QCoreApplication.translate("MainWindow", u"PR\u00c9NOM", None))
        self.label_Adresse.setText(QCoreApplication.translate("MainWindow", u"Adresse", None))
        self.label_Email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_Numero.setText(QCoreApplication.translate("MainWindow", u"Num\u00e9ro", None))
        self.Boutton_OK.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.Button_Annuler.setText(QCoreApplication.translate("MainWindow", u"Annuler", None))
        self.Button_recherche_personnel.setText("")
        self.Button_assignation_personnel.setText(QCoreApplication.translate("MainWindow", u"Assignation", None))
        self.Button_modifier_personnel.setText(QCoreApplication.translate("MainWindow", u"Modifier ", None))
        self.Button_supprime_personnel.setText(QCoreApplication.translate("MainWindow", u"Supprimer", None))
        self.Btn_liste.setText(QCoreApplication.translate("MainWindow", u"LISTE", None))
        self.Btn_ajouter.setText(QCoreApplication.translate("MainWindow", u"AJOUTER", None))
        self.Btn_organiser.setText(QCoreApplication.translate("MainWindow", u"ORGANISER", None))
        self.pb_listeProjet.setText(QCoreApplication.translate("MainWindow", u"LISTE PROJET", None))
        self.pb_ajoutProjet.setText(QCoreApplication.translate("MainWindow", u"AJOUT  PROJET", None))
        self.pb_orgniser.setText(QCoreApplication.translate("MainWindow", u"ORGANISER", None))
        self.pb_visualisation.setText(QCoreApplication.translate("MainWindow", u"VISUALISATION", None))
        ___qtablewidgetitem6 = self.tableWidget_projet.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem7 = self.tableWidget_projet.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"NOM", None));
        ___qtablewidgetitem8 = self.tableWidget_projet.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"SOCIETE", None));
        ___qtablewidgetitem9 = self.tableWidget_projet.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem10 = self.tableWidget_projet.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem11 = self.tableWidget_projet.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"DATE D\u00c9BUT", None));
        ___qtablewidgetitem12 = self.tableWidget_projet.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"DATE FIN", None));
        self.btn_actualiser_projet.setText(QCoreApplication.translate("MainWindow", u"ACTUALISER", None))
        self.Btn_ajouter_projet.setText(QCoreApplication.translate("MainWindow", u"AJOUTER", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"ANNULER", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"NOM PROJET", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SOCIETE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DATE DEBUT", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DATE FIN", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


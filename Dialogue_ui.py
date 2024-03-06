from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QSplitter, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(459, 286)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_Dialog = QStackedWidget(Dialog)
        self.stackedWidget_Dialog.setObjectName(u"stackedWidget_Dialog")
        self.SW_assigne_personnel = QWidget()
        self.SW_assigne_personnel.setObjectName(u"SW_assigne_personnel")
        self.widget = QWidget(self.SW_assigne_personnel)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 190, 46))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.comboBox_assignation = QComboBox(self.widget)
        self.comboBox_assignation.setObjectName(u"comboBox_assignation")

        self.verticalLayout_2.addWidget(self.comboBox_assignation)

        self.splitter = QSplitter(self.SW_assigne_personnel)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(60, 70, 145, 24))
        self.splitter.setOrientation(Qt.Horizontal)
        self.pushButton_assigner = QPushButton(self.splitter)
        self.pushButton_assigner.setObjectName(u"pushButton_assigner")
        self.pushButton_assigner.setMinimumSize(QSize(70, 25))
        self.pushButton_assigner.setMaximumSize(QSize(70, 25))
        self.splitter.addWidget(self.pushButton_assigner)
        self.pushButton_annuler_assigner = QPushButton(self.splitter)
        self.pushButton_annuler_assigner.setObjectName(u"pushButton_annuler_assigner")
        self.pushButton_annuler_assigner.setMinimumSize(QSize(70, 25))
        self.pushButton_annuler_assigner.setMaximumSize(QSize(70, 25))
        self.splitter.addWidget(self.pushButton_annuler_assigner)
        self.stackedWidget_Dialog.addWidget(self.SW_assigne_personnel)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget_Dialog.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget_Dialog)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"VEILLEZ SELECTIONNER UN PROJET", None))
        self.pushButton_assigner.setText(QCoreApplication.translate("Dialog", u"AJOUTER", None))
        self.pushButton_annuler_assigner.setText(QCoreApplication.translate("Dialog", u"ANNULER", None))
    # retranslateUi


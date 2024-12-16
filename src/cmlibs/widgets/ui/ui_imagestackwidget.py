# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imagestackwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ImageStackWidget(object):
    def setupUi(self, ImageStackWidget):
        if not ImageStackWidget.objectName():
            ImageStackWidget.setObjectName(u"ImageStackWidget")
        ImageStackWidget.resize(400, 112)
        ImageStackWidget.setMaximumSize(QSize(16777215, 112))
        self.verticalLayout = QVBoxLayout(ImageStackWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBoxImage = QGroupBox(ImageStackWidget)
        self.groupBoxImage.setObjectName(u"groupBoxImage")
        self.formLayout_2 = QFormLayout(self.groupBoxImage)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_1 = QLabel(self.groupBoxImage)
        self.label_1.setObjectName(u"label_1")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_1)

        self.imagePixelOutputLabel = QLabel(self.groupBoxImage)
        self.imagePixelOutputLabel.setObjectName(u"imagePixelOutputLabel")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.imagePixelOutputLabel)

        self.overrideScalingCheckBox = QCheckBox(self.groupBoxImage)
        self.overrideScalingCheckBox.setObjectName(u"overrideScalingCheckBox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.overrideScalingCheckBox)

        self.scalingLineEdit = QLineEdit(self.groupBoxImage)
        self.scalingLineEdit.setObjectName(u"scalingLineEdit")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.scalingLineEdit)

        self.label_2 = QLabel(self.groupBoxImage)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_2)


        self.verticalLayout.addWidget(self.groupBoxImage)


        self.retranslateUi(ImageStackWidget)

        QMetaObject.connectSlotsByName(ImageStackWidget)
    # setupUi

    def retranslateUi(self, ImageStackWidget):
        ImageStackWidget.setWindowTitle(QCoreApplication.translate("ImageStackWidget", u"Form", None))
        self.groupBoxImage.setTitle(QCoreApplication.translate("ImageStackWidget", u"Image", None))
        self.label_1.setText(QCoreApplication.translate("ImageStackWidget", u"Dimensions:", None))
        self.imagePixelOutputLabel.setText(QCoreApplication.translate("ImageStackWidget", u"AxBxC px", None))
        self.overrideScalingCheckBox.setText(QCoreApplication.translate("ImageStackWidget", u"Override pre-dertermined scaling", None))
        self.label_2.setText(QCoreApplication.translate("ImageStackWidget", u"Scaling:", None))
    # retranslateUi


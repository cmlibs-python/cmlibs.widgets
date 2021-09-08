# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modelsourceseditorwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ModelSourcesEditorWidget(object):
    def setupUi(self, ModelSourcesEditorWidget):
        if not ModelSourcesEditorWidget.objectName():
            ModelSourcesEditorWidget.setObjectName(u"ModelSourcesEditorWidget")
        ModelSourcesEditorWidget.resize(269, 542)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ModelSourcesEditorWidget.sizePolicy().hasHeightForWidth())
        ModelSourcesEditorWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ModelSourcesEditorWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listViewModelSources = QListView(ModelSourcesEditorWidget)
        self.listViewModelSources.setObjectName(u"listViewModelSources")

        self.verticalLayout.addWidget(self.listViewModelSources)

        self.frame = QFrame(ModelSourcesEditorWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 7, 0, 7)
        self.comboBoxAddSource = QComboBox(self.frame)
        self.comboBoxAddSource.addItem("")
        self.comboBoxAddSource.addItem("")
        self.comboBoxAddSource.addItem("")
        self.comboBoxAddSource.setObjectName(u"comboBoxAddSource")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxAddSource.sizePolicy().hasHeightForWidth())
        self.comboBoxAddSource.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.comboBoxAddSource)

        self.pushButtonApplySource = QPushButton(self.frame)
        self.pushButtonApplySource.setObjectName(u"pushButtonApplySource")
        self.pushButtonApplySource.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButtonApplySource)

        self.pushButtonDeleteSource = QPushButton(self.frame)
        self.pushButtonDeleteSource.setObjectName(u"pushButtonDeleteSource")

        self.horizontalLayout.addWidget(self.pushButtonDeleteSource)


        self.verticalLayout.addWidget(self.frame)

        self.groupBoxFileSource = QGroupBox(ModelSourcesEditorWidget)
        self.groupBoxFileSource.setObjectName(u"groupBoxFileSource")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBoxFileSource.sizePolicy().hasHeightForWidth())
        self.groupBoxFileSource.setSizePolicy(sizePolicy2)
        self.formLayout = QFormLayout(self.groupBoxFileSource)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setContentsMargins(7, 2, 7, 2)
        self.labelFileName = QLabel(self.groupBoxFileSource)
        self.labelFileName.setObjectName(u"labelFileName")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.labelFileName)

        self.labelTime = QLabel(self.groupBoxFileSource)
        self.labelTime.setObjectName(u"labelTime")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.labelTime)

        self.lineEditTime = QLineEdit(self.groupBoxFileSource)
        self.lineEditTime.setObjectName(u"lineEditTime")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEditTime)

        self.lineEditFileName = QLineEdit(self.groupBoxFileSource)
        self.lineEditFileName.setObjectName(u"lineEditFileName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEditFileName)

        self.pushButtonBrowseFileName = QPushButton(self.groupBoxFileSource)
        self.pushButtonBrowseFileName.setObjectName(u"pushButtonBrowseFileName")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButtonBrowseFileName)


        self.verticalLayout.addWidget(self.groupBoxFileSource)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ModelSourcesEditorWidget)

        QMetaObject.connectSlotsByName(ModelSourcesEditorWidget)
    # setupUi

    def retranslateUi(self, ModelSourcesEditorWidget):
        ModelSourcesEditorWidget.setWindowTitle(QCoreApplication.translate("ModelSourcesEditorWidget", u"Model Sources Editor", None))
        self.comboBoxAddSource.setItemText(0, QCoreApplication.translate("ModelSourcesEditorWidget", u"Add...", None))
        self.comboBoxAddSource.setItemText(1, QCoreApplication.translate("ModelSourcesEditorWidget", u"---", None))
        self.comboBoxAddSource.setItemText(2, QCoreApplication.translate("ModelSourcesEditorWidget", u"File", None))

        self.pushButtonApplySource.setText(QCoreApplication.translate("ModelSourcesEditorWidget", u"Apply", None))
        self.pushButtonDeleteSource.setText(QCoreApplication.translate("ModelSourcesEditorWidget", u"Delete...", None))
        self.groupBoxFileSource.setTitle(QCoreApplication.translate("ModelSourcesEditorWidget", u"File Source:", None))
        self.labelFileName.setText(QCoreApplication.translate("ModelSourcesEditorWidget", u"File name:", None))
        self.labelTime.setText(QCoreApplication.translate("ModelSourcesEditorWidget", u"Time:", None))
        self.pushButtonBrowseFileName.setText(QCoreApplication.translate("ModelSourcesEditorWidget", u"Browse...", None))
    # retranslateUi


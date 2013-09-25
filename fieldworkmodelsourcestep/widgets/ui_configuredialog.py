# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/configuredialog.ui'
#
# Created: Wed Jul  3 00:06:09 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        ConfigureDialog.setObjectName("ConfigureDialog")
        ConfigureDialog.resize(593, 253)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ConfigureDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(ConfigureDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.identifierLineEdit = QtGui.QLineEdit(self.groupBox)
        self.identifierLineEdit.setObjectName("identifierLineEdit")

        self.gridLayout.addWidget(self.identifierLineEdit, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.geometricFieldLineEdit = QtGui.QLineEdit(self.groupBox)
        self.geometricFieldLineEdit.setStyleSheet("selection-color: red;\n"
"color: green")
        self.geometricFieldLineEdit.setObjectName("geometricFieldLineEdit")
        self.horizontalLayout.addWidget(self.geometricFieldLineEdit)
        self.geometricFieldButton = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.geometricFieldButton.setFont(font)
        self.geometricFieldButton.setObjectName("geometricFieldButton")
        self.horizontalLayout.addWidget(self.geometricFieldButton)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(71, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(71, 0))
        self.label_4.setObjectName("label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ensembleLineEdit = QtGui.QLineEdit(self.groupBox)
        self.ensembleLineEdit.setStyleSheet("selection-color: red;\n"
"color: green")
        self.ensembleLineEdit.setObjectName("ensembleLineEdit")
        self.horizontalLayout_3.addWidget(self.ensembleLineEdit)
        self.ensembleButton = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.ensembleButton.setFont(font)
        self.ensembleButton.setObjectName("ensembleButton")
        self.horizontalLayout_3.addWidget(self.ensembleButton)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.previousLocationLabel = QtGui.QLabel(self.groupBox)
        self.previousLocationLabel.setMaximumSize(QtCore.QSize(0, 16777215))
        self.previousLocationLabel.setText("")
        self.previousLocationLabel.setObjectName("previousLocationLabel")
        self.gridLayout.addWidget(self.previousLocationLabel, 4, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.geometricFieldLineEdit)
        self.label_4.setBuddy(self.geometricFieldLineEdit)
        self.label.setBuddy(self.identifierLineEdit)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure - Fieldwork Model Source", None, QtGui.QApplication.UnicodeUTF8))
        self.geometricFieldLineEdit.setToolTip(QtGui.QApplication.translate("ConfigureDialog", "Maybe a combined geometricField and ensemble file", None, QtGui.QApplication.UnicodeUTF8))
        self.geometricFieldButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setToolTip(QtGui.QApplication.translate("ConfigureDialog", "Maybe a combined geometricField and ensemble file", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ConfigureDialog", "geometricField File:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ConfigureDialog", "ensemble File:", None, QtGui.QApplication.UnicodeUTF8))
        self.ensembleButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConfigureDialog", "Identifier:", None, QtGui.QApplication.UnicodeUTF8))


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
        self.verticalLayout = QtGui.QVBoxLayout(ConfigureDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ConfigureDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        
        # identifier 
        self.identifierLineEdit = QtGui.QLineEdit(self.groupBox)
        self.identifierLineEdit.setObjectName("identifierLineEdit")
        self.gridLayout.addWidget(self.identifierLineEdit, 0, 1, 1, 1)
        self.identifierLabel = QtGui.QLabel(self.groupBox)
        self.identifierLabel.setObjectName("identifierLabel")
        self.gridLayout.addWidget(self.identifierLabel, 0, 0, 1, 1)

        # geometric field
        self.geometricFieldHorizontalLayout = QtGui.QHBoxLayout()
        self.geometricFieldHorizontalLayout.setObjectName("geometricFieldHorizontalLayout")
        self.geometricFieldLineEdit = QtGui.QLineEdit(self.groupBox)
        self.geometricFieldLineEdit.setStyleSheet("selection-color: red;\n"
"color: green")
        self.geometricFieldLineEdit.setObjectName("geometricFieldLineEdit")
        self.geometricFieldHorizontalLayout.addWidget(self.geometricFieldLineEdit)
        self.geometricFieldButton = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.geometricFieldButton.setFont(font)
        self.geometricFieldButton.setObjectName("geometricFieldButton")
        self.geometricFieldHorizontalLayout.addWidget(self.geometricFieldButton)
        self.gridLayout.addLayout(self.geometricFieldHorizontalLayout, 1, 1, 1, 1)
        self.geometricFieldLabel = QtGui.QLabel(self.groupBox)
        self.geometricFieldLabel.setMinimumSize(QtCore.QSize(71, 0))
        self.geometricFieldLabel.setObjectName("geometricFieldLabel")
        self.gridLayout.addWidget(self.geometricFieldLabel, 1, 0, 1, 1)

        # ensemble
        self.ensembleHorizontalLayout = QtGui.QHBoxLayout()
        self.ensembleHorizontalLayout.setObjectName("ensembleHorizontalLayout")
        self.ensembleLineEdit = QtGui.QLineEdit(self.groupBox)
        self.ensembleLineEdit.setStyleSheet("selection-color: red;\n"
"color: green")
        self.ensembleLineEdit.setObjectName("ensembleLineEdit")
        self.ensembleHorizontalLayout.addWidget(self.ensembleLineEdit)
        self.ensembleButton = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.ensembleButton.setFont(font)
        self.ensembleButton.setObjectName("ensembleButton")
        self.ensembleHorizontalLayout.addWidget(self.ensembleButton)
        self.gridLayout.addLayout(self.ensembleHorizontalLayout, 2, 1, 1, 1)
        self.ensembleLabel = QtGui.QLabel(self.groupBox)
        self.ensembleLabel.setMinimumSize(QtCore.QSize(71, 0))
        self.ensembleLabel.setObjectName("ensembleLabel")
        self.gridLayout.addWidget(self.ensembleLabel, 2, 0, 1, 1)

        # mesh
        self.meshHorizontalLayout = QtGui.QHBoxLayout()
        self.meshHorizontalLayout.setObjectName("meshHorizontalLayout")
        self.meshLineEdit = QtGui.QLineEdit(self.groupBox)
        self.meshLineEdit.setStyleSheet("selection-color: red;\n"
"color: green")
        self.meshLineEdit.setObjectName("meshLineEdit")
        self.meshHorizontalLayout.addWidget(self.meshLineEdit)
        self.meshButton = QtGui.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.meshButton.setFont(font)
        self.meshButton.setObjectName("meshButton")
        self.meshHorizontalLayout.addWidget(self.meshButton)
        self.gridLayout.addLayout(self.meshHorizontalLayout, 3, 1, 1, 1)
        self.meshLabel = QtGui.QLabel(self.groupBox)
        self.meshLabel.setMinimumSize(QtCore.QSize(71, 0))
        self.meshLabel.setObjectName("meshLabel")
        self.gridLayout.addWidget(self.meshLabel, 3, 0, 1, 1)  
        
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.previousLocationLabel = QtGui.QLabel(self.groupBox)
        self.previousLocationLabel.setMaximumSize(QtCore.QSize(0, 16777215))
        self.previousLocationLabel.setText("")
        self.previousLocationLabel.setObjectName("previousLocationLabel")
        self.gridLayout.addWidget(self.previousLocationLabel, 5, 1, 1, 1)
      
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.geometricFieldLabel.setBuddy(self.geometricFieldLineEdit)
        self.ensembleLabel.setBuddy(self.ensembleLineEdit)
        self.meshLabel.setBuddy(self.meshLineEdit)
        self.identifierLabel.setBuddy(self.identifierLineEdit)

        self.retranslateUi(ConfigureDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ConfigureDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ConfigureDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigureDialog)

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QtGui.QApplication.translate("ConfigureDialog", "Configure - Fieldwork Model Source", None, QtGui.QApplication.UnicodeUTF8))
        self.geometricFieldLineEdit.setToolTip(QtGui.QApplication.translate("ConfigureDialog", "Maybe a combined geometric field, ensemble file, and mesh file", None, QtGui.QApplication.UnicodeUTF8))
        self.geometricFieldButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.geometricFieldLabel.setToolTip(QtGui.QApplication.translate("ConfigureDialog", "Maybe a combined geometric field, ensemble file, and mesh file", None, QtGui.QApplication.UnicodeUTF8))
        self.geometricFieldLabel.setText(QtGui.QApplication.translate("ConfigureDialog", "Geometric Field File:", None, QtGui.QApplication.UnicodeUTF8))
        self.ensembleLabel.setText(QtGui.QApplication.translate("ConfigureDialog", "Ensemble File:", None, QtGui.QApplication.UnicodeUTF8))
        self.meshLabel.setText(QtGui.QApplication.translate("ConfigureDialog", "Mesh File:", None, QtGui.QApplication.UnicodeUTF8))
        self.ensembleButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.meshButton.setText(QtGui.QApplication.translate("ConfigureDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.identifierLabel.setText(QtGui.QApplication.translate("ConfigureDialog", "Identifier:", None, QtGui.QApplication.UnicodeUTF8))


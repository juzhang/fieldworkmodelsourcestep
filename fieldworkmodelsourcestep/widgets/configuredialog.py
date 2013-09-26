'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''
import os

from PySide.QtGui import QDialog, QFileDialog, QDialogButtonBox

from fieldworkmodelsourcestep.widgets.ui_configuredialog import Ui_ConfigureDialog
from fieldworkmodelsourcestep.fieldworkmodeldata import FieldworkModelData

REQUIRED_STYLE_SHEET = 'border: 1px solid red; border-radius: 3px'
DEFAULT_STYLE_SHEET = ''

class ConfigureDialog(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''

    def __init__(self, state, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self._ui = Ui_ConfigureDialog()
        self._ui.setupUi(self)
        
        self.setState(state)
        self.validate()
        self._makeConnections()
        
    def _makeConnections(self):
        self._ui.geometricFieldButton.clicked.connect(self._geometricFieldButtonClicked)
        self._ui.ensembleButton.clicked.connect(self._ensembleButtonClicked)
        self._ui.meshButton.clicked.connect(self._meshButtonClicked)
        self._ui.geometricFieldLineEdit.textChanged.connect(self.validate)
        self._ui.ensembleLineEdit.textChanged.connect(self.validate)
        self._ui.meshLineEdit.textChanged.connect(self.validate)
        self._ui.identifierLineEdit.textChanged.connect(self.validate)
    
    def setState(self, state):
        self._ui.identifierLineEdit.setText(state._identifier)
        self._ui.geometricFieldLineEdit.setText(state._geometricFieldLocation)
        self._ui.ensembleLineEdit.setText(state._ensembleLocation)
        self._ui.meshLineEdit.setText(state._meshLocation)
    
    def getState(self):
        state = FieldworkModelData()
        state._identifier = self._ui.identifierLineEdit.text()
        state._geometricFieldLocation = self._ui.geometricFieldLineEdit.text()
        state._ensembleLocation = self._ui.ensembleLineEdit.text()
        state._meshLocation = self._ui.meshLineEdit.text()
        
        return state
        
    def validate(self):
        identifier_valid = len(self._ui.identifierLineEdit.text()) > 0
        if identifier_valid:
            self._ui.identifierLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.identifierLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)
            
        geometricField_valid = len(self._ui.geometricFieldLineEdit.text()) > 0
        if geometricField_valid:
            self._ui.geometricFieldLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.geometricFieldLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        ensemble_valid = len(self._ui.ensembleLineEdit.text()) > 0
        if ensemble_valid:
            self._ui.ensembleLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.ensembleLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        mesh_valid = len(self._ui.meshLineEdit.text()) > 0
        if mesh_valid:
            self._ui.meshLineEdit.setStyleSheet(DEFAULT_STYLE_SHEET)
        else:
            self._ui.meshLineEdit.setStyleSheet(REQUIRED_STYLE_SHEET)

        valid = identifier_valid and geometricField_valid and ensemble_valid and mesh_valid
        self._ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(valid)

        return valid
    
    def _lineEditFile(self, line_edit):
        (fileName, _) = QFileDialog.getOpenFileName(self, 'Select Fieldwork File', self._ui.previousLocationLabel.text()) 
        
        if fileName:
            location = os.path.basename(fileName)
            self._ui.previousLocationLabel.setText(location)
            line_edit.setText(fileName)
            
        self.validate()
    
    def _geometricFieldButtonClicked(self):
        self._lineEditFile(self._ui.geometricFieldLineEdit)
    
    def _ensembleButtonClicked(self):
        self._lineEditFile(self._ui.ensembleLineEdit)

    def _meshButtonClicked(self):
        self._lineEditFile(self._ui.meshLineEdit)


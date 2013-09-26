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

from PySide import QtCore, QtGui

from mountpoints.workflowstep import WorkflowStepMountPoint

from fieldworkmodelsourcestep.widgets.configuredialog import ConfigureDialog
from fieldworkmodelsourcestep.fieldworkmodeldata import FieldworkModelData

import sys
sys.path.append('../../../../')

class FieldworkModelSourceStep(WorkflowStepMountPoint):
    '''
    fieldwork model source step supplies fieldwork model source files
    from a location on disk.
    '''
    
    def __init__(self, location):
        super(FieldworkModelSourceStep, self).__init__('Fieldwork Model Source', location)
        self._state = FieldworkModelData()
        self._icon = QtGui.QImage(':/zincmodelsource/images/zinc_model_icon.png')   # change this
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port', 'http://physiomeproject.org/workflow/1.0/rdf-schema#provides', 'ju#fieldworkmodel'))
        
    def configure(self):
        d = ConfigureDialog(self._state)
        d.setModal(True)
        if d.exec_():
            self._state = d.getState()
            self.serialize(self._location)
            
        self._configured = d.validate()
        if self._configured and self._configuredObserver:
            self._configuredObserver()
    
    def getIdentifier(self):
        return self._state._identifier
     
    def setIdentifier(self, identifier):
        self._state._identifier = identifier
     
    def serialize(self, location):
        configuration_file = os.path.join(location, getConfigFilename(self._state._identifier))
        s = QtCore.QSettings(configuration_file, QtCore.QSettings.IniFormat)
        s.beginGroup('state')
        s.setValue('identifier', self._state._identifier)
        s.setValue('geometricfield', self._state._geometricFieldLocation)
        s.setValue('ensemble', self._state._ensembleLocation)
        s.setValue('mesh', self._state._meshLocation)
        s.endGroup()
     
    def deserialize(self, location):
        configuration_file = os.path.join(location, getConfigFilename(self._state._identifier))
        s = QtCore.QSettings(configuration_file, QtCore.QSettings.IniFormat)
        s.beginGroup('state')
        self._state._identifier = s.value('identifier', '')
        self._state._geometricFieldLocation = s.value('geometricField', '')
        self._state._ensembleLocation = s.value('ensemble', '')
        self._state._meshLocation = s.value('mesh', '')
        s.endGroup()
        d = ConfigureDialog(self._state)
        self._configured = d.validate()
        
    def portOutput(self):
        geometricField = fieldwork.geometric_field.load_geometric_field(self._state._geometricFieldLocation,
                                                                        self._state._ensembleLocation,
                                                                        self._state._meshLocation,
                                                                        )
        return geometricField
     
def getConfigFilename(identifier):
    return identifier + '.conf'


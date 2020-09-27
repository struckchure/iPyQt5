from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iQSS.iCard import iCardVariables
from iQSS import genericVariables
import configurations

'''
    Cards
'''


class Card(QtWidgets.QGroupBox):
    def __init__(
            self,
            accent:str=None,
            size:str='normal',
            header:dict={},
            body:dict={},
            footer:dict={},
            customVariables:dict={},
        ):
        super(Card, self).__init__()

        self.accent = accent
        self.size = size
        self.header = header
        self.body = body
        self.footer = footer
        self.customVariables = customVariables

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )

    def initialization(self):
        self.setCustomStyleSheet()
        self.createHeader()
        self.createBody()
        self.createFooter()
    
    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iCard/iCard.qss'),
        variables=iCardVariables.variables,
        output='iCard/iCard.css',
        ):
        variables = iUtils.dictMerger(
            variables,
            self.customVariables
        )
        
        self.currentVariables = variables

        self.customStyleSheet = iUtils.readQSS(
            qss=style,
            qssVariables=self.currentVariables,
            output_file=output,
            boundary='/* Card Basic */'
        )

        self.setStyleSheet(self.customStyleSheet)
    
    def createHeader(self):
        pass

    def createBody(self):
        pass

    def createFooter(self):
        pass


class CardHeader(QtWidgets.QGroupBox):
    def __init__(
            self,
            heading={},
            height=50,
            accent=None
        ):
        super(CardHeader, self).__init__()

        self.initialization()
    
    def initialization(self):
        pass

    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iCard/iCard.qss'),
        variables=iCardVariables.variables,
        output='iCard/iCard.css',
        ):
        variables = iUtils.dictMerger(
            variables,
            self.customVariables
        )
        
        self.currentVariables = variables

        self.customStyleSheet = iUtils.readQSS(
            qss=style,
            qssVariables=self.currentVariables,
            output_file=output,
            boundary='/* Card Header */'
        )

        self.setStyleSheet(self.customStyleSheet)


class CardBody(QtWidgets.QGroupBox):
    def __init__(
            self
        ):
        super(CardBody, self).__init__()

        self.initialization()
    
    def initialization(self):
        pass

    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iCard/iCard.qss'),
        variables=iCardVariables.variables,
        output='iCard/iCard.css',
        ):
        variables = iUtils.dictMerger(
            variables,
            self.customVariables
        )
        
        self.currentVariables = variables

        self.customStyleSheet = iUtils.readQSS(
            qss=style,
            qssVariables=self.currentVariables,
            output_file=output,
            boundary='/* Card Basic */'
        )

        self.setStyleSheet(self.customStyleSheet)


class CardFooter(QtWidgets.QGroupBox):
    def __init__(
            self
        ):
        super(CardFooter, self).__init__()

        self.initialization()
    
    def initialization(self):
        pass

    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iCard/iCard.qss'),
        variables=iCardVariables.variables,
        output='iCard/iCard.css',
        ):
        variables = iUtils.dictMerger(
            variables,
            self.customVariables
        )
        
        self.currentVariables = variables

        self.customStyleSheet = iUtils.readQSS(
            qss=style,
            qssVariables=self.currentVariables,
            output_file=output,
            boundary='/* Card Basic */'
        )

        self.setStyleSheet(self.customStyleSheet)

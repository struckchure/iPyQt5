from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iQSS.iGeneral import iCardVariables
from iQSS import genericVariables
import configurations

'''
    Cards
'''


class Card(QtWidgets.QGroupBox):
    def __init__(
        self,
        accent:str='primary',
        width:int=200,
        height:int=200,
        header:dict={},
        body:dict={},
        footer:dict={},
        customVariables:dict={},
        xFill:bool=False,
        yFill:bool=False
        ):
        super(Card, self).__init__()

        self.accent = accent
        self.height = height
        self.width = width
        self.xFill = xFill
        self.yFill = yFill
        
        self.header = iUtils.dictMerger(
            {
                'accent': accent,
                'child' : QtWidgets.QLabel('Header')
            },
            header
        )
        self.body = iUtils.dictMerger(
            {
                'accent': accent,
                'child' : QtWidgets.QLabel('Body')
            },
            body
        )
        self.footer = iUtils.dictMerger(
            {
                'accent': accent,
                'child' : QtWidgets.QLabel('Footer')
            },
            footer
        )
        self.customVariables = customVariables

        self.accentStyles = genericVariables.variables['accents'][self.accent]
        self.customVariables = iUtils.dictMerger(
            self.customVariables,
            self.accentStyles['normal'],
        )

        self.cardLayout = QtWidgets.QVBoxLayout()
        self.cardLayout.setContentsMargins(0, 0, 0, 0)

        if not self.width:
            self.width = 900
        if not self.height:
            self.height = 400
        
        if self.xFill:
            self.setMaximumWidth(self.width)
        if self.yFill:
            self.setMaximumHeight(self.height)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.setLayout(self.cardLayout)

        self.initialization()

    def initialization(self):
        self.setCustomStyleSheet()
        self.createHeader()
        self.createBody()
        self.createFooter()
    
    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iGeneral/iCard.qss'),
        variables=iCardVariables.variables,
        output='iGeneral/compiled/iCard.css',
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
        if self.header:
            self.cardHeader = CardHeader(
                accent=self.header['accent'],
                child=self.header
            )
            self.cardLayout.addWidget(
                self.cardHeader,
                stretch=0,
                alignment=QtCore.Qt.AlignTop
            )

    def createBody(self):
        self.cardBody = CardBody(
            accent=self.accent,
            child=self.body
        )
        self.cardLayout.addWidget(
            self.cardBody,
            stretch=0,
            alignment=QtCore.Qt.AlignHCenter
        )

    def createFooter(self):
        if self.footer:
            self.cardFooter = CardFooter(
                accent=self.footer['accent'],
                child=self.footer
            )
            self.cardLayout.addWidget(
                self.cardFooter,
                stretch=0,
                alignment=QtCore.Qt.AlignBottom
            )


class CardHeader(QtWidgets.QGroupBox):
    def __init__(
            self,
            height:int=50,
            accent:str=None,
            customVariables:dict={},
            child:dict={}
        ):
        super(CardHeader, self).__init__()

        self.child = iUtils.dictMerger(
            {
                'child': QtWidgets.QLabel('Header'),
                'alignment': QtCore.Qt.AlignLeft
            },
            child
        )
        self.customVariables = customVariables
        self.height = height
        self.accent = accent
        self.accentStyles = genericVariables.variables['accents'][self.accent]
        self.customVariables = iUtils.dictMerger(
            self.customVariables,
            self.accentStyles['normal'],
        )

        self.cardHeaderLayout = QtWidgets.QHBoxLayout()
        
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.setMaximumHeight(height)
        self.setLayout(self.cardHeaderLayout)

        self.initialization()

    def initialization(self):
        self.setCustomStyleSheet()
        self.addHeaderChild(
            self.child['child']
        )

    def setCustomStyleSheet(
            self,
            style=os.path.join(configurations.QSS_DIR, 'iGeneral/iCard.qss'),
            variables=iCardVariables.variables,
            output='iGeneral/compiled/iCard.css',
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
    
    def addHeaderChild(self, child):
        self.cardHeaderLayout.addWidget(
            child,
            stretch=0,
            alignment=self.child['alignment']
        )


class CardBody(QtWidgets.QGroupBox):
    def __init__(
            self,
            heading={},
            height=100,
            accent=None,
            customVariables:dict={},
            child={}
        ):
        super(CardBody, self).__init__()

        self.child = iUtils.dictMerger(
            {
                'child': QtWidgets.QLabel('Body'),
                'alignment': QtCore.Qt.AlignCenter
            },
            child
        )
        self.height = height
        self.accent = accent
        self.customVariables = customVariables
        self.accentStyles = genericVariables.variables['accents'][self.accent]
        self.customVariables = iUtils.dictMerger(
            self.customVariables,
            self.accentStyles['normal'],
        )

        self.cardBodyLayout = QtWidgets.QVBoxLayout()

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.setMaximumHeight(height)
        self.setLayout(self.cardBodyLayout)

        self.initialization()
    
    def initialization(self):
        self.setCustomStyleSheet()
        self.addBodyChild(
            self.child['child'],
            self.child['alignment']
        )

    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iGeneral/iCard.qss'),
        variables=iCardVariables.variables,
        output='iGeneral/compiled/iCard.css',
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
    
    def addBodyChild(self, child, alignment):
        self.cardBodyLayout.addWidget(
            child,
            stretch=0,
            alignment=alignment
        )


class CardFooter(QtWidgets.QGroupBox):
    def __init__(
            self,
            heading={},
            height=50,
            accent=None,
            customVariables:dict={},
            child:dict={}
        ):
        super(CardFooter, self).__init__()

        self.child = iUtils.dictMerger(
            {
                'child': QtWidgets.QLabel('Footer'),
                'alignment': QtCore.Qt.AlignLeft
            },
            child
        )
        self.customVariables = customVariables
        self.heading = heading
        self.height = height
        self.accent = accent
        self.accentStyles = genericVariables.variables['accents'][self.accent]
        self.customVariables = iUtils.dictMerger(
            self.customVariables,
            self.accentStyles['normal'],
        )

        self.cardFooterLayout = QtWidgets.QHBoxLayout()
        
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.setMaximumHeight(height)
        self.setLayout(self.cardFooterLayout)

        self.initialization()
    
    def initialization(self):
        self.setCustomStyleSheet()
        self.addFooterChild(
            self.child['child']
        )

    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iGeneral/iCard.qss'),
        variables=iCardVariables.variables,
        output='iGeneral/compiled/iCard.css',
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
    
    def addFooterChild(self, child):
        self.cardFooterLayout.addWidget(
            child,
            stretch=0,
            alignment=self.child['alignment']
        )

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iQSS.iGeneral import iButtonVariables
from iQSS import genericVariables
import configurations

'''
    Buttons
'''


class Button(QtWidgets.QPushButton):
    def __init__(
        self,
        text:str='Click me',
        icon:str=None,
        width:int=None,
        height:int=None,
        onClick=None,
        accent:str=None,
        size:str='normal',
        fill:bool=False,
        enabled:bool=True,
        customVariables:dict={},
        animation:dict={}
        ):
        super(Button, self).__init__()

        if accent:
            self.accent = accent
            self.accentStyles = genericVariables.variables['accents'][self.accent]

            animation = iUtils.dictMerger(
                animation,
                {
                    # Background Color

                    'bgStartValue': self.accentStyles['hover']['background-color'],
                    'bgEndValue': self.accentStyles['normal']['background-color'],
                    
                    # Color
                    
                    'cStartValue': self.accentStyles['normal']['color'],
                    'cEndValue': self.accentStyles['hover']['color'],
                },
            )
        
        self.customAnimations = iUtils.dictMerger(
            {
                # Background Color

                'bgStartValue': '#9330ef',
                'bgEndValue': 'white',
                'duration': 500,
                
                # Color
                
                'cStartValue': 'black',
                'cEndValue': 'white',
            },
            animation,
        )
        self.enabled = enabled
        self.onClick = onClick
        self.fill = fill
        
        self._animation = QtCore.QVariantAnimation(
            startValue=QtGui.QColor(self.customAnimations['bgStartValue']),
            endValue=QtGui.QColor(self.customAnimations['bgEndValue']),
            valueChanged=self.updateCustomStylesheet,
            duration=self.customAnimations['duration'],
        )

        if not width:
            width = iButtonVariables.sizes[size]['width']
        if not height:
            height = iButtonVariables.sizes[size]['height']

        self.setText(text)
        
        if not self.fill:
            self.setMaximumSize(
                width,
                height
            )
            self.customVariables = iUtils.dictMerger(
                customVariables,
                genericVariables.variables['sizes'][size]
            )
        else:
            self.customVariables = customVariables

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )

        if enabled:
            self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        else:
            self.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
            self.setWindowOpacity(0.45)
        
        self.initialization()

    def initialization(self):
        self.connectButton(self.onClick)
        self.setCustomStyleSheet()

    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iGeneral/iButton.qss'),
        variables=iButtonVariables.variables,
        output='iGeneral/compiled/iButton.css',
        ):
        variables = iUtils.dictMerger(
            variables,
            self.customVariables
        )

        variables['color'] = self.customAnimations['cStartValue']
        
        self.currentVariables = variables

        self.customStyleSheet = iUtils.readQSS(
            qss=style,
            qssVariables=self.currentVariables,
            output_file=output,
            boundary='/* Button Basic */'
        )

        self.setStyleSheet(self.customStyleSheet)
        self._animation.start()
    
    def updateCustomStylesheet(self, backgroundColor, **kwargs):
        cStartValue = (
            self.customAnimations['cStartValue']
            if self.customAnimations.get('cStartValue')
            else 'black'
        )
        cEndValue = (
            self.customAnimations['cEndValue']
            if self.customAnimations.get('cEndValue')
            else 'white'
        )

        color = (
            QtGui.QColor(cStartValue)
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor(cEndValue)
        )

        kwargs['color'] = color.name() # color
        kwargs['background-color'] = backgroundColor.name() # background-color

        kwargs = iUtils.dictMerger(self.currentVariables, kwargs)

        self.setCustomStyleSheet(variables=kwargs)

    def enterEvent(self, event):
        if self.enabled:
            self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
            self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.enabled:
            self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
            self._animation.start()
        super().leaveEvent(event)

    def connectButton(self, event):
        if event and self.enabled:
            self.clicked.connect(event)

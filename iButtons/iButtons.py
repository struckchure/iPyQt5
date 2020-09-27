from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

'''
    Base for Genrics
'''

from iBase.iBase import ButtonBase
from iUtils import iUtils
from iQSS.iButton import iButtonVariables
from iQSS import genericVariables
import configurations

'''
    Buttons
'''


class Button(QtWidgets.QPushButton, ButtonBase):
    def __init__(
            self,
            text:str='Click me',
            icon:str=None,
            event=None,
            width:int=200,
            height:int=50,
            accent:str='primary',
            customVariables:dict={},
            animation:dict={
                # Background Color

                'bgStartValue': '#9330ef',
                'bgEndValue': 'white',
                'duration': 400,
                
                # Color
                
                'cStartValue': 'black',
                'cEndValue': 'white',
            }
        ):
        super(Button, self).__init__()
        print(customVariables)

        self.accent = accent
        self.accentStyles = genericVariables.variables[self.accent]
        self.customVariables = iUtils.dictMerger(
            customVariables
        )

        self.customAnimations = iUtils.dictMerger(
            animation,
            # {
            #     # Background Color

            #     'bgStartValue': self.accentStyles['hover']['background-color'],
            #     'bgEndValue': self.accentStyles['normal']['background-color'],
            #     'duration': 600,
                
            #     # Color
                
            #     'cStartValue': self.accentStyles['normal']['color'],
            #     'cEndValue': self.accentStyles['hover']['color'],
            # }
        )
        
        self._animation = QtCore.QVariantAnimation(
            startValue=QtGui.QColor(self.customAnimations['bgStartValue']),
            endValue=QtGui.QColor(self.customAnimations['bgEndValue']),
            valueChanged=self.updateCustomStylesheet,
            duration=self.customAnimations['duration'],
        )

        self.setText(text)
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
        
        self.initialization()

    def initialization(self):
        self.setCustomStyleSheet()

    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iButton/iButton.qss'),
        variables=iButtonVariables.variables,
        output='iButton/iButton.css',
        ):
        variables = iUtils.dictMerger(
            variables,
            self.customVariables,
            # self.accentStyles['normal']
        )

        # variables['background-color'] = self.accentStyles['normal']['background-color']
        variables['color'] = self.customAnimations['cStartValue']
        
        print(
            iUtils.dictMerger(
                variables,
                self.accentStyles['normal']
            )
        )

        self.currentVariables = variables

        self.customStyleSheet = iUtils.readQSS(
            qss=style,
            qssVariables=self.currentVariables,
            output_file=output
        )

        self.setStyleSheet(self.customStyleSheet)
    
    def updateCustomStylesheet(self, backgroundColor, **kwargs):
        c1 = (
            self.customAnimations['cStartValue']
            if self.customAnimations.get('cStartValue')
            else 'black'
        )
        c2 = (
            self.customAnimations['cEndValue']
            if self.customAnimations.get('cEndValue')
            else 'white'
        )

        color = (
            QtGui.QColor(c1)
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor(c2)
        )

        kwargs['color'] = color.name() # color
        kwargs['background-color'] = backgroundColor.name() # background-color

        kwargs = iUtils.dictMerger(self.currentVariables, kwargs)

        self.setCustomStyleSheet(variables=kwargs)

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)


class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._animation = QtCore.QVariantAnimation(
            startValue=QtGui.QColor("#4CAF50"),
            endValue=QtGui.QColor("white"),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._update_stylesheet(QtGui.QColor("white"), QtGui.QColor("black"))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QtGui.QColor("black")
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor("white")
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):

        self.setStyleSheet(
            """
        QPushButton{
            background-color: %s;
            border: none;
            color: %s;
            padding: 16px 32px;
            text-align: center;
            text-decoration: none;
            font-size: 16px;
            margin: 4px 2px;
        }
        """
            % (background.name(), foreground.name())
        )

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)

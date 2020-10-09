from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import qtawesome as qta

import os

from iUtils import iUtils
from iQSS.iGeneral import iAlertVariables
from iGenerals.labels import Label
from iGenerals.buttons import Button
from iQSS import genericVariables
import configurations


'''
	Alerts
'''

class Alert(QtWidgets.QGroupBox):
    def __init__(
        self,
        text:str='Alert',
        width:int=None,
        height:int=None,
        accent:str='primary',
        size:str='normal',
        xFill:bool=False,
        yFill:bool=False,
        customVariables:dict={},
        child:dict={},
        dismissable:bool=True
        ):
        super(Alert, self).__init__()

        if accent:
            self.accent = accent
            self.accentStyles = genericVariables.variables['accents'][self.accent]
            customVariables = iUtils.dictMerger(
            	self.accentStyles['normal'],
            	customVariables,
            )

        self.dismissable = dismissable
        self.xFill = xFill
        self.yFill = yFill

        if not width:
            width = iAlertVariables.sizes[size]['width']
        if not height:
            height = 400

       	self.initialSize = (width, height)

        self.customVariables = iUtils.dictMerger(
            genericVariables.variables['sizes'][size],
            customVariables,
        )

        if not self.xFill:
            self.setMaximumWidth(width)

        if not self.yFill:
            self.setMaximumHeight(height)

        self.child = {
        	'child': Label(
        		text=text,
        		accent=accent,
        		width=width,
        		height=height,
        		customVariables={
        			'padding': '0px'
        		}
        	),
        	'alignment': QtCore.Qt.AlignCenter
        }

       	self.alertLayout = QtWidgets.QVBoxLayout()
       	self.alertLayout.setContentsMargins(0, 0, 0, 0)
       	self.alertLayout.setAlignment(self.child['alignment'])

       	self.setLayout(self.alertLayout)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        
        self.initialization()

    def initialization(self):
    	self.setCustomStyleSheet()
    	self.createDisissmable()
    	self.createChild(self.child)

    def setCustomStyleSheet(
        self,
        style=os.path.join(configurations.QSS_DIR, 'iGeneral/iAlert.qss'),
        variables=iAlertVariables.variables,
        output='iGeneral/compiled/iAlert.css',
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
            boundary='/* Alert */'
        )

        self.setStyleSheet(self.customStyleSheet)

    def createChild(self, child):
    	self.alertLayout.addWidget(child['child'])

    def createDisissmable(self):
    	if self.dismissable:
    		self.dismissButton = Button(
	    		icon='ei.remove',
	    		iconScale=1.0,
	    		iconSize=10,
	    		text='',
	    		accent=self.accent,
	    		width=30,
	    		height=20,
	    		onClick=self.dismiss,
	    		customVariables={
	    			'padding': '0px',
	    			'min-width': '10px',
	    			'min-height': '10px',
	    		}
    		)

    		self.alertLayout.addWidget(
	    		self.dismissButton,
	    		stretch=0,
	    		alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignTop
    		)

    		self._animation = QtCore.QVariantAnimation(
	            startValue=self.height(),
	            endValue=0,
	            valueChanged=self.updateSize,
	            duration=500,
	        )

    def dismiss(self):
    	self._animation.start()

    def updateSize(self, height):
    	self.setMaximumHeight(height)

    def resetSize(self):
    	self.setMaximumHeight(self.initialSize[1])

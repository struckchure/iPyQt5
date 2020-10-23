from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iGenerals.buttons import Button
from iGenerals.labels import Label
from iQSS.iGeneral import iModalsVariables
from iQSS import genericVariables
import configurations


'''
	Modal
'''


class Modal(QtWidgets.QWidget):
	def __init__(
		self,
		width:int=None,
		height:int=None,
		xFill:bool=False,
		yFill:bool=False,
		child:dict={},
		customVariables:dict={}
		):
		super(Modal, self).__init__()

		self.child = iUtils.dictMerger(
			{
				'child': Button(
					accent='dark'
				)
			},
			child
		)
		self.customVariables = iUtils.dictMerger(
			{},
			customVariables
		)

		self._animation = QtCore.QVariantAnimation(
		    startValue=0,
		    endValue=150,
		    valueChanged=self.moveModal,
		    duration=700,
		)

		resolution = QtWidgets.QDesktopWidget().availableGeometry().center()
		self.qr = self.frameGeometry()
		self.qr.moveCenter(resolution)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
		self.setSizePolicy(
			QtWidgets.QSizePolicy(
				QtWidgets.QSizePolicy.MinimumExpanding,
				QtWidgets.QSizePolicy.MinimumExpanding
			)
		)
		self.move(self.qr.center())

		self.xPos = 0

		self.modalLayout = QtWidgets.QVBoxLayout()

		self.setLayout(self.modalLayout)
           
		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createDismissable()
		self.addChild(self.child)

		self._animation.start()

	def setCustomStyleSheet(
	    self,
	    style=os.path.join(configurations.QSS_DIR, 'iGeneral/iModals.qss'),
	    variables=iModalsVariables.variables,
	    output='iGeneral/compiled/iModals.css',
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
	        boundary='/* Modal */'
	    )

	    self.setStyleSheet(self.customStyleSheet)

	def createDismissable(self):
		self.modalLayout.addWidget(
			Button(
				'',
				accent='transparent',
				icon='mdi.close',
				iconColor='black',
				iconScale=1.0,
				iconSize=10,
				size='xss',
				width=30,
	    		height=20,
	    		onClick=self.moveModal
			),
			stretch=0,
			alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignTop
		)

	def addChild(self, child):
		self.modalLayout.addWidget(child['child'])

	def moveModal(self, position):
		endValue = self._animation.endValue()
		startValue = self._animation.startValue()
		currentPosition = self.x(), self.y() - 1

		x = self.x()
		print(f'x: {x} ; y: {self.y()}')
		
		if self.xPos == 0:
			self.xPos = x * 0.85
			
			self.move(QtCore.QPoint(self.xPos, position))

	def retractModal(self):
		if self.xPos == 0:
			self.xPos = x * 0.85

		self.move(QtCore.QPoint(self.xPos, position))
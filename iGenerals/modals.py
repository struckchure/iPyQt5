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
				icon='mdi.close',
				iconColor='black',
				iconScale=1.0,
				iconSize=10,
				size='xss',
				width=30,
	    		height=20,
			),
			stretch=0,
			alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignTop
		)

	def addChild(self, child):
		self.modalLayout.addWidget(child['child'])

	def moveModal(self, position):
		x = self.x()
		if self.xPos == 0:
			self.xPos = x * 0.85

		self.move(QtCore.QPoint(self.xPos, position))


class PopUp(QtWidgets.QWidget):
	def __init__(self, title='School Manager', body='Body', buttonText='&Ok, thanks', parent=None):
		super(PopUp, self).__init__(parent=None)

		self.title = title
		self.body = body
		self.buttonText = buttonText

		self.windowLayout = QtWidgets.QVBoxLayout()

		# qss = utils.readQSS()
		# self.setStyleSheet(qss)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
		self.resize(300, 170)
		self.setMaximumSize(600, 600)
		self.setSizePolicy(
			QtWidgets.QSizePolicy(
				QtWidgets.QSizePolicy.MinimumExpanding,
				QtWidgets.QSizePolicy.MinimumExpanding
			)
		)
		resolution = QtWidgets.QDesktopWidget().availableGeometry().center()
		qr = self.frameGeometry()
		qr.moveCenter(resolution)
		self.move(qr.topLeft())
		self.setLayout(self.windowLayout)

		self.initialization()

	def initialization(self):
		self.titleLabel = QtWidgets.QLabel(self.title)
		self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.titleLabel.setObjectName('popUpTitle')
		self.titleLabel.setFixedSize(200, 40)
		self.windowLayout.addWidget(self.titleLabel, stretch=0, alignment=QtCore.Qt.AlignCenter)

		self.bodyLabel = QtWidgets.QLabel(self.body)
		self.bodyLabel.setObjectName('bodyLabel')
		self.bodyLabel.setAlignment(QtCore.Qt.AlignCenter)
		self.bodyLabel.setWordWrap(True)
		self.bodyLabel.setMaximumSize(500, 500)
		self.windowLayout.addWidget(self.bodyLabel, stretch=0, alignment=QtCore.Qt.AlignCenter)

		self.spacerLabel = QtWidgets.QLabel()
		self.spacerLabel.setFixedWidth(30)
		self.windowLayout.addWidget(self.spacerLabel, stretch=0, alignment=QtCore.Qt.AlignCenter)

		self.closeButton = QtWidgets.QPushButton(self.buttonText)
		self.closeButton.setObjectName('login')
		self.closeButton.setFixedSize(150, 30)
		self.closeButton.clicked.connect(self.close)
		self.windowLayout.addWidget(self.closeButton, stretch=0, alignment=QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

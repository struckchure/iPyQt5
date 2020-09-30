from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iGenerals.buttons import Button
from iQSS.iLayout import iLayoutVariables
from iQSS import genericVariables
import configurations

'''
	Container
'''


class Container(QtWidgets.QGroupBox):
	def __init__(
		self,
        child:dict={},
        position:dict={},
        customVariables:dict={}
		):
		super(Container, self).__init__()

		self.position = position
		self.customVariables = iUtils.dictMerger(
			customVariables
		)
		self.child = iUtils.dictMerger(
			{
				'child': Button()
			},
			child
		)

		self.containerLayout = QtWidgets.QVBoxLayout()

		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)
		self.setLayout(self.containerLayout)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.addChildWidget(self.child['child'])

	def setCustomStyleSheet(
		self,
		style=os.path.join(configurations.QSS_DIR, 'iLayout/iContainer.qss'),
		variables=iLayoutVariables.variables,
		output='iLayout/compiled/iContainer.css',
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
		    boundary='/* Container */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def addChildWidget(self, child):
		if child:
			self.containerLayout.addWidget(child)

	def addLayout(self, child):
		if child:
			self.containerLayout.addLayout(child)


'''
	Row
'''


class Row(QtWidgets.QGroupBox):
	def __init__(
		self
		):
		super(Row, self).__init__()

		self.initialization()

	def initialization(self):
		pass


'''
	Column
'''


class Column(QtWidgets.QGroupBox):
	def __init__(
		self
		):
		super(Column, self).__init__()

		self.initialization()

	def initialization(self):
		pass

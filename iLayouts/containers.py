from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iQSS.iLayout import iLayoutVariables
from iQSS import genericVariables
import configurations

'''
	Container
'''


class Container(QtWidgets.QGroupBox):
	def __init__(
		self
		):
		super(Container, self).__init__()

		self.initialization()

	def initialization(self):
		pass



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

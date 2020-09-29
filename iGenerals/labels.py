from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iQSS.iGeneral import iLabelVariables
from iQSS import genericVariables
import configurations

'''
    NavBar
'''


class Label(QtWidgets.QGroupBox):
	def __init__(
			self,
            text:str='Label',
            width=50,
            child:dict={},
            position:dict={},
            accent:str='primary',
            customVariables:dict={}
		):
		super(Label, self).__init__()

		self.text = text
		self.width = width
		self.child = child
		self.position = position
		self.accent = accent
		self.accentStyles = genericVariables.variables['accents'][self.accent]
		self.customVariables = iUtils.dictMerger(
			self.accentStyles['normal'],
			customVariables
		)
		
		self.navBarLayout = QtWidgets.QHBoxLayout()

		self.label = QtWidgets.QLabel(text)
		self.label.setAlignment(QtCore.Qt.AlignCenter)

		self.navBarLayout.addWidget(
			self.label,
			stretch=0,
			alignment=QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
		)

		self.setLayout(self.navBarLayout)
		self.setMaximumWidth(width)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()

	def setCustomStyleSheet(
			self,
			style=os.path.join(configurations.QSS_DIR, 'iGeneral/iLabel.qss'),
			variables=iLabelVariables.variables,
			output='iGeneral/compiled/iLabel.css',
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
		    boundary='/* Label */'
		)

		self.setStyleSheet(self.customStyleSheet)

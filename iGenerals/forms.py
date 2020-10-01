from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iQSS.iGeneral import iCardVariables
from iQSS import genericVariables
import configurations

'''
    TextInput
'''

class TextInput(QtWidgets.QGroupBox):
	def __init__(
		self,
		width:int=200,
		height:int=50,
		accent:str='primary',
		child:dict={},
		customVariables:dict={}
		):
		super(TextInput, self).__init__()

        self.height = height
        self.width = width
		self.accent = accent
		self.child = iUtils.dictMerger(
			{},
			child
		)
        self.customVariables = customVariables

        self.accentStyles = genericVariables.variables['accents'][self.accent]
        self.customVariables = iUtils.dictMerger(
            self.accentStyles['normal'],
            self.customVariables,
        )

        self.cardLayout = QtWidgets.QVBoxLayout()
        self.cardLayout.setContentsMargins(0, 0, 0, 0)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.setMaximumSize(self.width, self.height)
        self.setLayout(self.cardLayout)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()

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


'''
    ImageInput
'''


'''
    FileInput
'''

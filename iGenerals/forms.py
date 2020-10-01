from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import qtawesome as qta

import os

from iUtils import iUtils
from iQSS.iGeneral import iFormVariables
from iGenerals.labels import Label
from iQSS import genericVariables
import configurations

'''
    TextInput
'''

class TextInput(QtWidgets.QGroupBox):
	def __init__(
		self,
		width:int=200,
		height:int=60,
		child:dict={},
		customVariables:dict={},
		placeHolderText:str=None,
		password:bool=False
		):
		super(TextInput, self).__init__()

		self.height = height
		self.width = width
		self.child = iUtils.dictMerger(
			{
				'icon': {
					'icon': 'fa.user',
					'color': 'black',
					'scale': 0.9
				},
				'label': {
					'text': 'Username',
					'font-size': '15px'
				},
				'direction': QtWidgets.QBoxLayout.TopToBottom
			},
			child
		)
		self.customVariables = customVariables
		self.placeHolderText = placeHolderText
		self.password = password

		self.customVariables = iUtils.dictMerger(
		    self.customVariables
		)

		self.inputLayout = QtWidgets.QBoxLayout(self.child['direction'])
		self.inputLayout.setAlignment(QtCore.Qt.AlignTop)
		self.inputLayout.setContentsMargins(0, 0, 0, 0)
		self.inputLayout.setSpacing(0)

		self.setSizePolicy(
		    QtWidgets.QSizePolicy.Expanding,
		    QtWidgets.QSizePolicy.Expanding
		)
		self.setMaximumSize(self.width, self.height)
		self.setLayout(self.inputLayout)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createInput(self.child['icon'], self.child['label'])

	def setCustomStyleSheet(
		self,
		style=os.path.join(configurations.QSS_DIR, 'iGeneral/iForm.qss'),
		variables=iFormVariables.variables,
		output='iGeneral/compiled/iForm.css',
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
		    boundary='/* TextInput */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createInput(
		self,
		icon,
		label
		):
		if label:
			inputLabel = Label(
				text=label['text'],
				height=80,
				width=200,
				customVariables={
					'background-color': 'rgba(0, 0, 0, 0)',
					'color': 'black',
					'padding': '0',
					'margin': '0',
					'border-width': '0',
					'min-height': '35px',
					'font-size': label['font-size']
				}
			)
			self.inputLayout.addWidget(inputLabel)

		self.textInputLayout = QtWidgets.QHBoxLayout()
		self.textInputLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.textInputLayout.setContentsMargins(0, 0, 0, 0)
		self.textInputLayout.setSpacing(0)

		if icon:
			self.iconLabel = qta.IconWidget(
                icon['icon'],
                color=icon['color'],
                options=[
					{
						'scale_factor': icon['scale']
					}
				]
            )
			self.iconLabel.setObjectName('iconLabel')
			self.textInputLayout.addWidget(self.iconLabel)

		self.textInput = QtWidgets.QLineEdit()
		self.textInput.setMaximumSize(self.width, self.height)
		self.textInputLayout.addWidget(self.textInput)

		if self.placeHolderText:
			self.textInput.setPlaceholderText(self.placeHolderText)

		if self.password:
			self.textInput.setEchoMode(QtWidgets.QLineEdit.Password)

		self.inputLayout.addLayout(self.textInputLayout)

	def text(self):
		return self.textInput.text()


'''
    ImageInput
'''


'''
    FileInput
'''


'''
	Form
'''

class Form(QtWidgets.QGroupBox):
	def __init__(
		self,
		grid:bool=False,
		width:int=400,
		height:int=600,
		children:dict={},
		customVariables:dict={},
		onSubmit=None
		):
		super(Form, self).__init__()

		self.grid = grid
		self.customVariables = iUtils.dictMerger(
			{
				'border-width': '0',
				'padding': '20px'
			},
		    customVariables
		)
		self.children = iUtils.dictMerger(
			{
				'children': [
					TextInput(
					    child={
					        'icon': {
					            'icon': 'fa.user',
					            'color': 'black',
					            'scale': 0.9
					        },
					        'label': {
					            'text': 'Username',
					            'font-size': '12px'
					        },
					        'direction': QtWidgets.QBoxLayout.TopToBottom
					    },
					    width=300,
					    placeHolderText='John',
					    customVariables={
					        'font-size': '12px',
					        'border-color': 'grey',
					        'border-radius': '6px',
					    },
					),
					TextInput(
					    child={
					        'icon': {
					            'icon': 'fa.key',
					            'color': 'black',
					            'scale': 0.9
					        },
					        'label': {
					            'text': 'Password',
					            'font-size': '12px'
					        },
					        'direction': QtWidgets.QBoxLayout.TopToBottom
					    },
					    password=True,
					    width=300,
					    placeHolderText='keep it secret',
					    customVariables={
					        'font-size': '12px',
					        'border-color': 'grey',
					        'border-radius': '6px',
					    },
					)
				],
				'spacing': 0,
				'alignment': QtCore.Qt.AlignCenter
			},
			children
		)
		self.onSubmit = onSubmit

		if grid:
			self.formLayout = QtWidgets.QGridLayout()
		else:
			self.formLayout = QtWidgets.QVBoxLayout()

		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setSpacing(self.children['spacing'])
		self.formLayout.setAlignment(self.children['alignment'])

		self.setLayout(self.formLayout)
		self.setMaximumSize(width, height)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createForm(self.children['children'])

	def setCustomStyleSheet(
		self,
		style=os.path.join(configurations.QSS_DIR, 'iGeneral/iForm.qss'),
		variables=iFormVariables.variables,
		output='iGeneral/compiled/iForm.css',
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
		    boundary='/* Form */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createForm(self, children):
		for child in children:
			self.formLayout.addWidget(child)

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import qtawesome as qta

import os

from iUtils import iUtils
from iQSS.iGeneral import iFormVariables
from iGenerals.alerts import Alert
from iGenerals.buttons import Button
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
		password:bool=False,
		required=False
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
		self.required = required

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


class ImageInput(QtWidgets.QGroupBox):
	def __init__(
		self,
		width:int=200,
		height:int=60,
		child:dict={},
		customVariables:dict={},
		placeHolderText:str=None,
		required=False
		):
		super(ImageInput, self).__init__()

		self.height = height
		self.width = width
		self.child = iUtils.dictMerger(
			{
				'icon': {
					'icon': 'fa.image',
					'color': 'black',
					'scale': 0.9
				},
				'label': {
					'text': 'Image',
					'font-size': '15px'
				},
				'direction': QtWidgets.QBoxLayout.TopToBottom
			},
			child
		)
		self.customVariables = customVariables
		self.placeHolderText = placeHolderText
		self.required = required

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
		    boundary='/* ImageInput */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createInput(self, icon, label):
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

		self.imageInputLayout = QtWidgets.QHBoxLayout()
		self.imageInputLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.imageInputLayout.setContentsMargins(0, 0, 0, 0)
		self.imageInputLayout.setSpacing(0)

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
			self.imageInputLayout.addWidget(self.iconLabel, stretch=0, alignment=QtCore.Qt.AlignLeft)

		self.imageInput = QtWidgets.QLineEdit()
		self.imageInput.setReadOnly(True)
		self.imageInput.setMaximumSize(self.width, self.height)
		if self.placeHolderText:
			self.imageInput.setPlaceholderText(self.placeHolderText)
		self.imageInputLayout.addWidget(self.imageInput)

		self.imageInputButton = Button(
			text='...',
			accent='secondary',
			width=30,
			onClick=self.select_image_dialog
		)
		self.imageInputButton.setObjectName('inputButton')
		self.imageInputButton.setMaximumSize(self.width, self.height)
		self.imageInputLayout.addWidget(self.imageInputButton, stretch=0, alignment=QtCore.Qt.AlignRight)

		self.inputLayout.addLayout(self.imageInputLayout)

	def text(self):
		return self.imageInput.text()
	
	def select_image_dialog(self):
		self.file_dialog_window = QtWidgets.QFileDialog.getOpenFileName(self, 'Select image', 'C\\', 'Image (*.jpg *.png *.jpeg)')
		self.image_path = self.file_dialog_window[0]
		self.imageInput.setText(self.image_path)



'''
    FileInput
'''

class FileInput(QtWidgets.QGroupBox):
	def __init__(
		self,
		width:int=200,
		height:int=60,
		child:dict={},
		customVariables:dict={},
		placeHolderText:str=None,
		extensions:list=['csv', 'mp4', 'mkv', 'mp3', 'png', 'css', 'qss'],
		required=False
		):
		super(FileInput, self).__init__()

		self.height = height
		self.width = width
		self.child = iUtils.dictMerger(
			{
				'icon': {
					'icon': 'ei.file-new',
					'color': 'black',
					'scale': 0.9
				},
				'label': {
					'text': 'File',
					'font-size': '15px'
				},
				'direction': QtWidgets.QBoxLayout.TopToBottom
			},
			child
		)
		self.customVariables = customVariables
		self.placeHolderText = placeHolderText
		self.extensions = ''
		self.required = required

		for extension in extensions:
			self.extensions += f'*.{extension} '

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
		    boundary='/* FileInput */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createInput(self, icon, label):
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

		self.fileInputLayout = QtWidgets.QHBoxLayout()
		self.fileInputLayout.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
		self.fileInputLayout.setContentsMargins(0, 0, 0, 0)
		self.fileInputLayout.setSpacing(0)

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
			self.fileInputLayout.addWidget(self.iconLabel, stretch=0, alignment=QtCore.Qt.AlignLeft)

		self.fileInput = QtWidgets.QLineEdit()
		self.fileInput.setReadOnly(True)
		self.fileInput.setMaximumSize(self.width, self.height)
		if self.placeHolderText:
			self.fileInput.setPlaceholderText(self.placeHolderText)
		self.fileInputLayout.addWidget(self.fileInput)

		self.fileInputButton = Button(
			text='...',
			accent='secondary',
			width=30,
			onClick=self.select_image_dialog
		)
		self.fileInputButton.setObjectName('inputButton')
		self.fileInputButton.setMaximumSize(self.width, self.height)
		self.fileInputLayout.addWidget(self.fileInputButton, stretch=0, alignment=QtCore.Qt.AlignRight)

		self.inputLayout.addLayout(self.fileInputLayout)

	def text(self):
		return self.fileInput.text()
	
	def select_image_dialog(self):
		extensions = self.extensions
		self.file_dialog_window = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', 'C\\', f'File ({extensions})')
		self.image_path = self.file_dialog_window[0]
		self.fileInput.setText(self.image_path)


'''
	Form
'''

class Form(QtWidgets.QGroupBox):
	def __init__(
		self,
		grid:bool=False,
		width:int=400,
		height:int=900,
		accent:str='transparent',
		children:dict={},
		customVariables:dict={},
		onSubmit=None
		):
		super(Form, self).__init__()

		self.grid = grid
		self.accent = accent
		self.onSubmit = self.defaultOnSubmit
		self.accentStyles = genericVariables.variables['accents'][self.accent]
		self.customVariables = iUtils.dictMerger(
			{
				'border-width': '0',
				'padding': '20px'
			},
			self.accentStyles['normal'],
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
					    },
					    required=True
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
					    },
					    required=True
					),
					ImageInput(
						child={
					        'label': {
					            'text': 'Image',
					            'font-size': '12px'
					        },
					        'direction': QtWidgets.QBoxLayout.TopToBottom
					    },
					    width=300,
					    placeHolderText='choose image ...',
					    customVariables={
					        'font-size': '12px',
					        'border-color': 'grey',
					    },
					),
					FileInput(
						child={
					        'label': {
					            'text': 'File',
					            'font-size': '12px'
					        },
					        'direction': QtWidgets.QBoxLayout.TopToBottom
					    },
					    width=300,
					    placeHolderText='choose file ...',
					    customVariables={
					        'font-size': '12px',
					        'border-color': 'grey',
					    },
					),
				],
				'grids': [
					(0, 0, 1, 0),
					(1, 0, 1, 0),
					(2, 0, 1, 0),
					(3, 0, 1, 0),
				],
				'footer': Button(
					'Register',
					accent='dark',
					onClick=self.onSubmit,
					size='lg',
					width=300
				),
				'errorMessages':{
					'fieldErrors': [
						Alert(
							accent='danger',
							text='Username field is required',
		                    width=900,
		                    height=900,
						),
						Alert(
							accent='danger',
							text='Password field is required',
							width=900,
		                    height=900,
						),
						Alert(
							accent='danger',
							text='Image field is required',
							width=900,
		                    height=900,
						),
						Alert(
							accent='danger',
							text='Image field is required',
							width=900,
		                    height=900,
						),
					],
					'validationError': [],
				},
				'spacing': 5,
				'alignment': QtCore.Qt.AlignCenter
			},
			children
		)

		self.mainFormLayout = QtWidgets.QVBoxLayout()
		self.mainFormLayout.setContentsMargins(0, 0, 0, 0)
		self.mainFormLayout.setSpacing(5)
		self.mainFormLayout.setAlignment(QtCore.Qt.AlignCenter)

		self.setLayout(self.mainFormLayout)
		self.setMaximumSize(width, height)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		if grid:
			self.formLayout = QtWidgets.QGridLayout()
		else:
			self.formLayout = QtWidgets.QVBoxLayout()

		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setSpacing(self.children['spacing'])
		self.formLayout.setAlignment(self.children['alignment'])

		self.mainFormLayout.addLayout(self.formLayout)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createForm(self.children)

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
		if self.grid:
			x, y, xh, yh = 0, 0, 0, 0
			for child in children['children']:
				x, y, xh, yh = children['grids'][children['children'].index(child)]
				self.formLayout.addWidget(
					child,
					x,
					y,
					xh,
					yh
				)
			self.formLayout.addWidget(
				children['footer'],
				x + 1,
				y,
				xh,
				yh
			)
		else:
			for child in children['children']:
				self.formLayout.addWidget(child)
			self.formLayout.addWidget(children['footer'])

	def defaultOnSubmit(self):
		fieldValues = []

		for child in self.children['children']:
			if child.required:
				error = self.children['errorMessages']['fieldErrors'][self.children['children'].index(child)]
				if not child.text():
					error.resetSize()

					self.mainFormLayout.insertWidget(
						0,
						error,
						stretch=0,
						alignment=QtCore.Qt.AlignCenter
					)

					fieldValues = None

					break
				else:
					if error.height() > 0:
						error.dismiss()
			else:
				fieldValues.append(child.text())

		return fieldValues

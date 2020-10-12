from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iGenerals.buttons import Button
from iGenerals.labels import Label
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
				'child': QtWidgets.QVBoxLayout()
			},
			child
		)

		self.containerLayout = QtWidgets.QVBoxLayout()

		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

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
			self.setLayout(child)

	def addLayout(self, child):
		if child:
			self.containerLayout.addLayout(child)


'''
	Scroll
'''

class Scroll(QtWidgets.QScrollArea):
	def __init__(
		self,
        child:dict={},
        customVariables:dict={}
		):
		super(Scroll, self).__init__()

		self.customVariables = iUtils.dictMerger(
			customVariables
		)
		self.child = iUtils.dictMerger(
			{
				'child': Button()
			},
			child
		)

		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)
		self.setWidgetResizable(True)

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
		    boundary='/* Scroll */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def addChildWidget(self, child):
		if child:
			self.setWidget(child)


'''
	Row
'''


class Row(QtWidgets.QGroupBox):
	def __init__(
		self,
		accent:str='dark',
		children:dict={},
		customVariables:dict={},
		size:str='lg',
		width:int=None,
		height:int=None,
		xFill:bool=False,
		yFill:bool=False,
		):
		super(Row, self).__init__()

		self.accent = accent
		self.accentStyles = genericVariables.variables['accents'][self.accent]['normal']
		self.customVariables = iUtils.dictMerger(
			self.accentStyles,
			customVariables
		)
		self.children = iUtils.dictMerger(
			{
				'children': [],
				'spacing': 0,
				'alignment': QtCore.Qt.AlignLeft
			},
			children
		)
		self.xFill = xFill
		self.yFill = yFill
		self.size = size

		if not width:
			width = genericVariables.sizes[size]['width'] * 100
		if not height:
			height = genericVariables.sizes[size]['height']

		if width:
			self.setMaximumWidth(width)

		if height:
			self.setMaximumHeight(height)

		self.rowLayout = QtWidgets.QGridLayout()
		self.rowLayout.setContentsMargins(0, 0, 0, 0)
		self.rowLayout.setSpacing(self.children['spacing'])
		self.rowLayout.setAlignment(self.children['alignment'])

		self.setLayout(self.rowLayout)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createChildren(self.children)

	def setCustomStyleSheet(
		self,
		style=os.path.join(configurations.QSS_DIR, 'iLayout/iLayout.qss'),
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
		    boundary='/* Row */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createChildren(self, children):
		x, y = 0, 0
		for child in children['children']:
			self.rowLayout.addWidget(
				child,
				x,
				y,
				# stretch=0,
				alignment=children['alignment']
			)
			y += 1


'''
	Column
'''


class Column(QtWidgets.QGroupBox):
	def __init__(
		self,
		accent:str='dark',
		children:dict={},
		customVariables:dict={},
		size:str='lg',
		width:int=None,
		height:int=None,
		xFill:bool=False,
		yFill:bool=False,
		):
		super(Column, self).__init__()

		self.accent = accent
		self.accentStyles = genericVariables.variables['accents'][self.accent]['normal']
		self.customVariables = iUtils.dictMerger(
			self.accentStyles,
			customVariables
		)
		self.children = iUtils.dictMerger(
			{
				'children': [],
				'spacing': 0,
				'alignment': QtCore.Qt.AlignLeft
			},
			children
		)
		self.xFill = xFill
		self.yFill = yFill
		self.size = size

		if not width:
			width = genericVariables.sizes[size]['width']
		if not height:
			height = 900

		if not self.xFill:
			self.setMaximumWidth(width)

		if not self.yFill:
			self.setMaximumHeight(height)

		self.columnLayout = QtWidgets.QVBoxLayout()
		self.columnLayout.setContentsMargins(0, 0, 0, 0)
		self.columnLayout.setSpacing(self.children['spacing'])
		self.columnLayout.setAlignment(self.children['alignment'])

		self.setLayout(self.columnLayout)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createChildren(self.children)

	def setCustomStyleSheet(
		self,
		style=os.path.join(configurations.QSS_DIR, 'iLayout/iLayout.qss'),
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
		    boundary='/* Column */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createChildren(self, children):
		for child in children['children']:
			self.addChild(child)

	def addChild(self, child):
		self.columnLayout.addWidget(child)


'''
	Table
'''


class Table(QtWidgets.QGroupBox):
	def __init__(
		self,
		accent:str='dark',
		child:dict={},
		customVariables:dict={},
		width:int=None,
		height:int=None,
		):
		super(Table, self).__init__()

		self.accent = accent
		self.accentStyles = genericVariables.variables['accents'][self.accent]['normal']
		self.customVariables = iUtils.dictMerger(
			self.accentStyles,
			{
				'padding': '0px',
				'margin': '0px',
			},
			customVariables,
		)
		self.child = iUtils.dictMerger(
			{
				'header': {
					'children': [
						Column(
							xFill=False,
							yFill=True,
							width=60,
							accent=self.accent,
							children={
								'children': [
									Label(
										text='S/N',
										accent=self.accent,
										xFill=False,
										yFill=True,
										width=60,
										height=100,
										customVariables={
											'padding': '0px',
											'min-height': '0px',
											'min-width': '0px',
											'background-color': 'rgba(0, 0, 0, 0)'
										}
									),
								]
							}
						), # Serial Number
						Column(
							xFill=False,
							yFill=True,
							width=900,
							accent=self.accent,
							children={
								'children': [
									Label(
										text='First name',
										accent=self.accent,
										xFill=True,
										yFill=True,
										customVariables={
											'padding': '0px',
											'min-height': '0px',
											'background-color': 'rgba(0, 0, 0, 0)'
										}
									),
								]
							}
						), # First name
						Column(
							width=900,
							xFill=False,
							yFill=True,
							accent=self.accent,
							children={
								'children': [
									Label(
										text='Last name',
										accent=self.accent,
										xFill=True,
										yFill=True,
										customVariables={
											'padding': '0px',
											'min-height': '0px',
											'background-color': 'rgba(0, 0, 0, 0)'
										}
									),
								]
							}
						) # Last name
					],
				},
				'body': {
					'children': [
						[
							Label(
								text='1',
								accent=self.accent,
								xFill=True,
								yFill=True,
								width=100,
								height=100,
								customVariables={
									'padding': '0px',
									'min-height': '0px',
									'min-width': '0px',
									'background-color': 'rgba(0, 0, 0, 0)'
								}
							),
							Label(
								text='John',
								accent=self.accent,
								xFill=True,
								yFill=True,
								customVariables={
									'padding': '0px',
									'min-height': '0px',
									'background-color': 'rgba(0, 0, 0, 0)'
								}
							),
							Label(
								text='Doe',
								accent=self.accent,
								xFill=True,
								yFill=True,
								customVariables={
									'padding': '0px',
									'min-height': '0px',
									'background-color': 'rgba(0, 0, 0, 0)'
								}
							),
						],
						[
							Label(
								text='3',
								accent=self.accent,
								xFill=True,
								yFill=True,
								width=100,
								height=100,
								customVariables={
									'padding': '0px',
									'min-height': '0px',
									'min-width': '0px',
									'background-color': 'rgba(0, 0, 0, 0)'
								}
							),
							Label(
								text='Mary',
								accent=self.accent,
								xFill=True,
								yFill=True,
								customVariables={
									'padding': '0px',
									'min-height': '0px',
									'background-color': 'rgba(0, 0, 0, 0)'
								}
							),
							Label(
								text='Jane',
								accent=self.accent,
								xFill=True,
								yFill=True,
								customVariables={
									'padding': '0px',
									'min-height': '0px',
									'background-color': 'rgba(0, 0, 0, 0)'
								}
							),
						],
					],
					'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
				},
				'footer': {},
				'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
			},
			child
		)
		self.width = width
		self.height = height

		self.tableLayout = QtWidgets.QGridLayout()
		self.tableLayout.setContentsMargins(0, 0, 0, 0)
		self.tableLayout.setSpacing(0)

		if self.width:
			self.setMaximumWidth(self.width)

		if self.height:
			self.setMaximumWidth(self.height)

		self.setLayout(self.tableLayout)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createHeader(self.child)
		self.createBody(self.child)
		self.createFooter(self.child)

	def setCustomStyleSheet(
		self,
		style=os.path.join(configurations.QSS_DIR, 'iLayout/iLayout.qss'),
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
		    boundary='/* Table */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createHeader(self, child):
		header = child['header']['children']

		self.addHeaderItems(header)

	def addHeaderItems(self, items):
		x, y = 0, 0
		for item in items:
			self.tableLayout.addWidget(item, x, y)
			y += 1

	def createBody(self, child):
		body = child['body']

		stripe = 0

		for items in body['children']:
			if stripe % 2 == 0:
				self.addBodyItems(items, child, stripe=True)
			else:
				self.addBodyItems(items, child, stripe=False)

			stripe += 1

	def addBodyItems(self, items, child, stripe):
		accent = self.accent
		body = child['body']

		for item in items:
			index = items.index(item)
			header = child['header']['children'][index]

			if stripe:
				customVariables = genericVariables.variables['accents'][accent]['hover']
				item.customVariables = customVariables
	
			item.setCustomStyleSheet()

			header.addChild(item)

	def createFooter(self, child):
		pass

	def addFooterItems(self, items):
		pass

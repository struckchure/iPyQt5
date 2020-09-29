from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iQSS.iLayout import iLayoutVariables
from iQSS import genericVariables
from iGenerals.labels import Label
from iGenerals.buttons import Button
import configurations

'''
    NavBar
'''


class NavBar(QtWidgets.QGroupBox):
	def __init__(
			self,
            child:dict={},
            position:dict={},
            height:int=45,
            accent:str='primary',
            customVariables:dict={}
		):
		super(NavBar, self).__init__()

		self.position = position
		self.accent = accent
		self.accentStyles = genericVariables.variables['accents'][self.accent]
		self.customVariables = iUtils.dictMerger(
			self.accentStyles['normal'],
			customVariables
		)
		size = 'normal'
		w, h = 100, 50
		self.child = iUtils.dictMerger(
			{
				'title': {
					'child': Label(
						text='iPyQt5',
						width=100,
						accent=self.accent
					),
					'alignment': QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft
				},
				'body': {
					'children': [
						Button(
		                    'Home',
		                    accent=self.accent,
		                    size=size,
		                    width=w,
		                    height=h
		                ),
		                Button(
		                    'Gallery',
		                    accent=self.accent,
		                    size=size,
		                    width=w,
		                    height=h
		                ),
		                Button(
		                    'About',
		                    accent=self.accent,
		                    size=size,
		                    width=w,
		                    height=h
		                ),
		                Button(
		                    'Account',
		                    accent=self.accent,
		                    size=size,
		                    width=w,
		                    height=h
		                ),
					],
					'alignment': QtCore.Qt.AlignCenter
				},
				'end': {
					'children': [
						Button(
		                    'M',
		                    accent=self.accent,
		                    size=size,
		                    width=20,
		                    height=20
		                ),
		                Button(
		                    'S',
		                    accent=self.accent,
		                    size=size,
		                    width=20,
		                    height=20
		                ),
					],
					'alignment': QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight
				},
			},
			child
		)
		
		self.navBarLayout = QtWidgets.QHBoxLayout()
		self.navBarLayout.setContentsMargins(0, 0, 0, 0)

		self.navTitleLayout = QtWidgets.QHBoxLayout()
		self.navTitleLayout.setAlignment(self.child['title']['alignment'])
		self.navTitleLayout.setSpacing(0)
		self.navTitleLayout.setContentsMargins(0, 0, 0, 0)
		self.navBarLayout.addLayout(self.navTitleLayout)

		self.navBodyLayout = QtWidgets.QHBoxLayout()
		self.navBodyLayout.setAlignment(self.child['body']['alignment'])
		self.navBodyLayout.setSpacing(0)
		self.navBodyLayout.setContentsMargins(0, 0, 0, 0)
		self.navBarLayout.addLayout(self.navBodyLayout)

		self.navEndLayout = QtWidgets.QHBoxLayout()
		self.navEndLayout.setAlignment(self.child['end']['alignment'])
		self.navEndLayout.setSpacing(0)
		self.navEndLayout.setContentsMargins(0, 0, 0, 0)
		self.navBarLayout.addLayout(self.navEndLayout)

		self.setLayout(self.navBarLayout)
		self.setMaximumHeight(height)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createTitle()
		self.createBody()
		self.createEnd()

	def setCustomStyleSheet(
		self,
		style=os.path.join(configurations.QSS_DIR, 'iLayout/iLayout.qss'),
		variables=iLayoutVariables.variables,
		output='iLayout/compiled/iLayout.css',
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
		    boundary='/* NavBar */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createTitle(self):
		title = self.child['title']
		self.navTitleLayout.addWidget(
			title['child'],
			# stretch=0,
			# alignment=title['alignment']
		)

	def createBody(self):
		body = self.child['body']
		children = body['children']

		for child in children:
			self.navBodyLayout.addWidget(
				child
			)

	def createEnd(self):
		end = self.child['end']
		children = end['children']

		for child in children:
			self.navEndLayout.addWidget(
				child
			)


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

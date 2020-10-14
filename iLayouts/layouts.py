from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui

import os

from iUtils import iUtils
from iQSS.iLayout import iLayoutVariables
from iQSS import genericVariables
from iGenerals.labels import Label
from iGenerals.buttons import Button
from iGenerals.cards import CardHeader, CardBody, CardFooter
from .containers import Container
import configurations

'''
    NavBar
'''


class NavBar(QtWidgets.QGroupBox):
	def __init__(
		self,
        child:dict={},
        position:dict={},
        height:int=50,
        accent:str='primary',
        customVariables:dict={},
		shadowWidth:int=30,
		xIndex:float=0,
		yIndex:float=0
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
		w, h = 100, height
		self.child = iUtils.dictMerger(
			{
				'title': {
					'child': Label(
						text='iPyQt5',
						width=w,
						height=h,
						accent=self.accent,
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
		                    '',
		                    icon='mdi.bell-outline',
		                    iconColor='white',
		                    accent=self.accent,
		                    size=size,
		                    width=10,
		                    height=h
		                ),
						Button(
		                    '',
		                    icon='mdi.account-circle',
		                    iconColor='white',
		                    accent=self.accent,
		                    size=size,
		                    width=10,
		                    height=h
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

		self.graphicsEffect = QtWidgets.QGraphicsDropShadowEffect()
		self.graphicsEffect.setBlurRadius(shadowWidth)
		self.graphicsEffect.setXOffset(xIndex)
		self.graphicsEffect.setYOffset(yIndex)
		self.graphicsEffect.setColor(QtGui.QColor(0, 0, 0, 150))

		self.setGraphicsEffect(self.graphicsEffect)

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
	SideBar
'''


class SideBar(QtWidgets.QGroupBox):
	def __init__(
		self,
        child:dict={},
        position:dict={},
        width:int=300,
        collapseWidth:int=60,
        accent:str='primary',
        customVariables:dict={},
		shadowWidth:int=50,
		xIndex:float=0,
		yIndex:float=0
		):
		super(SideBar, self).__init__()

		self.position = position
		self.width_ = width
		self.sideBarMaxWidth = width
		self.collapseWidth = collapseWidth
		self.accent = accent
		self.accentStyles = genericVariables.variables['accents'][self.accent]
		self.customVariables = iUtils.dictMerger(
			self.accentStyles['normal'],
			customVariables
		)
		self.child = iUtils.dictMerger(
			{
				'title': {
					'alignment': QtCore.Qt.AlignTop
				},
				'body': {
					'children': [
						Button(
							text='Dashboard',
							icon='fa.tachometer',
							accent=self.accent,
							size='lg',
							customVariables={
								'padding': '10px 10px',
								'margin': '0px',
								'min-width': '0px',
								'text-align': 'left'
							}
						),
						Button(
							text='Profile',
							icon='fa.user',
							accent=self.accent,
							size='lg',
							customVariables={
								'padding': '10px 10px',
								'margin': '0px',
								'min-width': '0px',
								'text-align': 'left'
							}
						),
						Button(
							text='Settings',
							icon='fa.cog',
							accent=self.accent,
							size='lg',
							customVariables={
								'padding': '10px 10px',
								'margin': '0px',
								'min-width': '0px',
								'text-align': 'left'
							}
						),
					],
					'alignment': QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft
				},
				'end': {
					'alignment': QtCore.Qt.AlignBottom
				}
			},
			child
		)

		self.sideBarLayout = QtWidgets.QVBoxLayout()
		self.sideBarLayout.setAlignment(QtCore.Qt.AlignTop)
		self.sideBarLayout.setContentsMargins(0, 0, 0, 0)

		self.sideTitleLayout = QtWidgets.QVBoxLayout()
		self.sideTitleLayout.setAlignment(self.child['title']['alignment'])
		self.sideTitleLayout.setSpacing(0)
		self.sideTitleLayout.setContentsMargins(0, 0, 0, 0)
		self.sideBarLayout.addLayout(self.sideTitleLayout)

		self.sideBodyLayout = QtWidgets.QVBoxLayout()
		self.sideBodyLayout.setAlignment(self.child['body']['alignment'])
		self.sideBodyLayout.setSpacing(0)
		self.sideBodyLayout.setContentsMargins(0, 0, 0, 0)
		self.sideBarLayout.addLayout(self.sideBodyLayout)

		self.sideEndLayout = QtWidgets.QVBoxLayout()
		self.sideEndLayout.setAlignment(self.child['end']['alignment'])
		self.sideEndLayout.setSpacing(0)
		self.sideEndLayout.setContentsMargins(0, 0, 0, 0)
		self.sideBarLayout.addLayout(self.sideEndLayout)

		self.graphicsEffect = QtWidgets.QGraphicsDropShadowEffect()
		self.graphicsEffect.setBlurRadius(shadowWidth)
		self.graphicsEffect.setXOffset(xIndex)
		self.graphicsEffect.setYOffset(yIndex)
		self.graphicsEffect.setColor(QtGui.QColor(0, 0, 0, 150))

		self.setGraphicsEffect(self.graphicsEffect)
		self.setLayout(self.sideBarLayout)
		self.setMaximumWidth(width)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		self.initialization()
		self.toggleMenu()

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
		    boundary='/* SideBar */'
		)

		self.setStyleSheet(self.customStyleSheet)

	def createTitle(self):
		self.sideTitleLayout.addWidget(
			CardHeader(
				accent='dark'
			)
		)
		
	def createBody(self):
		for child in self.child['body']['children']:
			self.sideBodyLayout.addWidget(
				child
			)

	def createEnd(self):
		self.sideEndLayout.addWidget(
			CardFooter(
				accent=self.accent,
			)
		)

	def toggleMenu(self):
		maxWidth=self.sideBarMaxWidth - 100
		enable = self.isEnabled()
		collapseWidth = self.collapseWidth

		if enable:
			width = self.width()
			maxExtend = maxWidth
			standard = collapseWidth

			if width == collapseWidth:
				widthExtended = maxExtend
			else:
				widthExtended = standard

			self.animation = QtCore.QPropertyAnimation(self, b"minimumWidth")
			self.animation.setDuration(300)
			self.animation.setStartValue(width)
			self.animation.setEndValue(widthExtended)
			self.animation.valueChanged.connect(self.updateSize)
			self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animation.start()

	def updateSize(self, value):
		self.width_ = value
		self.setMaximumWidth(value)

	def enterEvent(self, event):
		self.toggleMenu()
		super().enterEvent(event)

	def leaveEvent(self, event):
		self.toggleMenu()
		super().leaveEvent(event)


'''
	Page
'''


class Page(QtWidgets.QWidget):
	def __init__(
		self,
		child:dict={},
		customVariables:dict={},
		showOnStart:bool=True
		):
		super(Page, self).__init__()

		self.showOnStart = showOnStart
		self.customVariables = iUtils.dictMerger(
			{
				'margin': '0',
				'padding': '0',
				'border-width': '0'
			},
			customVariables
		)
		self.child = iUtils.dictMerger(
			{
				'sideBar': {
					'child': SideBar(
						accent='dark'
					),
					'alignment': QtCore.Qt.AlignTop
				},
				'navBar': {
					'child': NavBar(
						accent='dark'
					),
					'alignment': QtCore.Qt.AlignCenter
				},
				'body': {
					'children': [
						Container(
							child={
								'child': QtWidgets.QVBoxLayout()
							}
						),
					],
					'alignment': QtCore.Qt.AlignBottom
				},
				'footer': {
					'child': '',
					'alignment': QtCore.Qt.AlignBottom
				}
			},
			child
		)

		self.pageLayout = QtWidgets.QHBoxLayout()
		self.pageLayout.setContentsMargins(0, 0, 0, 0)
		self.pageLayout.setSpacing(0)

		self.leftPageLayout = QtWidgets.QVBoxLayout()
		self.leftPageLayout.setContentsMargins(0, 0, 0, 0)
		self.leftPageLayout.setSpacing(0)
		self.pageLayout.addLayout(self.leftPageLayout)

		self.rightPageLayout = QtWidgets.QVBoxLayout()
		self.rightPageLayout.setAlignment(QtCore.Qt.AlignTop)
		self.rightPageLayout.setContentsMargins(0, 0, 0, 0)
		self.rightPageLayout.setSpacing(0)
		self.pageLayout.addLayout(self.rightPageLayout)

		self.setLayout(self.pageLayout)
		self.setSizePolicy(
			QtWidgets.QSizePolicy.Expanding,
			QtWidgets.QSizePolicy.Expanding
		)

		if self.showOnStart:
			self.initialization()

	def initialization(self):
		self.setCustomStyleSheet()
		self.createSideBar()
		self.createNavBar()
		self.createBody()
		self.createFooter()

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
		    boundary='/* Page */'
		)

	def createSideBar(self):
		self.leftPageLayout.addWidget(
			self.child['sideBar']['child']
		)

	def createNavBar(self):
		self.rightPageLayout.addWidget(
			self.child['navBar']['child']
		)

	def createBody(self):
		for child in self.child['body']['children']:
			self.rightPageLayout.addWidget(
				child
			)

	def createFooter(self):
		pass

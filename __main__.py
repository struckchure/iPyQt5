from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

from iGenerals.buttons import Button
from iGenerals.cards import Card
from iLayouts.layouts import NavBar, SideBar, Page
from iLayouts.containers import Container, Scroll
from iGenerals.labels import Label
from iQSS import genericVariables


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.accent = 'dark'
        accents = genericVariables.variables['accents']

        x, y = 0, 0

        self.leftLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addLayout(self.leftLayout)

        self.rightLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.addLayout(self.rightLayout)

        self.leftLayout.addWidget(
            SideBar(
                accent='dark',
                customVariables={
                    # 'max-width': '80px'
                }
            )
        )

        for accent in accents:
            w, h = 100, 50
            size = 'lg'
            self.rightLayout.addWidget(
                NavBar(
                    accent=accent,
                    child={
                        'title': {
                            'child': Label(
                                text='NavBar',
                                width=100,
                                accent=accent
                            ),
                            'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
                        },
                        'body': {
                            'children': [
                                Button(
                                    'Home',
                                    accent=accent,
                                    size=size,
                                    width=w,
                                    height=h
                                ),
                                Button(
                                    'Gallery',
                                    accent=accent,
                                    size=size,
                                    width=w,
                                    height=h
                                ),
                                Button(
                                    'About',
                                    accent=accent,
                                    size=size,
                                    width=w,
                                    height=h
                                ),
                                Button(
                                    'Account',
                                    accent=accent,
                                    size=size,
                                    width=w,
                                    height=h,
                                    onClick=self.fade
                                ),
                            ],
                            'alignment': QtCore.Qt.AlignRight
                        },
                        'end': {
                            'children': [],
                            'alignment': QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
                        },
                    },
                )
            )

        self.windowLayout = QtWidgets.QVBoxLayout()
        self.windowLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.mainGroup = QtWidgets.QGroupBox()
        self.mainGroup.setStyleSheet(
            '''
                QGroupBox {
                    border: 0;
                }
            '''
        )
        self.mainGroup.setLayout(self.windowLayout)

        self.mainScroll = QtWidgets.QScrollArea()
        self.mainScroll.setStyleSheet(
            '''
                QScrollArea {
                    border: 0;
                }
            '''
        )
        self.mainScroll.setWidget(self.mainGroup)
        self.mainScroll.setWidgetResizable(True)

        self.rightLayout.addWidget(self.mainScroll)

        self.setLayout(self.mainLayout)

        self.initialization()
    
    def initialization(self):
        self.buttonLayout = QtWidgets.QGridLayout()
        self.windowLayout.addLayout(self.buttonLayout)

        accents = genericVariables.variables['accents']
        sizes = genericVariables.variables['sizes']

        x, y = 0, 0

        for accent in accents:
            size = 'xs'
            self.buttonLayout.addWidget(
                Button(
                    f'{accent} {size}',
                    accent=accent,
                    size=size
                ),
                x,
                y
            )
            y += 1
        x += 1
        y = 0

        for accent in accents:
            size = 'sm'
            self.buttonLayout.addWidget(
                Button(
                    f'{accent} {size}',
                    accent=accent,
                    size=size
                ),
                x,
                y
            )
            y += 1
        x += 1
        y = 0

        for accent in accents:
            size = 'lg'
            self.buttonLayout.addWidget(
                Button(
                    f'{accent} {size}',
                    accent=accent,
                    size=size
                ),
                x,
                y
            )
            y += 1
        x += 1
        y = 0

        for accent in accents:
            self.buttonLayout.addWidget(
                Card(
                    accent=accent,
                    width=200,
                    header={
                        'accent': accent
                    },
                    footer={
                        'accent': accent
                    },
                    body={
                        'alignment': QtCore.Qt.AlignCenter,
                        'child': Button(
                            'warning',
                            accent='warning',
                            size='lg'
                        )
                    }
                ),
                x,
                y
            )
            y += 1
        x += 1
        y = 0
    
    def fade(self):
        self.setWindowOpacity(0.5)
        QtCore.QTimer.singleShot(1000, self.unfade)
     
    def unfade(self):
        self.setWindowOpacity(1)

    def resizeEvent(self, event):
        self.resizeFunction()
        super(Window, self).resizeEvent(event)

    def resizeFunction(self):
        print(self.width(), self.height())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    buttonLayout = QtWidgets.QGridLayout()

    accents = genericVariables.variables['accents']
    sizes = genericVariables.variables['sizes']

    x, y = 0, 0

    for accent in accents:
        size = 'xss'
        buttonLayout.addWidget(
            Button(
                f'{accent} {size}',
                accent=accent,
                size=size
            ),
            x,
            y
        )
        y += 1
    x += 1
    y = 0

    for accent in accents:
        size = 'xs'
        buttonLayout.addWidget(
            Button(
                f'{accent} {size}',
                accent=accent,
                size=size
            ),
            x,
            y
        )
        y += 1
    x += 1
    y = 0

    for accent in accents:
        size = 'sm'
        buttonLayout.addWidget(
            Button(
                f'{accent} {size}',
                accent=accent,
                size=size
            ),
            x,
            y
        )
        y += 1
    x += 1
    y = 0

    for accent in accents:
        size = 'lg'
        buttonLayout.addWidget(
            Button(
                f'{accent} {size}',
                accent=accent,
                size=size
            ),
            x,
            y
        )
        y += 1
    x += 1
    y = 0

    for accent in accents:
        buttonLayout.addWidget(
            Card(
                accent=accent,
                width=200,
                header={
                    'accent': accent
                },
                footer={
                    'accent': accent
                },
                body={
                    'alignment': QtCore.Qt.AlignCenter,
                    'child': Button(
                        'warning',
                        accent='warning',
                        size='lg'
                    )
                }
            ),
            x,
            y
        )
        y += 1
    x += 1
    y = 0


    windowLayout = QtWidgets.QVBoxLayout()
    windowLayout.addLayout(buttonLayout)
    
    mainGroup = QtWidgets.QGroupBox()
    mainGroup.setStyleSheet(
        '''
            QGroupBox {
                border: 0;
                background-color: rgba(0, 0, 0, 0)
            }
        '''
    )
    mainGroup.setLayout(windowLayout)

    mainScroll = QtWidgets.QScrollArea()
    mainScroll.setStyleSheet(
        '''
            QScrollArea {
                border: 0;
                background-color: rgba(0, 0, 0, 0)
            }
        '''
    )
    mainScroll.setWidget(mainGroup)
    mainScroll.setWidgetResizable(True)

    window = Page(
        child={
            'body': {
                'children': [
                    Scroll(
                        child={
                            'child': Container(
                                child={
                                    'child': windowLayout
                                },
                                customVariables={
                                    'padding-left': '0px',
                                    'padding-right': '0px',
                                    'margin-left': '0px',
                                    'margin-right': '0px',
                                }
                            )
                        }
                    ),
                ]
            }
        }
    )
    window.show()
    
    # window1 = Window()
    # window1.show()
    sys.exit(app.exec_())

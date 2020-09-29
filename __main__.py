from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

from iGenerals.buttons import Button
from iGenerals.cards import Card
from iLayouts.layouts import NavBar
from iGenerals.labels import Label
from iQSS import genericVariables


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.accent = 'dark'
        size = 'lg'
        w, h = 100, 50
        self.mainLayout.addWidget(
            NavBar(
                accent='dark',
                child={
                    'title': {
                        'child': Label(
                            text='NavBar',
                            width=100,
                            accent=self.accent
                        ),
                        'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
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

        self.mainLayout.addWidget(self.mainScroll)

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

        # self.windowLayout.addWidget(
        #     Button(
        #         'custom',
        #         animation={
        #             'bgStartValue': 'green',
        #             'bgEndValue': 'white', # this will be used as background-color
        #             'duration': 300,
        #             'cStartValue': 'white',
        #             'cEndValue': 'black',
        #         },
        #         customVariables={
        #             'border-radius': '5px',
        #             'border-width': '1px',
        #             'border-style': 'solid',
        #             'border-color': 'green',
        #         }
        #     )
        # )

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
                            size='lg',
                            # fill=True,
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

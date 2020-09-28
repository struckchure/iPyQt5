from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

from iGenerals.buttons import Button
from iGenerals.cards import Card


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

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
        self.mainScroll.setWidget(self.mainGroup)
        self.mainScroll.setWidgetResizable(True)

        self.mainLayout.addWidget(self.mainScroll)

        self.setLayout(self.mainLayout)

        self.initialization()
    
    def initialization(self):
        self.windowLayout.addWidget(
            Button(
                'primary',
                accent='primary'
            )
        )

        self.windowLayout.addWidget(
            Button(
                'secondary',
                accent='secondary'
            )
        )

        self.windowLayout.addWidget(
            Button(
                'success',
                accent='success',
                enabled=False,
                onClick=self.fade
            )
        )

        self.windowLayout.addWidget(
            Button(
                'info',
                accent='info',
                size='lg',
                onClick=self.fade
            )
        )

        self.windowLayout.addWidget(
            Button(
                'danger',
                accent='danger',
                size='sm'
            )
        )

        self.windowLayout.addWidget(
            Button(
                'warning',
                accent='warning',
                size='xs'
            )
        )

        self.windowLayout.addWidget(
            Button(
                'custom',
                animation={
                    'bgStartValue': 'green',
                    'bgEndValue': 'white', # this will be used as background-color
                    'duration': 300,
                    'cStartValue': 'white',
                    'cEndValue': 'black',
                },
                customVariables={
                    'border-radius': '5px',
                    'border-width': '1px',
                    'border-style': 'solid',
                    'border-color': 'green',
                }
            )
        )

        self.windowLayout.addWidget(
            Card(
                accent='primary',
                header={
                    'accent': 'primary',
                    'alignment': QtCore.Qt.AlignRight
                },
                footer={
                    'accent': 'primary'
                },
                body={
                    'alignment': QtCore.Qt.AlignCenter,
                    'child': Button(
                        'warning',
                        accent='warning',
                        size='xs'
                    ),
                }
            )
        )

        self.windowLayout.addWidget(
            Card(
                accent='secondary'
            )
        )

        self.windowLayout.addWidget(
            Card(
                accent='success'
            )
        )

        self.windowLayout.addWidget(
            Card(
                accent='warning'
            )
        )

        self.windowLayout.addWidget(
            Card(
                accent='info'
            )
        )

        self.windowLayout.addWidget(
            Card(
                accent='danger'
            )
        )
    
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

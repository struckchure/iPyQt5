from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
import qtawesome as qta

from iGenerals.buttons import Button
from iGenerals.cards import Card
from iGenerals.modals import Modal
from iGenerals.alerts import Alert
from iLayouts.layouts import NavBar, SideBar, Page
from iGenerals.forms import TextInput, Form
from iLayouts.containers import Container, Scroll, Row, Column, Table
from iGenerals.labels import Label
from iUtils import iUtils
from iQSS import genericVariables


class Window(Page):
    windowLayout = QtWidgets.QVBoxLayout()
    windowLayout.setSpacing(3)

    def __init__(self):
        super(Window, self).__init__(
            child={
                'body': {
                    'children': [
                        Scroll(
                            child={
                                'child': Container(
                                    child={
                                        # 'child': Button(
                                        #     accent='dark',
                                        #     onClick=self.showModal
                                        # )
                                        'child': self.windowLayout
                                    },
                                ),
                            }
                        ),
                    ]
                }
            }
        )

        self.customInitialization()

    def customInitialization(self):
        self.buttonLayout = QtWidgets.QGridLayout()
        self.buttonLayout.setSpacing(3)

        self.windowLayout.addLayout(self.buttonLayout)

        accents = genericVariables.variables['accents']

        x, y = 0, 0

        for accent in accents:
            size = 'xss'
            if accent != 'transparent':
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
            size = 'xs'
            if accent != 'transparent':
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
            if accent != 'transparent':
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
            if accent != 'transparent':
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
            if accent != 'transparent':
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

        for accent in accents:
            size = 'xss'
            if accent != 'transparent':
                self.buttonLayout.addWidget(
                    Alert(
                        accent=accent,
                        text=accent,
                        size=size,
                        xFill=True,
                        yFill=True,
                    ),
                    x,
                    y
                )
            y += 1
        x += 1
        y = 0

        self.buttonLayout.addWidget(
            Button(
                f'Button',
                size='lg',
                customVariables={
                    'border-radius': '5px',
                },
                animation={
                    # Background Color

                    'bgStartValue': 'blue',
                    'bgEndValue': 'green',
                    'duration': 500,
                    
                    # Color
                    
                    'cStartValue': 'white',
                    'cEndValue': 'black',
                },
                xFill=True,
                yFill=False
            ),
            x,
            y,
            1,
            len(accents)
        )

        self.windowLayout.addWidget(
            Form(
                grid=True,
                height=900,
                width=1500,
            )
        )

        self.windowLayout.addWidget(
            Row(
                accent='transparent',
                xFill=True,
                yFill=False,
                children={
                    'children': [
                        Button(
                            text='Row',
                            width=300,
                            size='lg',
                            accent='primary'
                        ),
                        Button(
                            text='Row',
                            width=300,
                            size='lg',
                            accent='primary'
                        ),
                        Button(
                            text='Row',
                            width=300,
                            size='lg',
                            accent='primary'
                        ),
                        Button(
                            text='Row',
                            width=300,
                            size='lg',
                            accent='primary'
                        ),
                        Button(
                            text='Row',
                            width=300,
                            size='lg',
                            accent='primary'
                        )
                    ],
                    'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignHCenter,
                    'spacing': 0
                }
            )
        )

        self.windowLayout.addWidget(
            Column(
                accent='transparent',
                xFill=False,
                yFill=True,
                children={
                    'children': [
                        Button(
                            text='Column',
                            accent='primary'
                        ),
                        Button(
                            text='Column',
                            accent='primary'
                        ),
                        Button(
                            text='Column',
                            accent='primary'
                        ),
                        Button(
                            text='Column',
                            accent='primary'
                        ),
                        Button(
                            text='Column',
                            accent='primary',
                            onClick=self.showModal
                        )
                    ],
                    'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignHCenter,
                    'spacing': 0
                }
            )
        )

        self.tableLayout = QtWidgets.QGridLayout()
        self.tableLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        x, y = 0, 0

        for accent in accents:
            self.tableLayout.addWidget(
                Table(
                    accent=accent
                ),
                x,
                y
            )

            y += 1

            if y >= 4:
                y = 0
                x += 1

        self.windowLayout.addLayout(self.tableLayout)

    def showModal(self):
        self.modal = Modal()
        self.modal.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

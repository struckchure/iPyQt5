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


def main():
    buttonLayout = QtWidgets.QGridLayout()
    buttonLayout.setSpacing(3)

    accents = genericVariables.variables['accents']

    x, y = 0, 0

    for accent in accents:
        size = 'xss'
        if accent != 'transparent':
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
        if accent != 'transparent':
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
        if accent != 'transparent':
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
        if accent != 'transparent':
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
        if accent != 'transparent':
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

    for accent in accents:
        size = 'xss'
        if accent != 'transparent':
            buttonLayout.addWidget(
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

    buttonLayout.addWidget(
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

    windowLayout = QtWidgets.QVBoxLayout()
    windowLayout.setSpacing(3)
    windowLayout.addLayout(buttonLayout)

    windowLayout.addWidget(
        Form(
            grid=True,
            height=900,
            width=1500,
        )
    )

    def showModal():
        modal = Modal(
            child={
            }
        )
        modal.show()

        print(modal)

    windowLayout.addWidget(
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
                        accent='primary',
                        onClick=showModal
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

    windowLayout.addWidget(Modal())

    windowLayout.addWidget(
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
                        accent='primary'
                    )
                ],
                'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignHCenter,
                'spacing': 0
            }
        )
    )

    tableLayout = QtWidgets.QGridLayout()
    tableLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

    x, y = 0, 0

    for accent in accents:
        tableLayout.addWidget(
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

    windowLayout.addLayout(tableLayout)

    app = QtWidgets.QApplication(sys.argv)
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
                                # child={
                                #     'child': Column(
                                #         accent='transparent',
                                #         xFill=True,
                                #         yFill=True,
                                #         children={
                                #             'children': [
                                #                 Row(
                                #                     accent='transparent',
                                #                     xFill=False,
                                #                     yFill=True,
                                #                     children={
                                #                         'children': [
                                #                             Column(
                                #                                 accent='transparent',
                                #                                 xFill=False,
                                #                                 yFill=True,
                                #                                 children={
                                #                                     'children': [
                                #                                         Button(
                                #                                             f'{accent} xss',
                                #                                             accent=accent,
                                #                                             size='xss'
                                #                                         ) for accent in accents if accent != 'transparent'
                                #                                     ],
                                #                                     'spacing': 5
                                #                                 }
                                #                             ), # Column
                                #                             Column(
                                #                                 accent='transparent',
                                #                                 xFill=False,
                                #                                 yFill=True,
                                #                                 children={
                                #                                     'children': [
                                #                                         Button(
                                #                                             f'{accent} xs',
                                #                                             accent=accent,
                                #                                             size='xs'
                                #                                         ) for accent in accents if accent != 'transparent'
                                #                                     ],
                                #                                     'spacing': 5
                                #                                 }
                                #                             ), # Column
                                #                             Column(
                                #                                 accent='transparent',
                                #                                 xFill=False,
                                #                                 yFill=True,
                                #                                 children={
                                #                                     'children': [
                                #                                         Button(
                                #                                             f'{accent} sm',
                                #                                             accent=accent,
                                #                                             size='sm'
                                #                                         ) for accent in accents if accent != 'transparent'
                                #                                     ],
                                #                                     'spacing': 5
                                #                                 }
                                #                             ), # Column
                                #                         ],
                                #                         'spacing': 5,
                                #                     }
                                #                 ), # Row
                                #                 Row(
                                #                     accent='transparent',
                                #                     xFill=True,
                                #                     yFill=True,
                                #                     children={
                                #                         'children': [
                                #                             Row(
                                #                                 accent='transparent',
                                #                                 xFill=True,
                                #                                 yFill=True,
                                #                                 children={
                                #                                     'children': [
                                #                                         Card(
                                #                                             accent=accent,
                                #                                             xFill=True,
                                #                                             yFill=True,
                                #                                             header={
                                #                                                 'accent': accent
                                #                                             },
                                #                                             footer={
                                #                                                 'accent': accent
                                #                                             },
                                #                                             body={
                                #                                                 'alignment': QtCore.Qt.AlignCenter,
                                #                                                 'child': Button(
                                #                                                     'warning',
                                #                                                     accent='warning',
                                #                                                     size='lg'
                                #                                                 )
                                #                                             }
                                #                                         ) for accent in accents if accent != 'transparent'
                                #                                     ],
                                #                                     'spacing': 5
                                #                                 }
                                #                             ), # Column
                                #                         ],
                                #                         'spacing': 5,
                                #                     }
                                #                 ), # Row
                                #             ],
                                #             'spacing': 0,
                                #         },
                                #     ), # Column
                                # },
                                customVariables={
                                    'padding-left': '0px',
                                    'padding-right': '0px',
                                    'margin-left': '0px',
                                    'margin-right': '0px',
                                }
                            ),
                        }
                    ),
                ]
            }
        }
    )

    window.show()

    sys.exit(app.exec_())


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


def mainOne():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    mainOne()

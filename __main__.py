from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys
import qtawesome as qta

from iGenerals.buttons import Button
from iGenerals.cards import Card
from iGenerals.alerts import Alert
from iLayouts.layouts import NavBar, SideBar, Page
from iGenerals.forms import TextInput, Form
from iLayouts.containers import Container, Scroll, Row, Column, Table
from iGenerals.labels import Label
from iQSS import genericVariables


def main():
    app = QtWidgets.QApplication(sys.argv)

    buttonLayout = QtWidgets.QGridLayout()

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
                    yFill=True
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
    windowLayout.addLayout(buttonLayout)

    windowLayout.addWidget(
        Form(
            grid=True,
            height=900,
            width=1500,
        )
    )

    windowLayout.addWidget(
        Row(
            xFill=True,
            yFill=False,
            children={
                'children': [
                    Button(
                        text='Row',
                        accent='primary'
                    ),
                    Button(
                        text='Row',
                        accent='primary'
                    ),
                    Button(
                        text='Row',
                        accent='primary'
                    ),
                    Button(
                        text='Row',
                        accent='primary'
                    ),
                    Button(
                        text='Row',
                        accent='primary'
                    )
                ],
                'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignHCenter
            }
        )
    )

    windowLayout.addWidget(
        Column(
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
                'alignment': QtCore.Qt.AlignLeft | QtCore.Qt.AlignHCenter
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

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

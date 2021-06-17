from PyQt5.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
    QSizePolicy
)
from PyQt5.QtCore import Qt


class LayoutBase(QGroupBox):

    '''
    Base layout using QVBoxLayout as default,
    center alignment on x and y axis
    '''

    OBJECT_TYPE = 'QGroupBox'

    MIN_WIDTH = 50
    MIN_HEIGHT = 50

    def __init__(self, *args, **kwargs):
        super(LayoutBase, self).__init__(*args, **kwargs)

        # set default vertical box layout for widget
        # center alignment and 0 content margins LRTB

        self.__Layout = QVBoxLayout()
        self.__Layout.setContentsMargins(0, 0, 0, 0)
        self.__Layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setLayout(self.__Layout)

        self.setDefaults()

    def setDefaults(self):
        self.setMinimumSize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )
        self.setContentsMargins(0, 0, 0, 0)

    def addWidget(self, *args, **kwargs):
        self.__Layout.addWidget(*args, **kwargs)

    def setStyleSheet(self, style):
        super(LayoutBase, self).setStyleSheet(style)

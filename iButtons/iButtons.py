from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui


'''
    Base for Genrics
'''

from iBase.iBase import ButtonBase

'''
    Buttons
'''


class Button(QtWidgets.QPushButton, ButtonBase):
    def __init__(
        self,
        text='Click me',
        icon=None,
        event=None,
        **kwargs
        ):
        super(Button, self).__init__()

        if 'padding' in kwargs:
            self.padding = kwargs['padding']

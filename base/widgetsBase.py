from PyQt5.QtWidgets import (
    QPushButton,
    QLineEdit,
    QLabel,
    QSizePolicy
)
from PyQt5.QtCore import Qt


class Button(QPushButton):

    '''
    Button base for buttons
    '''

    OBJECT_TYPE = 'QPushButton'

    MIN_WIDTH = 300
    MIN_HEIGHT = 50

    MAX_HEIGHT = 60

    WIDTH_RATIO = 1
    HEIGHT_RATIO = 1

    def __init__(self, *args, **kwargs):
        super(Button, self).__init__(*args, **kwargs)

        self.setDefaults()

    def setDefaults(self):
        self.setCursor(Qt.PointingHandCursor)
        self.setFocusPolicy(Qt.FocusPolicy())

        self.setMinimumSize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.setMaximumHeight(self.MAX_HEIGHT)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def setMaximumWidth(self, width):
        width *= self.WIDTH_RATIO

        super(Button, self).setMaximumWidth(width)

    def setMaximumHeight(self, height):
        height *= self.HEIGHT_RATIO

        super(Button, self).setMaximumHeight(height)

    def setMaximumSize(self, width, height):
        width *= self.WIDTH_RATIO
        height *= self.HEIGHT_RATIO

        super(Button, self).setMaximumSize(width, height)

    def setMinimumWidth(self, width):
        width *= self.WIDTH_RATIO

        super(Button, self).setMinimumWidth(width)

    def setMinimumHeight(self, height):
        height *= self.HEIGHT_RATIO

        super(Button, self).setMinimumHeight(height)

    def setMinimumSize(self, width, height):
        width *= self.WIDTH_RATIO
        height *= self.HEIGHT_RATIO

        super(Button, self).setMinimumSize(width, height)

    def setStyleSheet(self, style):
        super(Button, self).setStyleSheet(style)

    def onClick(self, event):
        self.clicked.connect(event)

    def onHover(self, event):
        super().enterEvent(event)

    def afterHover(self, event):
        super().leaveEvent(event)

    # def enterEvent(self, event):
    #     if self.enabled:
    #         self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
    #         self._animation.start()

    # def leaveEvent(self, event):
    #     if self.enabled:
    #         self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
    #         self._animation.start()


class TextInput(QLineEdit):

    '''
    Text input base
    '''

    OBJECT_TYPE = 'QLineEdit'

    MAX_HEIGHT = 60

    WIDTH_RATIO = 1
    HEIGHT_RATIO = 1

    def __init__(self, *args, **kwargs):
        super(TextInput, self).__init__(*args, **kwargs)

        self.setDefaults()

    def setDefaults(self):
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

        self.setMaximumHeight(self.MAX_HEIGHT)
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def setMaximumWidth(self, width):
        width *= self.WIDTH_RATIO

        super(TextInput, self).setMaximumWidth(width)

    def setMaximumHeight(self, height):
        height *= self.HEIGHT_RATIO

        super(TextInput, self).setMaximumHeight(height)

    def setMaximumSize(self, width, height):
        width *= self.WIDTH_RATIO
        height *= self.HEIGHT_RATIO

        super(TextInput, self).setMaximumSize(width, height)

    def setMinimumWidth(self, width):
        width *= self.WIDTH_RATIO

        super(TextInput, self).setMinimumWidth(width)

    def setMinimumHeight(self, height):
        height *= self.HEIGHT_RATIO

        super(TextInput, self).setMinimumHeight(height)

    def setMinimumSize(self, width, height):
        width *= self.WIDTH_RATIO
        height *= self.HEIGHT_RATIO

        super(TextInput, self).setMinimumSize(width, height)

    def setStyleSheet(self, style):
        super(TextInput, self).setStyleSheet(style)

    def onTextChange(self, event):
        self.textChanged.connect(event)


class Label(QLabel):

    '''
    Label base inherited from QLabel
    '''

    OBJECT_TYPE = 'QLabel'

    MAX_HEIGHT = 60

    WIDTH_RATIO = 1
    HEIGHT_RATIO = 1

    def __init__(self, *args, **kwargs):
        super(Label, self).__init__(*args, **kwargs)

        self.setDefaults()

    def setDefaults(self):
        self.setMaximumHeight(self.MAX_HEIGHT)
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

    def setMaximumWidth(self, width):
        width *= self.WIDTH_RATIO

        super(Label, self).setMaximumWidth(width)

    def setMaximumHeight(self, height):
        height *= self.HEIGHT_RATIO

        super(Label, self).setMaximumHeight(height)

    def setMaximumSize(self, width, height):
        width *= self.WIDTH_RATIO
        height *= self.HEIGHT_RATIO

        super(Label, self).setMaximumSize(width, height)

    def setMinimumWidth(self, width):
        width *= self.WIDTH_RATIO

        super(Label, self).setMinimumWidth(width)

    def setMinimumHeight(self, height):
        height *= self.HEIGHT_RATIO

        super(Label, self).setMinimumHeight(height)

    def setMinimumSize(self, width, height):
        width *= self.WIDTH_RATIO
        height *= self.HEIGHT_RATIO

        super(Label, self).setMinimumSize(width, height)


    def setStyleSheet(self, style):
        super(Label, self).setStyleSheet(style)

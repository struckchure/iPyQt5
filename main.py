from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys

from iBase.iBase import ButtonBase
from iButtons.iButtons import Button, PushButton



class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.windowLayout = QtWidgets.QVBoxLayout()
        self.windowLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.setLayout(self.windowLayout)

        self.initialization()
    
    def initialization(self):
        self.buttonTest = PushButton()
        self.buttonTest.setText(self.tr("Click Here"))
        self.buttonTest.setSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum
        )
        self.buttonTest.clicked.connect(self.fade)

        # self.windowLayout.addWidget(self.buttonTest)

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
                accent='success'
            )
        )

        self.windowLayout.addWidget(
            Button(
                'info',
                accent='info'
            )
        )

        self.windowLayout.addWidget(
            Button(
                'danger',
                accent='danger'
            )
        )

        self.windowLayout.addWidget(
            Button(
                'warning',
                accent='warning'
            )
        )
    
    def fade(self):
        self.setWindowOpacity(0.5)
        QtCore.QTimer.singleShot(1000, self.unfade)
     
    def unfade(self):
        self.setWindowOpacity(1)


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

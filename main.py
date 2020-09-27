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

        self.windowLayout.addWidget(self.buttonTest)

        self.buttonTest2 = Button('Click Here')
        self.buttonTest2.clicked.connect(self.fade)

        self.windowLayout.addWidget(self.buttonTest2)

        self.buttonTest3 = Button(
            'Click Here',
            accent='success',
            # customVariables={
            #     'border-color': 'red',
            #     'border-radius': '10px',
            #     'font-size': '20px',
            #     'max-width': '500px',
            #     'max-height': '70px',
            # },
            # animation={
            #     'bgStartValue': 'red',
            #     'bgEndValue': 'white',
            #     'duration': 1500,
            #     'cStartValue': 'blue',
            #     'cEndValue': 'white'
            # }
        )

        self.windowLayout.addWidget(self.buttonTest3)
    
    def fade(self):
        self.setWindowOpacity(0.5)
        QtCore.QTimer.singleShot(1000, self.unfade)
     
    def unfade(self):
        self.setWindowOpacity(1)


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

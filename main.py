from PyQt5 import QtWidgets
import sys

from iBase.iBase import ButtonBase
from iButtons.iButtons import Button


app = QtWidgets.QApplication(sys.argv)
app.exit()

test = Button()
print(test.padding)

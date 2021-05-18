from PyQt5.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QPushButton,
    QHBoxLayout
)
import sys


class App(QWidget):

    def __(self, *args, **kwargs):
        super(App).__init__(*args, **kwargs)

        self.button = QPushButton('Hello')

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.button)
        self.setLayout(self.button_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())

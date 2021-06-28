from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout
)
import sys


class App(QWidget):

    WINDOW_APP = QApplication(sys.argv)

    MIN_WIDTH = 500
    MIN_HEIGHT = 500
    DEFAULT_WINDOW_TITLE = "iPyQt5 | App"

    router = None
    store = None

    def __init__(self, router=None, store=None, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)

        self.setDefaults()

        self.setRouter(router)
        self.setStore(store)

        if router:
            self.setRouter(router)

        if store:
            self.setStore(store)

    def setDefaults(self):
        self.appLayout = QVBoxLayout()
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.appLayout)

        self.setMinimumSize(self.MIN_WIDTH, self.MIN_HEIGHT)
        self.setWindowTitle(self.DEFAULT_WINDOW_TITLE)

    def setRouter(self, router):
        self.router = router
        self.appLayout.addWidget(self.router)

    def setStore(self, store):
        self.store = store

    def getRouter(self):
        return self.router

    def getStore(self):
        return self.store

    def mount(self, showMaximized=True):
        if showMaximized:
            self.showMaximized()

        self.show()

        sys.exit(self.WINDOW_APP.exec_())


if __name__ == '__main__':
    window = App()
    window.mount()

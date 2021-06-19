from PyQt5.QtCore import Qt
from base.viewsBase import ViewBase as Page
from base.widgetsBase import TextInput, Button, Label
from css import engine as CSS


class Index(Page):

    def __init__(self, *args, **kwargs):
        super(Index, self).__init__(*args, **kwargs)

        self.setStyleSheet(
            CSS.getClasses(
                objectName=self.OBJECT_TYPE,
                classNames=[
                    'bg-gray-900',
                    'border-none'
                ]
            )
        )

        form = CSS.getClasses(
            objectName=['QLineEdit', 'QPushButton', 'QLabel'],
            classNames=[
                'bg-gray-800',
                'p-3',
                'text-white',
                'border-none',
            ]
        )

        pseduos = CSS.getPsuedoClasses(
            objectName=['QLineEdit', 'QPushButton'],
            psuedoClass={
                'hover': [
                    # 'bg-gray-700'
                ]
            }
        )
        form += pseduos

        FORM_WIDTH = 300

        self.pageTitle = Label('Welcome to iPyQt5')
        self.pageTitle.setMaximumSize(FORM_WIDTH, 60)
        self.pageTitle.setStyleSheet(form)
        self.addWidget(self.pageTitle)

        self.username = TextInput()
        self.username.setMaximumSize(FORM_WIDTH, 60)
        self.username.setStyleSheet(form)

        self.password = TextInput()
        self.password.setMaximumSize(FORM_WIDTH, 60)
        self.password.setStyleSheet(form)
        self.password.setEchoMode(TextInput.Password)
        self.password.onTextChange(self.set_username)

        self.button = Button('Login')
        self.button.setStyleSheet(
            form + CSS.getPsuedoClasses(
                objectName=['QPushButton'],
                psuedoClass={
                    'hover': [
                        'text-9xl'
                    ]
                }
            )
        )
        self.button.setMaximumSize(FORM_WIDTH, 60)
        self.button.onClick(self.routeToHome)

        self.addWidget(self.username)
        self.addWidget(self.password)
        self.addWidget(self.button)

    def set_username(self):
        self.username.setText(self.password.text())

    def routeToHome(self):
        from routes import router

        router.goToRoute('Home')


class Home(Page):

    def __init__(self, *args, **kwargs):
        super(Home, self).__init__(*args, **kwargs)

        self.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.setStyleSheet(
            CSS.getClasses(
                objectName=self.OBJECT_TYPE,
                classNames=[
                    'bg-yellow-900',
                    'p-10',
                    'border-none'
                ]
            )
        )

        form = CSS.getClasses(
            objectName=['QPushButton', 'QLineEdit', 'QLabel'],
            classNames=[
                'bg-gray-800',
                'p-3',
                'text-white',
            ]
        )

        pseduos = CSS.getPsuedoClasses(
            objectName=['QPushButton', 'QLineEdit', 'QLabel'],
            psuedoClass={
                'focus': [
                    'border-none'
                ],
                'pressed': [
                    'border-none'
                ]
            }
        )
        form += pseduos

        self.pageTitle = Label('Home')
        self.pageTitle.setStyleSheet(form)
        self.addWidget(self.pageTitle)

        self.username = TextInput()
        self.username.setStyleSheet(form)

        self.password = TextInput()
        self.password.setStyleSheet(form)
        self.password.setEchoMode(TextInput.Password)

        self.addWidget(self.username)
        self.addWidget(self.password)

        self.button2 = Button('Click')
        self.button2.setStyleSheet(form)
        self.button2.onClick(self.routeToIndex)

        self.addWidget(self.button2)

    def routeToIndex(self):
        from routes import router

        router.goToRoute('Index')

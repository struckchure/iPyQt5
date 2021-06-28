from PyQt5.QtWidgets import QStackedWidget
from iPyQt5.base.layoutsBase import LayoutBase


class Router(LayoutBase):

    '''
    Router Instance
        ```
        app = App(
            ...
            router=Router(
                routes={
                    'index': 'home',
                    'names': ['home', 'login', 'register'],
                    'views': [Home, LoginView, RegisterView]
                }
            )
            ...
        )
        ```
    '''

    routes = None

    def __init__(self, routes, *args, **kwargs):
        super(Router, self).__init__(*args, **kwargs)

        self.routes = routes
        self.createRoutes(self.routes)

    def createRoutes(self, routes):
        '''
        Create router for routes
        '''

        self.router = QStackedWidget()
        self.addWidget(self.router)
        '''
        Create new routes of Page instances
        '''

        self.routes = routes

        self.goToRoute(name=self.routes['index'])

    def getRoutes(self):
        '''
        returns all routers
        '''
        return self.routes

    def goToRoute(self, name, params=None):
        '''
        Go to a named route passing parameters along if necessary
        goToRoute(
            name='home',
            params={
                'args': [],
                'kwargs': {}
            }
        )
        '''

        routeIndex = self.getRoutes()['names'].index(name)
        routeView = self.getRoutes()['views'][routeIndex]

        self.addRouterView(routeView)
        self.setCurrentIndex(self.getCurrentIndex() + 1)

    def addRouterView(self, *args, **kwargs):
        self.router.addWidget(*args, **kwargs)

    def getCurrentIndex(self):
        return self.router.currentIndex()

    def setCurrentIndex(self, *args, **kwargs):
        self.router.setCurrentIndex(*args, **kwargs)

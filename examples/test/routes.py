from iPyQt5.app.router import Router
from pages import Index, Home, Render3D


routes = {
    'index': 'Index',
    'names': ['Index', 'Home', 'Render3D'],
    'views': [Index(), Home(), Render3D()]
}

router = Router(
    routes=routes
)

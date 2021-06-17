from app.router import Router
from pages import Index, Home


routes = {
    'index': 'Index',
    'names': ['Index', 'Home'],
    'views': [Index(), Home()]
}

router = Router(
    routes=routes
)

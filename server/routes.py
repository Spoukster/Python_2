import os
from functools import reduce
from importlib import __import__

from settings import INSTALLED_MODULES


# def get_server_routes():
#     routes = []
#     modules = []
#
#     for itm in os.listdir():
#         if os.path.isdir(itm) and itm != '__pycache__':
#             module = __import__(f'{itm}.routes')
#             modules.append(module)
#
#     for module in modules:
#         routes += getattr(module, 'routes', [])
#
#     return routes

def get_server_routes():
    return reduce(
        lambda routes, module: routes + getattr(module, 'routes', []),
        reduce(
            lambda submodules, module: submodules + [getattr(module, 'routes', [])],
            reduce(
                lambda modules, module: modules + [__import__(f'{module}.routes')],
                INSTALLED_MODULES,
                []
            ),
            []
        ),
        []
    )


def resolve(action, routes=None):
    routes_mapping = {
        route['action']: route['controller']
        for route in routes or get_server_routes()
    }
    return routes_mapping.get(action, None)

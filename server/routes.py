import os
from functools import reduce
from importlib import __import__


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
            lambda modules, dir: modules + [__import__(f'{dir}.routes')],
            filter(
                lambda itm: os.path.isdir(itm) and itm != '__pycache__',
                os.listdir()
            ),
            []
        ),
        []
    )

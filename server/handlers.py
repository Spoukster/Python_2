import logging

from routes import resolve
from protocol import make_400, make_404, validate_request, make_response


def handle_client_request(request):
    if validate_request(request):
        action_name = request.get('action')
        controller = resolve(action_name)
        if controller:
            try:
                return controller(request)
            except Exception as err:
                logging.critical(err, exc_info=True)
                return make_response(
                    request, 500,
                    'Internal server error'
                )
        else:
            logging.error(f'Action not found: {action_name}')
            return make_404(request)
    else:
        return make_400(request)

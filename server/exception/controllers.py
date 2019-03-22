from protocol import make_response, make_400


def get_error(request):
    raise Exception('Some test error')

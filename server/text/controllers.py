from protocol import make_response, make_400
from authentication import login_required, LoginRequired
from customlogging import stack_logging, StackLogging


@login_required
@stack_logging('Function %(func_name)s was called.')
def get_upper_text(request):
    data = request.get('data')
    if not data:
        return make_400(request)
    return make_response(
        request,
        200,
        data.upper()
    )


@LoginRequired()
@StackLogging('Request body: %(request_data)s.')
def get_lower_text(request):
    data = request.get('data')
    if not data:
        return make_400(request)
    return make_response(
        request,
        200,
        data.lower()
    )

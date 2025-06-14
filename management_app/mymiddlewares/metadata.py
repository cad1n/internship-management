class MetaData(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            message = 'Seja bem-vindo(a), %s!' % request.user.username
        else:
            message = 'Seja bem-vindo'

        request.session['message'] = message
        return None

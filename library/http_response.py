from django.http import HttpResponse


class HttpFailure(HttpResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status_code = 401


class HttpCrossDomainResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['Access-Control-Allow-Origin'] = '*'


class IntelligentResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['Access-Control-Allow-Origin'] = '*'

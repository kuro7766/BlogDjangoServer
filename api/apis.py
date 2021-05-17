from django.http import HttpRequest
from lib import *

import requests
def apis(r: HttpRequest):
    if r.method == 'GET':
        d=ml.extract_url_param_dict(r.get_full_path())
        if not d.__contains__('type'):
            return HttpFailure()
        if d['type']=='weather':
            res = HttpCrossDomainResponse()
            r=requests.get('http://www.weather.com.cn/data/cityinfo/101121301.html')
            res.content=r.content
            return res
    return HttpFailure()

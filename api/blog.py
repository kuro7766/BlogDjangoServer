import json

from django.http import HttpRequest
from controller import sql_controller
from lib import *

from inspect import getmembers, isfunction

from lib import ml
from controller import sql_controller

types = init_types(sql_controller)

# http://127.0.0.1:8000/blog?type=get_article_content&token=1&article_id=3
def blog(r: HttpRequest):
    params = ml.extract_url_param_dict(r.get_full_path())
    print('params : ',params)
    r = intelligent_response(types, params)
    print('return : ', r.content)

    return r

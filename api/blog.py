import importlib
import json

from django.http import HttpRequest
from controller import sql_controller
from lib import *

from inspect import getmembers, isfunction

from lib import ml
from controller import sql_controller


def init():
    result = {}
    for item in ml.getAllFiles('controller'):

        if not item.endswith('.py'):
            continue
        my_module = importlib.import_module(f'controller.{ml.path_to_filename(item)[:-3]}')
        my_dict = init_types(my_module)
        result = {**result, **my_dict}
    print(result)
    return result


types = init()


# http://127.0.0.1:8000/blog?type=get_article_content&token=1&article_id=3
def blog(r: HttpRequest):
    params = ml.extract_url_param_dict(r.get_full_path())
    r = intelligent_response(types, params)
    print('params : ', params)
    print('return : ', r.content)
    return r

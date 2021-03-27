import json

from django.http import HttpRequest
from controller import sql_controller
from lib import *

from inspect import getmembers, isfunction

from lib import ml
from controller import sql_controller


def api(r: HttpRequest):
    return HttpResponse('ok')

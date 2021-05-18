from inspect import getmembers, isfunction

import library.ml as ml
from library.sql import exec_sql
from library.http_response import *
from library.intelligent_response import *


def init_types(pkg):
    x = {}
    mem = getmembers(pkg, isfunction)
    for i in mem:
        x[i[0]] = i[1]
    return x

import json
from library import ml
import datetime

_file = 'default.sqlite3'


# deprecated
# class Response:
#     def __init__(self, success, data):
#         self.success = success
#         self.data = data


"""
 https://stackoverflow.com/questions/3286525/return-sql-table-as-json-in-python
 """


def exec_sql(
        sql_str
        , *params, json_str=True, single_result_detection=True):
    import sqlite3

    sql_script = sql_str
    db = sqlite3.connect(_file, check_same_thread=False)
    db.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']

    # https://stackoverflow.com/questions/15856976/transactions-with-python-sqlite3
    db.isolation_level = None

    cursor = db.cursor()

    l_result = None
    try:
        rows = cursor.execute(sql_script, params).fetchall()
    except sqlite3.Error as err:
        rows = []
        ml.error_log(err)
        # return Response(False, None)

    db.commit()
    db.close()

    l_result = [dict(ix) for ix in rows]
    if single_result_detection and len(l_result) == 1:
        l_result = l_result[0]

    if json_str:
        success_rt = json.dumps(l_result)  # CREATE JSON
    else:
        success_rt = l_result
    return success_rt
    # return Response(True, success_rt)

# def exec_all(sql_file):
#     import sqlite3
#     with open(sql_file, 'r') as sql_file:
#         sql_script = sql_file.read()
#         # sql_script = sql_script.format(*convert(params))
#         sql_file.close()
#
#     print(sql_script)
#     db = sqlite3.connect(file, check_same_thread=False)
#
#     cursor = db.cursor()
#     cursor.executescript(sql_script)
#     db.commit()
#     db.close()

import json
from library import ml
import datetime

_configs = {
    'host': '182.42.108.244',
    'user': 'erupt',
    'passwd': '3BMPXJ3tSkZPTZLf',
    'db': 'erupt'
}

import pymysql



def _get_db():
    db = pymysql.connect(host=_configs['host'], user=_configs['user'], passwd=_configs['passwd'], db=_configs['db'])
    return db


# conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')
# cur = conn.cursor()
# cur.execute("SELECT Host,User FROM user")
# for r in cur:
#     print(r)
# cur.close()
# conn.close()

def exec_sql(
        sql_str
        , *params, json_str=True, single_result_detection=True):
    sql_script = sql_str

    db = _get_db()

    # https://stackoverflow.com/questions/15856976/transactions-with-python-sqlite3
    db.isolation_level = None

    cursor = db.cursor(pymysql.cursors.DictCursor)

    l_result = None
    try:
        cursor.execute(sql_script, params)
        rows = cursor.fetchall()
        db.commit()
        db.close()
    except Exception as err:
        rows = []
        ml.error_log(err)
        # return Response(False, None)

    l_result = rows
    if single_result_detection and len(l_result) == 1:
        l_result = l_result[0]

    if json_str:
        success_rt = json.dumps(l_result)  # CREATE JSON
    else:
        success_rt = l_result
    return success_rt

# transaction implementation
# def exec_transaction(sql_list: list):
#     db = pymysql.connect(host=_configs['host'], user=_configs['user'], passwd=_configs['passwd'], db=_configs['db'])
#     sql.isolation_level = None
#     c = sql.cursor()
#     c.execute("begin")
#     try:
#         for _sql in sql_list:
#             if len(_sql) == 0:
#                 continue
#             elif len(_sql) == 1:
#                 c.execute(_sql[0])
#             else:
#                 c.execute(_sql[0], *_sql[1:])
#         c.execute("commit")
#     except sql.Error:
#         print("failed!")
#         c.execute("rollback")

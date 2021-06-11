import library.mysql_helper as mys
import library.sqlite_helper as lite


def exec_sql(
        sql_str
        , *params, json_str=True, single_result_detection=True):
    return mys.exec_sql(sql_str
                        , *params, json_str=json_str, single_result_detection=single_result_detection)

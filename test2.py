def init():
    import importlib.util
    spec = importlib.util.spec_from_file_location("module.name", "test_case.py")
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    print(foo.get_pic())


if __name__ == '__main__':
    # init()
    # print(' aaa   '.strip())
    from lib import *

    # language=sql
    # print(my_sql.exec_sql('select * from my_tag_table'))
    # print(my_sql.exec_sql('select * from my_tag_table'))
    # print(my_sql.exec_sql('select ? from my_tag_table', 'tag_name'))

    # language=sql
    # print(exec_sql('select * from article_table'))
    # print(exec_sql('select * from article_table'))
    # print(exec_sql('select * from article_table'))
    # print(exec_sql('select * from article_table'))
    # print(exec_sql('select * from article_table'))
    # print(exec_sql('select * from article_table'))
    # connection = my_sql._get_db()
    # try:
    #     with connection.cursor() as cursor:
    #         # sql = "INSERT INTO `my_tag_table` VALUES (%s, %s)"
    #         sql = "INSERT INTO `my_tag_table` VALUES (%s, %s)"
    #         cursor.execute(sql, (None, 'very-secret2'))
    #
    #     # connection is not autocommit by default. So you must commit to save changes.
    #     connection.commit()
    #
    # finally:
    #     connection.close()

    # language=sql
    # exec_sql('insert into tag_table values (?,?)','标签3','33')
    # language=sql
    # print(exec_sql('select * from tag_table'))

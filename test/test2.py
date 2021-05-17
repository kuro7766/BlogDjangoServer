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
    print(my_sql.exec_sql('select * from my_tag_table'))
    print(my_sql.exec_sql('select * from my_tag_table'))
    print(my_sql.exec_sql('select tag_name from my_tag_table'))
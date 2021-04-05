import importlib

from library.sql import exec_sql
from library import ml as ml
from lib import *
from api import blog


def init():
    import os
    os.remove('default.sqlite3')
    fs = ml.getAllFiles('sql/init')
    for f in fs:
        exec_sql(ml.read_string(f))
        # exec_file(f)

    init_test_case()


def init_test_case():
    # language=sql
    l = [
        "insert into user_info_table values (50,'a','a','公告哦2','https://github.com/kuro7766','https://wpa.qq.com/msgrd?v=3&uin=2280315050&site=qq&menu=yes','https://blog.csdn.net/qq_43380015',null,'http://kuroweb.cf/mmo1/','http://www.baidu.com')",
        "insert into article_table values (41,50,'测试文章',0,'描述','http://kuroweb.cf/picture/1615892316837.jpg',100,'测试标题1',0)"
        ,
        "insert into article_table values (42,50,'测试文章2',0,'描述2','http://kuroweb.cf/picture/1615892316837.jpg',100,'测试标题2',0)"
        ,
        # 只存储root文本信息在数据库中
        "insert into article_comments_table values (1,41,'userid:abc,comment:Nihao,reply:[...]',0)",
        'insert into article_tag_link_table values (1,41)',
        "insert into tag_table values ('标签1',1)",
        "insert into friend_link_table values (50,1,'http://www.baidu.com',0)",
        "insert into friend_link_table values (50,2,'http://www.sina.com.cn',1)"
    ]
    fs = ml.getAllFiles('articles')
    for f in fs:
        content = ml.read_string(f)
        exec_sql(
            "insert into article_table values (null,50,?,0,'描述2','http://kuroweb.cf/picture/1615892316837.jpg',100,'测试标题',0)",
            content)
    for i in l:
        exec_sql(i)


# 一键生成dart代码
def generate_dart():
    target = r'E:\code\flutter\blog_project\lib\vars\django_function.dart'
    s = '''import 'consts.dart';
class DjangoUrl {
    |1|
}
    '''
    for item in ml.getAllFiles('controller'):

        if not item.endswith('.py'):
            continue
        my_module = importlib.import_module(f'controller.{ml.path_to_filename(item)[:-3]}')

        for name_fun in getmembers(my_module, isfunction):
            f = name_fun[1].__code__.co_varnames[:name_fun[1].__code__.co_argcount]
            print(name_fun, f)

            print(f)
            name = name_fun[0]
            a_fun = f'''static {ml.bigCamel(name)}({",".join(f)}) =>Const.baseUrl + 'blog?type={name}{"".join(["&" + i + "=$" + i + "" for i in f])}';
    |1|'''
            s = s.replace("|1|", a_fun)
    s = s.replace("|1|", '')
    ml.write_string(target, s)


if __name__ == '__main__':
    init()
    # generate_dart()

    # print(exec_sql('select article_description from article_table'))
    # print(isinstance({},list))
    # language=SQL
    # print(1, exec_sql('select * from user_info_table where id=?', '50 or 1=1'))
    # print(2, exec_sql('select * from user_info_table where id=?', '50'))

    # s = 'select user_name from user_info_table'
    # 'insert into user_info_table values (null,1,1,1,1,1,1,1)'
    # print(exec_sql(s, json_str=True).data)

if __name__ == '__main__':
    from lib import *

    if os.path.exists('errors.txt'):
        os.remove('errors.txt')

    # language=sql
    exec_sql('create table if not exists article_comments_table ('
             'comment_id integer,'
             'article_id integer,'
             'comment_json text'
             ')')

    exec_sql('delete from e_upms_menu where id>10')

    # 初始化菜单
    # language=sql
    if not exec_sql("select * from e_upms_menu where name='用户管理'", json_str=False):
        exec_sql(
            "INSERT INTO erupt.e_upms_menu "
            "(id, create_time, update_time, code, icon, name, param, power_off, sort, status, type, value, create_user_id, update_user_id, parent_menu_id)"
            " VALUES (null, null, null, 'article_table', null, '文章管理', null, null, 80, 1, 'table', 'article_table', 1, null, 1);")
        exec_sql(
            "INSERT INTO erupt.e_upms_menu "
            "(id, create_time, update_time, code, icon, name, param, power_off, sort, status, type, value, create_user_id, update_user_id, parent_menu_id)"
            " VALUES (null, null, null, 'tag_table', null, '标签管理', null, null, 80, 1, 'table', 'tag_table', 1, null, 1);")
        exec_sql(
            "INSERT INTO erupt.e_upms_menu "
            "(id, create_time, update_time, code, icon, name, param, power_off, sort, status, type, value, create_user_id, update_user_id, parent_menu_id)"
            " VALUES (null, null, null, 'user_info_table', null, '用户管理', null, null, 80, 1, 'table', 'user_info_table', 1, null, 1);")
        exec_sql(
            "INSERT INTO erupt.e_upms_menu "
            "(id, create_time, update_time, code, icon, name, param, power_off, sort, status, type, value, create_user_id, update_user_id, parent_menu_id)"
            " VALUES (null, null, null, 'my_simple', null, '请删除', null, null, 80, 1, 'table', 'my_simple', 1, null, 1);")

    # 初始化标签
    # language=sql
    if not exec_sql("select * from tag_table where tag_name='旅游'", json_str=False):
        exec_sql('delete from tag_table where 1')
        s = '''INSERT INTO erupt.tag_table (id, tag_name) VALUES (null, '旅游');
        INSERT INTO erupt.tag_table (id, tag_name) VALUES (null, '技术');
        INSERT INTO erupt.tag_table (id, tag_name) VALUES (null, '校园')'''
        for item in s.split(';'):
            exec_sql(item)

    # 初始化用户
    # language=sql
    if not exec_sql("select * from user_info_table where user_name='a'", json_str=False):
        exec_sql("insert into user_info_table values(1,'ann','ann_lk','csdn','gm','gb','pwd','qq','tk','a')")

    # language=sql
    if not exec_sql("select * from e_upms_menu where name='请删除'", json_str=False):
        exec_sql(
            "INSERT INTO erupt.e_upms_menu "
            "(id, create_time, update_time, code, icon, name, param, power_off, sort, status, type, value, create_user_id, update_user_id, parent_menu_id)"
            " VALUES (null, null, null, 'my_simple', null, '请删除', null, null, 80, 1, 'table', 'my_simple', 1, null, 1);")

    exec_sql('delete from e_upms_menu where parent_menu_id=7')
    exec_sql('delete from e_upms_menu where id > 2 and id <= 10')
    # exec_sql('create table  test (?)', 'asf')

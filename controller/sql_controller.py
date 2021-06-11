from lib import *
import time
import json


# this file is sqlite queries

# language=sql
def insert_user(u, p):
    return exec_sql('insert into user_info_table values (null,?,?,null,null,null,null,null,null,null)', u, p,
                    json_str=True)


# language=sql
def get_user_tags(user_name):
    return exec_sql(
        'select tag_id from article_tag_link_table where tag_id in '
        '(select tag_id from article_tag_link_table where article_id in '
        '(select article_id from article_user_link_table where user_id='
        '(select id as user_id from user_info_table where user_name=?)'
        '))', user_name, single_result_detection=False)


# language=sql
def get_tag_name_by_id(tag_id):
    return exec_sql('select * from tag_table where tag_table.id=?', tag_id)


def login_to_get_token(u, p):
    r = exec_sql('select * from user_info_table where user_name=? ', u, json_str=False)
    token = f'{time.time()}{ml.random(0, 999)}'
    if not r:
        exec_sql('insert into user_info_table values (null,?,?,null,null,null,null,?,null,null)', u, p, token)
    exec_sql('update user_info_table set token=? where user_name=?', token, u)
    return exec_sql('select token from user_info_table where user_name=? and password=?', u, p)


def get_user_public_info_by_name(user_name):
    return exec_sql('''
    select announcement,github,qq,csdn,game,announcement_link from user_info_table where user_name=?
    ''', user_name)


def get_user_private_info_by_token(token):
    return exec_sql('''
    select * from user_info_table where token=?;
    ''', token)


# http://127.0.0.1:8000/blog?type=select_article_by_text&search=2&user=a
def select_article_by_text(search, user):
    # print(exec_sql('select user_id from user_info_table where user_name=?', user))

    # return exec_sql('''
    # select article_title,time13 from article_table where article_content like ?
    # or article_description like ?
    # and user_id = (select user_id from user_info_table where user_name=?)
    # ''', f"%{search}%", f"%{search}%", user, single_result_detection=False)

    return exec_sql('''
        select article_title,time13 from article_table 
        where  article_title like ? or article_description like ?
        and 
        id in (select article_id from article_user_link_table where user_id = (select id from user_info_table where user_name=?))
        ''', f"%{search}%",f"%{search}%", user, single_result_detection=False)


def update_user_info(token, announcement, github, qq, csdn):
    return exec_sql('''
        update user_info_table set announcement = ? 
        and github=?
        and qq=?
        and csdn=? 
        where token=?;
    ''', announcement, github, qq, csdn, token)


def select_article_id_by_user_name(user_name):
    return exec_sql('''
    select distinct article_id from article_user_link_table where user_id=(
        select user_id from user_info_table where user_name=?
    )
    ''', user_name, single_result_detection=False)


def select_article_info_by_user_name_and_page(user_name, page):
    return exec_sql('''
    select article_title,time13 from article_table where id=
     (select article_id from article_user_link_table where  user_id=(
        select id from user_info_table where user_name=?)
    ) order by time13 desc limit ?,?
    ''', user_name, int(page), int(page) + 10, single_result_detection=False)


def get_article_content(article_id):
    return exec_sql('''
    select article_content,article_title from article_table where id=?
    ''', article_id)


# def recent_article(user_name):
#     return exec_sql('''
#     select article_id from article_user_link_table where user_id = (select id from user_info_table where user_name=?)
#     order by time13 desc
#     limit 5
#     ''', user_name, single_result_detection=False)

def recent_article(user_name):
    return exec_sql('''
    select article_id from article_user_link_table where user_id = (select id from user_info_table where user_name=?)
    limit 5
    ''', user_name, single_result_detection=False)


def hot_article(user_name):
    return exec_sql('''
    select * from article_table
    order by visit_count desc limit 5
    ''', user_name, single_result_detection=False)


def select_article_id_picture_description(article_id):
    return exec_sql('''
        select id as article_id,picture_url,article_description
        from article_table where id=?
        ''', article_id)


def update_user_name(token, name):
    return exec_sql('''update user_info_table set user_name=? where token=?''', name, token)
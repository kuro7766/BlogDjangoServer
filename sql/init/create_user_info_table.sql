create table if not exists user_info_table
(
    id           integer primary key autoincrement ,
    user_name    text       ,
    password     text       ,
    announcement text,
    github       text,
    qq           text,
    csdn         text,
    token        text,
    game         text,
    announcement_link text
);
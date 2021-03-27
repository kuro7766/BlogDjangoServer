create table if not exists user_info_table
(
    id           integer primary key autoincrement,
    user_name    text unique not null,
    password     text        not null,
    announcement text,
    github       text,
    qq           text,
    csdn         text,
    token        text,
    game         text,
    announcement_link text
);
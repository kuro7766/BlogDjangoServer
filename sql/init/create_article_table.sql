create table if not exists article_table
(
    article_id          integer primary key autoincrement,
    user_id             integer,
    article_content     text,
    visit_count         integer,
    article_description text,
    picture_url         text,
    create_time         integer,
    article_title text,
    time13  text
);
create table if not exists article_comments_table
(
    comment_id   integer primary key autoincrement,
    article_id   integer,
    comment_json text,
    time13 integer
);
create table if not exists tag_table
(
    tag_name text unique ,
    tag_id   integer primary key autoincrement
);
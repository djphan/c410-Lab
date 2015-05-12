drop table if exists todolist;

create table todolist (
    rowid INTEGER primary key autoincrement,
	category text,
	priority INTEGER,
	description text 

);

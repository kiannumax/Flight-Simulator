All of the modules were written and tested on a MAC

Program currently uses a local based database, so it will not work on any other machine that doesn't
have the same database with same credentials.
Eventually this project will move to a cloud database, so multi-machine work will be possible.

Program currently uses 6 libraries(modules):
  4 built-in python3 libraries(modules): socket, sys, datetime, random
  And 2 global libraries(modules) which required an installation: bcrypt, geopy




SQL queries that were run to modify the structure of the table (also includes some test queries):
-------------------------------------------------------
drop table goal_reached;
drop table goal;
drop table users;

create table users(
    id int not null auto_increment,
    date_registered varchar(15) not null,
    IP varchar(20) not null,
    password varchar(50) not null,
    username varchar(15) not null,
    Primary key (ID)
)

SELECT COUNT(1) FROM users WHERE username = 'supremepirate' and password = 'tutik';

alter table users modify password nvarchar(72);
alter table games modify initial_airport varchar(40);

INSERT INTO users (username, password, date_registered, IP)
VALUES ('puprim', "agsd", '34,5', '124.0.0'), ('puprim', "agsd", '34,5', '124.0.0');
SELECT ROW_COUNT();

delete from users;
drop table game;

create table games(
    id int not null auto_increment,
    date_played date not null,
    initial_airport varchar(20) not null,
    distance double not null,
    airports_visited int not null,
    user_id int not null,
    Primary key (id),
    foreign key (user_id) references users(id)
);


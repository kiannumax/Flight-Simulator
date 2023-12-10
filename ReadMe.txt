Entire application was written and tested on MACs

Program currently uses a local based database, so it will not work on any other machine that doesn't
have the same database with same credentials.

Program currently uses 6 Python libraries(modules):
  2 built-in Python3 libraries(modules): datetime, random
  And 5 global libraries(modules) which required an installation: bcrypt, geopy, Flask, CORS, mysql.connector

Flask server is running on http://127.0.0.1:5000 on main.py file and has 11 different API Calls Handlers
main.py file imports all functions from different modules located under "backend" directory

All of those calls are coming from a different tab where HTML and their JavaScript files are opened and executed.
In total there are 5 different HTML files/pages.

-------------------------------------------------------------------------------------------------------------------------------

One additional API call was used in the application:

'https://api.ipify.org/?format=json' from  (https://www.ipify.org/)
It returns user's public IP address in JSON format {'ip': ....}

-------------------------------------------------------------------------------------------------------------------------------

JavaScript scripts did not have any external modules.
Only import and exports used between the scripts under the same directory

-------------------------------------------------------------------------------------------------------------------------------

3 Different Font styles were used throughout 5 different pages:

    Rubik (https://fonts.google.com/specimen/Rubik?query=rubik)
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Coiny&family=Rubik:wght@400;500;600;700&family=Sono:wght@400;600;700&display=swap" rel="stylesheet">

        font-family: 'Rubik', sans-serif;

    Roboto Slab (https://fonts.google.com/specimen/Roboto+Slab)
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto+Slab&display=swap" rel="stylesheet">

        font-family: 'Roboto Slab', sans-serif;

   Dhurjati (https://fonts.google.com/specimen/Dhurjati)
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Dhurjati&display=swap" rel="stylesheet">

        font-family: 'Dhurjati', sans-serif;

-------------------------------------------------------------------------------------------------------------------------------

Several ideas were taken from researching, but all of them were implemented manually with no copying. For example, custom
Alert, Confirm, and Prompt popups. But there was one element that was copied from external source:

The svg tag and its animation from game.html
However, little portion of CSS was modified.

Source: https://codepen.io/webduke/pen/RydqXg

-------------------------------------------------------------------------------------------------------------------------------

SQL queries that were run to modify the structure of the table:

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


alter table users modify password nvarchar(72);
alter table games modify initial_airport varchar(40);

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

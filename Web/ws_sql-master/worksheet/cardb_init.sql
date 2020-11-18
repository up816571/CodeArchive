create database if not exists ws_sql_example;

create table if not exists ws_sql_example.Cars (
  id int primary key auto_increment,
  reg varchar(8),
  make varchar(30),
  model varchar(15),
  year int(4),
  price decimal(12,2)
);

create database picgram;
create table picgram.signup(id int auto_increment primary key, email varchar(100), fullname varchar(100), username varchar(100), password varchar(100), created_by datetime, is_verify int , otp varchar(100));
select * from picgram.signup;

#also run this command
alter table picgram.signup add column bio varchar(1000) ;
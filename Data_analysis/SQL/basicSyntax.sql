# Data definition 
# The create statement 

create database Tertiary; 
use Tertiary;
create table students (name varchar(20));
#alter table students add column object_name database

alter table students add column age int;
alter table students
add column location varchar(20);

# rename object_type object_name to new_object_name
rename table students to Members;

create table info (age int);
DROP TABLE info; 

# TRUNCATE object_type object_name; 

TRUNCATE TABLE Members;


# Data manipulation language 
# Syntax: select * from object_name 

select * from employees;
use employees;

create database quiz_db;
use quiz_db;
create table questions(
id int auto_increment primary key,
question text not null,
option1 varchar(255),
option2 varchar(255),
option3 varchar(255),
option4 varchar(255),
answer varchar(255)
);
insert into questions(question,option1,option2,option3,option4,answer) values
('which command in linux terminal changes the current working directory to a specified directory?','ls','pwd','nano','cd','cd');
('which command creates a new directory?','man','cd','mkdir','ls','mkdir');
('which command displays the content of the file?','cat','touch','echo','cd','cat');
('which command lists the previously executed commands on the terminal?','clear','grep','find','history','history');


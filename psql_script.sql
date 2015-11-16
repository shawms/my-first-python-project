create database bank;
\c bank;
drop table bank_account;
drop table transactions;

create table bank_account (
    username    varchar(100) primary key
);

create table transactions (
    username    varchar(100) references bank_account(username),
    amount      integer
);

insert into bank_account values('shawnsaccount');
insert into transactions values('shawnsaccount', 23);
insert into transactions values('shawnsaccount', -15);
insert into transactions values('shawnsaccount', 10);
insert into transactions values('shawnsaccount', -7);

drop table if exists accounts;
drop table if exists clients;

create table clients (id serial primary key,
					  "name" varchar(100) not null);

create table accounts (id serial primary key,
					   client_id int not null,
					   account_type varchar(100) not null,
					   balance float not null check (balance >= 0));

alter table accounts
add constraint fk_client
foreign key (client_id)
references clients(id);



--Default values
insert into clients values (default, 'Susan');
insert into clients values (default, 'Patrick');
insert into clients values (default, 'Barbara');
insert into clients values (default, 'Stacy');
insert into clients values (default, 'Leroy');
insert into clients values (default, 'Tony');
insert into clients values (default, 'Tamara');
insert into clients values (default, 'Blake');
insert into clients values (default, 'Jamie');
insert into accounts values (default, 1, 'Checking', 10);
insert into accounts values (default, 2, 'Checking', 200);
insert into accounts values (default, 2, 'Savings', 300);
insert into accounts values (default, 2, 'Retirement', 1000);
insert into accounts values (default, 3, 'Checking', 110);
insert into accounts values (default, 4, 'Checking', 222);
insert into accounts values (default, 5, 'Checking', 3030);
insert into accounts values (default, 6, 'Savings', 404040);
insert into accounts values (default, 6, 'Retirement', 674536);
insert into accounts values (default, 7, 'Checking', 100);
drop table if exists accounts;
drop table if exists clients;

create table clients (id serial primary key,
					  "name" varchar(100) not null);

create table accounts (id serial primary key,
					   client_id int not null,
					   account_type varchar(100) not null,
					   balance money not null check (balance >= money(0)));
		
alter table accounts
add constraint fk_client
foreign key (client_id)
references clients(id);

		

--Default values
insert into clients values (default, 'Susan');
insert into clients values (default, 'Patrick');
insert into clients values (default, 'Barbara');
insert into accounts values (default, 1, 'Checking', 0);
insert into accounts values (default, 2, 'Savings', 200);
insert into accounts values (default, 3, 'Checking', 0);



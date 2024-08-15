create table Tasks(
	task_id varchar(10) NOT null primary key ,
	task_dueDate char(10) null,
	
	task_type char(1) not null,
	constraint check_task_type check (task_type in ('w','s','p','t')),
	
	task_name varchar(100) not null ,
	constraint check_task_name check (task_name like '%[a-zA-Z]%' or task_name like '%[א-ת]%' ),
	
		
	task_creationDate char(10) not null,
	constraint check_task_creationDate check (task_creationDate like  '[0-3][0-9]-[0-1][0-9]-[1-2][0-9][0-9][0-9]'),
	
	task_completeDate char(10) null,
	constraint check_task_completeDate check (task_completeDate like  '[0-3][0-9]-[0-1][0-9]-[1-2][0-9][0-9][0-9]'),
	

);






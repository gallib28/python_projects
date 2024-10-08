create table Tasks(
	task_id integer NOT null primary key AUTOINCREMENT ,
	task_dueDate char(10) null,
	
	task_type char(1) not null,
	constraint check_task_type check (task_type in ('w','s','p','t')),
	
	task_description varchar(100) not null ,
	constraint check_task_description check (task_description like '%[a-zA-Z]%' or task_name like '%[א-ת]%' ),
	
		
	task_status char(10) not null,
	constraint check_task_status check (task_status in (0,1)),
	
	task_completeDate char(10) null,
	constraint check_task_completeDate check (task_completeDate like  '[0-3][0-9]-[0-1][0-9]-[1-2][0-9][0-9][0-9]'),
	user_id integer , 
	FOREIGN KEY (user_id) references users(user_id) 

);

create table users (
	user_id char(1) not null primary key AUTOINCREMENT,
	task_id varchar(10) NOT null ,
	FOREIGN KEY (task_id) references Tasks(task_id) 
);


-- inserting to tasks 
insert into tasks(task_id,task_dueDate,task_name,task_status,task_completeDate) values (?,?,?,?,?)
-- inserting into users 
insert into users(user_id,task_id) values (?,?)





--update due_date
update table tasks 
set task_dueDate = {dueDate}
where user_id = {userId}, task_id={taskId}

--update task_type
update table tasks 
set task_type = {taskType}
where user_id = {userId}, task_id={taskId}

--update task_completeDate
update table tasks 
set task_completeDate = {taskCompleteDate}
where user_id = {userId}, task_id={taskId}

--update task_status
update table tasks 
set task_status = {taskStatus}
where user_id = {userId}, task_id={taskId}

--update task_description
update table tasks 
set task_description = {taskDescription}
where user_id = {userId}, task_id={taskId}



-- query to check due less than 5 
select task_dueDate 
from tasks 
where task_dueDate<= 5 ;
 
-- query to give the avg of finishing the tasks  
select avg(task_completeDate) 
from tasks  ; 

-- all task table 
SELECT * FROM Tasks;

-- Select all tasks for a specific user
SELECT * FROM Tasks WHERE user_id = {userId}; 

	-- Select specific task details
SELECT task_description, task_dueDate FROM Tasks WHERE task_id = {taskId};

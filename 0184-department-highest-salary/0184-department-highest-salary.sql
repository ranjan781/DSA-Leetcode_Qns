# Write your MySQL query statement below
-- Write your PostgreSQL query statement below
select d.name Department ,e.name Employee , e.salary Salary 
from Employee e 
join department d
on e.departmentId=d.Id
where (e.departmentId,e.salary) in(select departmentId, max(salary) from employee group by departmentId)
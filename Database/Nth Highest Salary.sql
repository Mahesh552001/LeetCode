CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      select distinct salary from (select Salary, dense_rank() over(order by Salary desc) as R from employee) as E where E.R=N
  );
END
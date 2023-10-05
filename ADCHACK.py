          Advance Database Concepts Practical 

 

Practical – 1 

Aim:  Writing PL/SQL Blocks with basic programming constructs by including following:  
 A. If...then...Else, IF...ELSIF...ELSE... END IF          B. Case statement 

(A) 
a. Write a PL/SQL program to take a numeric input from the user and check whether a user has entered an even number or an odd number using IF THEN ELSE statement. 

DECLARE 

   user_input NUMBER; 

BEGIN 

   -- Prompt the user for input 

   DBMS_OUTPUT.PUT('Enter a number: '); 

   -- Read the user's input 

   ACCEPT user_input NUMBER PROMPT ' '; 

    

   -- Check if the entered number is even or odd 

   IF MOD(user_input, 2) = 0 THEN 

      DBMS_OUTPUT.PUT_LINE('You entered an even number.'); 

   ELSE 

      DBMS_OUTPUT.PUT_LINE('You entered an odd number.'); 

   END IF; 

END; 

/ 

b. Write a PL/SQL program to find the greatest number among two given numbers. 

DECLARE 

   num1 NUMBER; 

   num2 NUMBER; 

   greatest NUMBER; 

BEGIN 

   -- Prompt the user for the first number 

   DBMS_OUTPUT.PUT('Enter the first number: '); 

   ACCEPT num1 NUMBER PROMPT ' '; 

 

   -- Prompt the user for the second number 

   DBMS_OUTPUT.PUT('Enter the second number: '); 

   ACCEPT num2 NUMBER PROMPT ' '; 

 

   -- Determine the greatest number 

   IF num1 > num2 THEN 

      greatest := num1; 

   ELSE 

      greatest := num2; 

   END IF; 

 

   -- Display the greatest number 

   DBMS_OUTPUT.PUT_LINE('The greatest number is: ' || greatest); 

END; 

/ 

B) 
a. Write a PL/SQL program to take input from a user for age and print a message according to the age entered by the user using IF THEN ELSIF ELSE END IF statement. (age<11 ‘I am Child’, age<20 ‘I am Young’, age<40 ‘I am in Thirties’, else ‘I am always Young’). 

DECLARE 

   age NUMBER; 

BEGIN 

   -- Prompt the user for their age 

   DBMS_OUTPUT.PUT('Enter your age: '); 

   ACCEPT age NUMBER PROMPT ' '; 

    

   -- Check the age and print a message accordingly 

   IF age < 11 THEN 

      DBMS_OUTPUT.PUT_LINE('I am Child'); 

   ELSIF age < 20 THEN 

      DBMS_OUTPUT.PUT_LINE('I am Young'); 

   ELSIF age < 40 THEN 

      DBMS_OUTPUT.PUT_LINE('I am in Thirties'); 

   ELSE 

      DBMS_OUTPUT.PUT_LINE('I am always Young'); 

   END IF; 

END; 

/ 

b. Write a PL/SQL program to print the grade based on the given marks with else condition (mark >= 70 ‘Grade A’, mark >=40 and mark<70 ‘Grade B’, mark >=35 and mark<40 ‘Grade C’, else "NoGrade'). 

DECLARE 

   marks NUMBER; 

   grade VARCHAR2(10); 

BEGIN 

   -- Prompt the user for the marks 

   DBMS_OUTPUT.PUT('Enter your marks: '); 

   ACCEPT marks NUMBER PROMPT ' '; 

    

   -- Determine the grade based on the marks 

   IF marks >= 70 THEN 

      grade := 'Grade A'; 

   ELSIF marks >= 40 THEN 

      grade := 'Grade B'; 

   ELSIF marks >= 35 THEN 

      grade := 'Grade C'; 

   ELSE 

      grade := 'NoGrade'; 

   END IF; 

 

   -- Display the grade 

   DBMS_OUTPUT.PUT_LINE('Your grade is: ' || grade); 

END; 

/ 

(C) 
a. Write a PL/SQL program to demonstrate a Simple CASE statement. 

DECLARE 

   day_of_week NUMBER; 

   day_name VARCHAR2(20); 

BEGIN 

   -- Prompt the user for the day of the week (1-7) 

   DBMS_OUTPUT.PUT('Enter the day of the week (1-7): '); 

   ACCEPT day_of_week NUMBER PROMPT ' '; 

 

   -- Use a CASE statement to determine the day name 

   CASE day_of_week 

      WHEN 1 THEN day_name := 'Sunday'; 

      WHEN 2 THEN day_name := 'Monday'; 

      WHEN 3 THEN day_name := 'Tuesday'; 

      WHEN 4 THEN day_name := 'Wednesday'; 

      WHEN 5 THEN day_name := 'Thursday'; 

      WHEN 6 THEN day_name := 'Friday'; 

      WHEN 7 THEN day_name := 'Saturday'; 

      ELSE day_name := 'Invalid day'; 

   END CASE; 

 

   -- Display the day name 

   DBMS_OUTPUT.PUT_LINE('The day is ' || day_name); 

END; 

/ 

b. Write a PL/SQL program to demonstrate a Searched CASE statement. 

DECLARE 

   score NUMBER; 

   grade VARCHAR2(2); 

BEGIN 

   -- Prompt the user for the score (0-100) 

   DBMS_OUTPUT.PUT('Enter your score (0-100): '); 

   ACCEPT score NUMBER PROMPT ' '; 

 

   -- Use a Searched CASE statement to determine the grade 

   CASE 

      WHEN score >= 90 THEN grade := 'A'; 

      WHEN score >= 80 THEN grade := 'B'; 

      WHEN score >= 70 THEN grade := 'C'; 

      WHEN score >= 60 THEN grade := 'D'; 

      ELSE grade := 'F'; 

   END CASE; 

 

   -- Display the grade 

   DBMS_OUTPUT.PUT_LINE('Your grade is ' || grade); 

END; 

/ 

 

 

Practical – 2: 

Aim: Writing Procedures in PL/SQL Block  

    Create an empty procedure, replace a procedure and call procedure 

-- Create an empty procedure 

CREATE OR REPLACE PROCEDURE empty_procedure AS 

BEGIN 

   NULL; -- Empty procedure, does nothing 

END empty_procedure; 

/ 

 

-- Call the empty procedure 

BEGIN 

   empty_procedure; 

END; 

/ 

b.Create a stored procedure and call it  

-- Create a stored procedure 

CREATE OR REPLACE PROCEDURE greet(name_in VARCHAR2) AS 

BEGIN 

   DBMS_OUTPUT.PUT_LINE('Hello, ' || name_in || '!'); 

END greet; 

/ 

 

-- Call the stored procedure 

BEGIN 

   greet('John'); 

END; 

/ 

c.Define procedure to insert data  

-- Create a procedure to insert data into a table 

CREATE OR REPLACE PROCEDURE insert_data(emp_id NUMBER, emp_name VARCHAR2) AS 

BEGIN 

   INSERT INTO employee(emp_id, emp_name) VALUES (emp_id, emp_name); 

   COMMIT; 

END insert_data; 

/ 

 

-- Call the procedure to insert data 

BEGIN 

   insert_data(101, 'Alice'); 

   insert_data(102, 'Bob'); 

END; 

/ 

d.A forward declaration of procedure   

-- Forward declaration of a procedure 

DECLARE 

   PROCEDURE my_procedure; 

END; 

/ 

 

-- Define and implement the procedure 

CREATE OR REPLACE PROCEDURE my_procedure AS 

BEGIN 

   DBMS_OUTPUT.PUT_LINE('This is my procedure.'); 

END my_procedure; 

/ 

 

-- Call the procedure 

BEGIN 

   my_procedure; 

END; 

/ 

1.create a procedure to swap numbers. 

CREATE OR REPLACE PROCEDURE swap_numbers( 

   INOUT num1 IN OUT NUMBER, 

   INOUT num2 IN OUT NUMBER 

) AS 

   temp NUMBER; 

BEGIN 

   temp := num1; 

   num1 := num2; 

   num2 := temp; 

END swap_numbers; 

/ 

2. create a procedure to find minimum of two numbers. 

CREATE OR REPLACE PROCEDURE find_minimum( 

   num1 NUMBER, 

   num2 NUMBER, 

   OUT min_number OUT NUMBER 

) AS 

BEGIN 

   IF num1 < num2 THEN 

      min_number := num1; 

   ELSE 

      min_number := num2; 

   END IF; 

END find_minimum; 

/ 

3. create a stored procedure and call it 

CREATE OR REPLACE PROCEDURE get_employee_details( 

   emp_id_in NUMBER, 

   emp_name_out OUT VARCHAR2 

) AS 

BEGIN 

   SELECT emp_name INTO emp_name_out 

   FROM employee 

   WHERE emp_id = emp_id_in; 

END get_employee_details; 

/ 

 

-- Call the procedure 

DECLARE 

   emp_name VARCHAR2(50); 

BEGIN 

   get_employee_details(101, emp_name); 

   DBMS_OUTPUT.PUT_LINE('Employee Name: ' || emp_name); 

END; 

/ 

4. define procedure to insert data. 

CREATE OR REPLACE PROCEDURE insert_employee_data( 

   emp_id NUMBER, 

   emp_name VARCHAR2 

) AS 

BEGIN 

   INSERT INTO employee(emp_id, emp_name) VALUES (emp_id, emp_name); 

   COMMIT; 

END insert_employee_data; 

/ 

 
5. define procedure to update data. 

CREATE OR REPLACE PROCEDURE update_employee_name( 

   emp_id NUMBER, 

   new_name VARCHAR2 

) AS 

BEGIN 

   UPDATE employee 

   SET emp_name = new_name 

   WHERE emp_id = emp_id; 

   COMMIT; 

END update_employee_name; 

/ 

 

 

 

 

 

 

 

 

 

 

Practical – 3 

Aim: Writing PL/SQL Blocks with basic programming constructs by including a GOTO to jump out of a loop and NULL as a statement inside IF.   

    Aim: Writing PL/SQL Blocks with basic programming constructs by including a GOTO to jump out of a loop and NULL as a statement inside IF. 

DECLARE 

   counter NUMBER := 1; 

BEGIN 

   -- Loop from 1 to 10 

   <<my_loop>> 

   LOOP 

      IF counter > 10 THEN 

         EXIT my_loop; -- Use GOTO-like behavior to exit the loop 

      END IF; 

       

      -- Print numbers 1 to 10 

      DBMS_OUTPUT.PUT_LINE(counter); 

      counter := counter + 1; 

   END LOOP; 

 

   -- Use NULL as a statement inside an IF block 

   IF counter > 5 THEN 

      NULL; -- Do nothing 

   ELSE 

      DBMS_OUTPUT.PUT_LINE('Counter is not greater than 5.'); 

   END IF; 

END; 

/ 

B)Aim: Writing PL/SQL Blocks with basic programming constructs by including a GOTO to jump out of a loop. 

DECLARE 

   counter NUMBER := 1; 

BEGIN 

   -- Loop from 1 to 10 

   <<my_loop>> 

   LOOP 

      -- Check the condition to exit the loop 

      IF counter > 10 THEN 

         GOTO exit_loop; -- Use GOTO to jump out of the loop 

      END IF; 

       

      -- Print numbers 1 to 10 

      DBMS_OUTPUT.PUT_LINE(counter); 

      counter := counter + 1; 

   END LOOP; 

 

   <<exit_loop>> -- Label to jump to 

   DBMS_OUTPUT.PUT_LINE('Loop exited.'); 

END; 

/ 

(C) Aim: Writing PL/SQL Blocks to demonstrate a Simple GOTO Statement. 

DECLARE 

   x NUMBER := 5; 

BEGIN 

   IF x > 0 THEN 

      GOTO my_label; 

   END IF; 

 

   DBMS_OUTPUT.PUT_LINE('This line is executed when x is not greater than 0'); 

 

   <<my_label>> 

   DBMS_OUTPUT.PUT_LINE('This line is executed when x is greater than 0'); 

END; 

/ 

 

 

 

 

 

 

 

 

Practical – 4 

Aim: Writing PL/SQL Blocks with basic programming constructs for following Iterative 
Structure:  
 a. While-loop Statements       b. For-loop Statements.   

(A) 
a. Write a PL/SQL program to print number from 1 to 5 using WHILE loop statement. 

DECLARE 

   counter NUMBER := 1; 

BEGIN 

   WHILE counter <= 5 LOOP 

      DBMS_OUTPUT.PUT_LINE(counter); 

      counter := counter + 1; 

   END LOOP; 

END; 

/ 

b. Write a PL/SQL program to print the odd numbers between 1 to 10 using the while loop. 

DECLARE 

   counter NUMBER := 1; 

BEGIN 

   WHILE counter <= 10 LOOP 

      IF MOD(counter, 2) = 1 THEN 

         DBMS_OUTPUT.PUT_LINE(counter); 

      END IF; 

      counter := counter + 1; 

   END LOOP; 

END; 

/ 

c. Write a PL/SQL program to print the numbers between 1 to N using the while loop. 

DECLARE 

   n NUMBER := 10; -- Change this value to set the upper limit 

   counter NUMBER := 1; 

BEGIN 

   WHILE counter <= n LOOP 

      DBMS_OUTPUT.PUT_LINE(counter); 

      counter := counter + 1; 

   END LOOP; 

END; 

/ 

(B) 
a. Write a PL/SQL program to print numbers from 1 to 10 using FOR loop statement. 

BEGIN 

   FOR counter IN 1..10 LOOP 

      DBMS_OUTPUT.PUT_LINE(counter); 

   END LOOP; 

END; 

/ 

 
b. Write a PL/SQL program to print the number in reverse order. 

BEGIN 

   FOR counter IN REVERSE 10..1 LOOP 

      DBMS_OUTPUT.PUT_LINE(counter); 

   END LOOP; 

END; 

/ 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Practical – 5: 

Aim: Writing Functions in PL/SQL Block.  
 a. Define and call a function 

-- Define a PL/SQL function 

CREATE OR REPLACE FUNCTION calculate_sum(a NUMBER, b NUMBER) 

RETURN NUMBER IS 

  result NUMBER; 

BEGIN 

  result := a + b; 

  RETURN result; 

END calculate_sum; 

 

-- Call the function and store the result in a variable 

DECLARE 

  x NUMBER := 10; 

  y NUMBER := 20; 

  sum_result NUMBER; 

BEGIN 

  sum_result := calculate_sum(x, y); 

  DBMS_OUTPUT.PUT_LINE('The sum is: ' || sum_result); 

END; 

 b. Define and use function in select clause 

Define the Function: 

CREATE OR REPLACE FUNCTION calculate_discount(total_amount NUMBER) RETURN NUMBER IS 

  discount NUMBER; 

BEGIN 

  IF total_amount >= 1000 THEN 

    discount := total_amount * 0.1; -- 10% discount 

  ELSE 

    discount := 0; -- No discount 

  END IF; 

  RETURN discount; 

END calculate_discount; 

Use the Function in a SELECT Clause: 

SELECT 

  invoice_number, 

  total_amount, 

  calculate_discount(total_amount) AS discount_amount 

FROM 

  invoices; 
 c. Call function in dbms_output.put_line  

-- Create a simple function 

CREATE OR REPLACE FUNCTION add_numbers(a NUMBER, b NUMBER) RETURN NUMBER IS 

  result NUMBER; 

BEGIN 

  result := a + b; 

  RETURN result; 

END add_numbers; 

 

-- Use the function within DBMS_OUTPUT.PUT_LINE 

BEGIN 

  DBMS_OUTPUT.PUT_LINE('The sum is: ' || TO_CHAR(add_numbers(5, 7))); 

END; 

/ 

Output: 

The sum is: 12 
 d. Recursive function 

DECLARE 

  result NUMBER; 

BEGIN 

  result := factorial(5); -- Calculate factorial of 5 

  DBMS_OUTPUT.PUT_LINE('Factorial of 5 is: ' || result); 

END; 

/ 

Output: 

Factorial of 5 is: 120 

e. Count Employee from a function and return value back  

Create table ‘employees’: 

CREATE TABLE employees ( 

  emp_id NUMBER, 

  emp_name VARCHAR2(50) 

); 
Create a function to count the employees: 

 CREATE OR REPLACE FUNCTION count_employees RETURN NUMBER IS 

  emp_count NUMBER; 

BEGIN 

  -- Use a SELECT statement to count the employees 

  SELECT COUNT(*) INTO emp_count FROM employees; 

 

  -- Return the count 

  RETURN emp_count; 

END count_employees; 

/ 

Call the function to get the count of employees: 

DECLARE 

  num_employees NUMBER; 

BEGIN 

  num_employees := count_employees(); -- Call the function 

  DBMS_OUTPUT.PUT_LINE('Number of Employees: ' || num_employees); 

END; 

/ 

f. Call function and store the return value to a variable 

Create a function called calculate_salary that calculates the salary of an employee based on some input parameters: 

CREATE OR REPLACE FUNCTION calculate_salary(emp_id NUMBER) RETURN NUMBER IS 

  salary NUMBER; 

BEGIN 

  -- Calculate salary based on emp_id 

  -- For demonstration purposes, let's assume a simple calculation 

  SELECT salary INTO salary FROM employees WHERE emp_id = emp_id; 

  RETURN salary; 

END calculate_salary; 

/ 

call this function and store the return value in a variable: 

DECLARE 

  emp_salary NUMBER; 

  employee_id NUMBER := 123; -- Replace with the desired employee ID 

BEGIN 

  emp_salary := calculate_salary(employee_id); -- Call the function and store the return value 

  DBMS_OUTPUT.PUT_LINE('Employee Salary: ' || emp_salary); 

END; 

/ 

A)Write a PL/SQL block to create a function to find maximum of two numbers. 

SET SERVEROUTPUT ON; 

 

CREATE OR REPLACE FUNCTION find_maximum(num1 NUMBER, num2 NUMBER) RETURN NUMBER IS 

    max_num NUMBER; 

BEGIN 

    IF num1 >= num2 THEN 

        max_num := num1; 

    ELSE 

        max_num := num2; 

    END IF; 

 

    RETURN max_num; 

END; 

/ 

 

DECLARE 

    num1 NUMBER := 10; 

    num2 NUMBER := 20; 

    max_value NUMBER; 

BEGIN 

    -- Call the function to find the maximum of two numbers 

    max_value := find_maximum(num1, num2); 

    DBMS_OUTPUT.PUT_LINE('The maximum of ' || num1 || ' and ' || num2 || ' is: ' || max_value); 

END; 

/ 

OUTPUT: 

The maximum of 10 and 20 is: 20 

B)Write a PL/SQL block to create a function to find square of a number. 

SET SERVEROUTPUT ON; 

 

CREATE OR REPLACE FUNCTION calculate_square(num NUMBER) RETURN NUMBER IS 

    square NUMBER; 

BEGIN 

    square := num * num; 

    RETURN square; 

END; 

/ 

 

DECLARE 

    input_num NUMBER := 5; 

    result_square NUMBER; 

BEGIN 

    -- Call the function to find the square of the number 

    result_square := calculate_square(input_num); 

    DBMS_OUTPUT.PUT_LINE('The square of ' || input_num || ' is: ' || result_square); 

END; 

/ 

OUTPUT: 

The square of 5 is: 25 

C)Write a PL/SQL block to create a function to find the total strength of Students using functions present in different departments. 

SET SERVEROUTPUT ON; 

 

-- Sample tables for demonstration purposes 

CREATE TABLE departments ( 

    department_id NUMBER, 

    department_name VARCHAR2(50), 

    student_count NUMBER 

); 

 

CREATE TABLE students ( 

    student_id NUMBER, 

    student_name VARCHAR2(100), 

    department_id NUMBER 

); 

 

-- Sample data for demonstration purposes 

INSERT INTO departments (department_id, department_name, student_count) 

VALUES (1, 'Computer Science', 100); 

 

INSERT INTO departments (department_id, department_name, student_count) 

VALUES (2, 'Electronics', 80); 

 

INSERT INTO students (student_id, student_name, department_id) 

VALUES (1, 'John Doe', 1); 

 

INSERT INTO students (student_id, student_name, department_id) 

VALUES (2, 'Jane Smith', 1); 

 

INSERT INTO students (student_id, student_name, department_id) 

VALUES (3, 'Michael Johnson', 2); 

 

INSERT INTO students (student_id, student_name, department_id) 

VALUES (4, 'Emily Brown', 2); 

 

-- Function to find the total strength of students using different departments 

CREATE OR REPLACE FUNCTION calculate_total_strength RETURN NUMBER IS 

    total_strength NUMBER := 0; 

BEGIN 

    -- Loop through departments and sum up student counts 

    FOR dept_rec IN (SELECT student_count FROM departments) 

    LOOP 

        total_strength := total_strength + dept_rec.student_count; 

    END LOOP; 

 

    RETURN total_strength; 

END; 

/ 

 

DECLARE 

    total_students NUMBER; 

BEGIN 

    -- Call the function to find the total strength of students 

    total_students := calculate_total_strength; 

    DBMS_OUTPUT.PUT_LINE('Total strength of students: ' || total_students); 

END; 

/ 

 

Output: 

Total strength of students: 180 

D)Writing a recursive Functions in PL/SQL Block. 

SET SERVEROUTPUT ON; 

 

CREATE OR REPLACE FUNCTION calculate_factorial(n NUMBER) RETURN NUMBER IS 

BEGIN 

    -- Base case: factorial of 0 is 1 

    IF n = 0 THEN 

        RETURN 1; 

    ELSE 

        -- Recursive call: factorial(n) = n * factorial(n - 1) 

        RETURN n * calculate_factorial(n - 1); 

    END IF; 

END; 

/ 

 

DECLARE 

    input_num NUMBER := 5; 

    result_factorial NUMBER; 

BEGIN 

    -- Call the recursive function to calculate factorial 

    result_factorial := calculate_factorial(input_num); 

    DBMS_OUTPUT.PUT_LINE('The factorial of ' || input_num || ' is: ' || result_factorial); 

END; 

/ 

OUTPUT: 

The factorial of 5 is: 120 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Practical – 6: 

Aim: Creating and working with Insert/Update/Delete Trigger using Before/After clause. 

    Aim: Salary difference  

CREATE OR REPLACE TRIGGER salary_difference_trigger 

BEFORE UPDATE OF salary ON employees 

FOR EACH ROW 

BEGIN 

   IF :new.salary - :old.salary BETWEEN 10 AND 15 THEN 

      -- Calculate and log the salary difference 

      INSERT INTO salary_changes_log (employee_id, old_salary, new_salary, change_date) 

      VALUES (:new.employee_id, :old.salary, :new.salary, SYSDATE); 

   END IF; 

END; 

/ 

    Aim: Trigger Uses Conditional Predicates to Detect Triggering Statement  

CREATE OR REPLACE TRIGGER conditional_trigger 

BEFORE INSERT OR UPDATE ON your_table 

FOR EACH ROW 

WHEN (new_value > 1000)  -- Specify your conditional predicate here 

BEGIN 

   -- Trigger code 

   -- This trigger will only fire when the new_value is greater than 1000. 

END; 

/ 

    Aim: Trigger Logs Changes to EMPLOYEES.SALARY  

CREATE OR REPLACE TRIGGER salary_change_log_trigger 

AFTER UPDATE ON employees 

FOR EACH ROW 

BEGIN 

   IF :new.salary <> :old.salary THEN 

      -- Log the salary change 

      INSERT INTO salary_change_log (employee_id, old_salary, new_salary, change_date) 

      VALUES (:new.employee_id, :old.salary, :new.salary, SYSDATE); 

   END IF; 

END; 

/ 

    Aim: Trigger for instead of.  

CREATE OR REPLACE TRIGGER instead_of_trigger 

INSTEAD OF INSERT ON your_view 

FOR EACH ROW 

BEGIN 

   -- Trigger code 

   -- This trigger will execute instead of an INSERT operation on the specified view. 

END; 

/ 

 

 

 

 

 

 

 

 

 

Practical – 7: 

Aim: 

Sequences: 
a. Creating simple Sequences with clauses like START WITH, INCREMENT BY, MAXVALUE, MINVALUE, CYCLE | NOCYCLE, CACHE | NOCACHE, ORDER | NOORDER. 
b. Creating and using Sequences for tables. 

    Creating simple Sequences with clauses like START WITH, INCREMENT BY, MAXVALUE, MINVALUE, CYCLE | NOCYCLE, CACHE | NOCACHE, ORDER | NOORDER. 

1.Creating a Sequence with Default Settings: 

CREATE SEQUENCE default_sequence; 

2.Creating a Sequence with Specific Start Value and Increment: 

CREATE SEQUENCE start_increment_sequence 

  START WITH 100 

  INCREMENT BY 5; 

 

3.Creating a Sequence with Maximum and Minimum Values: 

CREATE SEQUENCE bounded_sequence 

  START WITH 1 

  INCREMENT BY 1 

  MAXVALUE 1000 

  MINVALUE 10; 

 

4.Creating a Cyclic Sequence: 

CREATE SEQUENCE cyclic_sequence 

  START WITH 1 

  INCREMENT BY 2 

  MAXVALUE 10 

  MINVALUE 1 

  CYCLE; 

 

5.Creating a Cached Sequence: 

CREATE SEQUENCE cached_sequence 

  START WITH 1 

  INCREMENT BY 1 

  CACHE 100; 

 

6.Creating an Ordered Sequence: 

CREATE SEQUENCE ordered_sequence 

  START WITH 100 

  INCREMENT BY 10 

  MAXVALUE 500 

  MINVALUE 0 

  ORDER; 

 

7.Creating a Sequence with No Order: 

CREATE SEQUENCE no_order_sequence 

  START WITH 1000 

  INCREMENT BY -1 

  MAXVALUE 900 

  MINVALUE 800 

  NOORDER 

b.Creating and using Sequences for tables 

Step 1: Create a Sequence 

CREATE SEQUENCE employee_id_seq 

  START WITH 1 

  INCREMENT BY 1 

  NOCYCLE 

  NOCACHE;. 

Step 2: Create a Table 

CREATE TABLE employees ( 

  employee_id NUMBER PRIMARY KEY, 

  first_name VARCHAR2(50), 

  last_name VARCHAR2(50) 

); 

Step 3: Use the Sequence in an INSERT Statement 

-- Insert a new employee with a generated ID 

INSERT INTO employees (employee_id, first_name, last_name) 

VALUES (employee_id_seq.NEXTVAL, 'John', 'Doe'); 

 

-- Insert another employee with a generated ID 

INSERT INTO employees (employee_id, first_name, last_name) 

VALUES (employee_id_seq.NEXTVAL, 'Jane', 'Smith'); 

Step 4: Query the Table 

SELECT * FROM employees; 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Practical No. 8 

Aim: 
Write a SQL block to handle exception by writing: 
a. Predefined Exceptions, 
b. User-Defined Exceptions, 
c. Redeclared Predefined Exceptions 

A)System (Predefined) Exceptions 
a. ALREADY_EXIST 
b. NO_DATA_FOUND 
c. TOO_MANY_ROWS 
d. VALUE_ERROR 
e. ZERO_DIVIDE  

NO_DATA_FOUND: 

DECLARE 

  v_employee_name VARCHAR2(50); 

BEGIN 

  SELECT first_name INTO v_employee_name FROM employees WHERE employee_id = 1000; 

  DBMS_OUTPUT.PUT_LINE('Employee name: ' || v_employee_name); 

EXCEPTION 

  WHEN NO_DATA_FOUND THEN 

    DBMS_OUTPUT.PUT_LINE('No employee found with the specified ID.'); 

END; 

TOO_MANY_ROWS: 

 DECLARE 

  v_employee_name VARCHAR2(50); 

BEGIN 

  SELECT first_name INTO v_employee_name FROM employees WHERE department_id = 10; 

  DBMS_OUTPUT.PUT_LINE('Employee name: ' || v_employee_name); 

EXCEPTION 

  WHEN TOO_MANY_ROWS THEN 

    DBMS_OUTPUT.PUT_LINE('Multiple employees found; only one was expected.'); 

END; 

VALUE_ERROR: 

DECLARE 

  v_num NUMBER; 

BEGIN 

  v_num := TO_NUMBER('abc'); -- Attempting to convert a non-numeric value 

  DBMS_OUTPUT.PUT_LINE('Number: ' || v_num); 

EXCEPTION 

  WHEN VALUE_ERROR THEN 

    DBMS_OUTPUT.PUT_LINE('Error: Invalid conversion to number.'); 

END; 

ZERO_DIVIDE: 

DECLARE 

  v_result NUMBER; 

BEGIN 

  v_result := 10 / 0; -- Division by zero 

  DBMS_OUTPUT.PUT_LINE('Result: ' || v_result); 

EXCEPTION 

  WHEN ZERO_DIVIDE THEN 

    DBMS_OUTPUT.PUT_LINE('Error: Division by zero.'); 

END; 

(B) User defined Exceptions -  

DECLARE 

  -- Define a user-defined exception 

  custom_exception EXCEPTION; 

   

  -- Variables 

  dividend NUMBER := 10; 

  divisor NUMBER := 0; 

  result NUMBER; 

 

BEGIN 

  -- Check for division by zero 

  IF divisor = 0 THEN 

    -- Raise the user-defined exception 

    RAISE custom_exception; 

  ELSE 

    -- Perform the division 

    result := dividend / divisor; 

    DBMS_OUTPUT.PUT_LINE('Result: ' || result); 

  END IF; 

 

EXCEPTION 

  WHEN custom_exception THEN 

    DBMS_OUTPUT.PUT_LINE('Custom exception raised: Division by zero.'); 

  WHEN OTHERS THEN 

    DBMS_OUTPUT.PUT_LINE('An error occurred.'); 

END; 

C)Redeclared Predefined Exceptions –  

DECLARE 
  default_number NUMBER := 0; 
  i NUMBER := 5; 
  invalid_number EXCEPTION;    -- redeclare predefined exception 
BEGIN 
  INSERT INTO t VALUES(TO_NUMBER('100.00', '9G999')); 
EXCEPTION 
  WHEN INVALID_NUMBER THEN 
    DBMS_OUTPUT.PUT_LINE('Substituting default value for invalid number.'); 
    INSERT INTO t VALUES(default_number); 
END; 
/ 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Practical No. 9 

Aim:  
Writing PL/SQL Blocks with basic programming constructs by including following: 
a. Sequential Statements 
b. Unconstrained loop 

Main block: 

DECLARE 

  -- Declare variables 

  counter NUMBER := 1; 

  max_count NUMBER := 5; 

BEGIN 

  -- Sequential statements 

  DBMS_OUTPUT.PUT_LINE('Sequential Statements Example:'); 

 

  -- Loop using an unconstrained loop 

  LOOP 

    -- Check the loop termination condition 

    EXIT WHEN counter > max_count; 

     

    -- Print the current counter value 

    DBMS_OUTPUT.PUT_LINE('Counter: ' || counter); 

     

    -- Increment the counter 

    counter := counter + 1; 

  END LOOP; 

 

  -- More sequential statements after the loop 

  DBMS_OUTPUT.PUT_LINE('Loop completed.'); 

 

  -- You can continue with additional code here 

END; 

/ 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Practical No. 10 

Aim:  Create nested tables and work with nested tables. 

Main block: 

Declare a Nested Table Type: 

CREATE OR REPLACE TYPE int_nested_table AS TABLE OF NUMBER; 

Create a Table with a Nested Table Column: 

CREATE TABLE person_skills ( 

    person_id NUMBER, 

    skills int_nested_table 

); 

Insert Data into the Nested Table: 

INSERT INTO person_skills (person_id, skills) 

VALUES (1, int_nested_table(10, 20, 30)); 

Retrieve Data from the Nested Table: 

SELECT person_id, COLUMN_VALUE AS skill 

FROM person_skills, 

     TABLE(skills); 

Update Data in the Nested Table: 

UPDATE person_skills 

SET skills = int_nested_table(40, 50) 

WHERE person_id = 1; 

Delete Data from the Nested Table: 

DELETE FROM TABLE(SELECT skills FROM person_skills WHERE person_id = 1) 

WHERE COLUMN_VALUE = 40; 

Iterate Through the Nested Table: 

DECLARE 

   skills int_nested_table; 

BEGIN 

   SELECT skills 

   INTO skills 

   FROM person_skills 

   WHERE person_id = 1; 

 

   FOR i IN 1..skills.COUNT LOOP 

      DBMS_OUTPUT.PUT_LINE('Skill ' || i || ': ' || skills(i)); 

   END LOOP; 

END; 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Practical No. 11 

Aim: Write an Implicit and explicit cursor to complete the task.  

 1. Example Implicit and explicit cursor. 

Implicit cursors: 

Example: 

DECLARE 

  var_id Admin.id%type; 

  var_name Admin.name%type; 

BEGIN 

  SELECT id, name 

  INTO var_id, var_name 

  FROM Admin 

  WHERE id=1; 

    dbms_output.put_line('Id: ' || var_id || ' ' || 'Name: ' || var_name); 

    dbms_output.put_line('Number of rows processed: '||sql%rowcount); 

END; 

/ 

Output: 

Id: 1 Name: User1 

Number of rows processed: 1 

PL/SQL procedure successfully completed. 

 

Explicit cursors: 

DECLARE 

   CURSOR emp_cursor IS 

      SELECT employee_name, salary 

      FROM employees 

      WHERE department_id = 10; 

   emp_record employees%ROWTYPE; 

BEGIN 

   -- Open the cursor 

   OPEN emp_cursor; 

 

   -- Fetch and display data using the explicit cursor 

   LOOP 

      FETCH emp_cursor INTO emp_record; 

      EXIT WHEN emp_cursor%NOTFOUND; 

       

      -- Display the fetched data 

      DBMS_OUTPUT.PUT_LINE('Employee Name: ' || emp_record.employee_name); 

      DBMS_OUTPUT.PUT_LINE('Employee Salary: ' || emp_record.salary); 

   END LOOP; 

 

   -- Close the cursor 

   CLOSE emp_cursor; 

END; 

/ 

 

Implement all attributes: 
1. %isopen 
2. %found 
3. %notfound 
4. %rowcount 

Main block: 

DECLARE 

   CURSOR emp_cursor IS 

      SELECT employee_name, salary 

      FROM employees 

      WHERE department_id = 10; 

   emp_record emp_cursor%ROWTYPE; 

   rows_updated NUMBER; 

BEGIN 

   -- Check if the cursor is open 

   IF emp_cursor%ISOPEN THEN 

      DBMS_OUTPUT.PUT_LINE('Cursor is open.'); 

   ELSE 

      DBMS_OUTPUT.PUT_LINE('Cursor is closed.'); 

   END IF; 

 

   -- Open the cursor 

   OPEN emp_cursor; 

 

   -- Check if the cursor is open 

   IF emp_cursor%ISOPEN THEN 

      DBMS_OUTPUT.PUT_LINE('Cursor is open.'); 

   ELSE 

      DBMS_OUTPUT.PUT_LINE('Cursor is closed.'); 

   END IF; 

 

   -- Initialize row count 

   rows_updated := 0; 

 

   -- Loop to fetch and process rows 

   LOOP 

      FETCH emp_cursor INTO emp_record; 

 

      -- Check if a row was found 

      IF emp_cursor%FOUND THEN 

         DBMS_OUTPUT.PUT_LINE('Employee Name: ' || emp_record.employee_name); 

         DBMS_OUTPUT.PUT_LINE('Employee Salary: ' || emp_record.salary); 

      END IF; 

 

      -- Check if no more rows can be fetched 

      IF emp_cursor%NOTFOUND THEN 

         EXIT; 

      END IF; 

 

      -- Update salary (for demonstration purposes) 

      UPDATE employees 

      SET salary = salary + 1000 

      WHERE CURRENT OF emp_cursor; 

 

      -- Increment the row count 

      rows_updated := rows_updated + 1; 

   END LOOP; 

 

   -- Get the number of rows updated 

   DBMS_OUTPUT.PUT_LINE('Number of rows updated: ' || rows_updated); 

 

   -- Close the cursor 

   CLOSE emp_cursor; 

 

   -- Check if the cursor is open (after closing) 

   IF emp_cursor%ISOPEN THEN 

      DBMS_OUTPUT.PUT_LINE('Cursor is open.'); 

   ELSE 

      DBMS_OUTPUT.PUT_LINE('Cursor is closed.'); 

   END IF; 

END; 

/ 

Practical No. 12 

Aim: Create packages and use it in SQL block to complete the task. 

Main block: 

create or replace package pkg_demo is 

  function print_string return varchar2; 

  procedure proc_demo(id varchar2, name varchar2); 

end pkg_demo; 

Output: 

Package created. 

 

SQL> create table demo(id varchar2(20), name varchar2(20)); 

Table created. 

SQL> desc demo; 

Name                          Null? Type 

----------------------------------------- -------- ---------------------------- 

ID                                    VARCHAR2(20) 

NAME                                 VARCHAR2(20) 

 

create or replace package body pkg_demo is 

  --function implementation 

  function print_string return varchar2 is 

    begin 

      return 'This is print string function'; 

    end print_string; 

  --procedure implementation 

  procedure proc_demo(id varchar2, name varchar2) is 

    begin 

      insert into demo (id, name) values (id, name); 

    end; 

end pkg_demo; 

Output: 

Package body created. 

 

begin 

  dbms_output.put_line(pkg_demo.print_string); 

end; 

Output: 

This is print string function 

PL/SQL procedure successfully completed. 

 

SQL> select * from demo; 

no rows selected 

 

begin 

  pkg_demo.proc_demo('A001','Arun'); 

end; 

Output: 

PL/SQL procedure successfully completed. 

 

SQL> select * from demo; 

ID                    NAME 

-------------------- -------------------- 

A001               Arun 

 

SQL> drop package pkg_demo; 

Package dropped. 

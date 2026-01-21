CREATE DATABASE IF NOT EXISTS labdb;
USE labdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    gender ENUM('Male', 'Female', 'Other'),
    date_of_birth DATE,
    salary DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


 INSERT INTO users (name, email, gender, date_of_birth, salary) VALUES
('Aarav', 'aarav@example.com', 'Male', '1995-05-14', 65000.00),
('Ananya', 'ananya@example.com', 'Female', '1990-11-23', 72000.00),
('Raj', 'raj@example.com', 'Male', '1988-02-17', 58000.00),
('Sneha', 'sneha@example.com', 'Female', '2000-08-09', 50000.00),
('Farhan', 'farhan@example.com', 'Male', '1993-12-30', 61000.00),
('Priyanka', 'priyanka@example.com', 'Female', '1985-07-12', 84000.00),
('Aisha', 'aisha@example.com', 'Female', '1997-03-25', 56000.00),
('Aditya', 'aditya@example.com', 'Male', '1992-06-17', 69000.00),
('Meera', 'meera@example.com', 'Female', '1989-09-05', 77000.00),
('Ishaan', 'ishaan@example.com', 'Male', '2001-10-02', 45000.00),
('Tanvi', 'tanvi@example.com', 'Female', '1994-04-18', 62000.00),
('Rohan', 'rohan@example.com', 'Male', '1986-12-01', 75000.00),
('Zoya', 'zoya@example.com', 'Female', '1998-01-15', 54000.00),
('Karan', 'karan@example.com', 'Male', '1990-08-22', 68000.00),
('Nikita', 'nikita@example.com', 'Female', '1987-03-10', 71000.00),
('Manav', 'manav@example.com', 'Male', '1996-11-29', 61000.00),
('Divya', 'divya@example.com', 'Female', '1991-02-28', 57000.00),
('Harshit', 'harshit@example.com', 'Male', '1993-09-09', 65000.00),
('Ritika', 'ritika@example.com', 'Female', '1999-05-05', 52000.00),
('Imran', 'imran@example.com', 'Male', '1995-07-30', 63000.00),
('Juhi', 'juhi@example.com', 'Female', '1992-10-14', 59000.00),
('Tushar', 'tushar@example.com', 'Male', '1990-01-08', 73000.00),
('Lata', 'lata@example.com', 'Female', '1984-11-11', 78000.00),
('Yash', 'yash@example.com', 'Male', '1997-06-06', 64000.00),
('Fatima', 'fatima@example.com', 'Female', '1993-03-03', 55000.00);


SELECT * 
FROM users
order by name desc limit 25;

SELECT name , salary
FROM users
order by name desc limit 25;


CREATE TABLE student (
    sid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
	rn int,
    batch int
);

CREATE TABLE teacher (
    tid INT AUTO_INCREMENT PRIMARY KEY,
    ename VARCHAR(100) NOT NULL,
	doj date,
    salary int
);

ALTER TABLE users RENAME COLUMN name TO ename;
ALTER TABLE users RENAME COLUMN id TO eid;


CREATE TABLE booklist (
    isbn INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
	publication varchar(100)
    
);

CREATE TABLE book (
    bid INT AUTO_INCREMENT PRIMARY KEY,
    bname VARCHAR(100) NOT NULL,
    price int,
    author varchar(100)
);


CREATE TABLE issues (
    iid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
	doi date
);

INSERT INTO student (name, rn, batch) VALUES
('Alice Johnson', 101, 2023),
('Bob Smith', 102, 2023),
('Charlie Brown', 103, 2024),
('Diana Prince', 104, 2024),
('Evan Wilson', 105, 2025),
('Fiona Clark', 106, 2025),
('George Miller', 107, 2023),
('Hannah Lee', 108, 2024),
('Ian Wright', 109, 2025),
('Julia Hall', 110, 2023);   

INSERT INTO teacher (ename, doj, salary) VALUES
('Mr. Anderson', '2020-08-15', 50000),
('Ms. Taylor', '2019-06-01', 55000),
('Dr. Clark', '2021-03-10', 60000),
('Mrs. Davis', '2018-09-22', 52000),
('Prof. White', '2022-01-05', 58000),
('Mr. King', '2020-04-12', 54000),
('Ms. Moore', '2017-11-30', 56000),
('Dr. Hall', '2023-02-20', 62000),
('Mrs. Green', '2016-07-14', 53000),
('Prof. Young', '2021-09-08', 59000);   


INSERT INTO booklist (name, publication) VALUES
('The Great Gatsby', 'Scribner'),
('To Kill a Mockingbird', 'J.B. Lippincott & Co.'),
('1984', 'Secker & Warburg'),
('Pride and Prejudice', 'T. Egerton'),
('The Catcher in the Rye', 'Little, Brown and Company'),
('Lord of the Flies', 'Faber and Faber'),
('Animal Farm', 'Faber and Faber'),
('Brave New World', 'Chatto & Windus'),
('The Hobbit', 'George Allen & Unwin'),
('Fahrenheit 451', 'Ballantine Books');   


INSERT INTO book (bname, price, author) VALUES
('The Great Gatsby', 12, 'F. Scott Fitzgerald'),
('To Kill a Mockingbird', 15, 'Harper Lee'),
('1984', 14, 'George Orwell'),
('Pride and Prejudice', 10, 'Jane Austen'),
('The Catcher in the Rye', 13, 'Jane Austen'),
('Lord of the Flies', 11, 'William Golding'),
('Animal Farm', 9, 'George Orwell'),
('Brave New World', 16, 'Aldous Huxley'),
('The Hobbit', 18, 'J.R.R. Tolkien'),
('Fahrenheit 451', 12, 'Ray Bradbury');   


INSERT INTO issues (name, doi) VALUES
('Alice Johnson', '2026-01-10'),
('Bob Smith', '2026-01-11'),
('Charlie Brown', '2026-01-12'),
('Diana Prince', '2026-01-13'),
('Evan Wilson', '2026-01-14'),
('Fiona Clark', '2026-01-15'),
('George Miller', '2026-01-16'),
('Hannah Lee', '2026-01-17'),
('Ian Wright', '2026-01-18'),
('Julia Hall', '2026-01-19');   


select *
from teacher as t
order by t.ename asc;

select sum(salary) as sumsalary
from users;


select * from users
order by salary asc limit 1;

select name , publication 
from booklist
order by name,publication asc;


select avg(price) as average,author
from book
group by author;

select publication , count(*) as no_of_books 

from booklist
group by publication;



select bid , bname
from book
where price > (select avg(price) from book);

select bid , bname, author
from book 
where bname like 'S%';

select ename , bname , salary from teacher 
join book on teacher.tid = book.bid
where teacher.salary > (select avg(salary) from teacher);


select author from book
where (select count(*) from book) > 1;



 





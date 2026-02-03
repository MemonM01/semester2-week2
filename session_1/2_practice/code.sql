-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here

-- 1 --
SELECT Books.title, Members.name, Loans.loan_date FROM Books, Loans, Members
WHERE Books.id = Loans.member_id 
AND Loans.member_id = Members.id;


-- 2 --
SELECT Books.title, Loans.id FROM Books, Loans
WHERE Books.id = Loans.book_id;

-- 3 -- 
SELECT LibraryBranch.name, Books.title 
FROM LibraryBranch LEFT JOIN Books 
ON LibraryBranch.id = Books.branch_id;

-- 4 -- 
SELECT LibraryBranch.name, COUNT(Books.title) 
FROM LibraryBranch LEFT JOIN Books 
ON LibraryBranch.id = Books.branch_id
GROUP BY LibraryBranch.name;

-- 5 -- 
SELECT LibraryBranch.name, COUNT(Books.title) 
FROM LibraryBranch LEFT JOIN Books 
ON LibraryBranch.id = Books.branch_id
GROUP BY LibraryBranch.name
HAVING COUNT(Books.title) > 7;

-- 6 -- 
SELECT Members.name, COUNT(Loans.id) 
FROM Members LEFT JOIN Loans 
ON Members.id = Loans.member_id
GROUP BY Members.name;

-- 7 --
SELECT Members.name, COUNT(Loans.id) 
FROM Members LEFT JOIN Loans 
ON Members.id = Loans.member_id
GROUP BY Members.name
HAVING COUNT(Loans.id) = 0;

-- 8 -- 
SELECT LibraryBranch.name, COUNT(Loans.id)
FROM LibraryBranch, Books
LEFT JOIN Loans ON LibraryBranch.id = Books.branch_id
AND Books.id = Loans.book_id
GROUP BY LibraryBranch.name;

-- 9 --
SELECT Members.name, COUNT(Loans.id) 
FROM Members LEFT JOIN Loans 
ON Members.id = Loans.member_id
GROUP BY Members.name
HAVING COUNT(Loans.id) > 0;

-- 10 --
SELECT Books.title, Loans.loan_date,
CASE 
WHEN Loans.loan_date IS NULL THEN 'Unloaned book'
ELSE 'Loaned book'
END AS book_status
FROM Books LEFT JOIN Loans
ON Books.id = Loans.book_id;
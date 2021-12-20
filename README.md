# Report_Card_Generation

This generation is created using python where python is used as an interface(front-end) and MySQL(back-end) is used as a database to store the data.

Steps to create a table for this code :
1. Create a new database / use old database.
2. Create table marksheet with these columns.
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| ROLL_NO     | int         | NO   | PRI | NULL    |       |
| NAME        | varchar(30) | YES  |     | NULL    |       |
| ENGLISH     | float       | NO   |     | NULL    |       |
| PHYSICS     | float       | NO   |     | NULL    |       |
| CHEMISTRY   | float       | NO   |     | NULL    |       |
| MATHS       | float       | YES  |     | NULL    |       |
| BIOLOGY     | float       | YES  |     | NULL    |       |
| COMPUTER    | float       | YES  |     | NULL    |       |
| TOTAL_MARKS | float       | YES  |     | NULL    |       |
| AVERAGE     | float       | YES  |     | NULL    |       |
| GRADES      | char(5)     | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
3. Insert data through code.
4. Select * from marksheet (command to display data in MySQL).

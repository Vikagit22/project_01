# Задача 8 SQL код
# Написать программу, с помощью которой можно получать информацию о школе и студенте. 

CREATE TABLE Students(
Student_id INTEGER NOT NULL PRIMARY KEY,
Student_name TEXT NOT NULL,
School_id INTEGER NOT NULL
);
INSERT INTO Students (student_id, student_name, school_id)
VALUES
('201','Иван','1'),
('202','Петр','2'),
('203','Анастасия','3'),
('204','Игорь','4');

SELECT Students.student_id, Students.student_name, Students.School_id, School.School_Name from Students
JOIN School on Students.school_id = School.School_Id;

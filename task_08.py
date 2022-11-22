#создание таблицы students
import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = ''' CREATE TABLE STUDENTS
(
   Student_id integer NOT NULL PRIMARY KEY,
   Student_name TEXT NOT NULL,
   School_id INTEGER NOT NULL     
);
'''
cursor.execute(query)
connection.commit()
connection.close()

# наполнение таблицы students
import sqlite3
connection = sqlite3.connect('teatchers.db')
cursor = connection.cursor()
query = ''' INSERT INTO Students ( student_id, 
        student_name, school_id)
VALUES
('201', 'Иван', '1'), 
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4');  
'''
cursor.execute(query)
connection.commit()
connection.close()

# задача 08 для Pyton 
# написать программу с помощью которой по ID студента
# можно получать информацию о школе студента
import sqlite3
def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student_detail(student_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query1 = """SELECT * FROM Students WHERE student_Id = ?"""
    cursor.execute(select_query1, (student_id,))
    records = cursor.fetchall()
    a1 = (records[0][2])
    select_query2 = """ SELECT Students.student_id, Students.student_name, Students.School_id, School.School_Name from Students
    JOIN School on Students.school_id = School.School_Id;
     """
    cursor.execute(select_query2)
    school_name_student = cursor.fetchall()
    
    print ("Данные по студенту")
    for row in records:
      print ("ID студента", row[0])
      print ("Имя студента", row[1])
      print ("ID школы", row[2])
      print ("Название школы", school_name_student[a1-1][3])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных по школе ", error)

get_student_detail(203)
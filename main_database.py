print()
print("\tMAIN MENU")
print()
while(True):
print("Press 1 to customize Student Database\nPress 2 to customize Course Database\nPress 3 to
customize Batch Database\nPress 4 to customize Department Database\nPress 5 to customize Exam
Database\nPress 0 to EXIT")
x = int(input("Enter your choice: "))
if(x == 0):
break
elif(x == 1):
from Student_database import *
print()
print("\t Student Management Database ")
print()
while(True):
print("Press 1 to create a student\nPress 2 to update a student's details\nPress 3 to remove a
student\nPress 4 to generate report card of a student\nPress 0 to return to main menu")
y = int(input("Enter your choice: "))
if(y == 0):
break
elif(y == 1):
stud_id = input("Enter student ID: ")
stud_name = input("Enter student name: ")
createStudent(stud_id, stud_name)
elif(y == 2):
old_stud_id = input("Enter old student ID: ")
updateStudent(old_stud_id)
elif(y == 3):
stud_id = input("Enter student ID: ")
removeStudent(stud_id)
elif(y == 4):
stud_id = input("Enter student ID: ")
reportCard(stud_id)
else:
print("Invalid input. Try again.")
elif(x == 2):
from Course_database import *
print()
print("\t Course Management Database ")
print()
while(True):
print("Press 1 to create a course\nPress 2 to view performance of students on course\nPress
3 to show course statistics as histogram\nPress 0 to return to main menu")
y = int(input("Enter your choice: "))
if(y == 0):
break
elif(y == 1):
course_id = input("Enter course ID: ")
course_name = input("Enter course name: ")
createCourse(course_id, course_name)
elif(y == 2):
course_id = input("Enter course ID: ")
checkPerformance(course_id)
elif(y == 3):
stud_id = input("Enter course ID: ")
courseStatistics(course_id)
else:
print("Invalid input. Try again.")
elif(x == 3):
from Batch_database import *
print()
print("\t Batch Management Database ")
print()
while(True):
print("Press 1 to create a batch\nPress 2 to view all students in a batch\nPress 3 to show all
courses in a batch\nPress 4 to view performance of all students in a batch\nPress 5 to view pie chart
of percentage all students in a batch\nPress 0 to return to main menu")
y = int(input("Enter your choice: "))
if(y == 0):
break
elif(y == 1):
batch_name = input("Enter batch name: ")
createBatch(batch_name)
elif(y == 2):
batch_id = input("Enter batch ID: ")
viewStudents(batch_id)
elif(y == 3):
batch_id = input("Enter batch ID: ")
viewCourses(batch_id)
elif(y == 4):
batch_id = input("Enter batch ID: ")
viewPerformance(batch_id)
elif(y == 5):
batch_id = input("Enter batch ID: ")
pieChart(batch_id)
else:
print("Invalid input. Try again.")
elif(x == 4):
from Depertment_database import *
print()
print("\t Deparmant Management Database ")
print()
while(True):
print("Press 1 to create a department\nPress 2 to view all betches in a department\nPress 3 to
view average performance of all betches in a department\nPress 4 to view line plot of department
statistics\nPress 0 to return to main menu")
y = int(input("Enter your choice: "))
if(y == 0):
break
elif(y == 1):
department_id = input("Enter department ID: ")
department_name = input("Enter department name: ")
createDepartment(department_id, department_name)
elif(y == 2):
department_id = input("Enter department ID: ")
viewBatches(department_id)
elif(y == 3):
department_id = input("Enter department ID: ")
viewPerformanceD(department_id)
elif(y == 4):
department_id = input("Enter department ID: ")
linePlot(department_id)
else:
print("Invalid input. Try again.")
elif(x == 5):
from Exam_database import *
print()
print("\t Examination Management Database ")
print()
while(True):
print("Press 1 to enter marks of all students for an exam\nPress 2 to view performance of all
students in an exam\nPress 3 to show examination statistics as a scatter plot\nPress 0 to return to
main menu")
y = int(input("Enter your choice: "))
if(y == 0):
break
elif(y == 1):
course_id = input("Enter course ID: ")
enterMarks(course_id)
elif(y == 2):
course_id = input("Enter course ID: ")
viewPerformanceE(course_id)
elif(y == 3):
scatterPlot()
else:
print("Invalid input. Try again.")
else:
print("Invalid input. Try again.")
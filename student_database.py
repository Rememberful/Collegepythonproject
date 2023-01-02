import json
import csv
import pandas
from Batch_database import createBatch
def createStudent(stud_id, stud_name):
roll_no = int(stud_id[5:7])
batch_id = stud_id[:5]
data = [stud_id, stud_name, roll_no, batch_id]
csv_reader = []
with open("Student_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
with open("Student_database.csv", "a", newline = "\n") as f:
for i in range(0, len(csv_reader)):
if(csv_reader[i][0] == stud_id):
print("Student ID already exists")
return
csv_writer = csv.writer(f)
csv_writer.writerow(data)
with open("Batch_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
check = 0
for i in range(0, len(csv_reader)):
if(csv_reader[i][0] == batch_id):
check = 1
if(csv_reader[i][4] == ""):
csv_reader[i][4] = csv_reader[i][4] + stud_id
else:
csv_reader[i][4] = csv_reader[i][4] + ":" + stud_id
df = pandas.read_csv("Batch_database.csv")
df.loc[i-1, "list_of_students"] = csv_reader[i][4]
df.to_csv("Batch_database.csv", index = False)
if(check == 0):
print("Batch does not exist.... Creating new batch")
batch_name = batch_id[:3] + " 20" + batch_id[3:] + "-" + str(int(batch_id[3:]) + 4)
createBatch(batch_name)
with open("Batch_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
courses = []
for i in range(0, len(csv_reader)):
if(csv_reader[i][0] == batch_id):
courses = list(csv_reader[i][3].split(":"))
with open("Course_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
for i in range(0, len(csv_reader)):
for j in range(0, len(courses)):
if(csv_reader[i][0] == courses[j]):
if(csv_reader[i][2] == ""):
temp = {}
temp[stud_id] = 0
csv_reader[i][2] = json.dumps(temp)
else:
temp = json.loads(csv_reader[i][2])
temp[stud_id] = 0
csv_reader[i][2] = json.dumps(temp)
df = pandas.read_csv("Course_database.csv")
df.loc[i-1, "marks_obtained"] = csv_reader[i][2]
df.to_csv("Course_database.csv", index = False)
def updateStudent(old_stud_id):
csv_reader = []
with open("Student_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
check = 0
for i in range(0, len(csv_reader)):
if(csv_reader[i][0] == old_stud_id):
check = 1
break
if(check == 0):
print("Student ID does not exist")
return
while(True):
print("Press 1 to update name\nPress 2 to update student ID\nPress 0 to Exit")
x = int(input("Enter your choice: "))
if(x == 0):
break
elif(x == 1):
name = input("Enter updated name: ")
df = pandas.read_csv("Student_database.csv")
df.loc[i-1, "Name"] = name
df.to_csv("Student_database.csv", index = False)
elif(x == 2):
new_stud_id = input("Enter updated student ID: ")
df = pandas.read_csv("student_database.csv")
df.loc[i-1, "Student_ID"] = new_stud_id
df.to_csv("Student_database.csv", index = False)
removeStudent(old_stud_id)
createStudent(new_stud_id, csv_reader[i][1])
old_stud_id = new_stud_id
with open("Student_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
else:
print("Invalid input. Try again.")
def removeStudent(stud_id):
csv_reader = []
with open("Student_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
check = 0
for i in range(0, len(csv_reader)):
if(csv_reader[i][0] == stud_id):
check = 1
break
if(check == 0):
print("Student ID does not exist")
return
df = pandas.read_csv("Student_database.csv")
df.set_index("Student_ID")
df = df.drop(df.index[i-1])
df.to_csv("Student_database.csv", index = False)
with open("Course_databse.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
for i in range(0, len(csv_reader)):
if(i == 0):
continue
temp = csv_reader[i][2]
temp = json.loads(temp)
if stud_id in temp:
del temp[stud_id]
csv_reader[i][2] = json.dumps(temp)
df = pandas.read_csv("Course_database.csv")
for i in range(1, len(csv_reader)):
df.loc[i-1, "marks_obtained"] = csv_reader[i][2]
df.to_csv("Course_database.csv", index = False)
with open("Batch_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
for i in range(0, len(csv_reader)):
if(i == 0):
continue
temp = list(csv_reader[i][4].split(":"))
if stud_id in temp:
temp.remove(stud_id)
a = ":"
csv_reader[i][4] = a.join(temp)
df = pandas.read_csv("Batch-database.csv")
for i in range(1, len(csv_reader)):
df.loc[i-1, "list_of_students"] = csv_reader[i][4]
df.to_csv("Batch_database.csv", index = False)
def reportCard(stud_id):
name = ""
csv_reader= []
with open("Student_database.csv", "r", newline = "\n") as f:
csv_reader = list(csv.reader(f, delimiter=","))
check = 0
for i in range(0, len(csv_reader)):
if(csv_reader[i][0] == stud_id):
check = 1
name = csv_reader[i][1]
break
if(check == 0):
print("Student ID does not exist")
return
f = open((stud_id + ".txt"), "w")
a = "Student ID: " + stud_id + "\n"
b = "Name: " + name + "\n"
f.writelines([a, b])
with open("Course_database.csv", "r", newline = "\n") as fx:
csv_reader = list(csv.reader(fx, delimiter=","))
marks = []
subjects = []
for i in range(1, len(csv_reader)):
marks.append(json.loads(csv_reader[i][2]))
subjects.append(csv_reader[i][1])
total_marks = 0
divs = 0
for i in range(0, len(subjects)):
temp = marks[i]
if(isinstance(temp.get(stud_id), int)):
subject_marks = "Marks in " + subjects[i] + ": " + str(temp.get(stud_id)) + "% \n"
divs += 1
total_marks += temp.get(stud_id)
f.write(subject_marks)
grade = "Grade obtained: " + gradeCheck(total_marks/divs) + " \n"
f.write(grade)
f.close()
def gradeCheck(a):
if(a >= 90):
return "A"
elif(a >= 80):
return "B"
elif(a >= 70):
return "C"
elif(a >= 60):
return "D"
elif(a >= 50):
return "E"
else:
return "F"
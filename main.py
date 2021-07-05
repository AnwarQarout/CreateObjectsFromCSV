from EmployeeModel import Employee
import csv

myList = []
with open('Employee.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        employee = Employee(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        myList.append(employee)


myList.pop(0)
for employee in myList:
    employee.printEmployeeInfo()
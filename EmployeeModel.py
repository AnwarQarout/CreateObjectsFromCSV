class Employee:
    def __init__(self,id,name,salary,address,department,email,phone):
        self.id = id
        self.name = name
        self.salary = salary
        self.address = address
        self.department = department
        self.email = email
        self.phone = phone


    def printEmployeeInfo(self):
        print("ID : ",self.id, " name : ",self.name , "salary : ",self.salary,"\naddress: ",self.address," department: ",self.department , "email: ",self.email , "phone: ",self.phone)
        print("---------------")
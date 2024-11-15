#Parent class
class Person(object):
    def _init_(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

#Child class
class Employee(Person):
    def _init_(self,name,idnumber,salary,post):
        self.salary = salary    
        self.post = post
        Person._init_(self,name,idnumber)

a = Employee('Penguin', 20210401, 15000, "Intern")
a.display()

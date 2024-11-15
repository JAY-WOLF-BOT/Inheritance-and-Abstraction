class Person:
   def _init_(self, fname, lname):
      self.firstname = fname
      self.lastname = lname 

   def _init_(self):
      print(self.firstname, self.lastname) 

class Student(Person):
   def _init_(self, fname, lname, year):
      super()._init_(fname, lname)
      self.graduationyear = year

x = Student("Joey", "King", 2021)
x.printname()
print(x.graduationyear)      
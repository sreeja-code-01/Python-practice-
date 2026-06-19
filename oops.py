
class Student:
    name="sree"
    age=12
    salary=200000
s1=Student()
print(s1.name,s1.age,s1.salary)
----------
class Student:
    def __init__(self,name):
        self.name=name
s1=Student("priya")
print(s1.name)
--------
using method:-
class Student:
    def __init__(self,name):
       self.name=name
    def show(self):
       print(self.name)
s1=Student("sree")
s1.show()
-------
class Student:
   def show(self,name):
      print(name)
s1=Student()
n="abhi"
s1.show(n)
------
class Student:
    def __init__(self,marks_list):
        self.marks_list=marks_list
    def marks(self):
        for i in self.marks_list:
           print(i)
s1=Student([10,20,30])
s1.marks()
----------
class Student:
    def __init__(self,radius):
        self.radius=radius 
    def area(self):
         area=3.14*self.radius*self.radius
         print(area)
s1=Student(5)
s1.area()
-------
#abstraction
#wap using abstraction foe a vehicle class with start() method and a car class that prints "car is started"
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(Vehicle):
    def start(self):
        print("car is started")
s1=car()
s1.start()       
------------

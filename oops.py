
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
#wap abstract class electricity,bill method,chlid calss home
from abc import ABC,abstractmethod
class Elect(ABC):
    @abstractmethod
    def bill(self,units):
        pass
class Home(Elect):
    def bill(self,units):
        self.units=units
        print(self.units*5)
s1=Home
s1.bill(100)    
----------

#wap using abstraction for a shape class with an area() method and a square class that printtsarea of a square 
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class square(Shape):
    def area(self,a):
        self.a=a
        print("square area",a*a)
s1=square()
s1.area(5)
----------
#wap using abstraction 
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def show_balance(self):
        pass
class Savings(Bank):    
    def show_balance(self,balance):
        self.balance=balance
        print("balance is",self.balance)
s1=Savings()
s1.show_balance(500)       
------------------
#inheritance
class Animal:
    def eat(self):
        print("grass")
class Lion(Animal):
    def show(self):
        print("king of jungle")
s1=Lion()
s1.show()  
s1.eat()      
-------=--
class Vehicle:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed
class Car(Vehicle):
    def show(self):
        print(self.name,self.speed)
s1=Car("bmw",120)
s1.show()
-------------
class Shape:
    def __init__(self,s):
        self.s=s
class Area(Shape):
    def show(self):
        print(self.s*self.s) 
s1=Area(8)
s1.show()               
-----------
#constructor store balance child class savingsaacount ,method deposi some amount, display final balance
class Bank:
    def __init__(self,balance):
        self.balance=balance
class Savingsaccount(Bank):
    def deposit(self,deposit):
        self.balance+=deposit
        
        print(self.balance)
s1=Savingsaccount(10000)
s1.deposit(150)        
-------------
polymorphism:-
#polymorphisim-diff classes same method but behaves differently
#dog-sound()--bark,cat-sound()--meow,lion-sound()--roar
class Dog:
    def sound(self):
        print("bark")
class Cat:
    def sound(self):
        print("meow")
class Lion:
    def sound(self):
        print("roar")                
d=Dog()
d.sound()
c=Cat()
c.sound()
l=Lion()
l.sound()        
-------------
            

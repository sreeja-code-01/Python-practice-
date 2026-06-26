
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
---------------
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
#create abstract class shape with method area() square and rectangle
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        print("helllo world! tnis is me here")
class Square(Shape):
    def area(self,s):
        self.s=s
        super().area()         #super().area()-calls parent method &later comes back to square method and executes print(self.s*self.s)
        print(self.s*self.s)
class Rectangle(Shape):
    def area(self,l,b):
        self.l=l
        self.b=b         
        print(self.b*self.l)
s1=Square()
s1.area(3)
s2=Rectangle()
s2.area(2,6)     
------------
#food delivery
from abc import ABC,abstractmethod
class Food(ABC):
    @abstractmethod
    def taste(self):
        print("please order your food! delivery within 10 minutes")
class Pizza(Food):
    def taste(self):
        super().taste()
        print("chessy,chicken pizza")
class IceCream(Food):
    def taste(Self):
        print("sweet,chocalate flavour")        

s1=Pizza()
s1.taste()
s2=IceCream()
s2.taste()
----------
#bank transanction
from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        print("banks interest")
class SBI(Bank):
    def interest(self):
        super().interest()
        print("SBI interest=7%")
class HDFC(Bank):
    def interest(self):
        print("HDFC Interset=8%")
s1=SBI()
s1.interest()
s2=HDFC()
s2.interest()         
---------------
#HDFC loans category list with interest rate
from abc import ABC,abstractmethod
class HDFC(ABC):
    @abstractmethod
    def interest(self):
        print("bank interest")
class PersonalLoan(HDFC):
    def interest(self):
        super().interest()
        print("personal loan-11%")        
class GoldLoan(HDFC):
    def interest(self):
        print("gold loan-10%")
class HomeLoan(HDFC):
    def interest(self):
        print("hile loan-8%")
class EducationLoan(HDFC):
    def interest(self):
        print("education loan=10%")
s1=PersonalLoan()
s1.interest()
s2=GoldLoan()
s2.interest()
s3=HomeLoan()
s3.interest()
s4=EducationLoan()
s4.interest()                            
--------------
class Device:
    def details(self,brand):
        self.brand=brand
class Phone(Device):
    def show(self):
        pass            
class Smartphone(Phone):
     def display(self,internetconnection):
         self.internetconnection=internetconnection
         print(self.brand,self.internetconnection)
s1=Smartphone()
s1.details("oppo")
s1.show()
s1.display("bad")        
---------
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
       pass
class Car(Vehicle):
    def start(self,name):
        self.name=name
        print(self.name)
          
class Bike(Vehicle):
    def start(self,mileage):
        self.mileage=mileage
        print(self.mileage)
          
s1=Car()
s1.start("mahindra")
s2=Bike()
s2.start("120m")
---------------
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
#hospital syatem
class Person:
    def show(self,name):
        self.name=name
class Doctor(Person):
    def display(self,speciality):
        self.speciality=speciality
class Patient(Doctor):
    def item(self,disease):
        self.disease=disease
        print(self.name,self.speciality,self.disease)
s1=Patient()
s1.show("sreeja")
s1.display("cardiologist")
s1.item("fever")
 -------------             
#multiple inheritance
class Person:
    def detail(self,name):
        self.name=name
class Student(Person):
    def show(self,rollno):
        self.roll=rollno    
class Research(Student):
    def display(self,projectname):
        self.projectname=projectname    
        print(self.name,self.roll,self.projectname)    

s1=Research()
s1.detail("abhinay")
s1.show(1234)
s1.display("slash 2.o")
-----------
#ONLONE SHOPPING
class Product:
    def item(self,name):
        self.name=name
class Electronics(Product):
    def show(self,warranty):
        self.warranty=warranty
class Mobile(Electronics):
    def display(self,ram,storage):
        self.ram=ram
        self.storage=storage
        print(self.name,self.warranty,self.ram,self,storage)
s1=Mobile()
s1.item("chocolate")
s1.show("2 years")
s1.display(16,871)                        
-------------
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
#anstraction + inheritance
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        print("sound of diff animals")
class Dog(Animal):
          def sound(self):
              super().sound()
              print("bark")      
class Cat(Dog):
      def sound(self):
            super().sound()
            print("meow") 
s1=Cat()
output:-
sounf of diff animals
bark
meow
--------




s1.sound()
            

1st method with parameters:
def funt_name(para):
    print(para)
funct_name(value)

def add(a,b):
    print(a+b)
add(5,6)
output:'11
---------
def name(n):
   print(n)
name("sree")
output:-sreeja
---------
def name(n)
   print("hello im",n)
name("sree")
output:- hello im sree
--------
def fact(n)
   fact=1
 for i in range(1,n+1)
     fact=fact*i
    print(fact)
fact(5)
output:120
---------
def table(n)
for i in range(1,n+1)
     print(n*i)
table(5)
output:5
10
15
..
------------
def print_list(n)
    print(n)
print_list([1,2,3,4,5])
output:
1
2
3
4
5
(or)
def print_list(n)
for i in n
    print(i)
print_list([1,2,3,4,5])
output:-
[1,2,3,4,5]
-------------
2nd method with return type:

def funt_name(para):
    return para
result=funct_name(value)
print(result)
---------
def add(a,b)
return a+b
result=add(2,3)
print(result)
output:-5
(or)
def add(a,b)
print(a+b)
result=add(2,3)
print(result)
output:-5
none
---------
def max(a,b)
 if a>b:
   return a
 else:
   return b
result=max(5,6)
print(result)
(or)
if a>b:
   return a
 else:
   return b
print(max(5,6))
(or)
-----------
def check(a)
  if a%2==0
   return "even"
   else:
    return "odd"
print(check(5))
print(check(4))
print(check(8))
output;-
odd
even
even
--------
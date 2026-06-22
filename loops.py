while loop
while cond:
#some work
-------------
print no.feom 1to 5
num = 1

while num <= 5:
    print(num)
    num += 1
-------------
print no.s from 5 to 1
num = 5

while num >= 1:
    print(num)
    num -= 1
-----------
print even no.from 2 to 10
i=1
while i<=10
  if i%2==0
     print(i)
i=i+1
---------------
factorial of no.
 
n=int(input("n: ")
fact=1
i=1
while i<=n
   fact=fact*i
    i=i+1
   print(fact)
--------------
multiplication of 2 table
num = 1

while num <= 10:
    print(2 * num)
    num += 1
-----------------
print no.s from 1t0 5 except 3
num=1 
while num<=5
num=num+1
    if num == 3:
        continue  # continue means skip this part,if num==3 it skips and goes back to top num will increase to 4 

    print(num)
-----------------
store elm in list print using loop
list=[ 10,20,30,40,50]
idx=0
while idx<len(list)-1
 print(list[idx)
idx=idx+1
-----------------
search a no.in tuple using loop
tup=(10,20,30,40,50)
target=40
idx=0
while idx<len(list)-1
if(tup[idx]==target)
 print("found at indx",idx)
idx=idx+1
---------------
for loop:
1st method
for item in sequence:
#some work 

n=[1,2,3,4]
for item in n:
   print(item)
output:-
1 
2
3
4
"""item=1.    
print(item)
item=2
print(item).....so on"""
-----------
fruits=["app","orag","mango"]
for i in fruits:
print(i)
output:-
app
org
mango
----------
2nd method:-
.for i in range()
.for i in range(start,stop)
.for i in range(stat,stop,step)
----------
 print hello 3 time:
for i in range(4):
   print(i)
output:-hello
hello
hello
-------------
print feon 1 to 5

for i in range(1,6):# start from 0 and stop before 6 i.e 5
   print(i)  
output:-1
2
3
4
5
---------
print even no. from 2 to 10
for i in range(2,11,2) # start,stop,increase by
print(i)
output:-
2
4
6
8
10
-----------
print 6 table
for i in range(1,11)
 print("6 ×" i "="6*i)
(or)
for i in range(1,11)
   print(6*i)
------------
print no.s from 10 to 1
for i in range(10,0,-1)
print(i)
output:-
10
9
.
.

1
---------
factorial of no.
n=int(input("n: ")
fact=1
for i in range(1,n+1)
  fact=fact*i
   print(fact)
---------
print a string
for ch="sreeja"
  print(ch)
output:-
s
r
e
e
j
a
-------
print 1 to 20 skip 10 using continue 
for i in range(1,21)
    if(i==10)
      continue
       print(i)
output:-
1
2
3
.
.
9
11
12
.
.
20
---------
#count even and odd no.s:
n="123456789"
counteven=0
countodd=0
for i in n:
   if int(i) % 2 == 0:
      counteven=counteven+1
   else:
      countodd=countodd+1
print(counteven,countodd)      
------------
#COUNT NO.OF LOWER AND UPPER CASES IN A STRING"
n="SREEJAsree"
count=0
countsmall=0
for i in n:
    if i.isupper():
       count=count+1
    else:
        countsmall=countsmall+1
print(count,countsmall)        
--------------
#checks whether somethings is digit
n="sree"
for i in n:
    if i.isdigit():
        print("given input is digit")
    else:
        print("given input is string")
----------------------        -----------------

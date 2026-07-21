list= [2 1 3]
list.append(4)
print(list) # add element at end
list.sort()
print(list) # arranges in ascending order
list.sort(reverse=true)
print(list) # arrangesin descending order
list.reverse()
print(list)
list.pop(2) # 2nd index,removes element from particular index
print(list)
list.insert(index,element) # inserts element 
list.insert(1,5)
print(list)
list.remove(1) # removes 1st occurance of the element 
print(list)
output:-
2 1 3 4
1 2 3
3 2 1
3 1 2
1 3
2 5 3
2 3
‐-------------------------------
print 1st ans last no
list=[ 10 20 30 40 50]
print(list[0])
print(list[-1])
‐-------------------------------
enter 3 no.s & store in list
list=[]
l1=10
l2=20
l3=30
list.append(l1)
list.append(l2)
list.append(l3)
print(list)
‐-------------------------------
find largest smallest and sum of no.s and indx of any element in list: 
n=[ 10 20 30 40 50]
print(max(n))
print(min(n))
print(n.index(n))
‐-------------------------------
avg no.and find indx
n=[ 10 20 30 40 50]
avg=sum(n)/len()
print(avg)
‐-------------------------------
find list is empty

numbers = []

if len(numbers) == 0:
    print("List is empty")
else:
    print("List is not empty"
‐-------------------------------
find 2nd largest no.

numbers = [10, 50, 20, 40, 30]

numbers.sort()

print(numbers[-2])
‐-------------------------------
lists are mutable 
list[0]=5 # possible
strings are immutable 
str[0]="y" # not possible
‐-------------------------------
numbers = [10, 20, 30, 40]

numbers.reverse()
print(numbers)
‐-------------------------------
fruits = ["apple", "banana", "mango", "orange", "grapes"]
print(fruits)
‐-------------------------------
numbers = [5, 10, 15, 20]

if 10 in numbers:
    print("Found")
else:
    print("Not Found")
-----------
#cricket score analysis
scores=[45,0,78,102,15,60]
count=0
countcent=0
print("highest score=", max(scores))
print("lowest score=", min(scores))
for i in scores:
    if i>=50 and i<=99:
        count=count+1
    if i>=100:
        countcent=countcent+1    
print("no. of half centuries=",count)
print("no. of centuries=",countcent)        
-------------
#place even and odd no.s in separete list
num=[10,14,34,50,70,98]
adults=[]
youngsters=[]
seniorcitizens=[]
for i in num:
    if i<=19:
        youngsters.append(i)
    if i>19 and i<=50:
        adults.append(i)   
    if i>50:
        seniorcitizens.append(i)
print("adults =",adults)
print("youngsters =" ,youngsters)
print("senior citizens=" ,seniorcitizens)        
-----------
#check whether a no. is present list or not
num=[1,2,3,4,6]
for i in range(1,6):
    if i not in num:
        print(i)
 -------------------       ---------
#conversion of list into tuple
l=[1,2,3,4,5]
t=tuple(l)
print(t)
---------
#roate list from right
l2=[2,3,4,7,9,1]

last=l2.pop()  #pop()-removes last elemnt
l2.insert(0,last)
print(l2)
-------
#rotate list from list
l2=[2,3,4,7,9,1]
first=l2.pop(0)  
l2.append(first)
print(l2)
----------
#2nd smallest element
l1=[12,2,3,5]
small=min(l1)
l1.remove(small)
print(min(l1))
----------
merges two list 
1)l1=[1,2,3,4,6,8]
l2=[1,2,3,6,8,9,0,19,18,7,1]
d=[]
for i in l1:
    if i in l1:
        d.append(i)
    
for i in l2:
   if i not in d:   
     if i in l2:
        d.append(i)
print(d.sort(reverse=True))                
print(d)

2)l1=[1,2,3,4]
l2=[6,7,8,9,10]
l3=l1+l2
print(l3)

3)

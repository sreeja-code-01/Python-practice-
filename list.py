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




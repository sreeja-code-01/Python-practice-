dictonaries store key value pairs
mutable
dic={
"name":"sree",
"age":17,
"isready":true
}
print(dic)

. strings requires quotes
. no.s and boolean(true,false) does not need       quotes
. can print null dict
nulldict={}
print(nulldict)
output:-{} 

 dict methods:-
. dictname.keys() # return all keys
print(dict.keys())
. dictname.values() # return all values
print(dict.values())
. dictname.items() # return all key value pairs as tuples
. dictname.get() # 
‐-------------------------------
methods:-
return all values

student = {
    "name": "Abhinay",
    "age": 17
}

print(student.values())
‐------------------------------
return all key values together
student = {
    "name": "Abhinay",
    "age": 17
}

print(student.items())
‐-------------------------------
return all keys
student = {
    "name": "Abhinay",
    "age": 17
}

print(student.keys())
‐-------------------------------
removes a key
student = {
    "name": "Abhinay",
    "age": 17
}

student.pop("age")

print(student)
‐------------------------------
clears everything from dic
student = {
    "name": "Abhinay",
    "age": 17
}

student.pop("age")

print(student)
‐-------------------------------
student.get("name")
student.keys()
student.values()
student.items()
student.update({"age": 17})
student.pop("age")
student.clear()
‐-------------------------------
 #printing all keys and values
 mobilephone={
     "brand":"samsung",
     "price":15000,
     "model":"smtg"
}
mobilephone["brand"]="oppo"
mobilephone["colour"]="black"
for i in mobilephone:
    print(i,mobilephone[i])
-----------      -------------
 #calculate sum avg ,max value
student={
    "sreeja":10,
    "priya":30,
    "harika":50
}
sum=0
for i in student:
    sum=sum+student[i]
print(sum)  
avg=sum/3
print(avg)  
print(max(student.values()))
print(student["sreeja"],student["priya"],student["harika"])
-------------
#printing all keys and values
student={
    "name":"sreeja",
    "rollno":2,
    "college":"sfc"
}
for i in student:
    print(i,student[i])
----------
#convert list into dictonary
words=["apple","banana","apple","apple","banana","orange"]
d={}
for i in words:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1    
print(d)        
-----------
#reverse of a dict
student={
    "name":"sreeja",
    "rollno":2,
    "college":"sfc"
}
reverse_dict={}
for i in student:
    reverse_dict[student[i]]=i
print(reverse_dict)
-----------
#dict methods
student={
    "sreeja":27,
    "hariks":23,
    "shruthi":12
}
student["rahul"]=13
print(student.values())
print(student.items())
student.update({"akash":21})
print(student)
print(student.get("sreeja"))
------------
#check whether a no.  is subset or not(subset=all elements in one list must be present in another list)
l1=[1,2,3,4,5]
l2=[1,2,5,7,9,2,3]
flag=True
for i in l1:
    if i not in l2:
        flag=False
        
if flag:
    print("subset")        
else:
    print("not subset")    
 --------

d={
    "a":2,
    "b":7,
    "c":1,
    "d":4
}
max=0
for value in d.values():
   
        if value>max:
            max=value
print(max)            
---------
#removing duplicate value
d={
    "a":2,
    "b":4,
    "c":2,
    "d":90,
    "e":90
}
dup={}
for key,value in d.items():
    if value not in dup.values():
        dup[key]=value
    
print(dup)
print(dup.value("a"))
    ----------

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

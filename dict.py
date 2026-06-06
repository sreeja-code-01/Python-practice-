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
Nested dictonary:-
stud={
"name":"sree",
"age":17,
"sub":{
"phy":20,
"chem":10
}
}
print(stud)
print(stud["sub"])
print(stud["sub"]["chem"
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
    
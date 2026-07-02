
fl:main
f=open("data.txt","r")  
data=f.read()
print(data)
f.close()
f2:data
hello this is me
how r u
output:hello this is me
how r u
--------
f=open("data.txt","w")  
f.write("iam here")
f.close()
output:
iam here
-----
f=open("data.txt","a")  
f.write("\napple")
f.close()
ouput:
hello this is me
how r u
apple
--------
f=open("data.txt","r+")  
f.read()
f.write("mahe")
f.close()
f2:hello world
output
 hello world 
mahe
-------
f=open("data.txt","a+")  
f.write("\n this is me ")
f.seek(0)
print(f.read())
f.close()
f2;
hello
output: hello
this is me
-------
f=open("data.txt","w+")  
f.write("this is me")
f.seek(0)
print(f.read())
f.close()
f2:
hello
output 
this is me 
--------
check whether "learning" is present in file
f=open("data.txt","r")  
data=f.read()
if "learning" in content:
  print("found)
        else:
 print("not found")
f.close()
--------
print in separate lines
f=open("data.txt","r")  
for line in f:
 print(line)
 f.close()
 -------
 count lines in a file
 f=open("data.txt","r")
 count=len(readlines)
 print(count)
f.close()
----------
copy contents from one file to another 
f1=open("data.txt","r") 
data=f1.read()
f1.close()
f2=open("data.txt","w")
f2.write(data)
f.close()
-------
f.read()-reads the file
print(f.read())-reads and prints content on screen
-------
#writing content using 'with'
with open("sample.txt","r+") as f:
    f.write("stay home stay safe")   #no close() is needed
 ---------
#reading using 'with'
with open("sample.txt","r")as f:
    print(f.read())
 -------------
#writing usimg 'with'
with open("sample.txt","a+")as f:
    f.write("this is me! here to cde!welcome to code hub")
 ----------
3count vowels in a file
with open("sample.txt","r")as f:
    data=f.read()
    
    count=0
    for i in data:
        if i in "aeiou":
            count=count+1
    print(count)        
----------------         -----------
 #count consonants in a file

with open("sample.txt","r")as f:
    data=f.read()
    count=0
    for i in data:
        if i.isalpha() and not i in "aeiou":
            count=count+1
    print(count)
 ---------------
methods:-
1) swapcase=converting upper case to lower and vice versa    
with open("sample.txt","r")as f:
    data=f.read()
    print(data.swapcase())
2)lower=converts to lower case all words

with open("sample.txt","r")as f:
    data=f.read()
    print(data.lower())

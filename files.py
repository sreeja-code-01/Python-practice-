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




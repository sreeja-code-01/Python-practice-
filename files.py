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

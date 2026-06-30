#count unique elements in a list
l=[1,2,5,2,9,5,6,2,9]
s=set(l)
print(len(s))
---------------
#find most frequenet element
l=[1,2,4,2,1,5,7,2,4,4,4,4]
s={}
for i in l:
    if i in s:
        s[i]=s[i]+1
    else:
        s[i]=1
h=0
e=0
for i in s:
    if s[i]>h:
      h=s[i]
      e=i                    
print(e)    
-----------

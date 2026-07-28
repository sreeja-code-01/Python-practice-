#rock,paper,scissor game
import random
choose=input("rock,paper,scissor(r/p/s)= ").lower()
comp=random.choice(["r","p","s"])
print(comp)
if choose=="r" and comp=="p":
    print("u won")
elif choose=="r" and comp=="s":
    print("u won")
elif choose=="r" and comp=="r":
    print("draw")
elif choose=="p" and comp=="r":
    print("comp won")
elif choose=="p" and comp=="s":
    print("comp won")
elif choose=="p" and comp=="p":
    print("draw")
elif choose=="s" and comp=="r":
    print("comp won")
elif choose=="s" and comp=="p":
    print("u wonwon")
elif choose=="s" and comp=="s":
    print("drwa")
else:
    print("invalid choice")    
----------------------
#refactoring
import random
def decide(choice):
    if choice=="y":
        print(random.randint(1,6))
    elif choice=="n":
         print("donot roll")
    else:
         print("invalid choice")
def main():
    choice=input("roll dice(y/s)= ")

    decide(choice)
main()
--------
#image procssing
from PIL import Image
image=Image.open("ganesh.jpg")
image.save("dup.png")
print("Image saved succesfully")
-----------
#QR CODE
import qrcode
qr=qrcode.QRCode()
qr.add_data("1234568901837")
qr.make(fit=True)
image=qr.make_image()
image.save("no.png")
print("saved successfully")
---------------
#cafe management system
import random
print("welcome to giri cAfe")
dic={
    "manchuria":40,
     "drinks":50,
     "tea":15,
     "coffe":16
    }
print("here is the menu")
print("manchuria=40\ndrinks=50\ntea=15\ncoffe=16")
ordertotal=0
item1=input("enter ur 1st item= ")

if item1 in dic:
    ordertotal=ordertotal+dic[item1]
    print(f"ur  1st {item1} is here")
else:
    print("this item is not in menu")    
choice=input("do u want 2nd order (y/n)= ")  
if choice=="y":

  item2=input("enter ur 2nd item= ") 

  ordertotal=ordertotal+dic[item2]
  print(f"ur 2nd {item2} is here") 
else:
    print("no item here")
print("ur total bill is", ordertotal)
--------
#random password generator
import random
choice="ABCabc@$&1234"
choice1="abscdggfuAHDURUBRJ"
choice2="8754353"
choice3="@%$*^&!"
length=int(input("length: "))
user1=input("do u want to add letter (y/n): ")
user2=input("do u want to add s.c (y/n): ")
password=""
for i in range(length):
    if user1=="y" and user2=="y":
        password=password+random.choice(choice)

    elif user1=="y"and user2=="n":
        password=password+random.choice(choice1)
    elif user1=="n"and user2=="y":
        password=password+random.choice(choice3)    
    else:
        password=password+random.choice(choice2)    
print(password)        
---------------





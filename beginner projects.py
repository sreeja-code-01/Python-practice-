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








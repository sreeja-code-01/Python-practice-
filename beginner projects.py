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










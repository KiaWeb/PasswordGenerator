import random
import time
import os
import string
f=open("keys.txt","a")
def run():
    a=string.ascii_letters+string.digits
    xn=input("How many characters would you like the password to be:")
    b=random.choices(a,k=int(xn))
    f.write("\n"+b)
    print("Appended "+b+" to keys")
def start2(tmes):
    tames = 0
    elapsed = 0
    while True:
        while True:
            elapsed = elapsed + 1
            time.sleep(1)
            if tames == tmes:
                break
        run()
        tames = tames + 1
        if tames == tmes:
            f.close()
            print("Stopped, check keys.txt. Password amount: "+str(tames)+".")
            time.sleep(3)
            break
def start():
    tmes = input("How many passwords would you like this to generate? e.g 3: ")
    tmes = int(tmes)
    start2(tmes)
start()

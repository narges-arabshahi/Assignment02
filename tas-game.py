import random
while True:   
    a=int(input("Please enter 0= "))
    if a==0:
        tas=random.randint(1,6)
        print("number tas is",tas)
        if tas==6:
            print("you win!you can again tas: ")
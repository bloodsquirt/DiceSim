import random


loop="y"

while loop=="y":

    no=random.randint(1,6)

    if no==1:
        print("---------")
        print("|       |")
        print("|   0   |")
        print("|       |")
        print("---------")

    elif no==2:
        print("---------")
        print("| 0     |")
        print("|       |")
        print("|     0 |")
        print("---------")

    elif no==3:
        print("---------")
        print("| 0     |")
        print("|   0   |")
        print("|     0 |")
        print("---------")

    elif no==4:
        print("---------")
        print("| 0   0 |")
        print("|       |")
        print("| 0   0 |")
        print("---------")

    elif no==5:
        print("---------")
        print("| 0   0 |")
        print("|   0   |")
        print("| 0   0 |")
        print("---------")

    elif no==6:
        print("---------")
        print("| 0   0 |")
        print("| 0   0 |")
        print("| 0   0 |")
        print("---------")

    loop=input("Press y to roll the dice press n to exit: ")
    print("\n")

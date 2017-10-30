name = input("What is your name? ")
password = input("What is your password? ")
age = int(input("What is your age? "))

if name == "Mary":
    print("Hello Mary")
elif age < 30:
    print("You are not Mary, you child.")
elif age > 2000:
    print("You are not Mary. You are the great undead!")
elif age > 50:
    print("Your old ass aint Mary!")
else:
    print("Hello stranger")
    if password == "swordfish":
        print("Access Granted.")
    else:
        print("Wrong Password")

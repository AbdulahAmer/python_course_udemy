myage = 30
userage = int(input("Enter your age: "))

if myage > userage:
    print("Paul is",str(myage),"and you are",str(userage) + ". Paul is older than you.")
elif myage == userage:
    print("You and Paul are both",str(myage)+".")
else:
    print("Paul is", str(myage),"and you are",str(userage) + ". You are older than Paul")

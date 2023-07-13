choice = eval(input("Hours to Minutes (Enter 1) \nMinutes to Hours (Enter 2)"))
if (choice == 1):
    num = eval(input("How Many Hours?"))
    print ((num * 60), " minutes.")
elif(choice == 2):
    num = eval(input("How Many Minutes?"))
    print ((num //60), " hours.")
else:
    print ("Please enter 1 or 2")
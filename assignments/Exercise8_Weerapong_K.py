usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234" :
    print("Welcome to store!")
    print("apple 30 thb each")
    print("banana 7 thb each")
    print("pineapple 25 thb each")
    print("orange 8 thb each")
    apple = 30
    banana = 7
    pineapple = 25
    orange = 8
    print("pleae select :")
    print("--------------------")
    userChoice = int(input("1.apple 2.banana 3.pineapple 4.orange 5.done"))

    if userChoice == 1:
        print("how many apple do you want?")
        userQuantity = int(input())
        userChoice = apple
    elif userChoice == 2:
        print("how many banana do you want?")
        userQuantity = int(input())
        userChoice = banana
    elif userChoice == 3:
        print("how many banana do you want?")
        userQuantity = int(input())
        userChoice = pineapple
    elif userChoice == 4:
        print("how many banana do you want?")
        userQuantity = int(input())
        userChoice = orange
    else:
        print("calculating price")
    print("total is : ")
    total = userChoice * userQuantity
    print(total)
else:
    print("Wrong username")
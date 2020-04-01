import random


def user_number():
    number = int(input("enter a number between 0 and 10:\n"))
    return number


def random_number():
    return random.randint(0,10)


def evaluation():
    while 1 != 2:
        var_usrnum = user_number()
        var_rndnum = random_number()

        if var_usrnum > var_rndnum:
            print("too high")
        elif var_usrnum < var_rndnum:
            print("too low")
        else:
            print("correct")
            break
        newrndnum = str(var_rndnum)
        newusrnum = str(var_usrnum)
        print("random number was  " + newrndnum)
        print("your guess was  " + newusrnum)


if __name__ == "__main__":
    evaluation()




#
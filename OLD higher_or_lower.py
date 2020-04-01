import random
def user_number():
    number = input("enter a number between 0 and 10:\n")
    return number
def random_number():
    return random.randint(0,10)
def evaluation():
    var_usrnum = user_number()
    var_rndnum = random_number()


    if var_usrnum > var_rndnum:
        print ("too high")
    elif var_usrnum < var_rndnum:
        print ("too low")
    else:
        print ("correct")

    newrndnum = str(var_rndnum)
    newusrnum = str(var_usrnum)
    print ("random number was  " + newrndnum)
    print("your guess was  " + newusrnum)

evaluation()
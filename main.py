import random 

def checknumber(inputnumber):
    intnumber = int(inputnumber)
    print("Generating number....")
    computernumber = int(random.randint(1, 1000))
    if intnumber == computernumber:
        print(f"Our number was {computernumber}. You had {inputnumber}. It is a tie.")
    elif intnumber > computernumber:
        print(f"Our number was {computernumber}. You had {inputnumber}. You win by {intnumber-computernumber} points.")
    elif intnumber < computernumber:
        print(f"Our number was {computernumber}. You had {inputnumber}. We win by {computernumber-intnumber} points.")
def generatenumber():
    gennum = int(random.randint(1, 1000))
    print(f"Your number is {gennum}")
    return gennum
while True:
    userinput = input("Would you like to start a game?\n").lower()
    if (userinput == "yes"):
        ognum = generatenumber()
        otherinput = input("Would you like to generate new number?\n").lower()
        if otherinput == "yes":
            numbers = generatenumber()
            checknumber(numbers)
        else:
            checknumber(ognum)  
    else:
        pass
import random 

def checknumber(inputnumber):
    intnumber = int(inputnumber)
    print(f"Your number is {inputnumber}")
    print("Generating number....")
    computernumber = int(random.randint(1, 1000))
    if intnumber == computernumber:
        print(f"Our number was {computernumber}. You had {inputnumber}. It is a tie.")
    elif intnumber > computernumber:
        print(f"Our number was {computernumber}. You had {inputnumber}. You win by {intnumber-computernumber} points.")
    elif intnumber < computernumber:
        print(f"Our number was {computernumber}. You had {inputnumber}. We win by {computernumber-intnumber} points.")
while True:
    userinput = input("Pick a number 1-1000\n")
    isnumber = userinput.isnumeric()
    if isnumber == False:
        print("That is not a number dummy!")
    elif int(userinput) > 1000:
        print("Your number is above 1000.")
    else:
        checknumber(userinput)  

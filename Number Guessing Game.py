while True:
#Generate random integer between 1 and 100
    import random
    
    b = 100
    
    Score = 0
    print("You will have to guess a number between the lowermost limit you will choose and the uppermost limit you will choose.")
    print("Please enter the lowermost limit")
    user_input=input("Lowermost limit:  ")
    a = int(user_input)
    print("Please enter the uppermost limit")
    user_input=input("Uppermost Limit:  ")
   
    b = int(user_input)
    random_integer = random.randint(a, b)
    print("Loading random integer between " + str(a) + " and " + str(b) + "... (1%)")
    print("Loading random integer between " + str(a) + " and " + str(b) + "... (25%)")
    print("Loading random integer between " + str(a) + " and " + str(b) + "... (50%)")
    print("Loading random integer between " + str(a) + " and " + str(b) + "... (75%)")
    print("Loading random integer between " + str(a) + " and " + str(b) + "... (99%)")
    print("Loading random integer between " + str(a) + " and " + str(b) + "... (Done)")
    print("I have a number in mind between " + str(a) + " and " + str(b) + ", try and guess it!")
    while True:
        user_input=input("You:  ")
        while True:
            #Number is now user_input as an integer
            number = int(user_input)
            #If the input is exactly the integer the program was thinking of, this happens:
            if number == random_integer:
                print("You got it!")
                user_input=input(f"You got it in " + str(Score) + " tries!")
                #If the integer is too big, then this will happen:
            elif number > random_integer:
                print("Your guess is too big: try again")
                Score = Score + 1 
                break
            else:
                #If the integer is too small, then this will happen:
                print("Your guess is too small: try again")
                Score = Score + 1
                break



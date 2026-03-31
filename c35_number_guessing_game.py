import random
flag = True 

def get_integer(prompt):
    """
    Get an interger from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The string that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        #else: 
        print(f"{temp} is not a valid number")


help(get_integer)
#print(input.__doc__)
#print("*" * 80)
#print(get_integer.__doc__)
#print("*" * 80)

highest = 1000
answer = random.randint(1, highest)
print(answer)       # TODO: remove after testing
guess = 0 # initialize to any number that doesn't equal to answer

while guess != answer:
    guess = get_integer(f"Please guess a number between 1 to {highest}:")
    if guess == 0:
        break
    elif guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess > answer:
            print("please guess lower")
        else:
            print("Please guess higher")

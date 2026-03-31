low = 1
high = 1000

user_ans= int(input(f"Please think of a number between {low} and {high}: "))

guesses = 1

while True:
    print(f"\tGuessing in the range of {low} to {high}")
    guess = low + (high - low) // 2 
    high_low = input(f"My guess is {guess}. Should i guess higher or lower?"
                     " enter h or l, or c if my guess was correct: ").casefold()
    

    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess
        # pass
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess
        # pass
        high = guess - 1
    elif high_low == "c":
        print(f"I got it in {guesses} guesses")
        break
    else:
        print("Please enter h, l or c")

    # guesses = guesses + 1
    guesses += 1        # augmented assignment
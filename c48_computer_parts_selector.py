available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable",
                   "dvd drive"]

#valid_choice = [str(i) for i in range(1, len(available_parts) + 1)]

valid_choice = []
for i in range(1, len(available_parts) + 1):
    valid_choice.append(str(i))

current_choice = "-"
computer_parts = [] # create an empty list

available_parts.sort()

while current_choice != "0":
    if current_choice in valid_choice:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's alr in, so remove it
            print(f"Removing {current_choice}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {current_choice}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains {computer_parts}")
        
    else:
        print("Please add options from the list below:")
        for number, parts in enumerate(available_parts):
            print(f"{number + 1}: {parts}")
    
    current_choice = input("Please add your option:")
print(computer_parts)
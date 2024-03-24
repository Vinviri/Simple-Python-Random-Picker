import random

while True:
    Judul = input("Enter a title for this picker: ")
    inputs = []
    while True:
        value = input("Enter a value that you want to input (or press Enter to finish): ")
        if value == "":
            break
        inputs.append(value)

    print("\n" + Judul)
    print("\nWho's The Choosen One!?\n")

    if inputs:
        print("\nYou Entered:")
        for value in inputs:
            print(value)

        random_choice = random.choice(inputs)
        print("\nCongrats To: ", random_choice)
    else:
        print("No Inputs Provided.")

    repeat = input("\nDo you want to run the picker again? (yes/y/no/n): ")
    if repeat.lower() != "yes" and repeat.lower() != "y":
        print("Goodbye, Have a Nice Day (from Rafi)")
        break
    
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
with open("Input/names/invited_names.txt") as guests:
    list_of_guest = guests.readlines()
    print(list_of_guest)
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    for guest in list_of_guest:
        with open("Input/Letters/starting_letter.txt") as data:
            letter = data.read()
            stripped_name = guest.strip()
            updated_list = letter.replace("[name]", stripped_name)
            # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
            print(updated_list)
            with open(f'Output/ReadyToSend/letter_for_{stripped_name}.txt', mode="w") as completed_letter:
                completed_letter.write(updated_list)

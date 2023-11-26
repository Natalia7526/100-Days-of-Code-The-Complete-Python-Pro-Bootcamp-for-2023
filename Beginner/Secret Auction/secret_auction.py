import os

silent_auction = {}
name_list = []
continue_auction = True
while continue_auction != False:
    name = input("What is your name?: \n")
    price = int(input("What is your bid?: \n$"))
    silent_auction[name] = price
    print(silent_auction)
    new_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if new_bidders == "no":
        os.system('cls' if os.name == 'nt' else 'clear')
        continue_auction = False
        max_value = max(silent_auction.values())
        winner = [key for key, value in silent_auction.items() if value == max_value][0]
        print(f"The auction was won by {winner}, who offered {max_value}$")
    else:
        # the command to clear is `cls` on Windows and `clear` on most everything else
        os.system('cls' if os.name == 'nt' else 'clear')
        continue_auction = True



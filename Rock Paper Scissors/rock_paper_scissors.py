import random

rock = '''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ['Rock', 'Paper', 'Scissors']
game_images = [rock, paper, scissors]

print("Welcome in Rock, Paper, Scissors game!")
your_choice = int(input('''What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n'''))

print('''You selected: ''' + options[your_choice] + game_images[your_choice])

computer_choice = random.randint(0, 2)
print(f"Computer choose: " + options[computer_choice])
print(game_images[computer_choice])

if your_choice >= 3 or your_choice < 0:
    print("You typed an invalid number, you lose!")
elif computer_choice == 2 and your_choice == 0:
    print("You win!")
elif computer_choice == 0 and your_choice == 2:
    print("You lose !")
elif computer_choice == 2 and your_choice == 1:
    print("You lose !")
elif computer_choice == 1 and your_choice == 2:
    print("You win !")
elif computer_choice == 1 and your_choice == 0:
    print("You lose !")
elif computer_choice == 0 and your_choice == 1:
    print("You win !")
elif computer_choice == your_choice:
    print("It's a draw")


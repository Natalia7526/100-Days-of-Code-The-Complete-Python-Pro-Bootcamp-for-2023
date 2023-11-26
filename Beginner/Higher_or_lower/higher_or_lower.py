import random, os
from game_data import data

def print_comparison(player_a, player_b):
    print(f"Compare A: {player_a['name']}, a {player_a['description']}, from {player_a['country']}")
    print(f"Against B: {player_b['name']}, a {player_b['description']}, from {player_b['country']}")

def play_game():
    continue_game = True
    current_score = 0

    while continue_game:
        player_a, player_b = random.sample(data, k=2)

        print_comparison(player_a, player_b)

        decision = input("Who has more followers? Type 'A' or 'B': ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if decision == 'A' and player_a['follower_count'] > player_b['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        elif decision == 'B' and player_b['follower_count'] > player_a['follower_count']:
            current_score += 1
            print(f"You're right! Current score: {current_score}")
        else:
            continue_game = False
            print(f"Sorry that's wrong. Final score: {current_score}")

if __name__ == "__main__":
    play_game()
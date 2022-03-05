import random

CHOICES = [
    "rock",
    "paper",
    "scissors"
    ]

rock = CHOICES[0]
paper = CHOICES[1]
scissors = CHOICES[2]

def test_game():
    player_score = 0
    computer_score = 0

    while player_score <= 3 and computer_score <= 3:
        player_choice = input(f"Current Score: Player - {player_score}, Computer - {computer_score}\nWill you use rock, paper or scissors? ").lower()
        computer_choice = random.choice(CHOICES)
        round_result_win = f'\nPlayer chose {player_choice} Opponent chose {computer_choice}, Player wins!\n'
        round_result_loss = f'\nPlayer chose {player_choice} Opponent chose {computer_choice}, Opponent wins!\n'

        if player_choice == computer_choice:
            print(f'\nBoth players chose {player_choice}, it was a tie!\n')
            continue

        elif player_choice == rock:
            if computer_choice == scissors:
                print(round_result_win)
                player_score += 1
            else:
                print(round_result_loss)
                computer_score += 1

        elif player_choice == scissors:
            if computer_choice == paper:
                print(round_result_win)
                player_score += 1
            else:
                print(round_result_loss)
                computer_score += 1

        elif player_choice == paper:
            if computer_choice == rock:
                print(round_result_win)
                player_score += 1
            else:
                print(round_result_loss)
                computer_score += 1

        if player_score == 3 or computer_score == 3:
            print(f'\nGame over! Final scores: {player_score} - {computer_score}!\n')
            play_again = input('Want to play again? y/n ').lower()
            if play_again == 'y':
                player_score = 0
                computer_score = 0
                continue
            else:
                break
 
if __name__ == "__main__":
    test_game()
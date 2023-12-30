import random

def roll_dice():
    return random.randint(1, 6)

def snake_and_ladder(position):
    snakes_and_ladders = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
    return snakes_and_ladders.get(position, position)

def display_board(player1, player2):
    print(f"Player 1 is at position {player1} | Player 2 is at position {player2}")

def play_game():
    player1_position = 1
    player2_position = 1

    while player1_position < 100 and player2_position < 100:
        input("Player 1, press Enter to roll the dice...")
        dice_roll = roll_dice()
        player1_position += dice_roll
        player1_position = snake_and_ladder(player1_position)

        display_board(player1_position, player2_position)

        if player1_position >= 100:
            print("Player 1 wins!")
            break

        input("Player 2, press Enter to roll the dice...")
        dice_roll = roll_dice()
        player2_position += dice_roll
        player2_position = snake_and_ladder(player2_position)

        display_board(player1_position, player2_position)

        if player2_position >= 100:
            print("Player 2 wins!")
            break

if __name__ == "__main__":
    play_game()

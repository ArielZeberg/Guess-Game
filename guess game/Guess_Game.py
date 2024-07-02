import random
import json

# Save categories to a JSON file named 'words_bank.json'
with open('words_bank.json', 'w') as file:
    json.dump(categories, file)

# Load categories from the JSON file
with open('words_bank.json', 'r') as file:
    categories = json.load(file)

# Print available categories
print("Available categories:")
for category in categories.keys():
    print(category)

# Get the category input from the user
category = input("Select category: ")
if category not in categories:
    print("Error, category doesn't exist")
    exit()

# Select a random word from the chosen category
word = random.choice(categories[category])
# Initialize the covered word with underscores
covered = ["_" for _ in range(len(word))]
print(" ".join(covered))

# Get player names and initialize their scores
player1_name = input("Enter player1 name: ").capitalize()
player2_name = input("Enter player2 name: ").capitalize()
player1_score = 0
player2_score = 0

# Function to handle each player's turn
def game(player_name, word, covered, player_score):
    # Get the player's guess
    player_guess = input(f"{player_name}, it's your turn. Guess a letter: ")
    if player_guess in word:
        # If the guess is correct, update the covered word and score
        for i in range(len(word)):
            if player_guess == word[i]:
                covered[i] = player_guess
                player_score += 1
        print(" ".join(covered))
        correct_guess = True
    else:
        # If the guess is incorrect, inform the player
        print("Sorry, wrong guess")
        correct_guess = False
    return covered, player_score, correct_guess

# Main game loop
while "_" in covered:
    correct_guess = True
    # Player 1's turn
    while correct_guess:
        covered, player1_score, correct_guess = game(player1_name, word, covered, player1_score)
    correct_guess = True
    # Player 2's turn
    while correct_guess and "_" in covered:
        covered, player2_score, correct_guess = game(player2_name, word, covered, player2_score)

# Determine and print the winner
if player1_score > player2_score:
    print(f"{player1_name}, congrats! You're the winner!")
else:
    print(f"{player2_name}, congrats! You're the winner!")

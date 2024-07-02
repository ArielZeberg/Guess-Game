import random
import json

# Load categories from the json file
with open('/Users/yaarabenchayun/Desktop/programing study/Assaf/guess game/words_bank.json', 'r') as file:
    categories = json.load(file)

for category in categories.keys():
    print(category)

category = input("Select category: ")
if category not in categories:
    print("Error, category doesn't exist")
    exit()

word = random.choice(categories[category])
covered = ["_" for _ in range(len(word))]
print(" ".join(covered))

player1_name = input("Enter player1 name: ").capitalize()
player2_name = input("Enter player2 name: ").capitalize()
player1_score = 0
player2_score = 0

def game(player_name, word, covered, player_score):
    player_guess = input(f"{player_name}, it's your turn. Guess a letter: ")
    if player_guess in word:
        for i in range(len(word)):
            if player_guess == word[i]:
                covered[i] = player_guess
                player_score += 1
        print(" ".join(covered))
        correct_guess = True
    else:
        print("Sorry, wrong guess")
        correct_guess = False
    return covered, player_score, correct_guess

while "_" in covered:
    correct_guess = True
    while correct_guess:
        covered, player1_score, correct_guess = game(player1_name, word, covered, player1_score)
    correct_guess = True
    while correct_guess and "_" in covered:
        covered, player2_score, correct_guess = game(player2_name, word, covered, player2_score)

if player1_score > player2_score:
    print(f"{player1_name}, congrats! You're the winner!")
else:
    print(f"{player2_name}, congrats! You're the winner!")

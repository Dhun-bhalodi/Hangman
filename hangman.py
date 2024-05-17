import random

stages = ['''
  +---+
  |   |
  o   |
 /|\  |
 / \  |
      |
========
''','''
 +---+
  |   |
  o   |
 /|\  |
 /    |
      |
========
''','''
 +---+
  |   |
  o   |
 /|\  |
      |
      |
========
''','''
 +---+
  |   |
  o   |
 /|   |
      |
      |
========
''','''
 +---+
  |   |
  o   |
 /    |
      |
      |
========
''','''
 +---+
  |   |
  o   |
      |
      |
      |
========
''','''
+---+
  |   |
      |
      |
      |
      |
========
''']
word_list = ['camel','apple','pineapple']

chosen_word = random.choice(word_list)
lives = 6
print(chosen_word)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game=False
while not end_of_game:
    guess = input("Guess a letter:").lower()

    if guess in display:
        print(f"You've alredy guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You loose a life")
        lives -= 1
        if lives==0:
            end_of_game=True
            print("You loose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game=True
        print("You Win")

    print(stages[lives])
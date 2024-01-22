import random
word_list = ["woodcuter","baboon","camel"]
chosen_word= random.choice(word_list)

lives = 6

display = []
for letter in range(len(chosen_word)):
    display += "_"
print(display)

end = False
while not end :
    guess = input("guess a letter :").lower()
    for position in range(len(chosen_word)) :
     letter = chosen_word[position]
     print (f"current position : {position}\n curernt letter : {letter}\n guessed letter : {guess}")
    if letter == guess:
        display[position] = letter
    
    print(display)
    if guess not in chosen_word:
       lives -=1
       print("you loose")

    if "_" not in display:
     end = True
     print("you win")
    print(stages[lives]) 
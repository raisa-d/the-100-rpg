import random as r
from util import clear, enter, draw

# colors
orange = '\x1b[38;2;255;90;0m\x1b[1m'
green = "\033[32m"
bold = "\033[1m"
end = "\033[0m" # end any formatting
strike = "\033[9m" # strikethrough


# code decryption minigame for fixing dropship propulsion
def generate_code(length):
    symbols = ["&", "%", "$", "#", "@", "*", "+"]
    return ''.join(r.choice(symbols) for i in range(length))
def code_decryption_minigame():
    symbols_picked = []
    code_length = 4
    correct_code = generate_code(code_length)
    lives = 5
    minigame_title = f"{orange}{strike}Xx  {end} {orange}Decrypt the Code{strike}  xX{end}\n"
    # print(f"ANSWER: {correct_code}")

    while True:
        clear()
        print(f"{minigame_title:>110}")
        print("You encounter a control panel with mysterious symbols.\n")

        code_solved = True # checking if the entire code is correct
        for i in correct_code:
            if i in symbols_picked:
                print(f"{bold}{i}{end}", end=" ")
                code_solved = True
            else:
                print(f"{bold}_{end}", end = " ")
                code_solved = False
        
        print(f"\n\nSymbols: {bold}{orange}&, %, $, #, @, *, +{end}") ### consider changing this so it's kinda like hangman? correct symbols stay
        print(f"\n{lives} Lives Left")
        
        player_guess = input("\nGuess a symbol you think is in the code\n> ").strip().lower()

        if player_guess in symbols_picked: # if you already picked that symbol
            print(f'You\'ve already guessed symbol {player_guess}')
            lives -= 1
            enter()
            continue
        symbols_picked.append(player_guess) # add symbol to list

        if player_guess in correct_code: # if symbol is somewhere in the code
            print("You solved a piece of the code!")
            enter()
        else: # if symbol is not in the code
            print("\nThat symbol is not in the code.")
            lives -= 1
            enter()
        
        if code_solved: # if solve code
            return True

        if lives < 1 and code_solved == False:
            return False

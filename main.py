## The 100 RPG

import random as r, time as t
from crime import crimes
from util import clear, enter, draw, red, underline, bold, end, white, yellow, green, cyan, gold, blue, copper, purple, orange, gray
from cutscenes import intro
from events import go_to_Earth, character_qualities, game_plan
from items import rapier, dagger, multipurpose_knife, throwing_knives, shiv, wrench
from items import wristband, the_fleim, rations, small_waterskin, weapons_for_sale, tek_for_sale, potions_all
from characters import print_inventory, Player, azgeda, save_game
from battle import Battle

# default booleans
run = True # game is running
play = False # playing game

# booleans for locations
in_BaseCamp = False
in_MtWeather = False
in_Polis = False
in_TrikruWoods = False
in_Deadzone = False
in_ShallowValley = False
in_Tondc = False
in_Marketplace = False

def choose_crime(): # choose crime/create player instance
    while True:
        clear()
        print(f"{bold}What was your crime?\n(type in the number that corresponds with each crime to see details)\n{end}")
        draw()
        counter = 1
        for i in crimes:
            print(f"{bold}{cyan}{counter}. {crimes[i]['desc']}\n{end}")
            counter += 1 
        draw()
        crime = input("\n> ").strip().lower()
        
        if crime.isdigit() and 1 <= int(crime) <= len(crimes):
            crime_index = int(crime) - 1 # converting answer into index
            crime_choice = crimes[str(crime_index)]
            print(f"{bold}{crime_choice['title']}{end}")
            print(f"\n{bold}Back | {red}Skills | {orange}Items | {yellow}Implications | {green}Select |{end}")
            while True:
                info = input("\n> ").strip().lower()
                if info in ['skills', 'skill']: # if choose skills
                    print(f"\n{bold}{crime_choice['skills']}{end}")

                elif info in ['items', 'item']: # items
                    print(f"\n{bold}{crime_choice['items']}{end}")
                
                elif info in ['implications', 'imp', 'i']: # implications
                    print(f"\n{bold}{crime_choice['implications']}{end}")
                
                elif info in ['b', 'back', 'x', 'exit', 'l', 'leave']:
                    break

                elif info in ['select', 's']: # if select this character!
                    select = input('\nDid you mean to select this crime?\n> ').strip().lower() # confirming selection
                    
                    if select in ['y', 'yes']: # yes
                        char_name = input("\nWhat is your character's name?\n> ").strip().title()
                        while char_name == "": # if they don't write a name, make them
                            char_name = input('Please enter a name\n\n> ').strip().title()
                        
                        if crime_index == 0: # vital supplies
                            player = Player(char_name, 11, 11, 10, 14, 2, 15, 2, 16, 3, 13, 1, 11, 0, 9, -1, 2, 0, 12, 0, multipurpose_knife, wristband, {})
                            player.add_to_inv(multipurpose_knife, 1)
                            player.add_to_inv(wristband, 1)
                            player.add_to_inv(rations, 2)
                            player.add_to_inv(small_waterskin, 1)
                            character_qualities.append("others mistrust you")
                            return character_qualities
                        
                        elif crime_index == 1: # rebellion leader
                            player = Player(char_name, 12, 12, 10, 16, 3, 14, 2, 15, 2, 9, -1, 11, 0, 13, 1, 2, 0, 12, 1, throwing_knives, wristband, {})
                            player.add_to_inv(throwing_knives, 1)
                            player.add_to_inv(wristband, 1)
                            player.add_to_inv(rations, 2)
                            player.add_to_inv(small_waterskin, 1)
                        
                        elif crime_index == 2: # cannabis thief
                            player = Player(char_name, 10, 10, 10, 13, 1, 14, 2, 15, 2, 11, 0, 16, 3, 9, -1, 2, 0, 12, 2, shiv, wristband, {})
                            player.add_to_inv(shiv, 1)
                            player.add_to_inv(wristband, 1)
                            player.add_to_inv(rations, 2)
                            player.add_to_inv(small_waterskin, 1)

                        elif crime_index == 3: # second child
                            player = Player(char_name, 12, 12, 10, 16, 3, 15, 2, 14, 2, 11, 0, 9, -1, 13, 1, 2, 0, 12, 3, dagger, wristband, {})
                            player.add_to_inv(dagger, 1)
                            player.add_to_inv(wristband, 1)
                            player.add_to_inv(rations, 2)
                            player.add_to_inv(small_waterskin, 1)
                    
                        elif crime_index == 4: # falsely accused
                            player = Player(char_name, 10, 10, 10, 16, 3, 15, 2, 14, 2, 9, -1, 13, 1, 11, 0, 2, 0, 13, 4, wrench, wristband, {})
                            player.add_to_inv(wrench, 1)
                            player.add_to_inv(wristband, 1)
                            player.add_to_inv(rations, 2)
                            player.add_to_inv(small_waterskin, 1)
                            character_qualities.append("others mistrust you")
                            return character_qualities

                        return player

                    elif select in ['n', 'no']: # no
                        enter()
                        continue
                    
                    else: # invalid input handling
                        print(f"{red}{bold}Invalid command.\n{green}Valid commands:{white}['yes', 'y'\n'no', 'n']")
                        enter()
                        continue
                else: # invalid input handling
                    print(f"{red}{bold}Invalid command.\n{green}Valid commands:{end}\n['b', 'back', 'x', 'exit', 'l', 'leave'\n'skills', 'skill'\n'items', 'item'\n'implications', 'imp', 'i'\n'select', 's']")
                    enter()
                    break
                    
        else: # invalid input handling
            print(f'{red}{bold}Invalid command.\n{green}Please enter the number that corresponds\nwith the crime your character has committed{end}')
            enter()
            clear()
            continue

def go_to_Polis():
    clear()
    print(f"As you approach the imposing gates of {bold}{yellow}Polis{end} a sense of wonder\nand trepidation washes over you.\nThe ancient city stands as a testament to resilience in\na world devastated by nuclear catastrophe.\n")
    input(f"[{cyan}{bold}Enter{end}] to walk through the gates\n")
    inPolis = True
    while inPolis:
        clear()
        print(f"Location: {red}{underline}{bold}Polis{end}\n")
        print("The square is alive with the chatter of Grounders in various outfits,\neach representing their clan. Warriors bearing weapons stride with\nconfidence, while traders and healers offer their wares and services at their\nmarket stalls. Grounder children play among the bustling crowd.\n")
        print(f"{bold}Exit | {red}Save {white}| {gold}Inv {white}| {blue}Stats {white}| {copper}Marketplace{white} | {green}Converse {white}|{end}")
        action = input("> ").strip().lower()
        if action in ['x', 'exit']: # exit
            save_game(player, 'load.json') # save before exiting game
            print("Goodbye!")
            quit()
        if action in ['i', 'inv', 'inventory']: # inventory
            print_inventory(player)
        elif action == "save": # save
            save_game(player, 'load.json') # save game
        elif action in ['s', 'stats']: # stats
            player.print_stats()
        elif action in ['m', 'marketplace', 'market', 'store']: # marketplace
            go_to_Market()
        
        elif action in ['c', 'converse', 'talk']: # converse
            while True:
                clear()
                print(f'You walk towards the center of the square and see\na group of {bold}{yellow}Azgeda Gonas{end} whispering amongst themselves,\nand {bold}{purple}an elderly woman{end} adorned in Fleimkepa robes who\nis sharing wisdom with avid listeners who hang on to her every word.\n\nWho would you like to speak with?\n\n[{bold}{cyan}l{end}] to leave') ### ADD CONVERSATIONS HERE
                response = input('\n> ').strip().lower()
                if response is not None:
                    if response in ['azgeda gonas', 'azgeda', 'a', 'gonas', 'gona', 'g']:
                        if azgeda.HP <= 0: azgeda.HP = azgeda.maxHP # if you already fought them and their HP is 0, set it to max again so player can battle again
                        azgeda_battle = Battle(player, azgeda) # create instance of Battle class
                        result = azgeda_battle.start_battle()
                        
                        if result: # if you defeat the enemy
                            enter()
                            clear()
                            print(f"You have defeated the {azgeda_battle.enemy.name}!")
                            print(f"\n{bold}+ {copper}{azgeda_battle.enemy.drop_item.name}{white}\n+ {gold}{azgeda_battle.enemy.drop_GP} gp{white}\n+ {green}3 HP 🩸{end}")
                            
                            # drop items
                            azgeda_battle.plyr.add_to_inv(azgeda_battle.enemy.drop_item, 1)
                            azgeda_battle.plyr.gp += azgeda_battle.enemy.drop_GP
                            azgeda_battle.plyr.xp += 30
                            azgeda_battle.plyr.HP += 3
                            enter()
    
                        else: # if enemy defeats you 
                            print('\nYu gonplei ste odon.\nMay we meet again.')
                            quit()

                    elif response in ['woman', 'w', 'elderly woman', 'elder', 'fleimkepa', 'f', 'flamekeeper']:
                        if player.name.lower() == 'fleimkepa': ### change this interaction since fleimkepa is no longer a character choice
                            print('You walk closer to the woman and realize it is Luna,\nthe eldest remaining fleimkepa.\n')
                            t.sleep(1)
                            print("\"Young Fleimkepa, it is up to you now to\nprotect both the Fleim and the Heda who bears it.\nMeet me at the Temple so I may give you something.\"")
                            input(f"\n[{bold}{cyan}Enter{end}] to go to the Temple with Luna\n")
                            clear()
                            temple_title = f"{bold}{purple}[The Temple]{end}"
                            print(f"{temple_title:^80}\n")
                            print("The temple is a grand structure, crafted from weathered stone.\nInside, the air is thick with the scent of incense and the light\nof flickering candles. The temple walls depict the ancient histories\nof the past Commanders.\n")
                            t.sleep(3)
                            print(f"At the far end of the temple, Luna is standing by an elevated platform\nupon which rests the Fleim. She beckons to you:\n{bold}{purple}\"I am passing the Fleim on to you. Protect it, and the next Commander,\nwith your life.\"{end}\n\nWill you accept the honor?") ### Add a minigame/test in order to actually be given the Fleim?
                            yes_or_no = input("\n> ").strip().lower()
                            if yes_or_no in ['yes', 'y']:
                                print('She takes the flame, puts it in a black tin, and places it in your open hand.') ### write better narrative and add flame to inventory
                                player.add_to_inv(the_fleim, 1)
                            elif yes_or_no in ['no', 'n']:
                                print('You are no fleimkepa. You are a disgrace to our people.') ### add narrative here
                                enter()
                                break
                            else:
                                print('Please choose yes or no.') ### make a while loop?
                                enter() 
                        else:
                            print('The woman whispers something in your ear. (CHANGE THIS LATER)') ### add conversation non-fleimkepas have with her
                        enter()
                    elif response in ['x', 'exit', 'e', 'leave', 'l']: break
                    else: 
                        print(f"{red}Invalid command.{end}\n{green}Valid commands:{end}\n['azgeda gonas', 'azgeda', 'a', 'gonas', 'gona', 'g',\n'woman', 'w', 'elderly woman', 'elder', 'fleimkepa', 'f', 'flamekeeper',\n'x', 'exit', 'e', 'leave', 'l']")
                        enter()
                else: 
                    print(f"{red}Invalid command.{end}\n{green}Valid commands:{end}\n['trikru gonas', 'trikru', 't', 'gonas', 'gona', 'g',\n'woman', 'w', 'elderly woman', 'elder', 'fleimkepa', 'f', 'flamekeeper',\n'x', 'exit', 'e', 'leave', 'l']")
                    enter()
            
        else: # invalid input
            print(f"{red}{bold}Invalid{end} command.")
            t.sleep(0.5)
            print(f"\n{bold}{green}Valid{end} commands:\n['x', 'exit'\n'i', 'inv', 'inventory'\n's', 'stats'\n'm', 'marketplace', 'market', 'store'\n'c', 'converse', 'talk']")
            enter()
def go_to_BaseCamp(): ###
    pass
def go_to_MtWeather(): ###
    pass
def go_to_TrikruWoods(): ###
    pass
def go_to_Market(): 
    in_Marketplace = True
    while in_Marketplace:
        clear()
        print(f"The market stalls are adorned with colorful fabrics and\ngoods from each clan.\nThey offer you their wares as you pass by each stall.\n\n{bold}What kind of goods are you looking for?\n{end}")
        print(f"| {bold}{copper}Shuda {white}(Weapons) | {bold}{purple}Potions{white} | {bold}{blue}Tek{white} (Tek) | {bold}{gray}Leave |{end}")
        shop = input("> ").strip().lower()
        
        if shop in ['s', 'shuda', 'w', 'weapons']: # weapons shop
            while True:
                clear()
                print(f'{bold}{copper}Shuda Kofgeda{end}\n') ### ADD weapons shop
                print(f"{gold}Your Gold Pieces: {player.gp}{end}\n")
                # printing list of weapons
                print(f"{bold}Item\t\t\tPrice{end}\n")
                count = 1
                for w in weapons_for_sale:
                    if len(w.name) <= 12: print(f'{count}. {w.name.title()}\t\t{gold}[{w.price} gp]{end}')
                    else: print(f'{count}. {w.name.title()}\t{gold}[{w.price} gp]{end}')
                    count += 1

                print(f"\n[{bold}{cyan}l{end}] to leave shop")
                w_choice = input("\n> ").strip().lower()
                if not w_choice.isdigit(): # making sure it is a number answer
                    if w_choice in ['l', 'leave', 'e', 'exit', 'x',]:
                        break
                    else:
                        print(f"{red}Invalid input.{end}\nPlease enter the number corresponding\nto the item you want to select.")
                        enter()
                        continue
                
                elif w_choice.isdigit() and int(w_choice) <= len(weapons_for_sale): # if it's a number on the list
                    weapon_index = int(w_choice) - 1 # getting index of item in list
                    weapon_choice = weapons_for_sale[weapon_index] # assigning weapon they chose into value
                    print(f"{weapon_choice.name.title()}\nBuy | Read Desc | Exit")
                    answer = input("\n> ").strip().lower()
                    if answer in ['b', 'buy']:
                        if player.gp >= weapon_choice.price:
                            player.add_to_inv(weapon_choice, 1) # add item to player inventory
                            print(f'{green}>>{weapon_choice.name.title()} added to inventory<<{end}')
                            player.gp -= weapon_choice.price # take money out of account
                            enter()
                            continue
                        else: # if not enough money in account
                            print('You cannot afford this item right now.')
                            enter()
                            continue
                    elif answer in ['r', 'read', 'read desc', 'read description', 'desc']:
                        print(weapon_choice.desc)
                        enter()
                    elif answer in ['e', 'exit', 'x']:
                        continue
                    else: ### doesn't seem to actually handle None answer
                        print("Invalid command. Valid comands: ['b', 'buy'\n'r', 'read', 'read desc', 'read description', 'desc'\n'e', 'exit', 'x']")
                        enter()
                        continue
                else: # if choose a number that is not on list
                    print('Please choose a valid number.')
                    enter()
                    continue
        
        elif shop in ['p', 'potions']:
            while True:
                clear()
                print(f'{bold}{purple}Potions Kofgeda{end}\n')
                print(f"{gold}Your Gold Pieces: {player.gp}{end}\n")
                print(f"{bold}Item\t\t\tPrice{end}\n")
                count = 1
                for p in potions_all:
                    if len(p.name) <= 12: print(f'{count}. {p.name.title()}\t\t{gold}[{p.price} gp]{end}')
                    else: print(f'{count}. {p.name.title()}\t{gold}[{p.price} gp]{end}')
                    count += 1

                print(f"\n[{bold}{cyan}l{end}] to leave shop")
                p_choice = input("\n> ").strip().lower()
                if not p_choice.isdigit():
                    if p_choice in ['l', 'leave', 'e', 'exit', 'x',]: break
                    else:
                        print(f"{red}Invalid input.{end}\nPlease enter the number corresponding\nto the item you want to select.")
                        enter()
                        continue
                
                elif p_choice.isdigit() and int(p_choice) <= len(potions_all):
                    potion_index = int(p_choice) - 1
                    potion_choice = potions_all[potion_index]
                    print(f"{potion_choice.name.title()}\nBuy | Read Desc | Exit")
                    answer = input("\n> ").strip().lower()
                    if answer in ['b', 'buy']:
                        if player.gp >= potion_choice.price:
                            player.add_to_inv(potion_choice, 1)
                            print(f'{green}>>{potion_choice.name.title()} added to inventory<<{end}')
                            player.gp -= potion_choice.price
                            enter()
                            continue
                        else: 
                            print('You cannot afford this item.') 
                            continue
                    elif answer in ['r', 'read', 'read desc', 'read description', 'desc']:
                        print(potion_choice.desc)
                        enter()
                    elif answer in ['e', 'exit', 'x', 'l', 'leave']: continue
                    else: 
                        print("Invalid command. Valid comands: ['b', 'buy'\n'r', 'read', 'read desc', 'read description', 'desc'\n'e', 'exit', 'x', 'l', 'leave']")
                        enter()
                        continue
                else: 
                    print('Please choose a valid number.')
                    enter()
                    continue

        elif shop in ['t', 'tek', 'Tek', 'Teknology']:
            while True:
                clear()
                print(f'{bold}{blue}Tek Kofgeda{end}\n') ### ADD Tek shop
                print(f"{gold}Your Gold Pieces: {player.gp}{end}\n")
                print(f"{bold}Item\t\t\tPrice{end}\n")
                count = 1
                for tek in tek_for_sale:
                    if len(tek.name) <= 12: print(f'{count}. {tek.name.title()}\t\t{gold}[{tek.price} gp]{end}')
                    else: print(f'{count}. {tek.name.title()}\t{gold}[{tek.price} gp]{end}')
                    count += 1

                print(f"\n[{bold}{cyan}l{end}] to leave shop")
                tek_choice = input("\n> ").strip().lower()
                if not tek_choice.isdigit():
                    if tek_choice in ['l', 'leave', 'e', 'exit', 'x',]: break
                    else:
                        print(f"{red}Invalid input.{end}\nPlease enter the number corresponding\nto the item you want to select.")
                        enter()
                        continue
                
                elif tek_choice.isdigit() and int(tek_choice) <= len(tek_for_sale):
                    tek_index = int(tek_choice) - 1
                    tek_choice = tek_for_sale[tek_index]
                    print(f"{tek_choice.name.title()}\nBuy | Read Desc | Exit")
                    answer = input("\n> ").strip().lower()
                    if answer in ['b', 'buy']:
                        if player.gp >= tek_choice.price:
                            player.add_to_inv(tek_choice, 1)
                            print(f'{green}>>{tek_choice.name.title()} added to inventory<<{end}')
                            player.gp -= tek_choice.price
                            enter()
                            continue
                        else: 
                            print('You cannot afford this item.') 
                            enter()
                            continue
                    elif answer in ['r', 'read', 'read desc', 'read description', 'desc']:
                        print(tek_choice.desc)
                        enter()
                    elif answer in ['e', 'exit', 'x', 'l', 'leave']: continue
                    else: 
                        print("Invalid command. Valid comands: ['b', 'buy'\n'r', 'read', 'read desc', 'read description', 'desc'\n'e', 'exit', 'x', 'l', 'leave']")
                        enter()
                        continue
                else: 
                    print('Please choose a valid number.')
                    enter()
                    continue
                
        elif shop in ['l', 'leave', 'x', 'e', 'exit']:
            save_game(player, 'load.json') # save when you leave marketplace so saves any purchases made
            in_Marketplace = False
        else:
            print(f"{bold}{red}Invalid{white} command.\n\n{green}Valid{white} commands:\n{end}['s', 'shuda', 'w', 'weapons'\n'p', 'potions'\n't', 'tek', 'Tek', 'Teknology'\n'l', 'leave', 'x', 'e', 'exit'")
            enter()
            continue
def go_to_Deadzone(): ###
    pass
def go_to_Tondc(): ###
    pass
def go_to_ShallowValley(): ###
    pass

## RUN GAME ##
def main():
    mainMenu = True # default boolean
    while run:
        while mainMenu: # in main menu
            clear()
            draw()
            print("1. New Game\n2. Load Game\n3. Quit game") # menu options
            draw()
            choice = input("> ").strip().lower() # choice
            if choice in ['1', 'n', 'new', 'new game']: # new game
                intro() # calling introduction scene
                player = choose_crime() # choose crime and return player object based on their choice
                
                if player is not None: 
                    print(f"\n{bold}>> {player.name} created <<{end}") # successfully created player
                    enter()
                    mainMenu = False # leave mainMenu loop
                    play = True # switch to play loop
                else:
                    print("Invalid character selection. Please try again.")
                    enter()
                    mainMenu = True
            
                go_to_Earth(player) # calling go to Earth sequence

            elif choice in ['2', 'l', 'load', 'load game']: # load game
                player = Player.load_game('load.json') # assign loaded player
                if player is not None:
                    player = player
                    print(f"Welcome back, {player.name}")
                    enter()
                    mainMenu = False # leave mainManu, switch to play loop
                    play = True
                else:
                    print("Corrupt save file or no file found!")
                    enter()
                    mainMenu = True
                    play = False

            elif choice in ['3', 'q', 'quit', 'quit game', 'x']: # quit game
                quit = input("\nAre you sure you want to quit the game (y/n)?\n> ").strip().lower()
                if quit == "y":
                    clear()
                    print("Goodbye!")
                    exit()

            else: # if enter wrong thing
                print(f"{bold}{red}Invalid{white} command.\n{green}Valid{white} commands:{end}\n['1', 'n', 'new', 'new game'\n'2', 'l', 'load', 'load game'\n'3', 'q', 'quit', 'quit game', 'x']")
                enter()
                continue


        while play:
            save_game(player, 'load.json') # autosave at beginning of play loop
            game_plan(player)
            go_to_Polis()

if __name__ == "__main__":
    main()

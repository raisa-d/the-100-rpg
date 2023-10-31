import time as t
from util import clear, enter, bold, red, white, green, orange, end, draw, gold, orange, cyan, yellow, turquoise, blue, purple, lime, copper
from items import multipurpose_knife, throwing_knives, shiv, dagger, wrench, health_potion, parachute, rapier
from minigames import code_decryption_minigame
from cutscenes import get_to_dropship, launching_dropship, see_Earth, talk_to_Nyx
from skill_checks import intelligence_check, const_saving_throw, wisdom_check, charisma_check, skill_check
from characters import print_inventory, Player, save_game, NPC, print_stats
from battle import Battle

# list to keep track of which qualities player has earned as a result of decision-making
# how people will react to them in the future will depend on what qualities are in this list
character_qualities = []

def taken_to_dropship(user):
    while True: 
        clear()
        print('Guards suddenly rush into your cell and bark at you, "Let\'s go!"\nThey take you by your arm and drag you down the Ark corridors.')
        print('\nYou look around and see that the other prisoners are being\nherded in the same direction, looking terrified.\n')
        print('Do you...\na) try to ask the guard where they are taking you\nb) stay quiet')
        speak_up = input("\n> ").strip().lower()
        if speak_up == "a": # if ask where they're taking you
            print(f'{bold}The guard shoots you a menacing expression and grunts at you.')
            t.sleep(1)
            if user.crime_num == 0: # if crime was stealing vital stuff -- people don't trust you
                print(f'\nYou make eye contact with the prisoner to your left and try to\nnonverbally communicate "What the **** is going on?"\n\nThe prisoner gives you some side-eye.{end}')
                enter()
                break
            elif user.crime_num == 1: # if crime: leading a rebellion
                print(f'\nYou exchange a glance with another prisoner, who mouths to you\nin a panic: "They\'re sending us...down.{end}"') ### this NPC was arrested for treason? define who these prisoners are
                enter()
                break
            elif user.crime_num == 2: # if crime: cannabis thievery
                print(f'\nYou realize you\'re still a little bit baked from smoking\nthe last of the stash you had hidden in the air ducts in your cell.\n\nYou begin to realize you have no clue what\'s going on.{end}') ### 
                enter()
                break
            elif user.crime_num == 3: # if crime: 2nd child
                print(f'\nAnother prisoner tries to get your attention\nand has a panicked look on their face.{end}') ###
                enter()
                break
            elif user.crime_num == 4: # if crime: falsely accused
                print(f'\nYou look to your right and see a prisoner nearby\nstruggling to get out of a guard\'s grasp{end}')
                enter()
                break
        elif speak_up == "b": # if you don't
            print(f'The prisoner next to you is yelling "Where are you taking us?!" at one of the Guard members,\nwho maintains a cold and aggressive expression.{end}') ### you observe your surroundings and see worried faces, clues as to what could be happening
            enter()
            break
        else:
            print(f"{red}{bold}Invalid command.{green}\nValid commands:\n{white}['a', 'b']{end}")
            enter()
            clear()
            continue

# dropship malfunction
def dropship_malfunction(user): 
    clear()
    print(f"\n{bold}Suddenly, the descent turns into a {red}chaotic freefall.{white} The dropship\nshakes aggressively and you all try to grip anything stable. The\nengine becomes very loud, intesifying the feeling of {orange}imminent\ndanger{white} and helplessness.{end}")
    t.sleep(1)
    while True:
        print("\nDo you...\na) attempt to fix the issue or\nb) brace for impact?")
        fix_or_brace = input("> ").strip().lower()

        if fix_or_brace in ['a', 'fix', 'fix the issue', 'f']:
            clear()
            
            # investigation skill check
            print(f"\n{user.name} will use an investigation skill check to assess the malfunction")
            passed = skill_check(user, 8, "int", narration=True)
            # passed = intelligence_check(user, 8) ###TESTING 
            if passed:
                print("\nYou have successfully identified a damaged component in the dropship's propulsion system.")
                enter()
            else:
                print("\nYou were unsuccessful and did not figure out the source of the malfunction.\n")
                brace_for_impact(user)
                enter()
                break
        
            while passed: # if you pass ability check/successfully assess damage, move onto code decryption minigame to fix it
                fixed = code_decryption_minigame()
                if fixed is True: #if fixed system
                    print(f"{bold}{green}You successfully fixed the propulsion system!\n{end}")
                    enter()
                    clear()
                    safe_landing(user)
                    return True
                else: # if did not fix system
                    print(f"\n{red}{bold}You were unsuccessful at repairing the propulsion system.\nThe alarm blares.\nYou brace for impact.{end}") ### add that they become exhausted from having tried
                    enter()
                    brace_for_impact(user)
                    return False
        
        elif fix_or_brace in ['b', 'brace', 'brace for impact']:
            brace_for_impact(user)
            break
        else:
            print(f"{bold}{red}Invalid command.{green}\nValid commands:\n['a', 'fix', 'fix the issue', 'f',\n'b', 'brace', 'brace for impact']{end}")
            enter()
            clear()
            continue

def safe_landing(user): ### what happens if you fix dropship and have safe landing 
    # --> spaceship steadies, safe landing, respect & trust, access to salvage, exhaustino
    print("Thanks to you, the dropship stabilizes, and you land safely on the ground\nwith minimal turbulence.")
    t.sleep(1)
    print(f"\nOther survivors recognize your skills and will be more\nlikely to respect you and want to be your ally.\n\nAs a reward for successfully fixing the dropship malfunction,\nyou have received\n{bold}{green}+ 1 healing potion.{end}")
    user.exhaustion_level += 2
    user.apply_exhaustion_penalty()
    character_qualities.append("respect and trust") # add quality to list
    user.add_to_inv(health_potion, 1)
    enter()
    return character_qualities

def brace_for_impact(user): # what happens when you brace for impact --> crash landing, saving throw, result (consequences/rewards)
    clear()
    print("You grip your seat tightly as the dropship crashes with intense turbulence,\ncausing chaos & disorientation. When it hits the ground, you exhale with relief.")
    print("\nYou unbuckle your seatbelt and try to get up, but you're feeling dizzy.\nA fellow criminal named Lily comes up to you and asks if you're okay and\nhelps you stand up.\n")
    print("You must make a saving throw to assess how bad your injuries are.")
    enter()
    
    # rolling dice for saving throw 
    clear()
    s = f"{bold}{orange}Saving Throw{end}"
    print(f"{s:^105}")
    success = const_saving_throw(user, 14)
    enter()
    clear()
    if success: # if succeeded at saving throw
        print("\nYou are one of the lucky ones and made it to the ground\nwith no injuries, only a light migraine.")
    else: # if did not succeed
        print(f"\nYou have bruising and minor lacerations from the crash landing, but you made it to the ground!")
        user.HP -= 3
        print(f"\nYou lost 3 HP. You now have {user.HP}/{user.maxHP} HP 🩸")
    user.exhaustion_level += 1
    user.apply_exhaustion_penalty()
    print("\nThe shared survival experience strengthens your bonds\nwith the other survivors.")
    character_qualities.append("shared survival experience") # reward, people will respond better to you
    return character_qualities

def go_to_Earth(user): 
    taken_to_dropship(user) # prisoners being taken to dropship
    get_to_dropship()
    launching_dropship() # launching dropship from the Ark
    dropship_malfunction(user) # dropship malfunction and landing on Earth
    see_Earth() # see earth for the first time

def explore_woods(): ### CODE & WRITE THIS
    print("\n[Placeholder: You explore the woods.]\nTaking you to Polis...") 
    enter()

def fight_dante(user, target):
    battle_dante = Battle(user, target)
    result = battle_dante.start_battle()
            
    if result: # if you defeat the target
        enter()
        clear()
        print(f"You won the fight against {battle_dante.target.name} and he bites his tongue!")
        print(f"\n{bold}+ {copper}{battle_dante.target.drop_item.name}{white}\n+ {gold}{battle_dante.target.drop_GP} gp{white}\n+ {green}3 HP 🩸{end}")
        battle_dante.user.add_to_inv(battle_dante.target.drop_item, 1)
        battle_dante.user.gp += battle_dante.target.drop_GP
        battle_dante.user.xp += 30
        battle_dante.user.HP += 3
        target.HP = target.maxHP # setting Dante's HP back to full
        enter()
    else: # if target defeats you
        print('\nYou narrowly escape with your life, thanks to Dante\'s mercy.')
        user.exhaustion_level += 1 # become exhausted from the fight
        target.HP = target.maxHP 
        user.HP = 1
        enter()
                

def talk_to_prisoners(user, target): 
    clear()
    print("You walk up to a group gathered around talking about making the trek to Mount Weather.\nAt the center of it is Jules, charting a course.")
    who = input(f"Next to her is Dante. From what you know, he's rude but tough. Who do you want to talk to?\n\n{bold}{turquoise}| Jules {lime}| Dante |{end}\n> ").strip().lower()
    if who[0] == "j": # talk to Jules
        want_to_go = input('She asks you, "Do you want to come with me to search for Mount Weather?"').strip().lower()
        if want_to_go[0] == "y": # if yes
            pass ### CODE/WRITE THIS
        else: # if no
            pass ### CODE/WRITE THIS
    else: # talk to Dante
        clear()
        print('He looks you up and down and asks, "What the hell are you looking at?"')
        dante = input(f"\n{bold}{yellow}| Fight Dante {green}| Say \"You.\" |{end}\n> ").strip().lower()
        if dante[0] == "f": # fight
            fight_dante(user, target)
        else: # say "you"
            charismatic = skill_check(user, 17, "char", narration=False)
            #charismatic = charisma_check(user, 18) ###TESTING
            if charismatic: # scenario that happens if you pass charisma check
                pass ###
            else: # what happens if you fail charisma check
                print('He seems upset and seems to be getting ready to punch you.')
                enter()
                clear()
                fight_dante(user, target)

def take_a_rest(user):
    while True:
        clear()
        length = input(f"{bold}{green}| Short Rest {turquoise}| Long Rest |{end}\n> ").strip().lower()
        if length[0] == "s":
            length = "short"
        elif length[0] == "l":
            length = "long"
        else:
            print(f"\n{red}{bold}Please enter either{green} \"short\", \"long\" or the first letter of either command.")
            continue
        
        user.rest(length)
        enter()
        break

def check_dropship(user):
    while True:
        clear()
        print(f"\nYou look around the dropship for materials you can use to make a tent,\nas you'll need a place to sleep tonight.\n\n{bold}Let's do an investigation check\nto see what {user.name} notices.{end}")
        passed = skill_check(user, 6, "int", narration=True)
        # passed = intelligence_check(user, 6) ###TESTING
        enter()
        if passed:
            clear()
            print("You notice some parachutes you can use to build a tent.")
            
            # ask if the user wants to collect the parachute
            input(f"\n[{cyan}Enter{end}] to take parachute\n")
            user.add_to_inv(parachute, 1)
            print(f"{green}>> parachute added to inventory <<{end}")
            t.sleep(0.5)
            
            # player tries to build tent
            clear()
            passed_survival_check = skill_check(user, 9, "wis", narration=False)
            # passed_survival_check = wisdom_check(user, 9)###TESTING
            if passed_survival_check:
                user.remove_from_inv(parachute, 1)
                input("[Enter] to build tent\n")
                print(f"\n{bold}{green}You successfully built a tent and\nhave a place to sleep tonight!{end}") ### build tent
                enter()
                break
            else: ### what happens if you don't pass
                print(f"{bold}{red}You were unsuccessful and could not build the tent.{end}\n\nCross your fingers and hope you can get a fellow member of the 100\nto build it for you.")
                enter()
                break

        else:
            print("You don't seem to find anything in here.\nYou didn't look hard enough.")
            enter()
            break

def set_up_basecamp(user, target):
    checked_dropship = False # boolean to track whether player already checked dropship
    basecamp_title = f"{bold} \\\ LOCATION: Base Camp //{end}"
    decision = ""
    while True:
        clear()
        print(f"{basecamp_title:^90}\n")
        if checked_dropship == False:
            decision = input(f"{bold}{orange}| Back {yellow}| Talk to Gathered Prisoners {green}| Check Dropship For Materials {blue}| Rest |{end}\n> ")
        else:
            decision = input(f"{bold}{orange}| Back {yellow}| Talk to Gathered Prisoners {green}| Rest |{end}\n> ")
        if decision != "": # handling for empty string
            if decision[0] == "b":
                break
            elif decision[0] in ["d", "c"]: # check dropship
                if checked_dropship == False: # only if you haven't already checked it can you do this
                    check_dropship(user)
                checked_dropship = True
            elif decision[0] == "t": # talk to gathered prisoners
                # HP, maxHP, AC, str_mod, dex_mod, drop_item, drop_GP, equipped_weapon = None
                talk_to_prisoners(user, target)
            elif decision[0] == "r": # take a rest
                take_a_rest(user)
            elif decision[0] == "e": # explore woods
                explore_woods()
            else:
                print(f"{red}{bold}Invalid command.\n{green}Valid commands:{white}\nThe first letter of each option")
                enter()
                continue
        else:
            print(f"{red}{bold}Invalid command.\n{green}Valid commands:{white}\nThe first letter of each option")
            enter()
            continue
            

base_camp_is_setup = False # variable to track whether they moved on from this section. ### will probably need to add this to be saved so can return in same spot you left off
def game_plan(user, target): # making game plan and executing
    if base_camp_is_setup: # if already set up base camp
        pass
    else: ### code the setting up base camp scenario, having choice between exploring and setting up camp
        user_location = f"{bold}\\\ LOCATION: Dropship //{end}" # page title
        choice = "" # setting choice equal to an empty string
        while True:
            clear()
            print(f"{user_location:^90}\n")
            print(f"What would you like to do?{end}")
            print(f"\n{bold}{red}| Exit {orange}| Save {yellow}|  Inventory {green}| Stats |\n\n{blue}| Talk to Nyx {turquoise}| Explore Surrounding Area {purple}| Base Camp |{end}")
            choice = input("\n> ").strip().lower()
            
            if choice != "":
                if choice[0] == "x": # exit
                    save_game(user, 'load.json')
                    print("Goodbye!")
                    quit()
                
                elif choice in ["save", "s"]: # save
                    save_game(user, 'load.json')
                
                elif choice[0] == "i": # inventory
                    print_inventory(user)
                
                elif choice in ["stats", "stat"]:
                    print_stats(user)
                
                elif choice[0] in ["t", "n"]: # if choose talk to nyx, the person who suggested they explore
                    talk_to_Nyx(user)
                
                elif choice[0] in ["e"]: # if choose explore
                    explore_woods()
                    break
                
                elif choice[0] == "b": # if choose set up base camp
                    set_up_basecamp(user, target)
                
                else:
                    print(f"{red}{bold}Invalid command.\n{green}Valid commands:\n{white}'x'\n'save', 's'\nany word that starts with 'i'\n'stats', 'stat'\n't', 'n'\nanything that starts with 'e'\nanything that starts with 'b'")
                    enter()
                    continue
            else:
                print(f"{red}{bold}Invalid command.\n{green}Valid commands:\n{white}'x'\n'save', 's'\nany word that starts with 'i'\n'stats', 'stat'\n't', 'n'\nanything that starts with 'e'\nanything that starts with 'b'")
                enter()
                continue
        

    # after sequence is completed and the base camp is successfully set up, do
    # --> setting_up_camp.append['completed']. save setting_up_camp to save file. maybe have to add setting_up_camp to player?
    # --> and only run this if completed is NOT in setting_up_camp

# Changes to events.py since last github update:
'''
1. 
'''

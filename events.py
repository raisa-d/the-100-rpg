import time as t
from formatting import clear, enter, draw, diceRoll
from items import multipurpose_knife, throwing_knives, shiv, dagger, wrench
from minigames import code_decryption_minigame

bold = "\033[1m"
red = "\033[31m"
white = "\033[37m"
green = "\033[32m"
orange = '\x1b[38;2;255;90;0m\x1b[1m'
end = "\033[0m" # end any formatting

def taken_to_dropship(player):
    while True: 
        clear()
        print('Guards suddenly rush into your cell and bark at you, "Let\'s go!"\nThey take you by your arm and drag you down the Ark corridors.')
        print('\nYou look around and see that the other prisoners are being\nherded in the same direction, looking terrified.\n')
        print('Do you...\na) try to ask the guard where they are taking you\nb) stay quiet')
        speak_up = input("\n> ").strip().lower()
        if speak_up == "a": # if ask where they're taking you
            print(f'{bold}The guard shoots you a menacing expression and grunts at you.')
            t.sleep(1)
            if multipurpose_knife in player.inv: # if crime was stealing vital stuff -- people don't trust you
                print(f'\nYou make eye contact with the prisoner to your left and try to\nnonverbally communicate "What the **** is going on?"\n\nThe prisoner gives you some side-eye.{end}')
                enter()
                break
            elif throwing_knives in player.inv: # if crime: leading a rebellion
                print(f'\nYou exchange a glance with another prisoner, who mouths to you\nin a panic: "They\'re sending us...down.{end}"') ### this NPC was arrested for treason? define who these prisoners are
                enter()
                break
            elif shiv in player.inv: # if crime: cannabis thievery
                print(f'\nYou realize you\'re still a little bit baked from smoking\nthe last of the stash you had hidden in the air ducts in your cell.\n\nYou begin to realize you have no clue what\'s going on.{end}') ### 
                enter()
                break
            elif dagger in player.inv: # if crime: 2nd child
                print(f'\nAnother prisoner tries to get your attention\nand has a panicked look on their face.{end}') ###
                enter()
                break
            elif wrench in player.inv: # if crime: falsely accused
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
def dropship_malfunction(player): 
    print(f"\n{bold}Suddenly, the descent turns into a {red}chaotic freefall.{white} The dropship\nshakes aggressively and you all try to grip anything stable. The\nengine becomes very loud, intesifying the feeling of {orange}imminent\ndanger{white} and helplessness.{end}")
    t.sleep(1)
    while True:
        print("\nDo you...\na) attempt to fix the issue or\nb) brace for impact?")
        fix_or_brace = input("> ").strip().lower()
        dmg_identified = False
        if fix_or_brace in ['a', 'fix', 'fix the issue', 'f']:
            clear()
            
            # assess malfunction
            if "portable device" in player.inv:
                print("\nYou use your device and successfully identify a damaged component in the dropship\'s propulsion system")
                enter()
                dmg_identified = True
            else: # investigation skill check
                print(f"\n{player.name} will use an investigation skill check to assess the malfunction")
                t.sleep(1)
                print("\nRolling d20 and adding your intelligence modifier...")
                t.sleep(1)
                inv_check = diceRoll(20) + player.int_mod
                print(f"\nYou got {inv_check}")
                t.sleep(1)
                if inv_check > 8: # chose 6 as difficulty class for this task, don't want it to be unattainable but not too easy either
                    print("\nYou have successfully identified a damaged component in the dropship's propulsion system.")
                    dmg_identified = True
                    enter()
                else:
                    print("\nYou were unsuccessful and did not figure out the source of the malfunction.\n--> CONSEQUENCES") ### code consequences of failing to do this
                    dmg_identified = False
                    enter()
                    break
        
            while dmg_identified is True: # if you successfully assess damage, move onto code decryption minigame to fix it
                fixed = code_decryption_minigame()
                if fixed is True: #if they were successful
                    print("You successfully fixed the propulsion system!\n--> REWARDS") ### code rewards, what happens (spaceship steadies, safe landing, etc.)
                    enter()
                    return True
                else:
                    print("\nYou were unsuccessful at repairing the propulsion system and brace for impact.\n--> CONSEQUENCES")
                    enter()
                    return False
        
        elif fix_or_brace in ['b', 'brace', 'brace for impact']:
            print('WRITE WHAT HAPPENS IF YOU BRACE') ###
            enter()
            break
        else:
            print(f"{bold}{red}Invalid command.{green}\nValid commands:\n['a', 'fix', 'fix the issue', 'f',\n'b', 'brace', 'brace for impact']{end}")
            enter()
            clear()
            continue
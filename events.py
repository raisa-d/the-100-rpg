import time as t
from util import clear, enter, bold, red, white, green, orange, end, draw
from items import multipurpose_knife, throwing_knives, shiv, dagger, wrench, health_potion
from minigames import code_decryption_minigame
from cutscenes import get_to_dropship, launching_dropship
from skill_checks import intelligence_check, const_saving_throw

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
            if multipurpose_knife in user.inv: # if crime was stealing vital stuff -- people don't trust you
                print(f'\nYou make eye contact with the prisoner to your left and try to\nnonverbally communicate "What the **** is going on?"\n\nThe prisoner gives you some side-eye.{end}')
                enter()
                break
            elif throwing_knives in user.inv: # if crime: leading a rebellion
                print(f'\nYou exchange a glance with another prisoner, who mouths to you\nin a panic: "They\'re sending us...down.{end}"') ### this NPC was arrested for treason? define who these prisoners are
                enter()
                break
            elif shiv in user.inv: # if crime: cannabis thievery
                print(f'\nYou realize you\'re still a little bit baked from smoking\nthe last of the stash you had hidden in the air ducts in your cell.\n\nYou begin to realize you have no clue what\'s going on.{end}') ### 
                enter()
                break
            elif dagger in user.inv: # if crime: 2nd child
                print(f'\nAnother prisoner tries to get your attention\nand has a panicked look on their face.{end}') ###
                enter()
                break
            elif wrench in user.inv: # if crime: falsely accused
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
    print(f"\n{bold}Suddenly, the descent turns into a {red}chaotic freefall.{white} The dropship\nshakes aggressively and you all try to grip anything stable. The\nengine becomes very loud, intesifying the feeling of {orange}imminent\ndanger{white} and helplessness.{end}")
    t.sleep(1)
    while True:
        print("\nDo you...\na) attempt to fix the issue or\nb) brace for impact?")
        fix_or_brace = input("> ").strip().lower()

        if fix_or_brace in ['a', 'fix', 'fix the issue', 'f']:
            clear()
            
            # investigation skill check
            print(f"\n{user.name} will use an investigation skill check to assess the malfunction")
            passed = intelligence_check(user, 8) # will return True or False about whether passed the skill check or not
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
                    print("You successfully fixed the propulsion system!\n")
                    enter()
                    clear()
                    safe_landing(user)
                    return True
                else: # if did not fix system
                    print("\nYou were unsuccessful at repairing the propulsion system and brace for impact.") ### add that they become exhausted from having tried
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
    print(f"\nOther survivors recognize your skills and will be more\nlikely to respect you and want to be your ally.\n\nAs a reward for successfully fixing the dropship malfunction,\nyou have received\n{bold}{green}+ two healing potions.{end}")
    character_qualities.append("respect and trust") # add quality to list
    user.add_to_inv(health_potion, 2)
    enter()
    return character_qualities

def brace_for_impact(user): # what happens when you brace for impact --> crash landing, saving throw, result (consequences/rewards)
    clear()
    print("You grip your seat tightly as the dropship crashes with intense turbulence,\ncausing chaos & disorientation. When it hits the ground, you exhale with relief.")
    t.sleep(1)
    print("\nYou unbuckle your seatbelt and try to get up, but you're feeling dizzy.\n")
    draw()
    print("\nYou must make a saving throw to assess how bad your injuries are.")
    t.sleep(1)
    success = const_saving_throw(user, 14)
    enter()
    clear()
    if success: # if succeeded at saving throw
        print("\nYou are one of the lucky ones and made it to the ground\nwith no injuries, only a light migraine.")
        enter()
    else: # if did not succeed
        print(f"\nYou have bruising and minor lacerations from the crash landing,\nwhich may take a while to heal from unless you find medical supplies.")
        user.HP -= 4
        print(f"\nYou lost 4 HP. You now have {user.HP}/{user.maxHP} HP 🩸")
        character_qualities.append("minor injuries") # consequence
        enter()
    print("\nThe shared survival experience strengthens your bonds\nwith the other survivors.")
    character_qualities.append("shared survival experience") # reward, people will respond better to you
    return character_qualities

def go_to_Earth(user): 
    taken_to_dropship(user)
    get_to_dropship()
    launching_dropship()
    dropship_malfunction(user)

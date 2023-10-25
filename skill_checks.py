import time as t
from util import diceRoll, enter, bold, end, green, red

def roll_with_disadvantage(): # handles disadvantaged rolls incurred from exhaustion
    roll1 = diceRoll(20)
    roll2 = diceRoll(20)
    final_roll = min(roll1, roll2)
    return final_roll

def roll_d20():
    roll = diceRoll(20)
    return roll

def roll_d20_with_narration():
    roll = diceRoll(20)
    print("\nRolling d20...")
    t.sleep(0.5)
    print(f"\nYou rolled {roll}.\n")
    t.sleep(0.5)
    return roll

def disadvantage_with_narration():
    print("\nDue to exhaustion, you have a disadvantage and will use the lower of two dice rolls.")
    print("\nRolling first d20...")
    t.sleep(0.5)
    roll1 = diceRoll(20)
    print(f"\nYou rolled a {roll1}")
    print("\nRolling second d20...")
    t.sleep(0.5)
    roll2 = diceRoll(20)
    print(f"\nYou rolled a {roll2}")
    t.sleep(0.5)
    final_roll = min(roll1, roll2) # use the lower of the two rolls
    print(f"{bold}\nYou got {final_roll}.{end}\n")
    return final_roll

# intelligence skill check --> investigation, history, arcana, nature, religion
def intelligence_check(user, difficulty_class): # pass in player and difficulty class of what you're trying to do
    if user.exhaustion_level == 1: # if exhaustion level 1, roll with disadvantage
        roll = disadvantage_with_narration()
    else: # if not exhaustion lvl 1, no disadvantage to ability check rolls
        roll = roll_d20_with_narration()
    print("Adding your intelligence modifier...")
    t.sleep(1)
    int_check = roll + user.int_mod
    print(f"\n{bold}You got {int_check}.{end}")
    
    if int_check > difficulty_class:
        print(f"\n{bold}{green}You passed the skill check!{end}")
        #enter()
        return True
    else:
        print(f"\n{red}{bold}You did not pass the skill check.{end}")
        enter()
        return False

# wisdom check --> animal handling, insight, medicine, perception, survival
def wisdom_check(user, DC):
    pass

# charisma check --> deception, intimidation, performance, persuasion
def charisma_check(user, DC):
    pass

# strength skill check --> athletics
def strength_check(user, DC):
    pass

# dexterity skill check --> acrobatics, sleight of hand, stealth
def dex_check(user, DC):
    pass

# constitution saving throw
def const_saving_throw(user, DC):
    if user.exhaustion_level == 2: # if exhaustion level 2, disadvantage on saving throws
        roll = disadvantage_with_narration()
    else:
        roll = roll_d20_with_narration()
    t.sleep(1)
    if user.crime_num == 3: # second child has constitution proficiency and therefore adds proficiency bonus and constitution modifier
        print("Adding your constitution modifier and proficiency bonus...")
        const_check = roll + user.const_mod + user.prof_bonus
    else:
        print("Adding your constitution modifier...")
        const_check = roll + user.const_mod
    print(f"\n{bold}You got {const_check}.{end}")

    if const_check > DC: 
        print(f"\n{bold}{green}Your saving throw was successful!{end}") # successful usually means little to no injuries
        return True
    else:
        print(f"\n{red}{bold}Your saving throw was unsuccessful.{end}")
        return False

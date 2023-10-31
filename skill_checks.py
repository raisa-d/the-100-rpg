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

def disadvantage_with_narration():
    print("\nDue to exhaustion, you have a disadvantage.")
    roll1 = diceRoll(20)
    roll2 = diceRoll(20)
    final_roll = min(roll1, roll2) # use the lower of the two rolls
    return final_roll

def skill_check(user, DC, skill_name, narration=None): # skill_name will be the shortened version (i.e., "str", "dex", "int", "char", "wis"). narration is boolean for whether it should be narrated or not
        
        # if exhaustion level 1, roll with disadvantage
        if user.exhaustion_level == 1:
            if narration == True:
                roll = disadvantage_with_narration()
            else:
                roll = roll_with_disadvantage()
        
        # if not exhaustion lvl 1, no disadvantage to ability check rolls
        else:
            if narration == True:
                roll = roll_d20()
            else:
                roll = roll_d20()
        
        # adding ability modifier to roll
        if skill_name == "str":
            skill_check = roll + user.str_mod
        elif skill_name == "dex":
            skill_check = roll + user.dex_mod
        elif skill_name == "int":
            skill_check = roll + user.int_mod
        elif skill_name == "wis":
            skill_check = roll + user.wis_mod
        elif skill_name == "char":
            skill_check = roll + user.char_mod

        if skill_check > DC: # pass skill check
            return True
        else: # fail skill check
            return False

# constitution saving throw
def const_saving_throw(user, DC):
    if user.exhaustion_level == 2: # if exhaustion level 2, disadvantage on saving throws
        roll = disadvantage_with_narration()
    else:
        roll = roll_d20()
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

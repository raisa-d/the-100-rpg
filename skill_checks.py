import time as t
from util import diceRoll, enter, bold, end, green, red

def roll_d20():
    roll = diceRoll(20)
    print("\nRolling d20...")
    t.sleep(1)
    print(f"\nYou rolled {roll}.")
    t.sleep(1)
    return roll

# intelligence skill check --> investigation, history, arcana, nature, religion
def intelligence_check(user, difficulty_class): # pass in player and difficulty class of what you're trying to do
    roll = roll_d20()
    print("\nAdding your intelligence modifier...")
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
    roll = roll_d20()
    t.sleep(1)
    if user.crime_num == 3: # second child has constitution proficiency and therefore adds proficiency bonus and constitution modifier
        print("\nAdding your constitution modifier and proficiency bonus...")
        const_check = roll + user.const_mod + user.prof_bonus
    else:
        print("\nAdding your constitution modifier...")
        const_check = roll + user.const_mod
    print(f"\n{bold}You got {const_check}.{end}")

    if const_check > DC: 
        print(f"\n{bold}{green}Your saving throw was successful!{end}") # successful usually means little to no injuries
        return True
    else:
        print(f"\n{red}{bold}Your saving throw was unsuccessful.{end}")
        return False

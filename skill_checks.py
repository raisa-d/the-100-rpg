import time as t
from util import diceRoll, enter, bold, end, green, red

# intelligence skill check --> investigation, history, arcana, nature, religion
def intelligence_check(user, difficulty_class): # pass in player and difficulty class of what you're trying to do
    roll = diceRoll(20)
    print("\nRolling d20...")
    t.sleep(1)
    print(f"\nYou rolled {roll}.")
    t.sleep(1)
    
    print("\nAdding your intelligence modifier...")
    t.sleep(1)
    int_check = roll + user.int_mod
    print(f"\n{bold}You got {int_check}.{end}")
    
    if int_check > difficulty_class: # chose 6 as difficulty class for this task, don't want it to be unattainable but not too easy either
        print(f"\n{bold}{green}You passed the skill check!{end}")
        return True
    else:
        print(f"\n{red}{bold}You did not pass the skill check.{end}") ### code consequences of failing to do this
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

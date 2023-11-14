import time as t, random as r
from util import clear, enter, draw, diceRoll, bold, copper, gold, green, end, red, purple, yellow, lime, orange, turquoise, white, blue
from characters import print_inventory, Player
from skill_checks import roll_with_disadvantage, roll_d20

class Battle:
    def __init__(self, plyr, enemy):
        self.plyr = plyr # plyr refers to player, didn't want to confuse variables by naming this "player"
        self.enemy = enemy
    
    def start_battle(self): # handles battle itself
        round = 1 # tracking round number
        while self.enemy.HP > 0 and self.plyr.HP > 0: # while player & enemy are both alive
            global print_battle_title
            def print_battle_title(user, enemy): # function to bring battle title and both parties' HP
                clear()
                bt = f"{bold}{red}xX  Time to Battle  Xx{end}" # title
                pr = f"{bold}Round {round}{end}"
                print(f"{bt:^90}") # print battle screen
                print(f"{pr:^85}") # print current round number
                print(f"\n{bold}{purple}{user.name.title()}{end}: {user.HP}/{user.maxHP} HP 🩸\n{bold}{yellow}{enemy.name.title()}{end}: {enemy.HP} /{enemy.maxHP} HP 🩸")
            
            while True:
                print_battle_title(self.plyr, self.enemy) # printing screen title
                print("\nAttack | Use Item") # battle options
                attack_or_inv = input("\n> ").strip().lower() # input first move

                if attack_or_inv != "": # if not an empty string
                    if attack_or_inv[0] == "a": # choose attack
                        self.plyr_attack()
                    
                    elif attack_or_inv[0] in ["u", "i"]: # choose use item
                        print_inventory(self.plyr) # passing player into inventory function
                        print_battle_title(self.plyr, self.enemy)
                        print()
                        draw()
                        print("You used an inventory item as your turn.")
                        draw()
                    
                    else: # any other answer
                        print(f"{red}{bold}Invalid command.\n{green}Valid commands:{end}\n['a', 'attack'\n'use item', 'item', 'inv', 'i', 'u']")
                        enter()
                        continue
                else: # if answer with an empty string
                    print(f"{red}{bold}Invalid command.\n{green}Valid commands:{end}\n['a', 'attack'\n'use item', 'item', 'inv', 'i', 'u']")
                    enter()
                    continue

                if self.enemy.HP <= 0: # if enemy is dead
                    return True # player wins
                
                else: # if enemy is not dead, they will attack
                    self.reaction_turn()
                    self.enemy_attack()

                if self.plyr.HP <= 0: # if player dies
                    if self.enemy.name != "dante": # doing this because i want the fight with dante to be like a practice, not deadly
                        print("\nYu gonplei ste odon.\nMay we meet again.")
                        quit()
                    else:
                        return False

                round += 1 # adding onto round
                enter()

    def use_strength(self):
        if self.plyr.exhaustion_level == 2: # if exhaustion lvl 2, disadvantage on attack roll
            draw()
            attack_roll = roll_with_disadvantage() + self.plyr.str_mod
        else:
            draw()
            attack_roll = roll_d20() + self.plyr.str_mod
        return attack_roll

    def use_dex(self):
        if self.plyr.exhaustion_level == 2:
            draw()
            attack_roll = roll_with_disadvantage() + self.plyr.dex_mod
            print(f"{bold}\nYou got {attack_roll}.{end}\n")
        else:
            draw()
            attack_roll = roll_d20() + self.plyr.dex_mod
            print(f"{bold}\nYou got {attack_roll}.{end}\n")
        return attack_roll

    def plyr_attack(self): # player attack 
        str_or_dex = ""
        while True:
            print_battle_title(self.plyr, self.enemy)
            if self.plyr.equipped_weapon is not None: # if have a weapon
                if self.plyr.equipped_weapon.finesse == True: # if finesse weapon, choice of str or dex_mod
                    str_or_dex = input(f"\n{bold}| {turquoise}Strength ({self.plyr.str_mod}){white} | {blue}Dexterity ({self.plyr.dex_mod}){white} |{end}\n\n> ").strip().lower()
                
                if str_or_dex != "": ### CHANGE THIS SO IF YOU HAVE A MELEE OR RANGE WEAPON IT STILL WORKS, AS STR_OR_DEX WILL NOT BE ASSOCIATED WITH A VALUE
                    if str_or_dex in ["s", "strength"]: 
                        attack_roll = self.use_strength()

                    elif str_or_dex in ["d", "dex", "dexterity"]:
                        attack_roll = self.use_dex()
                    else:
                        print(f"{bold}{red}Invalid command.\n{green}Valid commands:\n{white}'strength', 'dexterity', 'dex', or the first letter of each word{end}")
                        enter()
                        continue

                else: # if string is empty or None
                    if self.plyr.equipped_weapon.melee:
                        attack_roll = self.use_strength()
                    elif self.plyr.equipped_weapon.range:
                        attack_roll = self.use_dex()
                
                # attack and damage rolls
                if attack_roll >= self.enemy.AC: # if attack roll successful, on to do damage
                    damage_roll = diceRoll(self.plyr.equipped_weapon.num_of_sides) + self.plyr.str_mod
                    self.enemy.lose_hp(damage_roll)
                    print(f'{bold}{lime}You are adept with your {self.plyr.equipped_weapon.name} and deal the {self.enemy.name} {damage_roll} damage!{end}')
                    draw()
                    break
                else: # if attack roll unsuccessful
                    print(f"{bold}{orange}You miss them and deal no damage.{end}")
                    draw()
                    break

            else: # code for unarmed strikes
                verbs = ["punch", "headbutt", "kick"]
                chosen_verb = r.choice(verbs) # randomly choose whether they punch, headbutt, or kick enemy to make it more intersting
                print()
                draw()
                print(f"{purple}{bold}You prepare to {chosen_verb} the {self.enemy.name}!{end}\n")

                # attack roll
                if self.plyr.crime_num in [1, 3, 4]: # these crimes have a unarmed strike Hit/DC of +5
                    attack_roll = roll_d20() + 5
                
                elif self.plyr.crime_num == 0: # vital supplies has DC of +4
                    attack_roll = roll_d20() + 4
                
                else: # cannabis thief has DC +3
                    attack_roll = roll_d20() + 3

                # damage roll
                if attack_roll >= self.enemy.AC: # if attack roll successful
                    
                    if self.plyr.crime_num == 4: #  for Falsely Accused criminal
                        damage_roll = diceRoll(4) + 3 # 1d4 + 3 damage
                        self.enemy.lose_hp(damage_roll) # subtract damage from enemy's HP
                    
                    else: # other characters' damage is 1 + their strength modifier
                        damage_roll = 1 + self.plyr.str_mod
                        self.enemy.lose_hp(damage_roll) # subtract damage from enemy's HP
                    
                    # print fight method
                    print(f'{bold}{lime}You deal the {self.enemy.name} {damage_roll} damage!{end}')
                    draw()
                    break

                else: # if attack roll unsuccessful
                    print(f"{bold}{orange}You miss them and deal no damage.{end}")
                    draw()
                    break
                

    def reaction_turn(self): # player reaction turn
        enter()
        while True:
            print_battle_title(self.plyr, self.enemy) # printing screen title # clear screen and print updated title screen

            # reaction turn
            print(f"\n{bold}{copper}| Reaction Turn |{end}")
            print(f"\n{bold}{turquoise}| Dodge {green}| Heal Wounds {gold}| Steal Gold |{end}")
            reaction = input("\n> ").strip().lower()
            
            if reaction != "": # if reaction is not an empty string
                if reaction[0] == "d": # if choose dodge
                    self.plyr.toggle_dodge()
                    draw()
                    print("You try to dodge the enemy") ### IMPLEMENT DODGING
                    break

                elif reaction[0] == "h": # if choose heal wounds
                    possible_HP = ["1", "2", "3"]
                    HP_gained = r.choice(possible_HP) # randomly choose how much they heal
                    # add HP to player
                    self.plyr.gain_health(int(HP_gained))
                    draw()
                    print(f"\n{green}{bold}You gained back {HP_gained} HP 🩸{end}")
                    break
                
                elif reaction[0] in ["s", "g"]: # if choose steal gold
                    possible_amounts = [1, 2, 3, 4, 5]
                    amt_stolen = r.choice((possible_amounts)) # randomly choose how much GP you steal between 1 and 5
                    self.plyr.gain_gp(int(amt_stolen)) # give player the GP
                    draw()
                    print(f"\n{bold}{gold}You stole {amt_stolen} GP!{end}")
                    break

                else: # if invalid input
                    print(f"{bold}{red}Invalid command.\n{green}Valid commands include:\n{white}'dodge', 'heal', 'steal', 'gold'\nor anything that begins with 'd', 'h', 's', or 'g'{end}")
                    enter()
                    continue
            else: # if reaction is an empty string
                print(f"{bold}{red}Invalid command.\n{green}Valid commands include:\n{white}'dodge', 'heal', 'steal', 'gold'\nor anything that begins with 'd', 'h', 's', or 'g'{end}")
                enter()
                continue

    def enemy_attack(self): # enemy attack
        enemy_str_or_dex = r.choice(("s", "d")) # randomly choose strength or dexterity for enemy
        
        if self.enemy.equipped_weapon.melee == True or enemy_str_or_dex == "s": # strength attack roll
            if self.plyr.is_dodging:
                enemy_attack_roll = roll_with_disadvantage() + self.enemy.str_mod # apply disadvantage if player dodges
            else:
                enemy_attack_roll = diceRoll(20) + self.enemy.str_mod
        elif self.enemy.equipped_weapon.range == True or enemy_str_or_dex == "d": # dexterity attack roll
            if self.plyr.is_dodging:
                enemy_attack_roll = roll_with_disadvantage() + self.enemy.str_mod
            else:
                enemy_attack_roll = diceRoll(20) + self.enemy.dex_mod
            
        if enemy_attack_roll >= self.plyr.AC: # if attack roll successful, on to do damage
            enemy_damage_roll = diceRoll(self.enemy.equipped_weapon.num_of_sides) + self.enemy.str_mod
            self.plyr.lose_health(enemy_damage_roll)
            print(f'\n{bold}{yellow}The {self.enemy.name.title()} dealt you {enemy_damage_roll} damage{end}')
            draw()
        else:
            print(f'\n{bold}{yellow}The {self.enemy.name} missed you and dealt no damage!{end}')
            draw()

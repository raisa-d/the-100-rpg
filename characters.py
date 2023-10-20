import time as t, pickle, random as r
from util import clear, enter, draw, diceRoll, bold, red, end, white, cyan, purple, underline, orange, yellow, green, blue, lime, teal, turquoise, gold, copper
from items import weapons_all, tek_all, Potion, Weapon, Item, Tek, Food, Drink, reaper_stick, dagger, butterfly_sword, rapier, knockout_gas, crossbow

class Character():
    def __init__(self, name, HP, maxHP, AC, str_mod, dex_mod, equipped_weapon=None):
        self.name = name
        self.HP = HP
        self.maxHP = maxHP
        self.AC = AC
        self.str_mod = str_mod
        self.dex_mod = dex_mod
        self.equipped_weapon = equipped_weapon

class Player(Character):
    def __init__(self, name, HP, maxHP, gp, str_ability, str_mod, dex_ability, dex_mod, const_ability, const_mod, int_ability, int_mod, wis_ability, wis_mod, char_ability, char_mod, prof_bonus, xp, AC, equipped_weapon=None, equipped_tek=None, inv=None):
        super().__init__(name, HP, maxHP, AC, str_mod, dex_mod, equipped_weapon)
        self.gp = gp

        # D&D ability scores/modifiers
        self.str_ability = str_ability # strength ability score
        self.dex_ability = dex_ability # dexterity ability score
        self.const_ability = const_ability # constitution
        self.const_mod = const_mod
        self.int_ability = int_ability # intelligence
        self.int_mod = int_mod
        self.wis_ability = wis_ability # wisdom
        self.wis_mod = wis_mod
        self.char_ability = char_ability # charisma
        self.char_mod = char_mod
        self.prof_bonus = prof_bonus # proficiency bonus
        
        self.xp = xp
        self.equipped_tek = equipped_tek
        if inv is None: # doing this so we don't have a mutable list set as the default
            self.inv = {}
        else:
            self.inv = inv

    def add_to_inv(self, item, quantity):
        if item in self.inv: # if already have this item
            self.inv[item] += quantity # add quantity of it to existing quantity
        else: # if new item
            self.inv[item] = quantity # create new entry in inventory

    def remove_from_inv(self, item, quantity):
        if item in self.inv:
            if self.inv[item] >= quantity: 
                self.inv[item] -= quantity
                if self.inv[item] == 0:
                    del self.inv[item] # remove entry if quantity reaches 0
            else:
                print(f"You don't have enough {item.name} in your inventory")
        else:
            print(f"You don't have {item.name} in your inventory")

    def equip_weapon(self, selected_weapon):
        found_weapon = None

        for weapon in weapons_all:  # if they choose a weapon that is in the weapons_all list
            if weapon.name == selected_weapon.name: 
                found_weapon = weapon
                break
        
        if found_weapon:
            self.equipped_weapon = found_weapon
            print(f"{green}>>{found_weapon.name} equipped<<{end}")
            enter()
        else:
            print(f"{red}You don't have {selected_weapon.name} in your inventory.{end}")
            enter()

    def equip_tek(self, selected_tek):
        found_tek = None

        for tek in tek_all:
            if tek.name == selected_tek.name:
                found_tek = tek
                break
        
        if found_tek:
            self.equipped_tek = found_tek
            print(f"{green}>>{found_tek.name} equipped<<{end}")
            enter()
        else:
            print(f"You don't have {selected_tek.name} in your inventory.")
            enter()

    def unequip(self, selected_item):
        if isinstance(selected_item, Weapon): # if it is a Weapon
            if self.equipped_weapon is not None: # checking that there is a weapon equipped
                if selected_item.name == self.equipped_weapon.name: # if you chose the equipped weapon
                    self.equipped_weapon = None # set equipped_weapon to None
                    print(f"\n{bold}{green}>> Unequipped {selected_item.name.title()} <<{end}") # print that it's been unequipped
                else: # if you chose a weapon that isn't the equipped weapon
                    print(f"{red}{bold}You do not have your {selected_item.name} equipped right now.{end}")
            else: # if there is no weapon equipped
                print(f"{red}{bold}You have no weapon equipped right now.{end}") 
        
        elif isinstance(selected_item, Tek): # if choose Tek
            if self.equipped_tek is not None: # checking that there is a weapon equipped
                if selected_item.name == self.equipped_tek.name: # if you chose the equipped weapon
                    self.equipped_tek = None # set equipped_tek to None
                    print(f"\n{bold}{green}>> Unequipped {selected_item.name.title()} <<{end}") # print that it's been unequipped
                else: # if you chose a weapon that isn't the equipped tek
                    print(f"{red}{bold}You do not have your {selected_item.name} equipped right now.{end}")
            else: # if there is no tek equipped
                print(f"{red}{bold}You have no tek equipped right now.{end}") 

    def battle(self, target): 
        round = 1
        while target.HP > 0: # battle loop
            # print battle screen and round number
            def print_battle_title():
                clear()
                bt = f"{bold}{red}xX  Time to Battle  Xx{end}" # title
                pr = f"{bold}Round {round}{end}"
                print(f"{bt:^90}") # print battle screen
                print(f"{pr:^90}") # round number
                print(f"\n{bold}{purple}{self.name.title()}{end}: {self.HP}/{self.maxHP} HP 🩸\n{bold}{yellow}{target.name.title()}{end}: {target.currentHP} /{target.HP} HP 🩸")
            print_battle_title()
            print("\nAttack | Use Item")
            attack_or_inv = input("> ").strip().lower()

            if attack_or_inv is not None:
                if attack_or_inv in ['a', 'attack']: # if choose attack
                    if self.equipped_weapon is not None:
                        if self.equipped_weapon.finesse == True: # if finesse weapon, choice of str or dex_mod
                                str_mod_or_dex_mod = input(f"Do you want to use your Strength ({self.str_mod}) or Dexterity ({self.dex_mod}) modifier?\n> ").strip().lower()
                    else: 
                        print('You need to equip a weapon before you battle')
                        break

                    # your move
                    print()
                    draw()
                    t.sleep(1)
                    if self.equipped_weapon.melee == True or (self.equipped_weapon.finesse == True and str_mod_or_dex_mod in ['s', 'str_mod', 'str']): # if choose str_mod or have to use str_mod bc melee weapon
                        attack_roll = diceRoll(20) + self.str_mod
                        if attack_roll >= target.armor_class: # if attack roll successful, on to do damage
                            damage_roll = diceRoll(self.equipped_weapon.num_of_sides) + self.str_mod
                            target.currentHP -= damage_roll
                            print(f'{bold}You were adept with your {self.equipped_weapon.name} and dealt the {target.name} {damage_roll} damage!{end}')
                        else: 
                            print(f"{bold}You miss them and deal no damage.{end}")
                    
                    elif self.equipped_weapon.range == True or (self.equipped_weapon.finesse == True and str_mod_or_dex_mod in ['d', 'dex_mod', 'dex_modterity']): # if choose dex_mod or need to use dex_mod because range weapon
                        attack_roll = diceRoll(20) + self.dex_mod
                        if attack_roll >= target.armor_class: # if attack roll successful, on to do damage
                            damage_roll = diceRoll(self.equipped_weapon.num_of_sides) + self.dex_mod
                            target.currentHP -= damage_roll
                            print(f'{bold}You were adept with your {self.equipped_weapon.name} and dealt the {target.name} {damage_roll} damage!{end}')
                        else: 
                            print(f"{bold}You miss them and deal no damage.{end}")
                
                    else:
                        print(f"{bold}{red}Invalid{end} command.\n\n{bold}{green}Valid{end} commands:\n's', 'str_mod', 'str'\n'd', 'dex_mod', 'dex_modterity'")
                        continue
                elif attack_or_inv in ['use item', 'item', 'inv', 'i', 'u']: # if want to use an item
                    print_inventory()
                    print_battle_title()
                    draw()
                    print(f"{bold}You used an inventory item as your turn.{end}")
                else:
                    print(f"{red}{bold}Invalid command.\n{green}Valid commands:{end}\n['a', 'attack'\n'use item', 'item', 'inv', 'i', 'u']")
                    t.sleep(1)
                    print_battle_title()
                    continue
            else:
                    print(f"{red}{bold}Invalid command.\n{green}Valid commands:{end}\n['a', 'attack'\n'use item', 'item', 'inv', 'i', 'u']")
                    t.sleep(1)
                    continue
            
            # if kill enemy
            if target.currentHP <= 0: # if enemy dies
                draw()
                t.sleep(1)
                print(f"\nYou have defeated the {target.name}!\n\nThey dropped a {bold}{copper}{target.dropItem.name}{end} and {gold}{target.dropGP} gp{end}.\n\nYou gained 3 HP back 🩸.")
                self.add_to_inv(target.dropItem, 1)
                self.gp += target.dropGP
                self.xp += 30
                self.HP += 3
                return self.inv, self.gp, self.xp

            # enemy's move
            t.sleep(1)
            if target.equipped_weapon.melee == True or target.equipped_weapon.finesse == True:
                tattack_roll = diceRoll(20) + target.strength
                if tattack_roll >= self.AC: # if attack roll successful, on to do damage
                    tdamage_roll = diceRoll(target.equipped_weapon.num_of_sides) + target.strength
                    self.HP -= tdamage_roll
                    print(f'\n{bold}The {target.name} dealt you {tdamage_roll} damage{end}')
                else: 
                    print(f'\n{bold}The {target.name} missed you and dealt no damage!{end}')
            
            elif target.equipped_weapon.range == True:
                tattack_roll = diceRoll(20) + target.dex
                if tattack_roll >= self.AC: # if attack roll successful, on to do damage
                    tdamage_roll = diceRoll(target.equipped_weapon.num_of_sides) + target.dex
                    self.HP -= tdamage_roll
                    print(f'\n{bold}The {target.name} dealt you {tdamage_roll} damage{end}')
                else: 
                    print(f'{bold}The {target.name} missed you and dealt no damage!{end}')
            draw()

            # if enemy kills self
            if self.HP <= 0:
                t.sleep(1)
                print('\nYu gonplei ste odon.\nMay we meet again.')
                quit()
            
            # if nobody dies
            if self.HP > 0 and target.HP > 0:
                
                t.sleep(1)
                print(f"\nYou have both survived round {round}! 🎉")
                round += 1
                t.sleep(1)
                enter()
                print_battle_title()
                
    def print_stats(self):
        clear()
        print(f"{bold}{underline}{self.name}{end}")
        print(f"\n{lime}{bold}Health{white}\t\t  | {self.HP}/{self.maxHP} 🩸\n{gold}Gold{white}\t\t  | {self.gp}")
        print(f"{cyan}Proficiency Bonus{white} | {self.prof_bonus}")
        print(f"{teal}XP {white}\t\t  | {self.xp}")
        print(f"{turquoise}Armor Class {white}\t  | {self.AC}{end}")
        draw()
        print(f"{bold}\n\t   Ability    Modifier")
        print(f"{red}Strength{white}     | {self.str_ability} | {self.str_mod}")
        print(f"{orange}Dexterity{white}    | {self.dex_ability} | {self.dex_mod}")
        print(f"{yellow}Constitution{white} | {self.const_ability} | {self.const_mod}")
        print(f"{green}Intelligence{white} | {self.int_ability} | {self.int_mod}")
        print(f"{blue}Wisdom{white}\t     | {self.wis_ability}  | {self.wis_mod}")
        print(f"{purple}Charisma{white}     | {self.char_ability} | {self.char_mod}")
        enter()

    def save_game(self, filename): # writing self to a file 
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
            print(f'{green}>>game saved<<{end}')
            t.sleep(0.5)
        except Exception as e:
            print(f"{red}Error saving game: {str(e)}{end}")

    @staticmethod
    def load_game(filename): ### FIX: There is a problem when loading from a new game, doesn't recognize self
        try:
            with open(filename, "rb") as file:
                loaded_player = pickle.load(file)
            print(f'{green}>>loaded successfully<<{end}')
            return loaded_player
        except FileNotFoundError:
            print(">>no saved game found<<")
            return None
        except Exception as e:
            print(f"{red}Error loading game: {str(e)}")

class Enemy(Character): 
    def __init__ (self, name, HP, maxHP, AC, str_mod, dex_mod, drop_item, drop_GP, equipped_weapon=None):
        super().__init__(name, HP, maxHP, AC, str_mod, dex_mod, equipped_weapon)
        self.drop_item = drop_item
        self.drop_GP = drop_GP

# enemy objects
### THINK ABOUT adding these attributes to Enemy: list of different attack options, 4 options for damage they can do to player (either damage can be randomly chosen or we give them str/dex modifiers for it), death (a unique string for how each enemy dies)
reaper = Enemy('reaper', 15, 15, 12, 1, 1, reaper_stick, 3, dagger)
azgeda = Enemy('azgeda warrior', 10, 10, 10, 1, 1, butterfly_sword, 5, rapier)
mountain_man = Enemy('mountain man', 18, 18, 15, 2, 2, knockout_gas, 10, crossbow)

random_enemy_list = [reaper, azgeda] # list of enemies that randomly spawn
random_enemy = r.choice(random_enemy_list) 
enemies_all = [reaper, azgeda, mountain_man]

def pretty_print(player): # just prints out the inventory pretty
    clear()
    print(f"{bold}{underline}{player.name}{end}")
    print(f"\n{green}Health{end}: {player.HP}/{player.maxHP} 🩸") # printing health
    print(f"{gold}Gold{end}: {player.gp}")
    if player.equipped_weapon is not None:
        print(f"\n{bold}Equipped Weapon:{end} {(player.equipped_weapon.name).title()}")
    else:
        print(f"\n{bold}Equipped Weapon:{end} {player.equipped_weapon}")
        
    if player.equipped_tek is not None:
        print(f"{bold}Equipped Tek:{end} {player.equipped_tek.name.title()}\n")
    else:
        print(f"{bold}Equipped Tek:{end} {player.equipped_tek}\n")
            
    print(f"\n{bold}{purple}Inventory:\n{end}")
        
    draw()
    counter = 1
    for item, quantity in player.inv.items(): # print inventory
        if isinstance(item, Item):
            print(f"{purple}{counter}.{white} ", *item.name.title(), f" x {quantity}", sep = "", end = "\n")
        counter += 1
    draw()

def print_inventory(player):
    while True:
        pretty_print(player)

        # inventory choices
        print(f"\n[{cyan}{bold}l{end}] to leave")
        choice = input("> ").strip().lower() # user input
        
        if choice in ['l', 'leave', 'x', 'exit']: # leave
            break
        
        elif choice.isdigit():
            item_index = int(choice) - 1 # converting choice into an index of the inventory
            if 0 <= item_index <len(player.inv): # check whether item_index is in valid range of indices for inventory
                selected_item = list(player.inv.keys())[item_index] # assigning selected_item to item in inventory
                
                for i in player.inv: # go through inventory line by line
                    if selected_item == i: # find selected item in list
                        print(f"\n{bold}{selected_item.name.title()}{end}\nWhat would you like to do?")
                        if isinstance(selected_item, Food):
                                print("| Back | Sell | Eat | Desc")
                        elif isinstance(selected_item, Drink) or isinstance(selected_item, Potion):
                                print("| Back | Sell | Drink | Desc")
                        else:
                            print("| Back | Sell | Equip | Unequip | Desc")
                        
                        option = input("\n> ").strip().lower()

                        if option in ['x', 'exit', 'b', 'back', 'l', 'leave']: # exit
                                break

                        elif option in ['s', 'sell']: # sell
                            player.remove_from_inv(selected_item, 1)
                            print(f"{gold}>> {selected_item.name} sold for {selected_item.price} gp <<{end}")
                            player.gp += selected_item.price
                            enter()
                            break

                        elif option in ['equip', 'e', 'eat', 'drink']: # use/equip item
                            if isinstance(selected_item, Potion): # if it's a potion
                                selected_item.drinkPotion(player)
                                enter()
                                break
                            elif isinstance(selected_item, Weapon): # if it's a weapon
                                player.equip_weapon(selected_item)
                                break
                            elif isinstance(selected_item, Tek): # if it's tek
                                player.equip_tek(selected_item)
                                break
                            elif isinstance(selected_item, Food): # if its food
                                selected_item.eat(player)
                                break
                            elif isinstance(selected_item, Drink): # if its a drink
                                selected_item.drink()
                                break
                        
                        elif option in ['u', 'unequip']:
                            try:
                                player.unequip(selected_item) # unequip Tek
                                enter()
                            except:
                                print("NOT WORKING")
                                enter()
                        
                        elif option in ['d', 'desc', 'description']: # description
                                print(selected_item.desc)
                                enter()
                                break
                        else:
                            print(f"{red}{bold}Invalid Command.\n{green}Valid Commands:\n{white}['s', 'sell'\n'x', 'exit', 'b', 'back', 'l', 'leave'\n'equip', 'e', 'eat', 'drink'\n'd', 'desc', 'description']{end}")
                            enter()

        else:
            print(f"{bold}{red}Invalid command.\n{green}Valid commands:{white}\n['l', 'leave', 'x', 'exit'\nor the corresponding number to the inventory item you want to select]{end}")
            enter()

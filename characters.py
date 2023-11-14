import time as t, pickle, random as r
from util import clear, enter, draw, diceRoll, bold, red, end, white, cyan, purple, underline, orange, yellow, green, blue, lime, teal, turquoise, gold, copper, gray
from items import weapons_all, tek_all, Potion, Weapon, Item, Tek, Food, Drink, reaper_stick, dagger, butterfly_sword, rapier, knockout_gas, crossbow, shiv
from skill_checks import roll_with_disadvantage, roll_d20

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
    def __init__(self, name, HP, maxHP, gp, str_ability, str_mod, dex_ability, dex_mod, const_ability, const_mod, int_ability, int_mod, wis_ability, wis_mod, char_ability, char_mod, prof_bonus, xp, AC, crime_num, equipped_weapon=None, equipped_tek=None, inv=None):
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
        
        self.crime_num = crime_num
        self.xp = xp
        self.equipped_tek = equipped_tek
        if inv is None: # doing this so we don't have a mutable list set as the default
            self.inv = {}
        else:
            self.inv = inv

        self.exhaustion_level = 0 # variable to track exhaustion level
        self.is_dodging = False # handles dodging state for Battle
    
    # function to handle losing health in battle (called in Battle class)
    def lose_health(self, num_hp_lost):
        self.HP -= num_hp_lost
        return self.HP
    
    # function to handle gaining health in battle (called in Battle class)
    def gain_health(self, num_hp_gained):
        self.HP += num_hp_gained
        return self.HP
    
    # function to handle gaining xp
    def gain_xp(self, xp_gained):
        self.xp += xp_gained
        return self.xp
    
    # function to handle gaining gp
    def gain_gp(self, gp_gained):
        self.gp += gp_gained
        return self.gp
    
    # function to toggle dodging state in Battle
    def toggle_dodge(self): 
        self.is_dodging = not self.is_dodging
    
    # method to handle exhaustion penalties
    def apply_exhaustion_penalty(self):
        # lvl 1 exhaustion: disadvantage on ability checks
        if self.exhaustion_level == 1:
            print(f"\nYou are mildly exhausted. You must rest, eat, or\ndrink water to regain your energy. While you are exhausted,\nyou have incurred a{red} disadvantage on ability checks.{end}")
        
        # lvl 2 exhaustion: disadvantage on attack rolls and saving throws
        elif self.exhaustion_level == 2:
            print(f"\n{bold}You are very exhausted. You must rest, eat, or\ndrink water to regain your energy. While you are very exhausted,\nyou will have a{red} disadvantage on attack rolls and saving throws.{end}")
        
        # lvl 3 exhaustion: HP max halved
        elif self.exhaustion_level == 3:
            self.maxHP = self.maxHP/2
            print("\nYou are very exhausted. Until you rest, eat, or drink,\nyour hit point maximum will be halved.")
            print(f"{self.name} currently has {self.HP}/{self.maxHP} HP 🩸")
    
    # method to handle taking a short or long rest
    def rest(self, short_or_long):
        if self.exhaustion_level > 0:
            if short_or_long == "short": # if choose a short rest
                print("You take a short rest and recover.")
                
                if self.exhaustion_level == 3: # if exhaustion lvl 3
                    self.maxHP = self.maxHP * 2 # set maxHP back to original maximum
                
                self.exhaustion_level -= 1 # remove 1 exhaustion level
            else: # if choose a long rest
                print("You take a long rest and fully recover.")
                
                if self.exhaustion_level == 3:
                    self.maxHP = self.maxHP * 2
                
                self.exhaustion_level = 0 # set exhaustion lvl back to zero, fully recovered
        else:
            print("You are not exhausted.")

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
    
    # function to handle enemy losing HP
    def lose_hp(self, hp_lost):
        self.HP -= hp_lost
        return self.HP

    # function to fill up enemy's HP (when need to respawn)
    def fill_hp(self):
        self.HP = self.maxHP
        return self.hp

class NPC(Character):
    def __init__(self, name, HP, maxHP, AC, str_mod, dex_mod, drop_item, drop_GP, equipped_weapon = None):
        super().__init__(name, HP, maxHP, AC, str_mod, dex_mod, equipped_weapon)
        self.drop_item = drop_item
        self.drop_GP = drop_GP

def print_stats(user):
        clear()
        print(f"{bold}{underline}{user.name}{end}")
        print(f"\n{lime}{bold}Health{white}\t\t  | {user.HP}/{user.maxHP} 🩸\n{gold}Gold{white}\t\t  | {user.gp}")
        print(f"{cyan}Proficiency Bonus{white} | {user.prof_bonus}")
        print(f"{teal}XP {white}\t\t  | {user.xp}")
        print(f"{turquoise}Armor Class {white}\t  | {user.AC}")
        print(f"{gray}Exhaustion\t  {white}| {user.exhaustion_level}{end}")
        draw()
        print(f"{bold}\n\t   Ability    Modifier")
        print(f"{red}Strength{white}     | {user.str_ability} | {user.str_mod}")
        print(f"{orange}Dexterity{white}    | {user.dex_ability} | {user.dex_mod}")
        print(f"{yellow}Constitution{white} | {user.const_ability} | {user.const_mod}")
        print(f"{green}Intelligence{white} | {user.int_ability} | {user.int_mod}")
        print(f"{blue}Wisdom{white}\t     | {user.wis_ability}  | {user.wis_mod}")
        print(f"{purple}Charisma{white}     | {user.char_ability} | {user.char_mod}")
        enter()

# enemy objects
### THINK ABOUT adding these attributes to Enemy: list of different attack options, 4 options for damage they can do to player (either damage can be randomly chosen or we give them str/dex modifiers for it), death (a unique string for how each enemy dies)
reaper = Enemy('reaper', 15, 15, 12, 1, 1, reaper_stick, 3, dagger)
azgeda = Enemy('azgeda warrior', 10, 10, 10, 1, 1, butterfly_sword, 5, rapier)
mountain_man = Enemy('mountain man', 18, 18, 15, 2, 2, knockout_gas, 10, crossbow)

random_enemy_list = [reaper, azgeda] # list of enemies that randomly spawn
random_enemy = r.choice(random_enemy_list) 
enemies_all = [reaper, azgeda, mountain_man]

# NPC objects
dante = NPC('dante', 15, 15, 15, 3, 2, shiv, 10, rapier)

def save_game(user, filename): # writing user to a file 
        try:
            with open(filename, "wb") as file:
                pickle.dump(user, file)
            print(f'{green}>> game saved <<{end}')
            t.sleep(0.5)
        except Exception as e:
            print(f"{red}Error saving game: {str(e)}{end}")

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
                            if selected_item.name == player.equipped_weapon.name: # if the item is the equipped item, remove it
                                player.equipped_weapon = None
                            if selected_item.name == player.equipped_tek.name:
                                player.equipped_tek = None

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
                                selected_item.drink(player)
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

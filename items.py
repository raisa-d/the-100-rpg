from util import red, end, bold, cyan, enter, green

class Item:
    num_of_items = 0 # counting total in-game Item
    def __init__(self, name, desc, price, isFood, isDrink, isWeapon, isTek):
        self.name = name
        self.desc = desc
        self.price = price
        self.isFood = False
        self.isDrink = False
        self.isWeapon = None
        self.isTek = None
    
        Item.num_of_items += 1

class Weapon(Item):
    def __init__(self, name, desc, price, isFood, isDrink, isWeapon, isTek, finesse, melee, range, num_of_sides):
        super().__init__(name, desc, price, isFood, isDrink, isWeapon, isTek)
        self.finesse = finesse
        self.melee = melee
        self.range = range
        self.num_of_sides = num_of_sides # which die needs to be rolled for that weapon

class Potion(Item):
    def __init__(self, name, desc, price, isFood, isDrink, isWeapon, isTek, effects):
        super().__init__(name, desc, price, isFood, isDrink, isWeapon, isTek)
        self.effects = effects
    
    def drinkPotion(self, user): # call function when want to drink potion/gain effectss from them
        if self.name == 'knowledge potion':
            print(knowledge_potion.effects)
            user.xp += 15
        elif self.name == 'health potion':
            print(health_potion.effects)
            user.HP += 5
        user.remove_from_inv(self, 1)
        return user.xp, user.HP

class Tek(Item):
    def __init__(self, name, desc, price, isFood, isDrink, isWeapon, isTek, effects):
        super().__init__(name, desc, price, isFood, isDrink, isWeapon, isTek)
        self.effects = effects
    
    def useTek(self, user): ###CODE THIS SO YOU CAN ACTUALLY USE IT IN A SCENARIO AND IT WILL INTERACT WITH RADIATION, ETC.
        if self.name == 'wristband':
            print(f"\nCHANGE THIS TO ACTUALLY AFFECT THINGS:\n{wristband.effects}") ### actually implement something you can do with it
        elif self.name == 'gas mask':
            print(f"\nCHANGE THIS TO ACTUALLY AFFECT THINGS:\n{gas_mask.effects}") ###
        elif self.name == 'the fleim':
            print(f"\nCHANGE THIS TO ACTUALLY AFFECT THINGS:\n{the_fleim.effects}") ###
        elif self.name == 'knockout gas':
            print(f"\nCHANGE THIS TO ACTUALLY AFFECT THINGS:\n{knockout_gas.effects}") ###

    def use_wristband(self):
        pass ### create functionality for radiation alert & turning on night vision, plus any other effectss you may add to it

class Food(Item):
    def __init__(self, name, desc, price, isFood, isDrink, isWeapon, isTek):
        super().__init__(name, desc, price, isFood, isDrink, isWeapon, isTek)
        self.isFood = True
        self.isDrink = False
                 
    def eat(self, user):
        if self.isFood:
            print(f"{bold}{red}You scarf down the {self.name} and relish in a warm belly.{end}")
            user.remove_from_inv(self, 1)
            enter()

class Drink(Item):
    def __init__(self, name, desc, price, isFood, isDrink, isWeapon, isTek):
        super().__init__(name, desc, price, isFood, isDrink, isWeapon, isTek)
        self.isFood = False
        self.isDrink = True

    def drink(self, user):
        if self.isDrink:
            print(f"{bold}{cyan}You gulp down the crisp {self.name}.{end}")
            user.remove_from_inv(self, 1)
            enter()

# consumable objects
rations = Food("1 days rations", "WRITE DESC", 5, True, False, False, False)
small_waterskin = Drink("small waterskin", "WRITE DESC", 2, False, True, False, False)
large_waterskin = Drink("large waterskin", "WRITE DESC", 4, False, True, False, False)
consumables_all = [rations, small_waterskin, large_waterskin]


# weapon objects
glaive = Weapon('glaive', 'This glaive boasts a gleaming obsidian blade with intricate,\nethereal runes etched along its length, set upon a polished, ebony-hued\nshaft adorned with menacing, dragon-shaped pommel.', 20, False, False, True, False, False, True, False, 10)
rapier = Weapon('rapier', 'This rapier is an elegantly slender and silvered blade,\nits handle intricately adorned with sapphire-encrusted crossguards\nand a hilt of black leather wrapped in silver thread.', 25, False, False, True, False, False, True, False, 8)
dagger = Weapon('dagger', 'The dagger gleams with a wickedly curved obsidian blade,\na hilt wrapped in midnight-blue leather, and\na pommel adorned with a menacing onyx gemstone.', 4, False, False, True, False, True, False, False, 4)
crossbow = Weapon('crossbow', 'This crossbow features a sleek, polished mahogany stock adorned\nwith intricate ivory inlays, a glistening steel barrel, and an\nexquisitely carved ebony trigger guard, giving it\nan air of both beauty and deadly precision.', 25, False, False, True, False, False, False, True, 8)
butterfly_sword = Weapon('butterfly sword', 'The butterfly sword boasts a pair of elegantly slender blades\nwith intricately carved jade hilts, their unique S-shaped guards\ndesigned for fluid, acrobatic combat Tekniques.', 10, False, False, True, False, True, False, False, 6)
reaper_stick = Weapon('reaper stick', 'WRITE DESCRIPTION', 10, False, False, True, False, False, True, False, 8)
reaper_cleaver = Weapon('reaper cleaver', 'The Reaper Cleaver is a massive, double-edged greataxe\nwith a rusted and jagged blade, imbued with a menacing aura,\nsuggesting the cruelty of its wielder.', 30, False, False, True, False, False, True, False, 8)
multipurpose_knife = Weapon('multipurpose knife', 'A compact tool featuring a sharp blade,\nserrated edge, firestarter, bone saw, and an LED flashlight', 50, False, False, True, False, False, True, False, 6)
throwing_knives = Weapon('throwing knives', 'Set of 5 sleek, lightweight knives balanced for precision,\nmaking them deadly when thrown accurately or used up close.', 10, False, False, True, False, True, False, False, 4)
shiv = Weapon('shiv', 'A small, sharp blade attached to a handle\nmade from scrap metal', 0, False, False, True, False, False, True, False, 6)
wrench = Weapon('mechanical wrench blade', 'Combines a a sturdy metal wrench with a retractable, razor-sharp blade\nOriginally designed for enginering repairs, the blade can be extended\nfor use as a melee weapon.', 0, False, False, True, False, False, True, False, 8)
shortbow = Weapon('shortbow', 'The shortbow\'s silent operation and lightweight design\nmake it an excellent choice for individuals relying on stealth\nand precision in their encounters', 25, False, False, True, False, False, False, True, 6)
weapons_all = [glaive, rapier, dagger, crossbow, butterfly_sword, reaper_stick, reaper_cleaver, multipurpose_knife, throwing_knives, shiv, wrench, shortbow]
weapons_for_sale = [glaive, rapier, dagger, crossbow, butterfly_sword, reaper_stick, reaper_cleaver, multipurpose_knife, throwing_knives, shortbow]

# list of all potion objects
health_potion = Potion('health potion', 'A glimmering green liquid', 3, False, True, False, False, f"{green}You ingest the green potion and gain 5 health{end}")
knowledge_potion = Potion('knowledge potion', 'A swirling pearl potion which helps you gain knowledge', 5, False, True, False, False, "You drink the potion and gain 15 XP")
potions_all = [health_potion, knowledge_potion]

# tek objects
wristband = Tek('wristband', 'These wristbands came with the original 102 to the ground.\nThey were used to measure their vital signs and to\ncommunicate with those still on the Ark.', 50, False, False, False, True, 'This helpful wristband will give you radiation alerts and night-vision.')
gas_mask = Tek('gas mask', 'A gas mask is crucial in a radiation-struck world.\nIt filters out knockout gas and other toxic pollutants.', 35, False, False, False, True, 'Renders the wearer immune to knockout gas\nand less susceptible to radiation and Earth\'s toxic air')
knockout_gas = Tek('vial of knockout gas','Knockout gas is used by the mountain men.\nIt is a potent chemical agent which, like\nthe name says, knocks out whoever inhales it.', 50, False, False, False, True, 'Everyone within a 10mi radius') ### change radius it affects?
the_fleim = Tek('the fleim', 'The Fleim, a sacred artifact, embodies the collective wisdom and\nspirits of past Commanders, guiding us with their knowledge and insight.', 3000, False, False, False, True, 'A natblida who wins the conclave must take the Fleim and\nrecite the lineage in order to ascend as Commander.\nThe Fleimkepa acts as protecter of the Fleim and of the Commander.')
tek_for_sale = [wristband, gas_mask, knockout_gas]
tek_all = [wristband, gas_mask, the_fleim, knockout_gas]

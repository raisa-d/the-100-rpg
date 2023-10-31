import time as t
from util import clear, enter, bold, red, cyan, end, gold, green, yellow

def intro(): # scene: get introduced to the game and choose your character
    clear()
    print("When the nuclear apocalypse destroyed Earth, groups\nof lucky individuals made it onto 13 space stations\nand shot themselves into space to ensure the survival\nof the human race. 12 space stations joined together\nand were renamed the Ark.")
    print("\nOn the Ark, every crime is punishable by death unless\nyou are under 18 years old, in which case, you get\nimprisoned in the Sky Box.")
    print("\n97 years post-apocalypse, and 100 years before the\nEarth will be survivable again, you\nare a prisoner on the Ark.\n")
    input(f"[{bold}{cyan}Enter{end}] to choose your crime\n")

def get_to_dropship(): # scene: getting to dropship
    clear()
    print('You approach the Boarding Bay. When you get there, you see\nprisoners being pushed into a dropship, strapped into\na seat, and tagged with a wristband.')
    print('\nSuddenly, you are being shoved into a seat and a wristband is\nclamped onto your wrist. It pinches a little bit.')
    print("\nOnce everyone is seated, a video of the Chancellor begins playing. He says:")
    print(f"\n{bold}{red}\"You are being sent to the ground to see if mankind can\nsurvive there. As you are criminals, we felt you were expendable.\n\nWe are dropping you on Mount Weather, where there is a bunker\nthat can supply 300 people for two years. Find those supplies\nas your life may depend on it.\n\nIf you do survive on Earth, your crimes will be forgiven.\"{end}")
    print("\nThe dropship doors close.")
    enter()

def launching_dropship(): # scene: launching dropship
    clear()
    print('LAUNCHING DROPSHIP IN')
    t.sleep(0.5)
    print('3...')
    t.sleep(1)
    print("2...")
    t.sleep(1)
    print("1...")
    t.sleep(1)
    print("\nYou launch into space.")
    t.sleep(1)
    print("\nYour body fills with exhilaration and fear as you hurtle through\nEarth's atmosphere. The anticipation of stepping outside and\nonto the ground makes your heart pound violently.")
    enter()

other_mount_weather = '''
                              ¸...¸
                          ¸.·´  ¸   `·.¸.·´·.
                         :::::::::::::::::::: 
                          `·.       ¸.·´ `·¸·´
'''

def Nyx_Jules_dialogue():
    clear()
    # Nyx dialogue
    print(f'You all gather around to make a survival plan. A You\'ve seen once before--\nyou remember their name is Nyx. They say to the group,\n\n{bold}{yellow}"We need to set up camp. I don\'t know how long we can survive here,\nbut we have to give it our best shot. We just got our freedom back and\nI, for one, want to be alive to experience it."{end}')
    enter()
        
    # Jules dialogue
    clear()
    print(f'Jules chimes in and says,\n\n{bold}{cyan}"What we really need is to get to Mount Weather. We won\'t survive\nlong otherwise on this radiation-infested planet."{end}')
    print(f"\nOthers start saying their piece. Most don't want to walk the 20 miles there.")
    enter()

def see_Earth(): 
    clear()
    mount_weather = (f'''{bold}{green} 
              /\\
             /  \\
            /    \\
      /\   /      \ /\\
     /  \/        \/  \\
    /                  \\
  /                      \\
/__________________________\\
{end}''') # ascii art of mount_weather range
    
    print(f"{mount_weather}")
    print(f"{gold}As the hatch of the dropship creaks open, the soft, golden\nlight of Earth's sun spills into the cramped, metallic\ninterior. For a moment, all is silent, the only sound being\nthe rustle of leaves. You look around and see a gorgeous")
    print("mountain range Southwest of you and there are woods all around.")
    print(f"\nYou take in a big gulp fresh air, the first you've ever had.\nEarth is just as beautiful as you imagined it would be.")
    print(f"\nAfter you take it in, you all start cheering and run out\nof the dropship in a celebration.{end}")
    enter()

# scene: talking to nyx
def talk_to_Nyx(user):
    print('\nYou approach Nyx. They look at you and say,')
    if user.crime_num == 4:
        print('"The dropship looks pretty beat up."') # they say this to the engineer, as maybe they will reinforce the dropship when they choose set up base camp
    elif user.crime_num == 2: # Nyx says this to the stoner
        print('"Earth is everything I dreamed it was.\nCan you believe the trees are really this green?"') ### change this?
    elif user.crime_num == 1: # they say this to the leader
        print("The comms system isn't working, we have no way\nto communicate with the Ark anymore.")
    else:
        print("Can you believe we're actually, truly FREE?!")
    enter()

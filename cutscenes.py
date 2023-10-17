import time as t
from formatting import clear, enter

# colors
bold = "\033[1m"
red = "\033[31m"
cyan = "\033[36m"
end = "\033[0m" # end any formatting

def intro(): # scene: get introduced to the game and choose your character
    clear()
    print("When the nuclear apocalypse destroyed Earth, groups\nof lucky individuals made it onto 13 space stations\nand shot themselves into space to ensure the survival\nof the human race. 12 space stations joined together\nand were renamed the Ark.")
    t.sleep(2)
    print("\nOn the Ark, every crime is punishable by death unless\nyou are under 18 years old, in which case, you get\nimprisoned in the Sky Box.")
    t.sleep(2)
    print("\n97 years post-apocalypse, you are a prisoner on the Ark.\n")
    t.sleep(2)
    input(f"[{bold}{cyan}Enter{end}] to choose your crime\n")

def get_to_dropship(): # scene: getting to dropship
    clear()
    print('You begin to approach the Boarding Bay. When you get there, you see\nprisoners being pushed into a dropship, strapped into a seat, and\ntagged with a wristband.')
    t.sleep(1)
    print('\nSuddenly, you are being shoved into a seat and a wristband is\nclamped onto your wrist. It pinches a little bit.')
    t.sleep(1)
    print("\nOnce everyone is seated, a video of the Chancellor begins playing. He says:")
    t.sleep(1)
    print(f"\n{bold}{red}\"You are being sent to the ground to see if mankind can\nsurvive there. As you are criminals, we felt you were expendable.\nIf you do survive on Earth, your crimes will be forgiven.\"{end}")
    t.sleep(1)
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
    print("\nYour body fills with exhilaration and fear as you hurtle through\nEarth's atmosphere. The anticipation of stepping outside and\nonto the ground makes your heart pound more violently.")
    t.sleep(1)
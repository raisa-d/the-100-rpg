import os, random as r

# colors
bold = "\033[1m"
normal = "\x1b[0m" + "\x1b[38;2;255;255;255m"
italic = "\033[3m"
underline = "\033[4m"
strike = "\033[9m" # strikethrough
end = "\033[0m" # end any formatting
gold = "\x1b[38;2;230;190;0m\x1b[1m"
silver = "\x1b[38;2;221;221;221m\x1b[1m"
copper = "\x1b[38;2;170;44;0m\x1b[1m"
red = "\033[31m"
orange = '\x1b[38;2;255;90;0m\x1b[1m'
yellow = "\033[33m"
green = "\033[32m"
blue =  "\033[34m"
lime = '\x1b[38;2;00;255;00m\x1b[1m'
turquoise = '\x1b[38;2;0;255;255m\x1b[1m'
teal = '\x1b[38;2;0;170;170m\x1b[1m'
purple = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"
gray = "\033[1;30m"

def Title(): # print out game header
    title = "The 100 Role Player Game"
    Title = f"{italic}{bold}{green}{title:^80}{end}"
    author = f"{purple}by @rai__bread{end}"
    print(Title)
    print(f"{author:^90}\n")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    Title()
def enter():
    input(f"\n[{bold}{cyan}Enter{end}] to continue\n")
def draw():
    print(f"{strike}Xx             xOx            xX{end}")

# diceroll function (used for attack & damage rolls)
def diceRoll(numOfSides):
  roll = r.randint(1, numOfSides)
  return roll

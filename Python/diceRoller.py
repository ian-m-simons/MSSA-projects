import random

def inputInt(prompt):
    success = False
    while (not success):
        num = input(prompt)
        try:
            num = int(num)
            success = True
        except:
            print("[ERROR] Input must be an integer")
    return num
def rollDice(sides, diceCount):
    total = 0
    for i in range(diceCount):
        landing = random.randint(1, sides)
        print("di ", i+1, "landed on ", landing)
        total += landing
    print("total comes to ", total)

def main():
   print("welcome!")
   sides = 6
   diceCount = 2
   while True:
       print("what would you like to do?")
       print("1) change type of dice (default 6 sided di")
       print("2) change number of dice (default 2)")
       print("3) roll dice")
       print("0) exit")
       choice = inputInt("option: ")
       if choice == 1:
           sides = inputInt("how many sides should your dice have? ")
       elif choice == 2:
           diceCount = inputInt("how many dice would you like to have? ")
       elif choice == 3:
           rollDice(sides, diceCount)
           print("\n\n\n")
       elif choice == 0:
           exit(0)
       else:
           print("[ERROR] invalid option")
   '''
    print("welcome!")
    sides = inputInt("how many sides should your dice have? ")
    print("ok we'll create ", sides, "sided dice!")
    diceCount = inputInt("how many dice should we roll? ")
    total = 0
    for i in range(diceCount):
        landing = random.randint(1, sides)
        print("di ", i+1, "landed on ", landing)
        total += landing
    print("total comes to ", total)
'''
if __name__ == "__main__":
    main()

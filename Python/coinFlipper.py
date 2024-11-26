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

def main():
    print("Welcom!")
    while True:
        print("please select an option")
        print("1) flip coin")
        print("0) exit")
        choice = inputInt("option: ")
        if choice == 1:
            number = random.randint(0,1)
            if number == 0:
                print("HEADS!")
            else:
                print("Tails!")
        elif choice == 0:
            exit(0)
        else:
            print("[ERROR] invalid option" )

if __name__ == "__main__":
    main()

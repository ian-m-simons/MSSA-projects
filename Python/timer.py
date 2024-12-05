import time

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
    timer = inputInt("Please enter time in seconds ")
#todo change timer so it uses the seconds from date time rather than sleep
#this will make it more accurate
    while timer > 0:
        print(timer, end='\r')
        timer -= 1
        time.sleep(1)
    print("Timer has expired")

if __name__ == "__main__":
    main()

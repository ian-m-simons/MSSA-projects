from datetime import datetime
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
#todo at the change of minute seconds and microseconds reset to 0 and timer freezes
    usefultime = datetime.now()
    savedtime = usefultime.timestamp()
    firstRun = True
    while timer > 0:
        ct = datetime.now()
        currenttime = ct.timestamp()
        if firstRun:
            print(str(timer)+"     ", end='\r')
            timer -= 1
            firstRun = False
        if currenttime >= savedtime + 1:
            if timer >1:
                print(str(timer)+"     ", end='\r')
                timer -= 1
                usefultime = datetime.now()
                savedtime = usefultime.timestamp()
            else:
                print(str(timer))
                timer -= 1
                time.sleep(1)
        else:
            pass
        
    print("Timer has expired")

if __name__ == "__main__":
    main()

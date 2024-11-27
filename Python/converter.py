

#features
def binToDec(num):
    index = 0
    result = 0
    while num > 0:
        if num % 10 == 1:
            result += 2**index
        else:
            pass
        num = num // 10
        index = index + 1
    return result

def decToBin(num):
    highestSquare = 0
    solution = ""
    while 2 ** highestSquare < num:
        highestSquare += 1
    for i in range(highestSquare, -1, -1):
        if 2 ** i <= num:
            num -= 2**i
            solution += "1"
        else:
            solution += "0"
    solution = int(solution)
    return solution

def AtoZ(num):
    if num == 10:
        return "A"
    elif num == 11:
        return "B"
    elif num == 12:
        return "C"
    elif num == 13:
        return "D"
    elif num == 14:
        return "E"
    elif num == 15:
        return "F"
    else:
        print("congrats you managed to break my code please submit bug report including all input used")
        exit(0)

def overTen(num):
    if num.upper() == "A":
        return 10
    elif num.upper() == "B":
        return 11
    elif num.upper() == "C":
        return 12
    elif num.upper() == "D":
        return 13
    elif num.upper() == "E":
        return 14
    elif num.upper() == "F":
        return 15
    else:
        print("congrats you managete to break my code, please submit a bug report including all input used")
        exit(0)


def hexToDec(numAsString):
    solution = 0
    index = 0
    while len(numAsString) > 0:
        if len(numAsString) == 1:
            workingNum = numAsString
            numAsString = ""
            try:
                workingNum = int(workingNum)
                solution += workingNum * (16 ** index)
            except:
                workingNum = overTen(workingNum)
                workingNum = int(workingNum)
                solution += (workingNum * (16 ** index))
        else:
            workingNum = numAsString[-1]
            numAsString = numAsString[0:-1]
            try:
                workingNum = int(workingNum)
                solution += (workingNum * (16 ** index))
            except:
                workingNum = overTen(workingNum)
                workingNum = int(workingNum)
                solution += (workingNum * (16 ** index))
        index += 1
    return solution

def decToHex(num):
    highestHex = 0
    solution = ""
    while 16 ** highestHex <= num:
        highestHex += 1
    for i in range(highestHex, 0, -1):
        digit = num % 16
        if digit >9:
            solution = AtoZ(digit) + solution
        else:
            solution = str(digit) + solution
        num = num // 16
        '''if 16**highestHex <= num:
            digit = num // 16**highestHex
            if digit > 9:
                solution += AtoZ(digit)
            else:
                solution += str(digit)
            num = num - 16**digit'''
    return solution
    

def binToHex():
    return 0

def hexToBin():
    return 0

#input verification functions
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

def verifyHex(num):
    for i in num:
        try:
            i = int(i)
            if (i > -1 and i <10):
                pass
        except:
            if i.upper() == "A":
                pass
            elif i.upper() == "B":
                pass
            elif i.upper() == "C":
                pass
            elif i.upper() == "D":
                pass
            elif i.upper() == "E":
                pass
            elif i.upper() == "F":
                pass
            else:
                return False
    return True
    

def verifyBin(num):
    workingNum = num
    while workingNum > 0:
        if workingNum % 10 == 0 or workingNum % 10 == 1:
            pass
        else: 
            return False
        workingNum = workingNum // 10
    return True

#mainMenu
def main():
    print("Welcome!")
    while True:
        print("Please select an option below")
        print("1) Convert decimal to binary")
        print("2) Convert binary to decimal")
        print("3) Convert decimal to hexadecimal")
        print("4) Convert hexadecimal to decimal")
        print("5) Convert binary to hexadecimal")
        print("6) Convert hexadecimal to binary")
        print("0) exit")
        choice = inputInt("option: ")

        if choice == 1:

            num = inputInt("please enter a decimal number: ")
            while num <0:
                print("Negative numbers are not currently supported, please enter a positive number")
                num = inputInt("please enter a decimal number: ")
            print(decToBin(num))
        elif choice == 2:
            num = inputInt("please enter a binary number: ")
            BinVerified = False
            BinVerified = verifyBin(num)
            while not BinVerified:
                print("[ERROR] input may only be a binary number (1 or 0)")
                num = inputInt("please enter a binary number: ")
                BinVerified = verifyBin(num)
            print(binToDec(num))
        elif choice == 3:
            num = inputInt("please enter a decimal number: ")
            print(decToHex(num))
        elif choice == 4:
            num = input("please enter a hexadecimal number: ")
            correctHex = verifyHex(num)
            while correctHex == False:
                print("0[Error] input may only contain 0-9 and A-F")
                num = input("please enter a hexadecimal number: ")
                correctHex = verifyHex(num)
            print(hexToDec(num))
        elif choice == 5:
            num = inputInt("please enter a binary number: ")
            BinVerified = False
            BinVerified = verifyBin(num)
            while not BinVerified:
                print("[ERROR] input may only be a binary number (1 or 0)")
                num = inputInt("please enter a binary number: ")
                BinVerified = verifyBin(num)
            num = binToDec(num)
            num = decToHex(num)
            print(num)
        elif choice == 6:
            num = input("please enter a hexadecimal number: ")
            correctHex = verifyHex(num)
            while correctHex == False:
                print("[ERROR] input may only contain 0-9 and A-F")
                num = input("please enter a hexadecimal number: ")
                correctHex = verifyHex(num)
            num = hexToDec(num)
            num = decToBin(num)
            print(num)
        elif choice == 0:
            exit(0)
        else:
            print("[Error] Invalid option")

if __name__ == "__main__":
    main()

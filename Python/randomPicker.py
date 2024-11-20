import random

def inputInt(prompt):
    success = False
    while (not success):
        option = input(prompt)
        try:
            option = int(option)
            success = True
        except:
            print("[ERROR] Input must be an integer")
    return option

def selectStudent(students):
    randomNum = random.randint(0, (len(students)-1))
    print(students[randomNum])
    students.pop(randomNum)
    return students

def main():
    print("Welcome!")
    raw_list = input("Please enter student names separated by a comma, press enter when all students have been added\n")
    students = raw_list.split(",")
    while (True):
        print("Please select an option below!")
        print("1) Enter new list of students")
        print("2) Select Student at random")
        print("3) Reset existing list of students")
        print("4) View remaining students")
        print("0) Exit Program")
        choice = inputInt("option: ")
        if choice == 1:
            raw_list = input("please enter student names separated by a comma, press enter when all students have been added\n")
            students = raw_list.split(",")
        elif choice == 2:
            if len(students) > 0:
                students = selectStudent(students)
            else:
                print("current list of students is empty, reset list or enter a new list")
        elif choice == 3:
            students = raw_list.split(",")
        elif choice == 4:
            for i in students:
                print(i)
        elif choice == 0:
            exit(0)
        else:
            print("[ERROR] invalid selection")

if __name__ == "__main__":
    main()
